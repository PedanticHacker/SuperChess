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


import datetime

import chess
import chess.svg
from PySide6 import QtCore, QtSvgWidgets, QtWidgets

from superchess import constants, managers


chess.svg.XX = (
    "<circle id='xx' r='5.5' cx='22.5' cy='22.5' fill='yellow' stroke='blue'/>"
)


class Clock(QtWidgets.QLCDNumber):
    """A chess clock to display the remaining time of a chess game."""

    def __init__(self, style: str) -> None:
        super().__init__()

        self._timer = managers.Timer()

        self.setStyleSheet(style)
        self.setFixedSize(constants.CLOCK_SIZE)
        self.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)

        self._display_current_time()

    def _display_current_time(self) -> None:
        """Display the current time."""
        current_time_text, current_time_text_length = self._time_data()
        self.setDigitCount(current_time_text_length)
        self.display(current_time_text)

    def _time_data(self) -> tuple[str, int]:
        """Return the time data as text and character length."""
        current_time = datetime.timedelta(seconds=self._timer.current_time)
        total_seconds = current_time.total_seconds()
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)

        if hours:
            time_text = f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
        else:
            time_text = f"{minutes:02.0f}:{seconds:02.0f}"

        time_text_length = len(time_text)
        return (time_text, time_text_length)


class EvaluationBar(QtWidgets.QProgressBar):
    """A bar to show the evaluation of a chessboard position."""

    def __init__(self) -> None:
        super().__init__()

        self._game = managers.Game()

        self.reset()
        self.setRange(0, 1000)
        self.setFixedSize(constants.EVALUATION_BAR_SIZE)
        self.setOrientation(QtCore.Qt.Orientation.Vertical)

        self._initialize_animation()
        self._retain_size_when_hidden()

    def _initialize_animation(self) -> None:
        """Initialize animation for the evaluation bar."""
        self._animation = QtCore.QPropertyAnimation()

        self._animation.setTargetObject(self)
        self._animation.setPropertyName(b"value")
        self._animation.valueChanged.connect(self.update)
        self._animation.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuint)

    def _retain_size_when_hidden(self) -> None:
        """Retain the size of the evaluation bar when it is hidden."""
        evaluation_bar_size_policy = self.sizePolicy()
        evaluation_bar_size_policy.setRetainSizeWhenHidden(True)
        self.setSizePolicy(evaluation_bar_size_policy)

    def flip(self) -> None:
        """Flip the evaluation bar relative to the current side."""
        self.setInvertedAppearance(self._game.side)

    def reset(self) -> None:
        """Reset the evaluation bar to its default state."""
        self.hide()
        self.flip()

    def animate(self, evaluation: chess.engine.Score) -> None:
        """Animate the evaluation bar to the given evaluation."""
        if evaluation.is_mate():
            absolute_moves_to_mate = abs(evaluation.mate() or 0)
            white_to_mate = absolute_moves_to_mate > 0
            animation_value = 0 if white_to_mate else 1000
            evaluation_text = f"M{absolute_moves_to_mate}"
        else:
            score = evaluation.score() or 0
            animation_value = 500 - score
            evaluation_text = f"{score / 100 :.2f}"

        self.setFormat(evaluation_text)
        self._animation.setEndValue(animation_value)
        self._animation.start()


class FENEditor(QtWidgets.QLineEdit):
    """The editor for chess data in the FEN format."""

    def __init__(self) -> None:
        super().__init__()

        self._chessboard = managers.Chessboard()

        self.setMaxLength(90)
        self.setText(chess.STARTING_FEN)
        self.setFixedSize(constants.FEN_EDITOR_SIZE)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.textEdited.connect(self.on_text_edited)

    def on_text_edited(self, fen: str) -> None:
        """Set a chessboard position from the given fen."""
        try:
            testing_position = self._chessboard.position
            testing_position.set_fen(fen)
        except (IndexError, ValueError):
            self.set_red_background_color()
        else:
            if testing_position.is_valid():
                self.clearFocus()
                self.reset_background_color()
                self._chessboard.set_position(testing_position)

    def set_red_background_color(self) -> None:
        """Set the background color to red."""
        self.setStyleSheet("background: red;")

    def reset_background_color(self) -> None:
        """Reset the background color to the default."""
        self.setStyleSheet("background: #c0d589;")

    def mouseDoubleClickEvent(self, event) -> None:
        """Select all text and paste an entry from the clipboard."""
        self.selectAll()
        self.paste()


class NotationTable(QtWidgets.QTableView):
    """A table view for the notation table."""

    def __init__(self):
        super().__init__()

        self.setShowGrid(False)
        self.setFixedSize(constants.NOTATION_TABLE_SIZE)
        self.verticalHeader().setSectionResizeMode(constants.FIXED_VERTICALLY)
        self.horizontalHeader().setSectionResizeMode(constants.STRETCHED_HORIZONTALLY)

        table_model = managers.TableModel()
        self.setModel(table_model)

        self.pressed.connect(self.on_pressed)

    def on_pressed(self) -> None:
        print("Notation table item pressed!")


class SVGChessboard(QtSvgWidgets.QSvgWidget):
    """A chessboard in SVG format."""

    def __init__(self) -> None:
        super().__init__()

        self._game = managers.Game()
        self._chessboard = managers.Chessboard()

        self.draw()

    def mousePressEvent(self, event) -> None:
        """Respond to pressing a mouse button."""
        ...

    def draw(self) -> None:
        """Draw the chessboard."""
        svg_chessboard = chess.svg.board(
            arrows=self._game.arrow,
            orientation=self._game.side,
            check=self._game.king_square,
            board=self._chessboard.position,
            squares=self._game.legal_squares,
            colors=self.default_chessboard_colors,
        )
        encoded_svg_chessboard = svg_chessboard.encode()
        self.load(encoded_svg_chessboard)

    def flip(self) -> None:
        """Flip the chessboard."""
        self._game.flip()

    @property
    def default_chessboard_colors(self) -> dict[str, str]:
        """Specify default colors for the chessboard."""
        return {
            "coord": "white",
            "margin": "lime",
            "square dark": "beige",
            "square light": "white",
            "arrow red": "#88202080",
            "arrow blue": "#00308880",
            "arrow green": "#15781b80",
            "arrow yellow": "#e68f0080",
            "square dark lastmove": "#8b000080",
            "square light lastmove": "#8b000080",
        }
