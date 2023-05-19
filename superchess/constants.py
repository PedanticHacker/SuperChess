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


from PySide6 import QtCore, QtWidgets

from gui import styles
from superchess import utilities


APP_NAME = "SuperChess"
APP_VERSION_NUMBER = "1.0.0"
APP_CUSTOM_STYLE = styles.custom()
APP_DEFAULT_STYLE = styles.default()

CHESSBOARD_SIZE = QtCore.QSize(600, 600)
CHESSBOARD_HEIGHT = CHESSBOARD_SIZE.height()
HALF_CHESSBOARD_WIDTH = CHESSBOARD_SIZE.width() // 2
CHESSBOARD_SCALE = CHESSBOARD_HEIGHT / 400
MARGIN_SCALE = 15 * CHESSBOARD_SCALE
SQUARE_SIZE = (CHESSBOARD_HEIGHT - 2 * MARGIN_SCALE) // 8

PROMOTION_DIALOG_SIZE = QtCore.QSize(350, 100)
FEN_EDITOR_SIZE = QtCore.QSize(CHESSBOARD_HEIGHT, 20)
EVALUATION_BAR_SIZE = QtCore.QSize(40, CHESSBOARD_HEIGHT)
NOTATION_TABLE_SIZE = QtCore.QSize(HALF_CHESSBOARD_WIDTH, CHESSBOARD_HEIGHT)

CLOCK_SIZE = QtCore.QSize(200, 50)
CLOCK_HEIGHT = CLOCK_SIZE.height()
CLOCK_SPACING = CHESSBOARD_HEIGHT - (3 * CLOCK_HEIGHT)

FIXED_VERTICALLY = QtWidgets.QHeaderView.ResizeMode.Fixed
STRETCHED_HORIZONTALLY = QtWidgets.QHeaderView.ResizeMode.Stretch

BLACK_ROOK_ICON = utilities.svg_icon("black rook")
WHITE_ROOK_ICON = utilities.svg_icon("white rook")
BLACK_QUEEN_ICON = utilities.svg_icon("black queen")
WHITE_QUEEN_ICON = utilities.svg_icon("white queen")
BLACK_BISHOP_ICON = utilities.svg_icon("black bishop")
BLACK_KNIGHT_ICON = utilities.svg_icon("black knight")
WHITE_BISHOP_ICON = utilities.svg_icon("white bishop")
WHITE_KNIGHT_ICON = utilities.svg_icon("white knight")

FLIP_ICON = utilities.svg_icon("flip")
QUIT_ICON = utilities.svg_icon("quit")
ABOUT_ICON = utilities.svg_icon("about")
APP_LOGO_ICON = utilities.svg_icon("app logo")
NEW_GAME_ICON = utilities.svg_icon("new game")
SETTINGS_ICON = utilities.svg_icon("settings")
LOAD_ENGINE_ICON = utilities.svg_icon("load engine")
PUSH_MOVE_NOW_ICON = utilities.svg_icon("push move now")
STOP_ANALYSIS_ICON = utilities.svg_icon("stop analysis")
START_ANALYSIS_ICON = utilities.svg_icon("start analysis")

ACCEPT_ROLE = QtWidgets.QDialogButtonBox.ButtonRole.AcceptRole

OK = QtWidgets.QDialogButtonBox.StandardButton.Ok
CANCEL = QtWidgets.QDialogButtonBox.StandardButton.Cancel

MINIMUM_SIZE_POLICY = QtWidgets.QSizePolicy(
    QtWidgets.QSizePolicy.Policy.Minimum,
    QtWidgets.QSizePolicy.Policy.Minimum,
)
