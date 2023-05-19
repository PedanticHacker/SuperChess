# Copyright 2023 Boštjan Mejak
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# “Software”), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sys
from typing import Any
from pathlib import Path
from platform import system

import chess
import chess.engine
from PySide6 import QtCore, QtWidgets

from gui import dialogs
from superchess import constants, utilities


class AppLock:
    """The main GUI thread, locked to one instance of SuperChess."""

    def __init__(self) -> None:
        self._app = QtWidgets.QApplication()
        self._app.setApplicationName(constants.APP_NAME)
        self._app.setDesktopFileName(constants.APP_NAME)
        self._app.setWindowIcon(constants.APP_LOGO_ICON)
        self._app.setStyleSheet(constants.APP_DEFAULT_STYLE)
        self._app.setApplicationVersion(constants.APP_VERSION_NUMBER)

        self._lock_file = QtCore.QLockFile("superchess.lock")

    def __enter__(self) -> QtCore.QLockFile:
        if self._lock_file.tryLock():
            return self._lock_file

        QtWidgets.QMessageBox.warning(
            QtWidgets.QWidget(),
            "Warning",
            "SuperChess is already running!",
        )
        sys.exit()

    def __exit__(self, *args, **kwargs) -> None:
        self._app.exec()


class Chessboard:
    """A manager that manages the chessboard."""

    def __init__(self) -> None:
        self._position = chess.Board()

    def fen(self) -> str:
        """
        Return the current FEN.

        > Trim the half-move clock and the full-move number.
        """
        return self._position.fen()[-4]

    def set_position(self, position: chess.Board) -> None:
        """Set a chessboard position from the given position."""
        self._position = position

    def set_root_position(self) -> None:
        """Set all 32 pieces to their root position."""
        self._position = self.position.root()

    @property
    def position(self) -> chess.Board:
        """Return the currently set chessboard position."""
        return self._position


class Engine:
    """A manager for a UCI chess engine."""

    def __init__(self) -> None:
        self._engine_triggered = False
        self._analysis_triggered = False

        self._chessboard = Chessboard()
        self._thread = QtCore.QThreadPool()

    def load(self, file_path: str) -> None:
        """Load a chess engine by the given file_path."""
        try:
            self._engine = chess.engine.SimpleEngine.popen_uci(file_path)
        except OSError:
            utilities.warn(
                title="Chess Engine Error",
                message="The chess engine has failed to load.",
            )

    def play(self) -> chess.engine.PlayResult:
        """Trigger the chess engine to think and return a result."""
        return self._engine.play(
            board=self._chessboard.position,
            ponder=utilities.load_setting("engine", "pondering"),
            limit=chess.engine.Limit(black_clock=None, white_clock=None),
        )

    def start_analysis(self) -> None:
        """Start a chessboard position analysis by the chess engine."""
        ...

    def stop_analysis(self) -> None:
        """Stop a chessboard position analysis by the chess engine."""
        ...

    def trigger_engine(self) -> None:
        """Trigger the chess engine to make a move."""
        self._engine_triggered = True
        self._thread.start(self.play)

    def trigger_analysis(self) -> chess.engine.InfoDict:
        """Trigger the chess engine to analyze a position."""
        with self._engine.analysis(self._chessboard.position) as analysis:
            return analysis.info

    def quit(self) -> None:
        """Quit the chess engine process."""
        self._engine.quit()

    @property
    def name(self) -> str:
        """Return the name of a chess engine."""
        return self._engine.id.get("name", default="nothing")

    @property
    def default_path(self) -> str:
        """Return a file path to the default Stockfish chess engine."""
        os_name = "macOS" if system() == "Darwin" else system()
        path = Path(f"superchess/engines/Stockfish/{os_name}/stockfish.exe")
        return str(path)

    def is_analysis_triggered(self) -> bool:
        """Check whether chess engine analysis is triggered."""
        return self._analysis_triggered

    def is_engine_triggered(self) -> bool:
        """Check whether the chess engine is triggered."""
        return self._engine_triggered


class Game:
    """A manager for the state of a chess game."""

    def __init__(self) -> None:
        self._notation: list[str] = []
        self._positions: list[chess.Board] = []
        self._arrow: list[tuple[chess.Square, chess.Square]] = []

        self._engine = Engine()
        self._chessboard = Chessboard()

        self.reset()

    def reset(self) -> None:
        """Reset the current game to its initial state."""
        self._arrow.clear()
        self._notation.clear()
        self._positions.clear()
        self._chessboard.position.reset()

        self._capture = False
        self._engine_turn = utilities.load_setting("engine", "white")
        self._pondering = utilities.load_setting("engine", "pondering")
        self._side = not self._engine_turn

        self.reset_squares()

    def flip(self) -> None:
        """Flip the current side."""
        self._side = not self._side

    def reset_squares(self) -> None:
        """Reset the current origin and target squares."""
        self._origin_square = -1
        self._target_square = -1

    def find_move_by(self, square: chess.Square) -> None:
        """Find a move by the given square."""
        try:
            move = self._chessboard.position.find_move(
                self._origin_square,
                self._target_square,
            )
        except ValueError:
            self._origin_square = square
        else:
            if move.promotion is not None:
                move.promotion = self.promotion_piece()
            self.push_human_move(move)

    def promotion_piece(self) -> None | chess.PieceType:
        """Return a promotion piece if one is selected."""
        promotion_dialog = dialogs.Promotion(self.player_color)
        return promotion_dialog.piece

    def push(self, move: chess.Move) -> None:
        """Push the given move."""

        self._capture = self._chessboard.position.is_capture(move)

        notation_item = self._chessboard.position.san_and_push(move)
        self._notation.append(notation_item)

        position = self._chessboard.position.copy()
        self._positions.append(position)

        self.reset_squares()
        self.set_arrow_from(move)
        utilities.play_sound_effect("capture" if self.is_capture() else "move")

    def push_human_move(self, move: chess.Move) -> None:
        """Push a legal human move with the given move."""
        self.push(move)
        self.update_game_state()
        self._engine.trigger_engine()

    def push_engine_move(self, move: chess.Move) -> None:
        """Push a legal chess engine move with the given move."""
        self.push(move)
        self.update_game_state()

    def update_game_state(self) -> None:
        """Update the current state of a chess game."""
        # self._black_clock.toggle_timer_state()
        # self._white_clock.toggle_timer_state()

        # self._engine.stop_analysis()
        # self._evaluation_bar.reset()
        # utilities.label().clear()

        if self.is_game_over():
            # self._black_clock.stop_timer()
            # self._white_clock.stop_timer()

            self.show_game_result()
            # self.offer_new_game()

        # if self._engine.has_resigned():
        #     self._black_clock.stop_timer()
        #     self._white_clock.stop_timer()
        #     utilities.label(f"{self._engine.name} has resigned!")

        # self._chessboard.draw()

    def show_game_result(self) -> str:
        """Show the result of a game."""
        game_result = self._chessboard.position.result(claim_draw=True)
        game_result_rewordings = {
            "*": "Undetermined!",
            "0-1": "Black wins!",
            "1-0": "White wins!",
            "1/2-1/2": "It's a draw!",
        }
        return game_result_rewordings[game_result]

    def set_arrow_from(self, move: chess.Move) -> None:
        """Set an arrow from the given move."""
        self._arrow = [(move.from_square, move.to_square)]

    def pass_turn_to_engine(self) -> None:
        """Pass the current turn to the chess engine."""
        self._engine_turn = self._chessboard.position.turn
        # utilities.save_settings()

    def is_black_on_turn(self) -> bool:
        """Return True if Black is on turn, else False."""
        return self._chessboard.position.turn == chess.BLACK

    def is_capture(self) -> bool:
        """Return True if a move is a capture, else False."""
        return self._capture

    def is_game_in_progress(self) -> bool:
        """Return True if a game is in progress, else False."""
        return bool(self._notation)

    def is_game_over(self) -> bool:
        """Return True if the game is over, else False."""
        return self._chessboard.position.is_game_over(claim_draw=True)

    def is_engine_on_turn(self) -> bool:
        """Return True if the chess engine is on turn, else False."""
        return self._chessboard.position.turn == self._engine_turn

    def is_side_flipped(self) -> bool:
        """Return True if Black plays from the bottom, else False."""
        return self._side == chess.BLACK

    def is_white_on_turn(self) -> bool:
        """Return True if White is on turn, else False."""
        return self._chessboard.position.turn == chess.WHITE

    @property
    def arrow(self) -> list[tuple[chess.Square, chess.Square]]:
        """Return an arrow for a pushed move."""
        return self._arrow

    @property
    def fen(self) -> str:
        """Return the current FEN."""
        return self._chessboard.fen()

    @property
    def king_square(self) -> None | chess.Square:
        """Return the square of a king in check."""
        if not self._chessboard.position.is_check():
            return None
        return self._chessboard.position.king(self._chessboard.position.turn)

    @property
    def legal_squares(self) -> None | list[chess.Square]:
        """Return all legal squares from the legal moves of a piece."""
        if self._origin_square is None:
            return None

        legal_moves = self._chessboard.position.generate_legal_moves(
            chess.BB_SQUARES[self._origin_square],
        )
        return [legal_move.to_square for legal_move in legal_moves]

    @property
    def player_color(self) -> chess.Color:
        """Return True if White is on turn, else False."""
        return self.is_white_on_turn()

    @property
    def player_on_turn(self) -> str:
        """Return either White or Black as the player on turn."""
        return "White" if self.is_white_on_turn() else "Black"

    @property
    def side(self) -> chess.Color:
        """Return the side that plays from the bottom."""
        return self._side


class TableModel(QtCore.QAbstractTableModel):
    """A table model for the notation table."""

    def __init__(self) -> None:
        super().__init__()

        self._items: list[str] = []

    def data(self, index=None, role=QtCore.Qt.ItemDataRole.DisplayRole) -> Any:
        """Provide notation items as data to the table."""
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            item_index = 2 * index.row() + index.column()

            if 0 <= item_index < len(self._items):
                return self._items[item_index]

        return None

    def flags(self, index=None) -> QtCore.Qt.ItemFlag:
        """Set notation item interactability relative to data."""
        if self.data(index):
            return (
                QtCore.Qt.ItemFlag.ItemIsEnabled | QtCore.Qt.ItemFlag.ItemIsSelectable
            )
        return QtCore.Qt.ItemFlag.NoItemFlags

    def rowCount(self, parent=None) -> int:
        """Provide rows for the notation table."""
        return 1 + len(self._items) // 2

    def columnCount(self, parent=None) -> int:
        """Provide two columns for the notation table."""
        return 2

    def headerData(
        self,
        section: int,
        orientation: QtCore.Qt.Orientation,
        role: int = QtCore.Qt.ItemDataRole.DisplayRole,
    ) -> Any:
        """
        Provide data for horizontal and vertical headers.

        > Provide the horizontal header with names White and Black.
        > Provide the vertical header with a table row counter starting
          from 1.
        """
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return ["White", "Black"][section]

            if orientation == QtCore.Qt.Orientation.Vertical:
                return section + 1

        return None

    def update(self) -> None:
        """Update the notation table with new data."""
        self.layoutChanged.emit()


class Timer(QtCore.QTimer):
    """A timer for the chess clock."""

    def __init__(self) -> None:
        super().__init__()

        self.setInterval(1000)
        self.setTimerType(QtCore.Qt.TimerType.PreciseTimer)

        self.set_time_from_settings()
        self.timeout.connect(self.update_time)

    def set_time_from_settings(self) -> None:
        """Set current time from the settings."""
        seconds = utilities.load_setting("clock", "time")
        increment = utilities.load_setting("clock", "increment")
        self._current_time = seconds + increment

    def update_time(self) -> None:
        """Subtract one second from the current time."""
        self._current_time -= 1

        if not self._current_time:
            self.stop()

    def reset(self) -> None:
        """Reset time as set in the settings."""
        self.stop()
        self.set_time_from_settings()

    @property
    def current_time(self) -> int:
        """Return the value of current time."""
        return self._current_time
