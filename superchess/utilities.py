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


import tomllib
from typing import Any

from PySide6 import QtCore, QtGui, QtMultimedia, QtWidgets


def about(title: str, message: str) -> None:
    """Show a message with the given title and message."""
    parent = QtWidgets.QMessageBox()
    QtWidgets.QMessageBox.about(parent, title, message)


def ask(title: str, message: str) -> QtWidgets.QMessageBox.StandardButton:
    """Ask a question with the given title and message."""
    parent = QtWidgets.QMessageBox()
    return QtWidgets.QMessageBox.question(parent, title, message)


def create_button(icon: QtGui.QIcon) -> QtWidgets.QPushButton:
    """Return a button by the given icon."""
    icon_size = QtCore.QSize(56, 56)
    button = QtWidgets.QPushButton()
    button.setIconSize(icon_size)
    button.setIcon(icon)
    return button


def inform(title: str, message: str) -> None:
    """Inform about something with the given title and message."""
    parent = QtWidgets.QMessageBox()
    QtWidgets.QMessageBox.information(parent, title, message)


def load_setting(group: str, name: str) -> Any:
    """Load a setting value by the given group and name."""
    with open("superchess/settings.toml", "rb") as settings_file:
        settings = tomllib.load(settings_file)
    return settings[group][name]


def play_sound_effect(filename: str = "move") -> None:
    """
    Play a sound effect by the given filename.

    > The acceptable values for the filename argument are either "move"
      or "capture".
    """
    file_url = QtCore.QUrl.fromLocalFile(f"gui/sounds/{filename}.wav")
    sound_effect = QtMultimedia.QSoundEffect()
    sound_effect.setSource(file_url)
    sound_effect.play()


def svg_icon(filename: str) -> QtGui.QIcon:
    """Return an SVG icon by the given filename."""
    return QtGui.QIcon(f"gui/icons/{filename}.svg")


def warn(title: str, message: str) -> None:
    """Warn about something with the given title and message."""
    parent = QtWidgets.QMessageBox()
    QtWidgets.QMessageBox.warning(parent, title, message)
