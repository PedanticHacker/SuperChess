## About SuperChess

SuperChess is a GUI app for playing chess against a UCI chess engine.

### Source code

The source code is completely written in **Python**.

### Third-party software

SuperChess uses the **PySide6** GUI framework, the **python-chess**
library, and the **Stockfish** chess engine.

### Components

SuperChess provides a chessboard with pieces, clocks, FEN text editor,
and a table for notation in SAN format.

### Piece movement

Moving the pieces is bound to the rules of standard chess.

To move a piece on the board from one square to another is by clicking
the piece and then clicking its target square.

Note: the drag-and-drop ability to move the pieces is not supported.

### Move legality indication

After clicking a piece, certain squares become marked with a dot which
indicates a legal move.

### Appearance

The following screenshots reveal how SuperChess looks like.

![SuperChess on Windows 11](link "SuperChess on Windows 11")
*Changing the settings.*

![SuperChess on Windows 11](link "SuperChess on Windows 11")
*Selecting a move from the chess notation table.*

![SuperChess on Windows 11](link "SuperChess on Windows 11")
*Analyzing a position by the default Stockfish 15.1 chess engine.*

![SuperChess on Windows 11](link "SuperChess on Windows 11")
*Promoting a White's pawn to a queen, a rook, a bishop, or a knight.*

## Chess engine

By default, SuperChess uses the Stockfish chess engine version 15.1 for
Windows and Linux-based platforms, but version 14.1 for macOS.

However, a different chess engine can be loaded and played against, but
it must support the UCI protocol.

## Requirements

A few requirements must be met to run SuperChess successfully. The ones
listed below must be installed on the operating system. Otherwise, the
the provided links should be followed to then install any requirement
that is missing.

(1) Firstly, the Python programming language must be installed:

- [**Python 3.11.3**](https://www.python.org/downloads/release/python-3113)

(2) Secondly, in a command-line interface with admin privileges, the
following must be installed:

- **PySide6**, by executing the command `pip install PySide6`
- **python-chess**, by executing the command `pip install chess`

Alternatively, **PySide6** and **python-chess** can also be installed
using the `pip` package manager in a command-line interface with admin
privileges by navigating to the top-level directory of SuperChess and
then executing the command `pip install -r requirements.txt`.

## How to start it

To start SuperChess and play chess, run the `main.py` file in your IDE.

Alternatively, you can also execute the command `python main.py` in your
command-line interface from the top-level directory of SuperChess.

## Credits and links

**(1)** Thanks to all of the developers for their dedicated work on the
**_Python_** programming language!

- [Source code](https://github.com/python/cpython)
- [Downloads page](https://www.python.org/downloads)

**(2)** Thanks to all of the developers for their dedicated work on the
**_PySide6_** GUI framework!

- [PyPI (Python Package Index) page](https://pypi.org/project/PySide6)

**(3)** Thanks to developer Niklas Fiekas for his dedicated work on the
**_python-chess_** library!

- [Source code](https://github.com/niklasf/python-chess)
- [PyPI (Python Package Index) page](https://pypi.org/project/chess)

**(4)** Thanks to all of the developers for their dedicated work on the
**_Stockfish_** chess engine!

- [Source code](https://github.com/official-stockfish/Stockfish)
- [Downloads page](https://stockfishchess.org/download)

## License

SuperChess is licensed under the MIT License.

The contents of the LICENSE file provide all the information about the
permissions, limitations, and conditions of the license.
