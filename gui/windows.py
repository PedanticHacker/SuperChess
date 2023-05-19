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


from pathlib import Path
from datetime import date

from PySide6 import QtCore, QtGui, QtWidgets

from gui import dialogs, widgets
from superchess import constants, managers, storage, utilities


HOME_DIRECTORY = Path.home()
COPYRIGHT_YEAR = date.today().year
BLACK_STYLE = "color: white; background: black;"
WHITE_STYLE = "color: black; background: white;"

ALIGN_TOP = QtCore.Qt.AlignmentFlag.AlignTop
ALIGN_LEFT = QtCore.Qt.AlignmentFlag.AlignLeft
ALIGN_RIGHT = QtCore.Qt.AlignmentFlag.AlignRight


class MainWindow(QtWidgets.QMainWindow):
    """The main window of SuperChess."""

    def __init__(self) -> None:
        super().__init__()

        self._game = managers.Game()
        self._engine = managers.Engine()
        self._fen_editor = widgets.FENEditor()
        self._chessboard = managers.Chessboard()
        self._engine_name_label = QtWidgets.QLabel()
        self._notification_label = QtWidgets.QLabel()
        self._chess_opening_label = QtWidgets.QLabel()
        self._black_clock = widgets.Clock(BLACK_STYLE)
        self._white_clock = widgets.Clock(WHITE_STYLE)
        self._evaluation_bar = widgets.EvaluationBar()
        self._notation_table = widgets.NotationTable()
        self._svg_chessboard = widgets.SVGChessboard()

        self.create_actions()
        self.create_menu_bar()
        self.create_tool_bar()
        self.create_status_bar()
        self.set_window_layout()
        self.load_default_engine()
        self.toggle_tool_bar_buttons()

    def create_actions(self) -> None:
        """Create actions for the menu bar and the tool bar."""
        self.about_action = QtGui.QAction()
        self.about_action.setText("About")
        self.about_action.setShortcut("Ctrl+Shift+A")
        self.about_action.setIcon(constants.ABOUT_ICON)
        self.about_action.triggered.connect(self.show_about)
        self.about_action.setStatusTip("Shows the About message.")

        self.flip_action = QtGui.QAction()
        self.flip_action.setText("Flip")
        self.flip_action.setShortcut("Ctrl+Shift+F")
        self.flip_action.setIcon(constants.FLIP_ICON)
        self.flip_action.triggered.connect(self.flip)
        self.flip_action.setStatusTip("Flips the side.")

        self.load_engine_action = QtGui.QAction()
        self.load_engine_action.setShortcut("Ctrl+E")
        self.load_engine_action.setText("Load engine...")
        self.load_engine_action.setIcon(constants.LOAD_ENGINE_ICON)
        self.load_engine_action.triggered.connect(self.load_engine)
        self.load_engine_action.setStatusTip("Shows the file manager.")

        self.new_game_action = QtGui.QAction()
        self.new_game_action.setText("New game")
        self.new_game_action.setShortcut("Ctrl+Shift+N")
        self.new_game_action.setIcon(constants.NEW_GAME_ICON)
        self.new_game_action.setStatusTip("Offers a new game.")
        self.new_game_action.triggered.connect(self.offer_new_game)

        self.push_move_now_action = QtGui.QAction()
        self.push_move_now_action.setText("Push move now")
        self.push_move_now_action.setShortcut("Ctrl+Shift+P")
        self.push_move_now_action.setStatusTip("Pushes a move now.")
        self.push_move_now_action.setIcon(constants.PUSH_MOVE_NOW_ICON)
        self.push_move_now_action.triggered.connect(self.push_move_now)

        self.settings_action = QtGui.QAction()
        self.settings_action.setText("Settings...")
        self.settings_action.setShortcut("Ctrl+Shift+S")
        self.settings_action.setIcon(constants.SETTINGS_ICON)
        self.settings_action.setStatusTip("Shows the Settings window.")
        self.settings_action.triggered.connect(self.show_settings_dialog)

        self.start_analysis_action = QtGui.QAction()
        self.start_analysis_action.setText("Start analysis")
        self.start_analysis_action.setShortcut("Ctrl+Shift+A")
        self.start_analysis_action.setIcon(constants.START_ANALYSIS_ICON)
        self.start_analysis_action.triggered.connect(self.start_analysis)
        self.start_analysis_action.setStatusTip("Starts the engine analysis.")

        self.stop_analysis_action = QtGui.QAction()
        self.stop_analysis_action.setText("Stop analysis")
        self.stop_analysis_action.setShortcut("Ctrl+Shift+X")
        self.stop_analysis_action.setIcon(constants.STOP_ANALYSIS_ICON)
        self.stop_analysis_action.triggered.connect(self.stop_analysis)
        self.stop_analysis_action.setStatusTip("Stops the engine analysis.")

        self.quit_action = QtGui.QAction()
        self.quit_action.setText("Quit...")
        self.quit_action.setShortcut("Ctrl+Q")
        self.quit_action.setIcon(constants.QUIT_ICON)
        self.quit_action.triggered.connect(self.quit)
        self.quit_action.setStatusTip("Offers to quit SuperChess.")

    def create_menu_bar(self) -> None:
        """Create a menu bar with actions in separate menus."""

        # Menu bar
        menu_bar = self.menuBar()

        # General menu
        general_menu = menu_bar.addMenu("General")

        # Edit menu
        edit_menu = menu_bar.addMenu("Edit")

        # Help menu
        help_menu = menu_bar.addMenu("Help")

        # General menu > Load engine...
        general_menu.addAction(self.load_engine_action)

        # General menu separator
        general_menu.addSeparator()

        # General menu > Quit...
        general_menu.addAction(self.quit_action)

        # Edit menu > Settings...
        edit_menu.addAction(self.settings_action)

        # Help menu > About
        help_menu.addAction(self.about_action)

    def create_tool_bar(self) -> None:
        """Create a tool bar with buttons in separate areas."""

        # General area
        general_area = self.addToolBar("General")

        # Edit area
        edit_area = self.addToolBar("Edit")

        # Help area
        help_area = self.addToolBar("Help")

        # General area > Quit
        general_area.addAction(self.quit_action)

        # Edit area > New game
        edit_area.addAction(self.new_game_action)

        # Edit area > Flip sides
        edit_area.addAction(self.flip_action)

        # Edit area > Push move now
        edit_area.addAction(self.push_move_now_action)

        # Edit area > Start analysis
        edit_area.addAction(self.start_analysis_action)

        # Edit area > Stop analysis
        edit_area.addAction(self.stop_analysis_action)

        # Edit area > Settings
        edit_area.addAction(self.settings_action)

        # Edit area > Load engine
        edit_area.addAction(self.load_engine_action)

        # Help area > About
        help_area.addAction(self.about_action)

    def create_status_bar(self) -> None:
        """Create a status bar to show various info."""
        status_bar = self.statusBar()
        status_bar.addWidget(self._chess_opening_label)
        status_bar.addPermanentWidget(self._engine_name_label)

    def set_window_layout(self) -> None:
        """Set a custom layout for widgets on the main window."""
        widget_container = QtWidgets.QWidget(self)
        widget_container.setSizePolicy(constants.MINIMUM_SIZE_POLICY)

        self._clock_layout = QtWidgets.QVBoxLayout()
        self._clock_layout.addWidget(self._black_clock)
        self._clock_layout.addSpacing(constants.CLOCK_SPACING)
        self._clock_layout.addWidget(self._white_clock)
        self.flip_clocks() if not self._game.side else None

        grid_layout = QtWidgets.QGridLayout()
        grid_layout.addLayout(self._clock_layout, 0, 0, ALIGN_RIGHT)
        grid_layout.addWidget(self._svg_chessboard, 0, 1)
        grid_layout.addWidget(self._evaluation_bar, 0, 2)
        grid_layout.addWidget(self._notation_table, 0, 3, ALIGN_LEFT)
        grid_layout.addWidget(self._fen_editor, 1, 1)
        grid_layout.addWidget(self._notification_label, 2, 1, ALIGN_TOP)

        widget_container.setLayout(grid_layout)
        self.setCentralWidget(widget_container)

    def load_default_engine(self):
        """Load the default Stockfish chess engine."""
        self._engine.load(self._engine.default_path)

    def toggle_tool_bar_buttons(self) -> None:
        """Toggle the tool bar buttons of the chess engine."""
        self.push_move_now_action.setEnabled(True)
        self.start_analysis_action.setEnabled(True)
        self.stop_analysis_action.setDisabled(True)

        if self._engine.is_engine_triggered():
            self.push_move_now_action.setDisabled(True)
            self.stop_analysis_action.setDisabled(True)
            self.start_analysis_action.setDisabled(True)

        if self._engine.is_analysis_triggered():
            self.stop_analysis_action.setEnabled(True)
            self.push_move_now_action.setDisabled(True)
            self.start_analysis_action.setDisabled(True)

        if self._game.is_game_over():
            self.push_move_now_action.setDisabled(True)
            self.stop_analysis_action.setDisabled(True)
            self.start_analysis_action.setDisabled(True)

    def quit(self) -> None:
        """Trigger closing the main window to quit SuperChess."""
        self.close()

    def flip(self) -> None:
        """Flip the side."""
        self.flip_clocks()
        self._evaluation_bar.flip()
        self._svg_chessboard.flip()
        self._svg_chessboard.draw()

    def push_move_now(self) -> None:
        """Pass the turn to the chess engine to push a move."""
        self._game.pass_turn_to_engine()

    def show_settings_dialog(self) -> None:
        """Show the Settings dialog."""
        settings_dialog = dialogs.Settings()
        settings_dialog.exec()

    def load_engine(self) -> None:
        """Show a file manager to load a file of a UCI chess engine."""
        parent = self
        title = "File Manager"
        home_directory = str(HOME_DIRECTORY)
        engine_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent,
            title,
            home_directory,
        )

        if engine_file:
            self._engine.load(engine_file)
            self._engine.trigger_engine()

    def show_about(self) -> None:
        """Show the About message."""
        utilities.about(
            title="About",
            message=(
                f"A GUI app for playing chess against a UCI chess engine.\n\n"
                f"Copyright {COPYRIGHT_YEAR} Boštjan Mejak\n"
                f"MIT License"
            ),
        )

    def flip_clocks(self) -> None:
        """Flip the clocks on the bottom and the top."""
        bottom_clock = self._clock_layout.takeAt(2).widget()
        top_clock = self._clock_layout.takeAt(0).widget()
        self._clock_layout.insertWidget(0, bottom_clock)
        self._clock_layout.insertWidget(2, top_clock)

    def closeEvent(self, event) -> None:
        """Offer to quit SuperChess."""
        answer = utilities.ask(
            title="Quit",
            message="Do you want to quit SuperChess?",
        )

        if answer == answer.Yes:
            event.accept()
            self._engine.quit()
        else:
            event.ignore()

    def start_analysis(self) -> None:
        """Start a chessboard position analysis by the chess engine."""
        self._engine.start_analysis()
        self._evaluation_bar.show()
        self.toggle_tool_bar_buttons()

    def stop_analysis(self) -> None:
        """Stop a chessboard position analysis by the chess engine."""
        self._engine.stop_analysis()
        self.toggle_tool_bar_buttons()

    def show_fen(self) -> None:
        """Show a FEN in the FEN editor."""
        fen = self._chessboard.position.fen()
        self._fen_editor.setText(fen)
        self._fen_editor.reset_background_color()

    def show_evaluation(self, evaluation) -> None:
        """Show a position evaluation by the given evaluation."""
        self._evaluation_bar.animate(evaluation)

    def show_variation(self, variation: str) -> None:
        """Show a variation of moves by the given variation."""
        self._notification_label.setText(variation)

    def show_chess_opening(self) -> None:
        """Show an ECO code and a chess opening name for a position."""
        fen = self._game.fen
        chess_openings = storage.chess_openings()

        if fen in chess_openings:
            eco_code, chess_opening_name = chess_openings[fen]
            chess_opening = f"{eco_code}: {chess_opening_name}"
            self._chess_opening_label.setText(chess_opening)

    def start_new_game(self) -> None:
        """Start a new game by resetting everything."""
        if self._game.is_side_flipped():
            self.flip_clocks()

        self._game.reset()
        # self._timer.reset_time()
        # self._timer.reset_time()
        self._notification_label.clear()
        self._chess_opening_label.clear()

        self._engine.stop_analysis()
        self._evaluation_bar.reset()
        self._engine.trigger_engine()

        self.toggle_tool_bar_buttons()

    def offer_new_game(self) -> None:
        """Offer to start a new game."""
        answer = utilities.ask(
            title="New Game",
            message="Do you want to start a new game?",
        )

        if answer == answer.Yes:
            self.start_new_game()
