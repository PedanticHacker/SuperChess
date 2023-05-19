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


import chess
from PySide6 import QtWidgets

from superchess import constants, utilities


class Promotion(QtWidgets.QDialog):
    """A pawn promotion to a queen, a rook, a bishop, or a knight."""

    def __init__(self, player_color: chess.Color) -> None:
        super().__init__()

        self._piece = -1
        self._player_color = player_color
        self.button_box = QtWidgets.QDialogButtonBox()

        self.setWindowTitle("Pawn Promotion")
        self.setFixedSize(constants.PROMOTION_DIALOG_SIZE)

        self.create_icons()
        self.create_buttons()
        self.add_buttons_to_box()
        self.handle_dialog_events()

        self.exec()

    def create_icons(self) -> None:
        """Set promotion piece icons relative to the promoter."""
        self.rook_icon = (
            constants.WHITE_ROOK_ICON
            if self.is_white_promoting()
            else constants.BLACK_ROOK_ICON
        )

        self.queen_icon = (
            constants.WHITE_QUEEN_ICON
            if self.is_white_promoting()
            else constants.BLACK_QUEEN_ICON
        )

        self.bishop_icon = (
            constants.WHITE_BISHOP_ICON
            if self.is_white_promoting()
            else constants.BLACK_BISHOP_ICON
        )

        self.knight_icon = (
            constants.WHITE_KNIGHT_ICON
            if self.is_white_promoting()
            else constants.BLACK_KNIGHT_ICON
        )

    def create_buttons(self) -> None:
        """Create a button for each promotion piece."""
        self.rook_button = utilities.create_button(icon=self.rook_icon)
        self.queen_button = utilities.create_button(icon=self.queen_icon)
        self.bishop_button = utilities.create_button(icon=self.bishop_icon)
        self.knight_button = utilities.create_button(icon=self.knight_icon)

    def add_buttons_to_box(self) -> None:
        """Add promotion piece buttons to the button box."""
        self.button_box.addButton(self.queen_button, constants.ACCEPT_ROLE)
        self.button_box.addButton(self.rook_button, constants.ACCEPT_ROLE)
        self.button_box.addButton(self.bishop_button, constants.ACCEPT_ROLE)
        self.button_box.addButton(self.knight_button, constants.ACCEPT_ROLE)

    def handle_dialog_events(self) -> None:
        """Handle dialog events."""
        self.button_box.accepted.connect(self.accept)
        self.rook_button.clicked.connect(self.on_rook_button_clicked)
        self.queen_button.clicked.connect(self.on_queen_button_clicked)
        self.bishop_button.clicked.connect(self.on_bishop_button_clicked)
        self.knight_button.clicked.connect(self.on_knight_button_clicked)

    def on_rook_button_clicked(self) -> None:
        """Set the promotion piece to be a rook."""
        self._piece = chess.ROOK

    def on_queen_button_clicked(self) -> None:
        """Set the promotion piece to be a queen."""
        self._piece = chess.QUEEN

    def on_bishop_button_clicked(self) -> None:
        """Set the promotion piece to be a bishop."""
        self._piece = chess.BISHOP

    def on_knight_button_clicked(self) -> None:
        """Set the promotion piece to be a knight."""
        self._piece = chess.KNIGHT

    def is_white_promoting(self) -> bool:
        """Return True if White is promoting, else False."""
        return self._player_color == chess.WHITE

    @property
    def piece(self) -> chess.PieceType:
        """Return the promotion piece that was clicked."""
        return self._piece


class Settings(QtWidgets.QDialog):
    """A dialog that provides changing the settings."""

    def __init__(self) -> None:
        super().__init__()

        self.button_box = QtWidgets.QDialogButtonBox()
        self.button_box.setStandardButtons(constants.OK | constants.CANCEL)

        self.set_groups()
        self.set_options()
        self.set_widget_layout()
        self.handle_dialog_events()

        self.setWindowTitle("Settings")

    def set_groups(self) -> None:
        """
        Set two groups.

        > Set a group for the chess engine options.
        > Set a group for the time control options.
        """
        self.engine_group = QtWidgets.QGroupBox()
        self.engine_group.setTitle("Chess engine")
        # self.engine_group.setDisabled()

        self.time_control_group = QtWidgets.QGroupBox()
        self.time_control_group.setTitle("Time control")
        # self.time_control_group.setDisabled()

    def set_options(self) -> None:
        """Set options that represent the settings."""
        self.option_black = QtWidgets.QRadioButton()
        self.option_black.setText("Black")
        self.option_black.setChecked(utilities.load_setting("engine", "black"))

        self.option_white = QtWidgets.QRadioButton()
        self.option_white.setText("White")
        self.option_white.setChecked(utilities.load_setting("engine", "white"))

        self.option_pondering = QtWidgets.QCheckBox()
        self.option_pondering.setText("Pondering")
        self.option_pondering.setChecked(utilities.load_setting("engine", "pondering"))

        self.option_time = QtWidgets.QComboBox()
        self.option_time.addItem("1 minute", 60)
        self.option_time.addItem("3 minutes", 180)
        self.option_time.addItem("5 minutes", 300)
        self.option_time.addItem("10 minutes", 600)
        self.option_time.addItem("20 minutes", 1200)
        self.option_time.addItem("30 minutes", 1800)
        self.option_time.addItem("1 hour", 3600)
        self.option_time.addItem("2 hours", 7200)
        self.option_time.setCurrentIndex(
            self.option_time.findData(utilities.load_setting("clock", "time"))
        )

        self.option_increment = QtWidgets.QComboBox()
        self.option_increment.addItem("0 seconds", 0)
        self.option_increment.addItem("6 seconds", 6)
        self.option_increment.addItem("12 seconds", 12)
        self.option_increment.addItem("30 seconds", 30)
        self.option_increment.setCurrentIndex(
            self.option_increment.findData(utilities.load_setting("clock", "increment"))
        )

    def set_widget_layout(self) -> None:
        """Set a custom layout for the widgets of the dialog."""
        engine_layout = QtWidgets.QVBoxLayout()
        engine_layout.addWidget(self.option_black)
        engine_layout.addWidget(self.option_white)
        engine_layout.addWidget(self.option_pondering)
        self.engine_group.setLayout(engine_layout)

        time_control_layout = QtWidgets.QHBoxLayout()
        time_control_layout.addWidget(self.option_time)
        time_control_layout.addWidget(self.option_increment)
        self.time_control_group.setLayout(time_control_layout)

        dialog_layout = QtWidgets.QVBoxLayout()
        dialog_layout.addWidget(self.engine_group)
        dialog_layout.addWidget(self.time_control_group)
        dialog_layout.addWidget(self.button_box)
        self.setLayout(dialog_layout)

    def handle_dialog_events(self) -> None:
        """Handle dialog events."""
        self.accepted.connect(self.save_settings)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def save_settings(self) -> None:
        """Save the settings."""
        ...
