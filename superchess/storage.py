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


def chess_openings() -> dict[str, tuple[str, str]]:
    """
    Return a dictionary with chess openings.

    The dictionary's key is a FEN containing a tuple with an ECO code
    and a chess opening name.
    """
    return {
        "rn1qkbnr/ppp2ppp/8/3p4/5p2/6PB/PPPPP2P/RNBQK2R w KQkq -": (
            "A00",
            "Amar Gambit",
        ),
        "rn1qkbnr/ppp2ppp/8/3p4/8/6PB/PPPPP3/RNBQ1RK1 b kq -": (
            "A00",
            "Amar Opening: Gent Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/5P2/6PN/PPPPP2P/RNBQKB1R b KQkq -": (
            "A00",
            "Amar Opening: Paris Gambit",
        ),
        "rnbqkbnr/pppppppp/8/8/8/7N/PPPPPPPP/RNBQKB1R b KQkq -": (
            "A00",
            "Amar Opening",
        ),
        "r1bqkb1r/ppp2ppp/2np1n2/4p3/2P5/1PN1P3/P2P1PPP/R1BQKBNR w KQkq -": (
            "A00",
            "Amsterdam Attack",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/8/P6P/1PPPPPP1/RNBQKBNR w KQkq -": (
            "A00",
            "Anderssen Opening: Creepy Crawly Formation, Classical Defense",
        ),
        "rnbqkbnr/1ppppppp/8/p7/1P6/P7/2PPPPPP/RNBQKBNR b KQkq -": (
            "A00",
            "Anderssen Opening: Polish Gambit",
        ),
        "rnbqkbnr/pppppppp/8/8/8/P7/1PPPPPPP/RNBQKBNR b KQkq -": (
            "A00",
            "Anderssen Opening",
        ),
        "rnb1kbnr/pppp1ppp/8/4p3/6Pq/5P2/PPPPP2P/RNBQKBNR w KQkq -": (
            "A00",
            "Barnes Opening: Fool's Mate",
        ),
        "rnbqkbnr/ppp1pp1p/6p1/8/3Pp3/2P2P2/PP4PP/RNBQKBNR b KQkq -": (
            "A00",
            "Barnes Opening: Gedult Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/8/4p3/2N2P2/PPPP2PP/R1BQKBNR b KQkq -": (
            "A00",
            "Barnes Opening: Gedult Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/8/5P2/PPPPPKPP/RNBQ1BNR b kq -": (
            "A00",
            "Barnes Opening: Hammerschlag Variation",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/1P2P3/8/P1PP1PPP/RNBQKBNR b KQkq -": (
            "A00",
            "Caro-Kann Defense: Labahn Attack",
        ),
        "rnbqkbnr/pppppppp/8/8/8/7P/PPPPPPP1/RNBQKBNR b KQkq -": (
            "A00",
            "Clemenz Opening",
        ),
        "rnbqkbnr/ppppppp1/8/7p/6P1/7P/PPPPPP2/RNBQKBNR b KQkq -": (
            "A00",
            "Clemenz Opening: Spike Lee Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/P6P/8/1PPPPPP1/RNBQKBNR b KQkq -": (
            "A00",
            "Crab Opening",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/3P4/4P3/PPP2PPP/RNBQKBNR b KQkq -": (
            "A00",
            "Englund Gambit Declined: Reversed French Variation",
        ),
        "r1bq1rk1/ppp2ppp/2nb1n2/3pp3/P7/1PP1P1P1/1B1P1P1P/RN1QKBNR b KQ -": (
            "A00",
            "Formation: Cabbage Attack",
        ),
        "r1bq1rk1/ppp2ppp/2nb1n2/3pp3/8/PPPPPPP1/7P/RNBQKBNR b KQ -": (
            "A00",
            "Formation: Hippopotamus Attack",
        ),
        "r1bq1rk1/ppp2ppp/2nb1n2/3pp3/8/P2PP1PP/1PPN1PB1/R1BQK1NR b KQ -": (
            "A00",
            "Formation: Shy Attack",
        ),
        "rnbqkbnr/pppppppp/8/8/8/5P2/PPPPP1PP/RNBQKBNR b KQkq -": (
            "A00",
            "Gedult Opening",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/8/P6P/1PPPPPP1/RNBQKBNR b KQkq -": (
            "A00",
            "Global Opening",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/6P1/8/PPPPPP1P/RNBQKBNR w KQkq -": (
            "A00",
            "Grob Opening: Alessi Gambit",
        ),
        "rnbqkbnr/pppppp1p/8/6p1/5PP1/8/PPPPP2P/RNBQKBNR b KQkq -": (
            "A00",
            "Grob Opening: Double Grob Variation, Coca-Cola Gambit",
        ),
        "rnbqkbnr/pppppp1p/8/6p1/6P1/8/PPPPPP1P/RNBQKBNR w KQkq -": (
            "A00",
            "Grob Opening: Double Grob Variation",
        ),
        "rnbqkbnr/ppp1ppp1/8/3p3P/8/8/PPPPPPBP/RNBQK1NR b KQkq -": (
            "A00",
            "Grob Opening: Grob Gambit, Basman Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/6P1/8/PPPPPPBP/RNBQK1NR w KQkq -": (
            "A00",
            "Grob Opening: Grob Gambit Declined",
        ),
        "rn1qkbnr/ppp1pppp/8/3p4/2P3b1/8/PP1PPPBP/RNBQK1NR b KQkq -": (
            "A00",
            "Grob Opening: Grob Gambit, Fritz Gambit",
        ),
        "q3kbnr/p1pnpppp/8/8/2Pp2b1/8/PP1PPP1P/RNBQK1NR w KQk -": (
            "A00",
            "Grob Opening: Grob Gambit, Fritz Gambit, Romford Countergambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3p4/3p2P1/2P5/PP2PPBP/RNBQK1NR b KQkq -": (
            "A00",
            "Grob Opening: Grob Gambit, Keres Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/8/2p3P1/1P6/P2PPPBP/RNBQK1NR b KQkq -": (
            "A00",
            "Grob Opening: Grob Gambit, Richter-Grob Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/6P1/8/PPPPPPBP/RNBQK1NR b KQkq -": (
            "A00",
            "Grob Opening: Grob Gambit",
        ),
        "rnbqk2r/pp2nppp/2pb4/3p4/2PPp1P1/2N4P/PP2PPB1/R1BQK1NR w KQkq -": (
            "A00",
            "Grob Opening: Keene Defense, Main Line",
        ),
        "rnbqkbnr/pp3ppp/2p5/3pp3/6P1/7P/PPPPPPB1/RNBQK1NR w KQkq -": (
            "A00",
            "Grob Opening: Keene Defense",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/6P1/7P/PPPPPP2/RNBQKBNR w KQkq -": (
            "A00",
            "Grob Opening: London Defense",
        ),
        "rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR b KQkq -": (
            "A00",
            "Grob Opening",
        ),
        "rn1qkbnr/ppp1pppp/8/8/2Pp2b1/8/PP1PPPBP/RNBQK1NR w KQkq -": (
            "A00",
            "Grob Opening: Romford Countergambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p2P1/8/8/PPPPPPBP/RNBQK1NR b KQkq -": (
            "A00",
            "Grob Opening: Spike Attack",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/2P3P1/8/PP1PPPBP/RNBQK1NR b KQkq -": (
            "A00",
            "Grob Opening: Spike, Hurst Attack",
        ),
        "rnbqkbnr/ppp1pppp/8/8/4p1P1/2N5/PPPP1P1P/R1BQKBNR b KQkq -": (
            "A00",
            "Grob Opening: Zilbermintz Gambit",
        ),
        "rnbqkbnr/ppp1ppp1/8/7p/4p1P1/2N5/PPPP1P1P/R1BQKBNR w KQkq -": (
            "A00",
            "Grob Opening: Zilbermintz Gambit, Schiller Defense",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/4p1P1/2NP4/PPP2P1P/R1BQKBNR b KQkq -": (
            "A00",
            "Grob Opening: Zilbermintz Gambit, Zilbermintz-Hartlaub Gambit",
        ),
        "r1bqkbnr/ppp3pp/2n5/4Pp2/3pN3/6P1/PPP1PP1P/R1BQKBNR w KQkq f6": (
            "A00",
            "Hungarian Opening: Asten Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/1P6/6P1/P1PPPPBP/RNBQK1NR b KQkq -": (
            "A00",
            "Hungarian Opening: Bücker Gambit",
        ),
        "rnbqk1nr/ppp1bppp/8/3p4/4p2N/P2P2P1/1PP1PP1P/RNBQKB1R b KQkq -": (
            "A00",
            "Hungarian Opening: Burk Gambit",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/8/6P1/PPPPPPBP/RNBQK1NR w KQkq -": (
            "A00",
            "Hungarian Opening: Catalan Formation",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/8/6P1/PPPPPP1P/RNBQKBNR w KQkq -": (
            "A00",
            "Hungarian Opening: Dutch Defense",
        ),
        "rnbqkb1r/pppppppp/5n2/8/8/6P1/PPPPPP1P/RNBQKBNR w KQkq -": (
            "A00",
            "Hungarian Opening: Indian Defense",
        ),
        "rnbqkbnr/ppppppp1/8/7p/8/6P1/PPPPPP1P/RNBQKBNR w KQkq -": (
            "A00",
            "Hungarian Opening: Lasker Simul Special Variation",
        ),
        "rnbqkbnr/pppppp1p/8/6p1/8/6P1/PPPPPP1P/RNBQKBNR w KQkq -": (
            "A00",
            "Hungarian Opening: Myers Defense",
        ),
        "rnbqkbnr/ppppp2p/6p1/7Q/4p3/6P1/PPPP1P1P/RNB1KBNR w KQkq -": (
            "A00",
            "Hungarian Opening: Pachman Gambit",
        ),
        "rn1qkbnr/ppp2ppp/8/3p4/5p2/6PB/PPPPP2P/RNBQ1RK1 b kq -": (
            "A00",
            "Hungarian Opening: Paris Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/8/5NP1/PPPPPP1P/RNBQKB1R b KQkq -": (
            "A00",
            "Hungarian Opening: Reversed Alekhine Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/8/1P2p3/6P1/P1PPPP1P/RNBQKBNR b KQkq -": (
            "A00",
            "Hungarian Opening: Reversed Brooklyn Defense, Brooklyn Benko Gambit",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/8/6P1/PPPPPPBP/RNBQK1NR w KQkq -": (
            "A00",
            "Hungarian Opening: Reversed Modern Defense",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4p2N/6P1/PPPPPP1P/RNBQKB1R b KQkq -": (
            "A00",
            "Hungarian Opening: Reversed Norwegian Defense",
        ),
        "rnbqkbnr/pppppppp/8/8/8/6P1/PPPPPP1P/RNBQKBNR b KQkq -": (
            "A00",
            "Hungarian Opening",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/8/6P1/PPPPPP1P/RNBQKBNR w KQkq -": (
            "A00",
            "Hungarian Opening: Sicilian Invitation",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/8/6P1/PPPPPPBP/RNBQK1NR w KQkq -": (
            "A00",
            "Hungarian Opening: Slav Formation",
        ),
        "rnbqkbnr/pppppp1p/6p1/8/8/6P1/PPPPPP1P/RNBQKBNR w KQkq -": (
            "A00",
            "Hungarian Opening: Symmetrical Variation",
        ),
        "rnbqkbnr/ppppppp1/8/8/7p/5NP1/PPPPPP1P/RNBQKB1R w KQkq -": (
            "A00",
            "Hungarian Opening: van Kuijk Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/2p5/1P4P1/P2PPPBP/RNBQK1NR b KQkq -": (
            "A00",
            "Hungarian Opening: Winterberg Gambit",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/3P4/3BPN2/PPP2PPP/RNBQK2R w KQkq -": (
            "A00",
            "Indian Game: Colle System, King's Indian Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/7P/7R/PPPPPPP1/RNBQKBN1 b Qkq -": (
            "A00",
            "Kádas Opening: Beginner's Trap",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/1P5P/8/P1PPPPP1/RNBQKBNR b KQkq -": (
            "A00",
            "Kádas Opening: Kádas Gambit",
        ),
        "rnbqkbnr/pp2pppp/8/3p4/3p3P/2P2N2/PP2PPP1/RNBQKB1R b KQkq -": (
            "A00",
            "Kádas Opening: Kádas Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/3p3P/2P5/PP2PPP1/RNBQKBNR b KQkq -": (
            "A00",
            "Kádas Opening: Kádas Gambit",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/3PP2P/8/PPP2PP1/RNBQKBNR b KQkq -": (
            "A00",
            "Kádas Opening: Myers Variation",
        ),
        "rnbqkbnr/pppppppp/8/8/7P/8/PPPPPPP1/RNBQKBNR b KQkq -": (
            "A00",
            "Kádas Opening",
        ),
        "rnbqkbnr/pppppp1p/8/6p1/7P/8/PPPPPPP1/RNBQKBNR w KQkq -": (
            "A00",
            "Kádas Opening: Schneider Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/8/4p2P/3P4/PPP2PP1/RNBQKBNR b KQkq -": (
            "A00",
            "Kádas Opening: Steinbok Gambit",
        ),
        "rnbqkbnr/pppppp1p/6p1/8/6P1/3P4/PPP1PP1P/RNBQKBNR b KQkq -": (
            "A00",
            "Mieses Opening: Myers Spike Attack",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/8/3P4/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A00",
            "Mieses Opening: Reversed Rat Variation",
        ),
        "rnbqkbnr/pppppppp/8/8/8/3P4/PPP1PPPP/RNBQKBNR b KQkq -": (
            "A00",
            "Mieses Opening",
        ),
        "rn1qkbnr/ppp1pppp/8/3p1b2/1P6/8/PBPPPPPP/RN1QKBNR w KQkq -": (
            "A00",
            "Polish Opening: Baltic Defense",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/1P6/8/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A00",
            "Polish Opening: Birmingham Gambit",
        ),
        "rnbqkbnr/pppp2pp/5p2/1P2p3/8/8/PBPPPPPP/RN1QKBNR b KQkq -": (
            "A00",
            "Polish Opening: Bugayev Advance Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/1P6/P7/2PPPPPP/RNBQKBNR b KQkq -": (
            "A00",
            "Polish Opening: Bugayev Attack",
        ),
        "rnbqkbnr/ppp2ppp/3p4/4p3/1P6/8/PBPPPPPP/RN1QKBNR w KQkq -": (
            "A00",
            "Polish Opening: Czech Defense",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/1P6/8/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A00",
            "Polish Opening: Dutch Defense",
        ),
        "rnb1kbnr/ppp1pppp/3q4/3p4/1P6/8/PBPPPPPP/RN1QKBNR w KQkq -": (
            "A00",
            "Polish Opening: German Defense",
        ),
        "r1bqkbnr/pppppppp/2n5/8/1P6/8/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A00",
            "Polish Opening: Grigorian Variation",
        ),
        "rnbqkb1r/pppppppp/7n/8/1P6/8/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A00",
            "Polish Opening: Karniewski Variation",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/1P6/8/PBPPPPPP/RN1QKBNR w KQkq -": (
            "A00",
            "Polish Opening: King's Indian Variation",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/1P2P3/8/PBPP1PPP/RN1QKBNR b KQkq -": (
            "A00",
            "Polish Opening: King's Indian Variation, Schiffler Attack",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/PP6/8/1BPPPPPP/RN1QKBNR b KQkq -": (
            "A00",
            "Polish Opening: Myers Variation",
        ),
        "rnb1kbnr/ppp2ppp/3q4/4p3/1P2p3/P4P2/1BPP2PP/RN1QKBNR b KQkq -": (
            "A00",
            "Polish Opening: Orangutan-Diemer Gambit",
        ),
        "rnbqkb1r/1p3ppp/2p1pn2/P2p4/4P3/P2P4/1BP2PPP/RN1QKBNR b KQkq -": (
            "A00",
            "Polish Opening: Orangutan-Hartlaub Gambit",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/1P6/8/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A00",
            "Polish Opening: Outflank Variation",
        ),
        "rnbqkb1r/1ppp1ppp/p3pn2/1P6/8/8/PBPPPPPP/RN1QKBNR w KQkq -": (
            "A00",
            "Polish Opening: Queenside Defense",
        ),
        "rnbqkb1r/p1pp1ppp/1p2pn2/1P6/8/8/PBPPPPPP/RN1QKBNR w KQkq -": (
            "A00",
            "Polish Opening: Queen's Indian Variation",
        ),
        "rnbqkbnr/pppppppp/8/8/1P6/8/P1PPPPPP/RNBQKBNR b KQkq -": (
            "A00",
            "Polish Opening",
        ),
        "1nbqkb1r/1ppp1ppp/4pn2/1P6/8/8/2PPPPPP/BN1QKBNR b Kk -": (
            "A00",
            "Polish Opening: Rooks Swap Line",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/1P1p4/8/4P3/PBPP1PPP/RN1QKBNR b KQkq -": (
            "A00",
            "Polish Opening: Schiffler-Sokolsky Variation",
        ),
        "rnbqkbnr/1p1ppppp/8/pp6/4P3/8/PBPP1PPP/RN1QKBNR b KQkq -": (
            "A00",
            "Polish Opening: Schühler Gambit",
        ),
        "rnbqkbnr/p1pppppp/8/1p6/1P6/8/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A00",
            "Polish Opening: Symmetrical Variation",
        ),
        "r1b1k1nr/ppppq2p/2n2pp1/4pP2/1bB1P3/8/PBPP2PP/RN1QK1NR w KQkq -": (
            "A00",
            "Polish Opening: Tartakower Gambit, Brinckmann Variation",
        ),
        "rnbqkbnr/pppp2pp/5p2/4p3/1P2P3/8/PBPP1PPP/RN1QKBNR b KQkq -": (
            "A00",
            "Polish Opening: Tartakower Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/8/2p1p3/1P6/8/PBPPPPPP/RN1QKBNR w KQkq -": (
            "A00",
            "Polish Opening: Wolferts Gambit",
        ),
        "rnbqkbnr/pppppppp/8/8/8/2P5/PP1PPPPP/RNBQKBNR b KQkq -": (
            "A00",
            "Saragossa Opening",
        ),
        "rnbqk1nr/pp3ppp/8/2ppp3/8/P2PP3/P1P2PPP/1RBQKBNR b Kkq -": (
            "A00",
            "Sodium Attack: Celadon Variation",
        ),
        "rnbqkbnr/pppppp1p/6p1/8/6P1/N7/PPPPPP1P/R1BQKBNR b KQkq -": (
            "A00",
            "Sodium Attack: Chenoboskion Variation",
        ),
        "r1bqkbnr/pppp2pp/2n5/4pp2/2N1P3/8/PPPP1PPP/R1BQKBNR w KQkq -": (
            "A00",
            "Sodium Attack: Durkin Gambit",
        ),
        "rnbqkbnr/pppppppp/8/8/8/N7/PPPPPPPP/R1BQKBNR b KQkq -": (
            "A00",
            "Sodium Attack",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/8/3P4/PPPNPPPP/R1BQKBNR b KQkq -": (
            "A00",
            "Valencia Opening",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/8/P1N5/1PPPPPPP/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening: Battambang Variation",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/8/2N2N2/PPPPPPPP/R1BQKB1R w KQkq -": (
            "A00",
            "van Geet Opening: Billockus-Johansen Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/4P3/2N4P/PPPP1PP1/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening: Caro-Kann Variation, St. Patrick Attack",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/5P2/2N5/PPPPP1PP/R1BQKBNR w KQkq -": (
            "A00",
            "van Geet Opening: Damhaug Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/8/4p3/2N2P2/PPPP2PP/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening: Dougherty Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/8/4p3/2NP4/PPP2PPP/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening: Dunst-Perrenet Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/1P6/2N5/P1PPPPPP/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening: Düsseldorf Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/4p3/1PNP4/P1P2PPP/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening: Gladbacher Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/8/2B1p3/2N5/PPPP1PPP/R1BQK1NR b KQkq -": (
            "A00",
            "van Geet Opening: Hector Gambit",
        ),
        "r1bqkbnr/ppp2ppp/2np4/4P3/8/2N5/PPPPP1PP/R1BQKBNR w KQkq -": (
            "A00",
            "van Geet Opening: Hergert Gambit",
        ),
        "rn1qkbnr/ppp2ppp/4b3/3pp2Q/8/2N1P3/PPPP1PPP/R1B1KBNR w KQkq -": (
            "A00",
            "van Geet Opening: Hulsemann Gambit",
        ),
        "rnbqkb1r/pp2p1pp/5n2/2p2p2/1P1p1P2/5N2/P1PPPNPP/R1BQKB1R b KQkq -": (
            "A00",
            "van Geet Opening: Jendrossek Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/8/4p3/2NP4/PPP2PPP/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening: Klüver Gambit",
        ),
        "rnbqkbnr/p1pppppp/8/1p6/8/2N5/PPPPPPPP/R1BQKBNR w KQkq -": (
            "A00",
            "van Geet Opening: Laroche Gambit",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3pp2Q/8/2N1P3/PPPP1PPP/R1B1KBNR w KQkq -": (
            "A00",
            "van Geet Opening: Liebig Gambit",
        ),
        "rnbqkbnr/pp2pppp/8/2p5/3pNP2/8/PPPPP1PP/R1BQKBNR w KQkq -": (
            "A00",
            "van Geet Opening: Melleby Gambit",
        ),
        "rnbqkbnr/pppppp1p/6p1/8/7P/2N5/PPPPPPP1/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening: Myers Attack",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/3P4/2N2N2/PPP1PPPP/R1BQKB1R b KQkq -": (
            "A00",
            "van Geet Opening: Napoleon Attack",
        ),
        "r1bqkbnr/pp1ppppp/2n5/8/7Q/2N5/PPP1PPPP/R1B1KBNR b KQkq -": (
            "A00",
            "van Geet Opening: Novosibirsk Variation",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/3pNP2/8/PPPPP1PP/R1BQKBNR w KQkq -": (
            "A00",
            "van Geet Opening: Pfeiffer Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/3pNP2/5N2/PPPPP1PP/R1BQKB1R b KQkq -": (
            "A00",
            "van Geet Opening: Pfeiffer Gambit, Sleipnir Countergambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/8/2N5/PPPPPPPP/R1BQKBNR w KQkq -": (
            "A00",
            "van Geet Opening: Reversed Nimzowitsch Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/Q7/2N5/PPP1PPPP/R1B1KBNR b KQkq -": (
            "A00",
            "van Geet Opening: Reversed Scandinavian Variation",
        ),
        "rnbqkbnr/pppppppp/8/8/8/2N5/PPPPPPPP/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening",
        ),
        "r1bqkbnr/pp1ppppp/2n5/8/3N4/2N5/PPP1PPPP/R1BQKB1R b KQkq -": (
            "A00",
            "van Geet Opening: Sicilian Two Knights Variation",
        ),
        "rnbqk1nr/ppp2ppp/8/3pp3/1b1P4/2N1P3/PPP2PPP/R1BQKBNR w KQkq -": (
            "A00",
            "van Geet Opening: Sleipnir Gambit",
        ),
        "rnbqkb1r/pppppppp/5n2/8/6P1/2N5/PPPPPP1P/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening: Tübingen Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/8/2N5/PPPPPPPP/1RBQKBNR b Kkq -": (
            "A00",
            "van Geet Opening: Twyble Attack",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/8/2NP2P1/PPP1PP1P/R1BQKBNR b KQkq -": (
            "A00",
            "van Geet Opening: Venezolana Variation",
        ),
        "rnbqkbnr/ppp1pp1p/8/3p2p1/5P2/2N5/PPPPP1PP/R1BQKBNR w KQkq -": (
            "A00",
            "van Geet Opening: Warsteiner Gambit",
        ),
        "rnbqkbnr/p1pp1ppp/8/1p2p3/8/1B2P3/PPPP1PPP/RNBQK1NR b KQkq -": (
            "A00",
            "van 't Kruijs Opening: Bouncing Bishop Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/8/5p2/2N1PN2/PPPP2PP/R1BQKB1R b KQkq -": (
            "A00",
            "van 't Kruijs Opening: Keoni-Hiva Gambit, Akahi Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/5p2/2N1PN2/PPPP2PP/R1BQKB1R b KQkq -": (
            "A00",
            "van 't Kruijs Opening: Keoni-Hiva Gambit, Alua Variation",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3p4/5p2/P1N1PN2/1PPP2PP/R1BQKB1R b KQkq -": (
            "A00",
            "van 't Kruijs Opening: Delayed Keoni-Hiva Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3p4/5p2/2N1PN2/PPPP2PP/R1BQKB1R b KQkq -": (
            "A00",
            "van 't Kruijs Opening: Keoni-Hiva Gambit, Ekolu Variation",
        ),
        "rnbqkbnr/pppppppp/8/8/8/4P3/PPPP1PPP/RNBQKBNR b KQkq -": (
            "A00",
            "van 't Kruijs Opening",
        ),
        "r1bqkbnr/pp1ppppp/2n5/2p5/8/2NP2P1/PPP1PP1P/R1BQKBNR b KQkq -": (
            "A00",
            "Venezolana Opening",
        ),
        "r1bqkbnr/p1pnpppp/1p6/3p4/P2P4/2N5/1PP1PPPP/R1BQKBNR w KQkq -": (
            "A00",
            "Ware Opening: Cologne Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/P7/R7/1PPPPPPP/1NBQKBNR b Kkq -": (
            "A00",
            "Ware Opening: Meadow Hay Trap",
        ),
        "rnbqkbnr/pppppppp/8/8/P7/8/1PPPPPPP/RNBQKBNR b KQkq -": (
            "A00",
            "Ware Opening",
        ),
        "rnbqkbnr/ppp3pp/P7/3ppp2/8/4P3/1PPP1PPP/RNBQKBNR b KQkq -": (
            "A00",
            "Ware Opening: Ware Gambit",
        ),
        "rn1qkbnr/pbpppppp/8/1P6/8/8/1PPPPPPP/RNBQKBNR w KQkq -": (
            "A00",
            "Ware Opening: Wing Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/8/2N2N2/PPPPPPPP/R1BQKB1R b KQkq -": (
            "A00",
            "Zukertort Opening: Reversed Mexican Defense",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/8/1P6/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Classical Variation",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/8/1P6/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Dutch Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/8/1P6/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: English Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/8/BP6/P1PPPPPP/RN1QKBNR b KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Graz Attack",
        ),
        "rnbqkb1r/pppppppp/5n2/8/8/1P6/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Indian Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/8/1P2P3/PBPP1PPP/RN1QKBNR b KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Modern Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/8/1P6/PBPPPPPP/RN1QKBNR w KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Modern Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/8/1P6/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Modern Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/8/1P6/PBPPPPPP/RN1QKBNR b KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Modern Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/5P2/1P6/PBPPP1PP/RN1QKBNR b KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Pachman Gambit",
        ),
        "rnbqkbnr/pppp2pp/4p3/5p2/4P3/1P6/PBPP1PPP/RN1QKBNR b KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Ringelbach Gambit",
        ),
        "rnbqkbnr/pppppppp/8/8/8/1P6/P1PPPPPP/RNBQKBNR b KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/6P1/1P6/PBPPPP1P/RN1QKBNR b KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Spike Variation",
        ),
        "rnbqkbnr/p1pppppp/1p6/8/8/1P6/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Symmetrical Variation",
        ),
        "rnbqkbnr/p1pppppp/8/1p6/8/1P6/P1PPPPPP/RNBQKBNR w KQkq -": (
            "A01",
            "Nimzowitsch-Larsen Attack: Polish Variation",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/1P3P2/5N2/P1PPP1PP/RNBQKB1R b KQkq -": (
            "A02",
            "Bird Opening: Batavo-Polish Attack",
        ),
        "rnbqkbnr/ppp1p1pp/8/3p1p2/3P1P2/8/PPP1P1PP/RNBQKBNR w KQkq -": (
            "A02",
            "Bird Opening: Double Duck Formation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/5P2/2N5/PPPPP1PP/R1BQKBNR b KQkq -": (
            "A02",
            "Bird Opening: From Gambit, Bahr Gambit",
        ),
        "rnbqkb1r/ppp2ppp/3P1n2/8/8/8/PPPPP1PP/RNBQKBNR w KQkq -": (
            "A02",
            "Bird Opening: From Gambit, Langheld Gambit",
        ),
        "rnbqk1nr/ppp2p1p/3b4/6p1/8/5N2/PPPPP1PP/RNBQKB1R w KQkq -": (
            "A02",
            "Bird Opening: From Gambit, Lasker Variation",
        ),
        "rnbqk2r/ppp2ppp/3b3n/8/3P4/5N2/PPP1P1PP/RNBQKB1R b KQkq -": (
            "A02",
            "Bird Opening: From Gambit, Lipke Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/5P2/8/PPPPP1PP/RNBQKBNR w KQkq -": (
            "A02",
            "Bird Opening: From Gambit",
        ),
        "rnbqkbnr/pppppp1p/8/6p1/5P2/8/PPPPP1PP/RNBQKBNR w KQkq -": (
            "A02",
            "Bird Opening: Hobbs Gambit",
        ),
        "rnbqkbnr/pppppp2/7p/6p1/5P2/5N2/PPPPP1PP/RNBQKB1R w KQkq -": (
            "A02",
            "Bird Opening: Hobbs-Zilbermintz Gambit",
        ),
        "rnbqkb1r/pppppppp/7n/8/5P2/8/PPPPP1PP/RNBQKBNR w KQkq -": (
            "A02",
            "Bird Opening: Horsefly Defense",
        ),
        "rnbqkbnr/pppp2pp/5p2/4P3/8/8/PPPPP1PP/RNBQKBNR w KQkq -": (
            "A02",
            "Bird Opening: Lasker Gambit",
        ),
        "rnbqkb1r/pppppppp/5n2/8/2P2P2/8/PP1PP1PP/RNBQKBNR b KQkq -": (
            "A02",
            "Bird Opening: Mujannah Formation",
        ),
        "rnbqkbnr/p1pppppp/8/1p6/5P2/8/PPPPP1PP/RNBQKBNR w KQkq -": (
            "A02",
            "Bird Opening: Myers Defense",
        ),
        "rnbqkb1r/ppppnppp/8/4P3/8/8/PPPPP1PP/RNBQKBNR w KQkq -": (
            "A02",
            "Bird Opening: Platz Gambit",
        ),
        "rnbqkb1r/pppppppp/5n2/8/5P2/8/PPPPP1PP/RNBQKBNR w KQkq -": (
            "A02",
            "Bird Opening",
        ),
        "rnbqkbnr/pppppppp/8/8/5P2/8/PPPPP1PP/RNBQKBNR b KQkq -": (
            "A02",
            "Bird Opening",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4P3/8/8/PPPPP1PP/RNBQKBNR w KQkq -": (
            "A02",
            "Bird Opening: Schlechter Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/8/2p5/3p1P2/2P2N2/PP2P1PP/RNBQKB1R b KQkq -": (
            "A02",
            "Bird Opening: Siegener Gambit",
        ),
        "rnbqkb1r/ppppp1pp/5n2/8/4pPP1/2N5/PPPP3P/R1BQKBNR b KQkq -": (
            "A02",
            "Bird Opening: Swiss Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/4PP2/8/PPPP2PP/RNBQKBNR b KQkq -": (
            "A02",
            "Bird Opening: Wagner-Zwitersch Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/5PP1/8/PPPPP2P/RNBQKBNR b KQkq -": (
            "A03",
            "Bird Opening: Dutch Variation, Dudweiler Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/5P2/8/PPPPP1PP/RNBQKBNR w KQkq -": (
            "A03",
            "Bird Opening: Dutch Variation",
        ),
        "rnbqkb1r/pp2pppp/5n2/2pp4/5P2/4PN2/PPPP2PP/RNBQKB1R w KQkq -": (
            "A03",
            "Bird Opening: Lasker Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/2P2P2/8/PP1PP1PP/RNBQKBNR b KQkq -": (
            "A03",
            "Bird Opening: Sturm Gambit",
        ),
        "rnbqkb1r/pp2pppp/5n2/2p5/3p1P2/1P2PN2/PBPP2PP/RN1QKB1R b KQkq -": (
            "A03",
            "Bird Opening: Thomas Gambit",
        ),
        "rnbqkb1r/ppp1pppp/5n2/8/4pP2/2N5/PPPPQ1PP/R1B1KBNR b KQkq -": (
            "A03",
            "Bird Opening: Williams Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/4PP2/8/PPPP2PP/RNBQKBNR b KQkq -": (
            "A03",
            "Bird Opening: Williams Gambit",
        ),
        "rnbqkb1r/ppp1pppp/5n2/8/4pP2/2N5/PPPPN1PP/R1BQKB1R b KQkq -": (
            "A03",
            "Bird Opening: Williams-Zilbermintz Gambit",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1P5/8/4PN2/PPP2PPP/RNBQKB1R w KQkq -": (
            "A04",
            "Colle System: Rhamphorhynchus Variation",
        ),
        "rnb1k1nr/pp1pppbp/1q4p1/2p5/2PPP3/5N2/PP3PPP/RNBQKB1R w KQkq -": (
            "A04",
            "Modern Defense: Semi-Averbakh Variation, Polish Variation",
        ),
        "rnb1k1nr/pp2ppbp/3p2p1/q1P5/2P1P3/5N2/PP3PPP/RNBQKB1R w KQkq -": (
            "A04",
            "Modern Defense: Semi-Averbakh Variation, Pterodactyl Variation Accepted",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/2PPP3/5N2/PP3PPP/RNBQKB1R w KQkq -": (
            "A04",
            "Modern Defense: Semi-Averbakh Variation, Pterodactyl Variation",
        ),
        "rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq -": (
            "A04",
            "Zukertort Opening",
        ),
        "r1bqkb1r/pppppppp/n6n/8/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Drunken Cavalry Variation",
        ),
        "rnbqkb1r/pppppnpp/5p2/8/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Arctic Defense, Drunken Knight Variation",
        ),
        "rnbqkbnr/ppppp1pp/5p2/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Arctic Defense",
        ),
        "rnbqkbnr/ppppppp1/7p/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Basman Defense",
        ),
        "r1bqkbnr/pppppppp/2n5/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Black Mustang Defense",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Dutch Variation",
        ),
        "rnbqkbnr/pppppp1p/8/6p1/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Herrstrom Gambit",
        ),
        "rnbqkbnr/pppppp1p/6p1/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Kingside Fianchetto Variation",
        ),
        "rnbqkb1r/ppppp1pp/5n2/5p2/4P3/3P1N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "A04",
            "Zukertort Opening: Deferred Lisitsin Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "A04",
            "Zukertort Opening: Lisitsin Gambit",
        ),
        "rnbqkbnr/ppp1pppp/3p4/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Pirc Invitation",
        ),
        "rnbqkbnr/p1pppppp/8/1p6/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Polish Defense",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Queen's Gambit Invitation",
        ),
        "rnbqkbnr/p1pppppp/1p6/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Queenside Fianchetto Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Ross Gambit",
        ),
        "rnbqkbnr/3p1ppp/p3p3/1pp5/2P5/2N2NP1/PP1PPP1P/R1BQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Shabalov Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Sicilian Invitation",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Slav Invitation",
        ),
        "rnbqkbnr/pp1ppppp/8/8/3p4/4PN2/PPP2PPP/RNBQKB1R b KQkq -": (
            "A04",
            "Zukertort Opening: Speelsmet Gambit",
        ),
        "rnbqkbnr/1ppppppp/p7/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: St. George Defense",
        ),
        "r1bqkbnr/ppp2ppp/2p5/8/8/8/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: The Walrus",
        ),
        "rnbqkbnr/ppp2ppp/3p4/4p3/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Vos Gambit",
        ),
        "rn1qkbnr/ppp1pppp/3p4/8/4P1b1/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Wade Defense",
        ),
        "rnbqkbnr/1ppppppp/8/p7/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A04",
            "Zukertort Opening: Ware Defense",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/8/5NP1/PPPPPP1P/RNBQKB1R w KQkq -": (
            "A05",
            "King's Indian Attack",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/1P6/5NP1/P1PPPP1P/RNBQKB1R b KQkq -": (
            "A05",
            "King's Indian Attack: Smyslov Variation",
        ),
        "rnbqkb1r/p1pppppp/5n2/1p6/8/5NP1/PPPPPP1P/RNBQKB1R w KQkq -": (
            "A05",
            "King's Indian Attack: Spassky Variation",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/8/5NP1/PPPPPP1P/RNBQKB1R w KQkq -": (
            "A05",
            "King's Indian Attack: Symmetrical Defense",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p4/8/3P1NP1/PPP1PPBP/RNBQ1RK1 w - -": (
            "A05",
            "King's Indian Attack: Wahls Defense",
        ),
        "rnbqkb1r/pppppppp/5n2/8/1P6/5N2/P1PPPPPP/RNBQKB1R b KQkq -": (
            "A05",
            "Polish Opening: Zukertort System",
        ),
        "rnbqkb1r/pppppppp/5n2/8/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A05",
            "Zukertort Opening",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/8/1P3NP1/PBPPPPBP/RN1Q1RK1 b - -": (
            "A05",
            "Zukertort Opening: Double Fianchetto Attack",
        ),
        "rnbqkb1r/pppppppp/5n2/8/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "A05",
            "Zukertort Opening: Lemberger Gambit",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/PP6/5N2/2PPPPPP/RNBQKB1R b KQkq -": (
            "A05",
            "Zukertort Opening: Myers Polish Attack",
        ),
        "rnbqkb1r/pppppppp/5n2/8/8/1P3N2/P1PPPPPP/RNBQKB1R b KQkq -": (
            "A05",
            "Zukertort Opening: Nimzowitsch-Larsen Variation",
        ),
        "rnbqkb1r/pppppppp/5n2/8/8/4PN2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "A05",
            "Zukertort Opening: Quiet System",
        ),
        "r1bqkb1r/pppppppp/2n2n2/8/8/2N2N2/PPPPPPPP/R1BQKB1R w KQkq -": (
            "A05",
            "Zukertort Opening",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/8/1P3N2/P1PPPPPP/RNBQKB1R b KQkq -": (
            "A06",
            "Nimzowitsch-Larsen Attack: Classical Variation",
        ),
        "rnbqkb1r/pp2pppp/5n2/2pp4/4P3/1P3N2/PBPP1PPP/RN1QKB1R b KQkq -": (
            "A06",
            "Nimzowitsch-Larsen Attack: Norfolk Gambit",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/4P3/1P3N2/P1PP1PPP/RNBQKB1R b KQkq -": (
            "A06",
            "Nimzowitsch-Larsen Attack: Norfolk Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/8/5N2/PPPPPPPP/RNBQKB1R w KQkq -": (
            "A06",
            "Zukertort Opening",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/8/5N2/PPPPPPPP/RNBQKBR1 b Qkq -": (
            "A06",
            "Zukertort Opening: Ampel Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/8/3P1N2/PPP1PPPP/RNBQKB1R b KQkq -": (
            "A06",
            "Zukertort Opening: Old Indian Attack",
        ),
        "rnbqkbnr/pp2pppp/8/2p5/2p5/1P2PN2/P2P1PPP/RNBQKB1R b KQkq -": (
            "A06",
            "Zukertort Opening: Pachman Gambit",
        ),
        "rnbqkbnr/pp2pppp/8/2p5/2p5/1PN2N2/P2PPPPP/R1BQKB1R b KQkq -": (
            "A06",
            "Zukertort Opening: Regina-Nu Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/1P6/5N2/P1PPPPPP/RNBQKB1R b KQkq -": (
            "A06",
            "Zukertort Opening: Santasiere's Folly Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "A06",
            "Zukertort Opening: Tennison Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/P7/5N2/1PPPPPPP/RNBQKB1R b KQkq -": (
            "A06",
            "Zukertort Opening: The Potato",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2P5/5NP1/PP1PPP1P/RNBQKB1R w KQkq -": (
            "A07",
            "English Opening: Anglo-Indian Defense, Grünfeld Formation",
        ),
        "rnbqkbnr/ppp1pp1p/8/3p2p1/8/5NP1/PPPPPP1P/RNBQKB1R w KQkq -": (
            "A07",
            "Hungarian Opening: Wiedenhagen-Beta Gambit",
        ),
        "rnbqkbnr/ppp1pp1p/6p1/3p4/8/5NP1/PPPPPP1P/RNBQKB1R w KQkq -": (
            "A07",
            "King's Indian Attack: Double Fianchetto",
        ),
        "r2qkbnr/pppnpppp/8/3p4/6b1/5NP1/PPPPPPBP/RNBQK2R w KQkq -": (
            "A07",
            "King's Indian Attack: Keres Variation",
        ),
        "rn1qkbnr/ppp1pppp/8/3p4/6b1/5NP1/PPPPPP1P/RNBQKB1R w KQkq -": (
            "A07",
            "King's Indian Attack: Keres Variation",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/8/5NP1/PPPPPP1P/RNBQKB1R w KQkq -": (
            "A07",
            "King's Indian Attack: Omega-Delta Gambit",
        ),
        "rnbqk2r/ppp1npbp/6p1/3pp3/8/3P1NP1/PPP1PPBP/RNBQ1RK1 w kq -": (
            "A07",
            "King's Indian Attack: Pachman System",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/8/5NP1/PPPPPP1P/RNBQKB1R b KQkq -": (
            "A07",
            "King's Indian Attack",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/8/5NP1/PPPPPP1P/RNBQKB1R w KQkq -": (
            "A07",
            "King's Indian Attack: Sicilian Variation",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/3p4/6b1/5NP1/PPPPPPBP/RNBQ1RK1 w kq -": (
            "A07",
            "King's Indian Attack: Yugoslav Variation",
        ),
        "r1bqkbnr/pp2pppp/2n5/2pp4/8/5NP1/PPPPPPBP/RNBQK2R w KQkq -": (
            "A08",
            "King's Indian Attack: French Variation",
        ),
        "r1bq1rk1/pp2bppp/2n1pn2/2pp4/4P3/3P1NP1/PPPN1PBP/R1BQR1K1 b - -": (
            "A08",
            "King's Indian Attack: Sicilian Variation",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/8/5NP1/PPPPPPBP/RNBQK2R b KQkq -": (
            "A08",
            "King's Indian Attack: Sicilian Variation",
        ),
        "r1bqkbnr/pp3ppp/2n1p3/2pp4/3P4/5NP1/PPP1PPBP/RNBQ1RK1 b kq -": (
            "A08",
            "Zukertort Opening: Reversed Grünfeld Variation",
        ),
        "rnbqkbnr/pp2pppp/8/2p5/1PPp4/5N2/P2PPPPP/RNBQKB1R w KQkq -": (
            "A09",
            "Réti Opening: Advance Variation, Michel Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/8/2Pp4/5N2/PP1PPPPP/RNBQKB1R w KQkq -": (
            "A09",
            "Réti Opening: Advance Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/8/2Pp4/5N2/PP1PPPPP/RNBQKBR1 b Qkq -": (
            "A09",
            "Réti Opening: Penguin Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/8/2p5/5N2/PP1PPPPP/RNBQKB1R w KQkq -": (
            "A09",
            "Réti Opening: Réti Gambit Accepted",
        ),
        "rn1qkbnr/ppp1pppp/4b3/8/2p5/4PN2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "A09",
            "Réti Opening: Réti Gambit, Keres Variation",
        ),
        "rnbqkbnr/pp2pppp/8/2p5/1PPp4/4PN2/P2P1PPP/RNBQKB1R b KQkq -": (
            "A09",
            "Réti Opening: Reversed Blumenfeld Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/2P5/5N2/PP1PPPPP/RNBQKB1R b KQkq -": (
            "A09",
            "Réti Opening",
        ),
        "rnbqkbnr/p1p1pppp/8/1p1p4/2P5/5N2/PP1PPPPP/RNBQKB1R w KQkq -": (
            "A09",
            "Réti Opening: Zilbermintz Gambit",
        ),
        "r1bqkb1r/ppp1p1pp/2np1n2/5p2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "A10",
            "Dutch Defense: Krause Variation",
        ),
        "rnbqkbnr/pppp1p1p/6p1/4p3/2P1P3/8/PP1P1PPP/RNBQKBNR w KQkq -": (
            "A10",
            "English Opening: Adorjan Defense",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/2P1P3/8/PP1P1PPP/RNBQKBNR b KQkq -": (
            "A10",
            "English Opening: Anglo-Dutch Defense, Hickmann Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/2P5/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A10",
            "English Opening: Anglo-Dutch Defense",
        ),
        "rnbqkbnr/ppp1p1pp/3p4/5p2/2P1P3/5N2/PP1P1PPP/RNBQKB1R b KQkq -": (
            "A10",
            "English Opening: Anglo-Dutch Variation, Chabanon Gambit",
        ),
        "rnbqkb1r/ppppp1pp/5n2/5p2/2P1P3/2N5/PP1P1PPP/R1BQKBNR b KQkq -": (
            "A10",
            "English Opening: Anglo-Dutch Variation, Ferenc Gambit",
        ),
        "r1bqkbnr/pppppppp/2n5/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A10",
            "English Opening: Anglo-Lithuanian Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3P4/8/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A10",
            "English Opening: Anglo-Scandinavian Defense, Löhn Gambit",
        ),
        "rnb1kbnr/ppp1pppp/8/q7/8/2N5/PP1PPPPP/R1BQKBNR w KQkq -": (
            "A10",
            "English Opening: Anglo-Scandinavian Defense, Malvinas Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/2P5/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A10",
            "English Opening: Anglo-Scandinavian Defense",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3P4/8/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A10",
            "English Opening: Anglo-Scandinavian Defense, Schulz Gambit",
        ),
        "rnbqkbnr/pppppp1p/6p1/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A10",
            "English Opening: Great Snake Variation",
        ),
        "rnbqkbnr/p1pppppp/8/1p6/2P5/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A10",
            "English Opening: Jaenisch Gambit",
        ),
        "rnbq1rk1/1p3pbp/p1pp1np1/4p3/2P1P3/2NP2P1/PP2NPBP/R1BQ1RK1 w - -": (
            "A10",
            "English Opening: King's English Variation, Botvinnik System, Prickly Pawn Pass System",
        ),
        "rnbqk1nr/ppppppbp/8/6p1/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A10",
            "English Opening: Myers Variation",
        ),
        "rnbqkb1r/ppppp1pp/5n2/8/2P1p1P1/2N5/PP1P1P1P/R1BQKBNR b KQkq -": (
            "A10",
            "English Opening: Porcupine Variation",
        ),
        "rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR b KQkq -": (
            "A10",
            "English Opening",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/2P3P1/8/PP1PPP1P/RNBQKBNR b KQkq -": (
            "A10",
            "English Opening: Wade Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/4p1p1/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A10",
            "English Opening: Zilbermintz Gambit",
        ),
        "r1bq1rk1/pppn1pbp/5np1/4p3/2P5/2N1PN2/PP2BPPP/R1BQ1RK1 w - -": (
            "A10",
            "King's Indian Defense: Semi-Classical Variation, Exchange Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2PPP3/4BP2/PP4PP/RN1QKBNR b KQkq -": (
            "A10",
            "Modern Defense: Averbakh Variation, Pseudo-Sämisch",
        ),
        "rnbqk1nr/pppp1pbp/6p1/4p3/2PPP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "A10",
            "Modern Defense: Neo-Modern Defense",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A11",
            "English Opening: Caro-Kann Defensive System",
        ),
        "rnbqkb1r/pp2pp1p/2p2np1/3p4/2P5/1P3N2/PB1PPPPP/RN1QKB1R w KQkq -": (
            "A12",
            "Réti Opening: Anglo-Slav Variation, Bled Variation",
        ),
        "rn1qkbnr/pp2pppp/2p5/3p4/2P3b1/1P3N2/P2PPPPP/RNBQKB1R w KQkq -": (
            "A12",
            "Réti Opening: Anglo-Slav Variation, Bogoljubov Variation",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/3p4/2P5/1P3N2/PB1PPPPP/RN1QKB1R b KQkq -": (
            "A12",
            "Réti Opening: Anglo-Slav Variation, Bogoljubov Variation",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/2P5/1P3N2/P2PPPPP/RNBQKB1R b KQkq -": (
            "A12",
            "Réti Opening: Anglo-Slav Variation, Bogoljubov Variation",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/3p4/2P3b1/1P3N2/PB1PPPPP/RN1QKB1R w KQkq -": (
            "A12",
            "Réti Opening: Anglo-Slav Variation, Capablanca Variation",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/3p1b2/2P5/1P3NP1/P2PPP1P/RNBQKB1R w KQkq -": (
            "A12",
            "Réti Opening: Anglo-Slav Variation, London Defensive System",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/3p1b2/2P5/1P3N2/PB1PPPPP/RN1QKB1R w KQkq -": (
            "A12",
            "Réti Opening: Anglo-Slav Variation, New York System",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/3p4/2P3b1/1P3NP1/P2PPP1P/RNBQKB1R w KQkq -": (
            "A12",
            "Réti Opening: Anglo-Slav Variation, Torre System",
        ),
        "rnbqk2r/ppp2ppp/3bpn2/3p4/2P5/5NP1/PP1PPPBP/RNBQK2R w KQkq -": (
            "A13",
            "English Opening: Agincourt Defense, Bogoljubov Defense",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/8/2p5/5NP1/PP1PPPBP/RNBQK2R w KQkq -": (
            "A13",
            "English Opening: Agincourt Defense, Catalan Defense Accepted",
        ),
        "rn1qkbnr/pbp2ppp/1p2p3/3p4/2P5/5NP1/PP1PPPBP/RNBQ1RK1 b kq -": (
            "A13",
            "English Opening: Agincourt Defense, Catalan Defense",
        ),
        "rnbqkbnr/pp3ppp/4p3/2pp4/2P5/5NP1/PP1PPP1P/RNBQKB1R w KQkq -": (
            "A13",
            "English Opening: Agincourt Defense, Catalan Defense",
        ),
        "rnbqkb1r/pp3ppp/2p1pn2/3p4/2P5/5NP1/PP1PPPBP/RNBQK2R w KQkq -": (
            "A13",
            "English Opening: Agincourt Defense, Catalan Defense, Semi-Slav Defense",
        ),
        "rnbqkbnr/pp3ppp/2p1p3/3p4/2P5/5NP1/PP1PPP1P/RNBQKB1R w KQkq -": (
            "A13",
            "English Opening: Agincourt Defense, Kurajica Defense",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/2P5/5N2/PP1PPPPP/RNBQKB1R w KQkq -": (
            "A13",
            "English Opening: Agincourt Defense",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/2P5/5N2/PP1PPPPP/RNBQKB1R b KQkq -": (
            "A13",
            "English Opening: Agincourt Defense",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A13",
            "English Opening: Agincourt Defense",
        ),
        "r1bqk2r/pp2bppp/2n1pn2/2pp4/2P5/1P3NP1/P2PPPBP/RNBQ1RK1 w kq -": (
            "A13",
            "English Opening: Agincourt Defense, Tarrasch Defense",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2pp4/2P5/1P2PN2/PB1P1PPP/RN1QKB1R b KQkq -": (
            "A13",
            "English Opening: Agincourt Defense, Wimpy System",
        ),
        "rnbqk2r/ppp1bppp/4pn2/3p4/2P5/5NP1/PP1PPPBP/RNBQK2R w KQkq -": (
            "A13",
            "English Opening: Neo-Catalan Defense Declined",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/2P5/5NP1/PP1PPP1P/RNBQKB1R w KQkq -": (
            "A13",
            "English Opening: Neo-Catalan",
        ),
        "rnbqkb1r/2pp1ppp/p3pn2/1p6/2P5/5NP1/PP1PPPBP/RNBQK2R w KQkq -": (
            "A13",
            "English Opening: Romanishin Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A13",
            "Horwitz Defense: Zilbermintz Gambit",
        ),
        "r1bqk2r/pp2bppp/2n1p3/2pn4/8/2N2NP1/PP1PPPBP/R1BQ1RK1 w kq -": (
            "A14",
            "English Opening: Agincourt Defense, Keres Defense",
        ),
        "rnbqk2r/ppp1bppp/4pn2/3p4/2P5/5NP1/PP1PPPBP/RNBQ1RK1 b kq -": (
            "A14",
            "English Opening: Agincourt Defense, Neo-Catalan Declined",
        ),
        "rnbq1rk1/pp2bppp/2p1pn2/3p4/2P5/1P3NP1/PB1PPPBP/RN1Q1RK1 b - -": (
            "A14",
            "Réti Opening: Anglo-Slav Variation, Bogoljubov Variation, Stonewall Line",
        ),
        "rnbqk2r/ppppppbp/5np1/8/2P1P3/2N2N2/PP1P1PPP/R1BQKB1R b KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, Anti-Anti-Grünfeld Variation",
        ),
        "rn1qkb1r/pbpppp1p/1p3np1/8/2P5/5NP1/PP1PPPBP/RNBQK2R w KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, King's Indian Formation, Double Fianchetto Variation",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/2P5/5N2/PP1PPPPP/RNBQKB1R w KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, King's Indian Formation",
        ),
        "rnbqkb1r/pppppppp/5n2/8/2P5/5N2/PP1PPPPP/RNBQKB1R b KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, King's Knight Variation",
        ),
        "rnbqkb1r/ppp1pppp/3p1n2/8/2P5/5N2/PP1PPPPP/RNBQKB1R w KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, Old Indian Formation",
        ),
        "rnbqkb1r/pppppppp/5n2/8/1PP5/8/P2PPPPP/RNBQKBNR b KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, Orangutan Variation",
        ),
        "rn1qkb1r/pbpp1ppp/1p2pn2/8/2P5/5NP1/PP1PPPBP/RNBQK2R w KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, Queen's Indian Formation",
        ),
        "rnbqkb1r/p1pppppp/1p3n2/8/2P5/5N2/PP1PPPPP/RNBQKB1R w KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, Queen's Indian Formation",
        ),
        "rnbqkb1r/1ppp1ppp/p3pn2/8/2P5/5NP1/PP1PPP1P/RNBQKB1R w KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, Romanishin Variation",
        ),
        "rnbqkb1r/ppp1pppp/8/3n4/8/5N2/PP1PPPPP/RNBQKB1R w KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, Scandinavian Defense, Exchange Variation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/2P5/5N2/PP1PPPPP/RNBQKB1R w KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, Scandinavian Defense",
        ),
        "rnbqkb1r/pp1ppp1p/2p2np1/8/2P5/5NP1/PP1PPP1P/RNBQKB1R w KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense, Slav Formation",
        ),
        "rnbqkb1r/pppppppp/5n2/8/2P5/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A15",
            "English Opening: Anglo-Indian Defense",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/1PPP4/4PN2/PB3PPP/RN1QKB1R b KQ -": (
            "A15",
            "Polish Opening: King's Indian Variation, Sokolsky Attack",
        ),
        "rnbqk2r/ppp2pbp/6p1/3np3/8/2N2NP1/PP1PPPBP/R1BQK2R w KQkq -": (
            "A16",
            "English Opening: Anglo-Grünfeld Defense, Korchnoi Variation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq -": (
            "A16",
            "English Opening: Anglo-Grünfeld Defense",
        ),
        "rnbqkb1r/ppp1pp1p/1n4p1/8/8/2N3P1/PP1PPPBP/R1BQK1NR w KQkq -": (
            "A16",
            "English Opening: Anglo-Indian Defense, Anglo-Grünfeld Variation",
        ),
        "rnbqkb1r/ppp1pp1p/6p1/8/8/2n3P1/PP1PPPBP/R1BQK1NR w KQkq -": (
            "A16",
            "English Opening: Anglo-Indian Defense, Anglo-Grünfeld Variation",
        ),
        "rnbqkb1r/ppp1pppp/8/3n4/8/2N2N2/PP1PPPPP/R1BQKB1R b KQkq -": (
            "A16",
            "English Opening: Anglo-Indian Defense, Anglo-Grünfeld Variation",
        ),
        "rnbqkb1r/pppppppp/5n2/8/2P5/2N5/PP1PPPPP/R1BQKBNR b KQkq -": (
            "A16",
            "English Opening: Anglo-Indian Defense, Queen's Knight Variation",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/8/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq -": (
            "A17",
            "English Opening: Anglo-Indian Defense, Hedgehog System",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bP5/2N2N2/PP1PPPPP/R1BQKB1R w KQkq -": (
            "A17",
            "English Opening: Anglo-Indian Defense, Nimzowitsch-English Opening",
        ),
        "rnbqkb1r/p1pp1ppp/1p2pn2/8/2P5/2N2N2/PP1PPPPP/R1BQKB1R w KQkq -": (
            "A17",
            "English Opening: Anglo-Indian Defense, Queen's Indian Formation",
        ),
        "rn1qkb1r/pbpp1ppp/1p2pn2/8/2P1P3/2NB1N2/PP1P1PPP/R1BQK2R b KQkq -": (
            "A17",
            "English Opening: Anglo-Indian Defense, Queen's Indian Variation",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bP3P1/2N2N2/PP1PPP1P/R1BQKB1R b KQkq -": (
            "A17",
            "English Opening: Anglo-Indian Defense, Zvjaginsev-Krasenkow Attack",
        ),
        "r1bqkb1r/pppp1ppp/2n1pn2/8/2P1P3/2N5/PP1P1PPP/R1BQKBNR w KQkq -": (
            "A18",
            "English Opening: Mikėnas-Carls Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3pP3/2P5/2N5/PP1P1PPP/R1BQKBNR b KQkq -": (
            "A18",
            "English Opening: Mikėnas-Carls Variation",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/8/2P1P3/2N5/PP1P1PPP/R1BQKBNR b KQkq -": (
            "A18",
            "English Opening: Mikėnas-Carls Variation",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/2p1P3/2P5/2N5/PP1P1PPP/R1BQKBNR w KQkq -": (
            "A19",
            "English Opening: Anglo-Indian Defense, Flohr-Mikėnas-Carls Variation, Nei Gambit",
        ),
        "rnbqkb1r/pp1p1ppp/4pn2/2p5/2P1P3/2N5/PP1P1PPP/R1BQKBNR w KQkq -": (
            "A19",
            "English Opening: Mikėnas-Carls, Sicilian",
        ),
        "rnbqkbnr/pppp1pp1/8/4p2p/2P5/6P1/PP1PPP1P/RNBQKBNR w KQkq -": (
            "A20",
            "English Opening: Drill Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/8/2P1p3/5N2/PP1PPPPP/RNBQKB1R w KQkq -": (
            "A20",
            "English Opening: King's English Variation, Nimzowitsch-Flohr Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/2P5/5N2/PP1PPPPP/RNBQKB1R b KQkq -": (
            "A20",
            "English Opening: King's English Variation, Nimzowitsch Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/2P5/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A20",
            "English Opening: King's English Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/8/2P2p2/4PN2/PP1P2PP/RNBQKB1R b KQkq -": (
            "A20",
            "English Opening: King's English Variation, Kahiko-Hula Gambit",
        ),
        "rnbqkbnr/pp3ppp/2pp4/4p3/2P5/2N3P1/PP1PPP1P/R1BQKBNR w KQkq -": (
            "A21",
            "English Opening: King's English Variation, Keres Defense",
        ),
        "rnbqk1nr/pppp1ppp/8/4p3/1bP5/2N5/PP1PPPPP/R1BQKBNR w KQkq -": (
            "A21",
            "English Opening: King's English Variation, Kramnik-Shirov Counterattack",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR b KQkq -": (
            "A21",
            "English Opening: King's English Variation, Reversed Sicilian Variation",
        ),
        "rnbqkbnr/ppp2ppp/3p4/4p3/2P5/2N2N2/PP1PPPPP/R1BQKB1R b KQkq -": (
            "A21",
            "English Opening: King's English Variation",
        ),
        "rn1qkbnr/ppp2ppp/3p4/4p3/2P3b1/2N2N2/PP1PPPPP/R1BQKB1R w KQkq -": (
            "A21",
            "English Opening: King's English Variation, Smyslov Defense",
        ),
        "r2qkbnr/ppp2ppp/2npb3/4p3/2P5/2N3P1/PP1PPPBP/R1BQK1NR w KQkq -": (
            "A21",
            "English Opening: King's English Variation, Troger Defense",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2P5/2N3P1/PP1PPP1P/R1BQKBNR b KQkq -": (
            "A22",
            "English Opening: Carls-Bremen System",
        ),
        "rnbqkb1r/pppp1ppp/8/6N1/2P1p1n1/2N5/PP1PPPPP/R1BQKB1R w KQkq -": (
            "A22",
            "English Opening: King's English, Erbenheimer Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2P2P2/2N5/PP1PP1PP/R1BQKBNR b KQkq -": (
            "A22",
            "English Opening: King's English, Mazedonisch",
        ),
        "rnbqkb1r/p1pp1ppp/5n2/1p4N1/2P1p3/2N5/PP1PPPPP/R1BQKB1R w KQkq -": (
            "A22",
            "English Opening: King's English Variation, Bellon Gambit",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3pp3/2P5/2N3P1/PP1PPP1P/R1BQKBNR w KQkq -": (
            "A22",
            "English Opening: King's English Variation, Two Knights Variation, Reversed Dragon Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq -": (
            "A22",
            "English Opening: King's English Variation, Two Knights Variation",
        ),
        "rnbqk2r/pppp1ppp/5n2/4p3/1bP5/2N3P1/PP1PPP1P/R1BQKBNR w KQkq -": (
            "A22",
            "English Opening: King's English Variation, Two Knights Variation, Smyslov System",
        ),
        "rnbqkb1r/pp1p1ppp/2p2n2/4p3/2P5/2N3P1/PP1PPP1P/R1BQKBNR w KQkq -": (
            "A23",
            "English Opening: King's English Variation, Two Knights Variation, Keres Variation",
        ),
        "rnbqkb1r/pppp1p1p/5np1/4p3/2P5/2N3P1/PP1PPP1P/R1BQKBNR w KQkq -": (
            "A24",
            "English Opening: King's English Variation, Two Knights Variation, Fianchetto Line",
        ),
        "r1bqk2r/ppp2pbp/2np2pn/4p3/2P5/2N1P1P1/PP1PNPBP/R1BQK2R w KQkq -": (
            "A25",
            "English Opening: Closed Defense, Taimanov Variation",
        ),
        "r1bqk2r/pppp1pbp/2n3pn/4p3/2P5/2N3P1/PP1PPPBP/1RBQK1NR w Kkq -": (
            "A25",
            "English Opening: Closed Defense, Taimanov Variation",
        ),
        "r2qk1nr/ppp2pbp/2npb1p1/4p3/2P5/2N1P1P1/PP1PNPBP/R1BQK2R w KQkq -": (
            "A25",
            "English Opening: King's English Variation, Bremen-Hort Variation",
        ),
        "r1bqk1nr/pppp1pbp/2n3p1/4p3/2P5/2NP2P1/PP2PPBP/R1BQK1NR b KQkq -": (
            "A25",
            "English Opening: King's English Variation, Closed System",
        ),
        "r1bqk1nr/pppp1pbp/2n3p1/4p3/2P5/2N3P1/PP1PPPBP/1RBQK1NR b Kkq -": (
            "A25",
            "English Opening: King's English Variation, Hungarian Attack",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq -": (
            "A25",
            "English Opening: King's English Variation, Reversed Closed Sicilian Variation",
        ),
        "r1bqk1nr/pppp1pbp/2n3p1/4p3/2P5/2N3P1/PP1PPPBP/R1BQK1NR w KQkq -": (
            "A25",
            "English Opening: King's English Variation, Taimanov Variation",
        ),
        "r1bqk1nr/ppp2pbp/2np2p1/4p3/2P1P3/2NP2P1/PP3PBP/R1BQK1NR b KQkq -": (
            "A26",
            "English Opening: King's English Variation, Botvinnik System",
        ),
        "r1bqk1nr/ppp2pbp/2np2p1/4p3/2P5/2NP2P1/PP2PPBP/R1BQK1NR w KQkq -": (
            "A26",
            "English Opening: King's English Variation, Closed System, Full Symmetry Line",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/2P5/2N2N2/PP1PPPPP/R1BQKB1R b KQkq -": (
            "A27",
            "English Opening: King's English Variation, Three Knights System",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2P1P3/2N2N2/PP1P1PPP/R1BQKB1R b KQkq -": (
            "A28",
            "English Opening: Four Knights System, Nimzowitsch Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/8/2PPp3/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "A28",
            "English Opening: King's English Variation, Four Knights Variation, Bradley Beach Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2P5/2NP1N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "A28",
            "English Opening: King's English Variation, Four Knights Variation, Flexible Line",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2P5/P1N2N2/1P1PPPPP/R1BQKB1R b KQkq -": (
            "A28",
            "English Opening: King's English Variation, Four Knights Variation, Korchnoi Line",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/4p3/2P5/2b1PN2/PPQP1PPP/R1B1KB1R w KQkq -": (
            "A28",
            "English Opening: King's English Variation, Four Knights Variation, Quiet Line",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2P5/2N1PN2/PP1P1PPP/R1BQKB1R b KQkq -": (
            "A28",
            "English Opening: King's English Variation, Four Knights Variation, Quiet Line",
        ),
        "r1bqr1k1/pppp1ppp/2n2n2/3NpQ2/1bP5/4PN2/PP1P1PPP/R1B1KB1R b KQ -": (
            "A28",
            "English Opening: King's English Variation, Four Knights Variation, Quiet Line",
        ),
        "r1bqk2r/pppp1pp1/5n1p/4n3/2PN3B/2P5/P3PPPP/R2QKB1R w KQkq -": (
            "A28",
            "English Opening: King's English Variation, Four Knights Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2P5/2N2N2/PP1PPPPP/R1BQKB1R w KQkq -": (
            "A28",
            "English Opening: King's English Variation, Four Knights Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2P5/2N2NP1/PP1PPP1P/R1BQKB1R b KQkq -": (
            "A29",
            "English Opening: King's English Variation, Four Knights Variation, Fianchetto Line",
        ),
        "r2qk2r/1b1nbppp/pp1ppn2/8/2PQ4/1PN2NP1/P3PPBP/R1BR2K1 w kq -": (
            "A30",
            "English Opening: Symmetrical, Hedgehog, Flexible Formation",
        ),
        "rn1qk2r/pb1pbppp/1p2pn2/2p5/2P5/2N2NP1/PP1PPPBP/R1BQ1RK1 w kq -": (
            "A30",
            "English Opening: Symmetrical Variation, Hedgehog Defense",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2p5/1PP5/5N2/P2PPPPP/RNBQKB1R b KQkq -": (
            "A30",
            "English Opening: Symmetrical Variation, Napolitano Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/2P5/8/PP1PPPPP/RNBQKBNR w KQkq -": (
            "A30",
            "English Opening: Symmetrical Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/1PP5/8/P2PPPPP/RNBQKBNR b KQkq -": (
            "A30",
            "English Opening: Wing Gambit",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2p5/2PP4/5N2/PP2PPPP/RNBQKB1R b KQkq -": (
            "A31",
            "English Opening: Symmetrical Variation, Anti-Benoni Variation",
        ),
        "rnbqkb1r/pp1p1ppp/4pn2/8/2PN4/8/PP2PPPP/RNBQKB1R w KQkq -": (
            "A32",
            "English Opening: Symmetrical Variation, Anti-Benoni Variation, Spielmann Defense",
        ),
        "r1b1kb1r/pp1p1ppp/1qn1pn2/8/2PN4/2N3P1/PP2PP1P/R1BQKB1R w KQkq -": (
            "A33",
            "English Opening: Symmetrical Variation, Anti-Benoni Variation, Geller Variation",
        ),
        "r1bqkb1r/pp1p1ppp/2n1pn2/8/2PN4/2N5/PP2PPPP/R1BQKB1R w KQkq -": (
            "A33",
            "English Opening: Symmetrical Variation, Anti-Benoni Variation, Spielmann Defense",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2p5/2P5/2N3P1/PP1PPP1P/R1BQKBNR b KQkq -": (
            "A34",
            "English Opening: Symmetrical Variation, Fianchetto Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/2P5/2N5/PP1PPPPP/R1BQKBNR b KQkq -": (
            "A34",
            "English Opening: Symmetrical Variation, Normal Variation",
        ),
        "rnbqkb1r/ppn1pppp/8/2p5/8/2N3P1/PP1PPPBP/R1BQK1NR w KQkq -": (
            "A34",
            "English Opening: Symmetrical Variation, Rubinstein Variation",
        ),
        "rnbqkb1r/pp2pppp/8/2pn4/8/2N2N2/PP1PPPPP/R1BQKB1R w KQkq -": (
            "A34",
            "English Opening: Symmetrical Variation, Three Knights Variation",
        ),
        "r1bqkb1r/pp1ppppp/2n2n2/2p5/2P5/2N2N2/PP1PPPPP/R1BQKB1R w KQkq -": (
            "A35",
            "English Opening: Symmetrical Variation, Four Knights Variation",
        ),
        "r1bqkbnr/pp1ppppp/2n5/2p5/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq -": (
            "A35",
            "English Opening: Symmetrical Variation, Two Knights Variation",
        ),
        "r1bqk1nr/pp1pppbp/2n3p1/2p5/2P1P3/2N3P1/PP1P1PBP/R1BQK1NR b KQkq -": (
            "A36",
            "English Opening: Symmetrical Variation, Botvinnik System",
        ),
        "r1bqk1nr/pp1p1pbp/2n3p1/2p1p3/2P5/2N1P1P1/PP1P1PBP/R1BQK1NR w KQkq -": (
            "A36",
            "English Opening: Symmetrical Variation, Reversed Botvinnik System",
        ),
        "r1bqkbnr/pp1ppppp/2n5/2p5/2P5/2N3P1/PP1PPP1P/R1BQKBNR b KQkq -": (
            "A36",
            "English Opening: Symmetrical Variation, Fianchetto Variation",
        ),
        "r1bqk1nr/pp1pppbp/2n3p1/2p5/2P5/2N3P1/PP1PPPBP/R1BQK1NR w KQkq -": (
            "A36",
            "English Opening: Symmetrical Variation, Symmetrical Variation",
        ),
        "r1bqk1nr/pp1p1pbp/2n3p1/2p1p3/2P5/2N2NP1/PP1PPPBP/R1BQK2R w KQkq -": (
            "A37",
            "English Opening: Symmetrical Variation, Reversed Botvinnik System",
        ),
        "r1bqk1nr/pp1pppbp/2n3p1/2p5/2P5/2N2NP1/PP1PPPBP/R1BQK2R b KQkq -": (
            "A37",
            "English Opening: Symmetrical Variation, Two Knights Line",
        ),
        "r1bq1rk1/pp1pppbp/2n2np1/2p5/2P5/1PN2NP1/P2PPPBP/R1BQ1RK1 b - -": (
            "A38",
            "English Opening: Symmetrical Variation, Double Fianchetto",
        ),
        "r1bq1rk1/pp1pppbp/2n2np1/2p5/2P5/2NP1NP1/PP2PPBP/R1BQ1RK1 b - -": (
            "A38",
            "English Opening: Symmetrical Variation, Duchamp Variation",
        ),
        "r1bqk2r/pp1pppbp/2n2np1/2p5/2P5/2N2NP1/PP1PPPBP/R1BQK2R w KQkq -": (
            "A38",
            "English Opening: Symmetrical Variation, Full Symmetry Line",
        ),
        "r1bq1rk1/pp1pppbp/2n2np1/2p5/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 b - -": (
            "A39",
            "English Opening: Symmetrical Variation, Mecking Variation",
        ),
        "r1bqkbnr/pppppppp/n7/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Australian Defense",
        ),
        "rnbqk2r/pp2npbp/3p2p1/2pP4/4P3/2N2N2/PP3PPP/R1BQKB1R w KQkq -": (
            "A40",
            "Benoni Defense: Franco-Sicilian Hybrid Variation",
        ),
        "rnbqkbnr/pppppp1p/8/6p1/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Borg Defense: Borg Gambit",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/3P4/3BPN2/PPP2PPP/RNBQK2R w KQkq -": (
            "A40",
            "Colle System: Pterodactyl Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q7/3N4/3BP3/PPP2PPP/RNBQK2R w KQkq -": (
            "A40",
            "Colle System: Siroccopteryx Variation",
        ),
        "rnbqkbnr/pppp2pp/4p3/5p2/3P1BP1/8/PPP1PP1P/RN1QKBNR b KQkq -": (
            "A40",
            "Dutch Defense: Senechaud Gambit",
        ),
        "rnbqk2r/pp4pp/2pbpn2/3p1p2/2PP4/5NP1/PP2PPBP/RNBQ1RK1 w kq -": (
            "A40",
            "Dutch Defense: Stonewall Variation, Modern Variation",
        ),
        "rnbqkbnr/p2p2pp/4p3/1PpP1p2/4P3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "A40",
            "English Defense: Blumenfeld-Hiva Gambit",
        ),
        "rn1qkbnr/pbpp1ppp/1p6/4p3/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "A40",
            "English Defense: Eastbourne Gambit",
        ),
        "rn1qkb1r/pbpp2pp/1p2pn2/5P2/2PP4/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "A40",
            "English Defense: Hartlaub Gambit Accepted",
        ),
        "rn1qkbnr/pbpp2pp/1p2p3/3P1p2/2P1P3/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "A40",
            "English Defense: Hartlaub Gambit Declined",
        ),
        "r2qkbnr/pbpp1ppp/1pn1p3/8/2PPP3/3B4/PP3PPP/RNBQK1NR w KQkq -": (
            "A40",
            "English Defense: Perrin Variation",
        ),
        "rn1qkb1r/pbpp2pp/1p2p2n/5P2/2PP4/5P2/PP4PP/RNBQKBNR w KQkq -": (
            "A40",
            "English Defense: Poli Gambit",
        ),
        "rnbqkbnr/p1pp1ppp/1p2p3/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "English Defense",
        ),
        "rnbqkbnr/p1pppppp/1p6/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "English Defense",
        ),
        "rnb1k1nr/pppp1ppp/8/2bPp3/4P2q/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "A40",
            "Englund Gambit Complex Declined: Diemer Counterattack",
        ),
        "rnbqkbnr/pppp1ppp/8/3Pp3/8/8/PPP1PPPP/RNBQKBNR b KQkq -": (
            "A40",
            "Englund Gambit Complex Declined",
        ),
        "r1b1kbnr/ppppqppp/2n5/4P3/8/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A40",
            "Englund Gambit Complex: Englund Gambit",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b1P3/8/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A40",
            "Englund Gambit Complex: Felbecker Gambit",
        ),
        "rnbqkbnr/ppp2ppp/3p4/4P3/8/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Englund Gambit Complex: Hartlaub-Charlick Gambit",
        ),
        "rnb1kbnr/pppp1ppp/8/4P3/7q/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Englund Gambit Complex: Mosquito Gambit",
        ),
        "r1bqkbnr/pppp2pp/2n2p2/4P3/8/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A40",
            "Englund Gambit Complex: Deferred Soller Gambit",
        ),
        "rnbqkbnr/pppp2pp/5p2/4P3/8/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Englund Gambit Complex: Soller Gambit",
        ),
        "r1b1kbnr/ppppqppp/2n5/3QP3/8/5N2/PPP1PPPP/RNB1KB1R b KQkq -": (
            "A40",
            "Englund Gambit Complex: Stockholm Variation",
        ),
        "r1bqkb1r/ppppnppp/2n5/4P3/8/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A40",
            "Englund Gambit Complex: Zilbermintz Gambit",
        ),
        "r1bqkbnr/pppp1pp1/2n4p/4P3/8/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A40",
            "Englund Gambit Complex: Zilbermintz Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/3P4/5N2/PPP1PPPP/RNBQKB1R b KQkq -": (
            "A40",
            "Englund Gambit Declined: Reversed Alekhine Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/8/3Pp3/8/PPP1PPPP/RNBQKBNR b KQkq -": (
            "A40",
            "Englund Gambit Declined: Reversed Brooklyn Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/8/3Pp3/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A40",
            "Englund Gambit Declined: Reversed Krebs Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4N3/3Pp3/8/PPP1PPPP/RNBQKB1R b KQkq -": (
            "A40",
            "Englund Gambit Declined: Reversed Mokele Mbembe Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Englund Gambit",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Horwitz Defense",
        ),
        "rnbqk1nr/pppp1ppp/4p3/8/1bPP4/2N5/PP2PPPP/R1BQKBNR b KQkq -": (
            "A40",
            "Kangaroo Defense: Keres Defense, Transpositional Variation",
        ),
        "rnbqk1nr/pppp1ppp/4p3/8/1bPP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Kangaroo Defense",
        ),
        "r1bqkbnr/pppp1ppp/8/3Pp3/2Pn4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Mikėnas Defense: Cannstatter Variation",
        ),
        "r1bqkbnr/ppppnppp/8/3Pp3/2P5/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Mikėnas Defense: Lithuanian Variation",
        ),
        "r1bqkbnr/pppp1ppp/8/8/2n5/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "A40",
            "Mikėnas Defense: Pozarek Gambit",
        ),
        "r1bqkbnr/pppppppp/2n5/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Mikėnas Defense",
        ),
        "rnbqk1nr/pp1pp2p/6p1/2pP1p2/2P5/2P5/P3PPPP/R1BQKBNR w KQkq -": (
            "A40",
            "Modern Defense: Beefeater Variation",
        ),
        "rnbqkb1r/pppppp1p/5np1/7P/3P4/8/PPP1PPP1/RNBQKBNR b KQkq -": (
            "A40",
            "Modern Defense: Lizard Defense, Pirc-Diemer Gambit",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/3P4/5NP1/PPP1PPBP/RNBQK2R w KQkq -": (
            "A40",
            "Modern Defense: Queen's Pterodactyl Formation",
        ),
        "rnbqkbnr/pppppp1p/6p1/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Modern Defense",
        ),
        "rnbqkbnr/pppppppp/8/3P4/8/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Montevideo Defense",
        ),
        "rnbqkbnr/p1pppppp/8/1p6/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Polish Defense",
        ),
        "rn1qkbnr/pbpppppp/8/1B6/3PP3/8/PPP2PPP/RNBQK1NR b KQkq -": (
            "A40",
            "Polish Defense: Spassky Gambit Accepted",
        ),
        "rnb1k1nr/pp2pp1p/3p2p1/q1pP4/2P1P3/2P5/P4PPP/R1BQKBNR w KQkq -": (
            "A40",
            "Modern Defense: Pterodactyl Defense, Benoni Gambit Accepted, Beefeater Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1pP4/2P1P3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "A40",
            "Modern Defense: Pterodactyl Defense, Central Benoni Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1pP4/2P5/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "A40",
            "Modern Defense: Pterodactyl Defense, Queen's Benoni Variation",
        ),
        "rnb1k1nr/pp1ppp1p/6p1/q1pP4/2P5/2P5/P3PPPP/R1BQKBNR w KQkq -": (
            "A40",
            "Modern Defense: Pterodactyl Defense, Queen's Pteranodon Variation",
        ),
        "rnbqk1nr/pp1pppbp/6p1/2p5/2PP4/2N1P3/PP3PPP/R1BQKBNR b KQkq -": (
            "A40",
            "Modern Defense: Pterodactyl Defense, Quiet Line",
        ),
        "rnbqkbnr/pp2pppp/2pp4/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A40",
            "Queen's Pawn Game: Anglo-Slav Opening",
        ),
        "r1b1kb1r/ppppq1pp/2n2n2/3Q4/8/5N2/PPP1PPPP/RNB1KB1R w KQkq -": (
            "A40",
            "Queen's Pawn Game: Englund Gambit",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q7/3P1B2/5N2/PP2PPPP/RN1QKB1R w KQkq -": (
            "A40",
            "Queen's Pawn Game: London System, Pterodactyl Variation",
        ),
        "rnbqk1nr/ppp1ppbp/6p1/3p4/3P4/2N2N2/PPP1PPPP/R1BQKB1R w KQkq -": (
            "A40",
            "Queen's Pawn Game: Veresov Attack, Fianchetto Defense",
        ),
        "rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq -": (
            "A40",
            "Queen's Pawn Game",
        ),
        "rnbqkb1r/p2ppppp/2p2n2/1p6/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "A40",
            "Slav-Indian Defense: Kudischewitsch Gambit",
        ),
        "rn1qkbnr/1bpp1ppp/p3p3/1p6/3PP3/3B1N2/PPP2PPP/RNBQK2R w KQkq -": (
            "A40",
            "St. George Defense: Polish Variation",
        ),
        "rnbqkbnr/pppppppp/8/3PP3/8/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "A40",
            "Zaire Defense",
        ),
        "rnbqkb1r/pppppp1p/6pn/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A40",
            "Zukertort Defense: Kingside Variation",
        ),
        "rn1qkbnr/ppp2ppp/3pb3/4P3/2P5/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A41",
            "English Rat Defense: Pound Gambit",
        ),
        "rnbqkbnr/ppp2ppp/3p4/4p3/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "A41",
            "King's Pawn Game: Maróczy Defense",
        ),
        "rnbqk1nr/ppp1ppbp/3p2p1/8/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "A41",
            "Modern Defense",
        ),
        "rnbqkbnr/ppp1pppp/3p4/8/2PP4/8/PP2PPPP/RNBQKBNR b KQkq -": (
            "A41",
            "Old Indian Defense",
        ),
        "rnbqkbnr/ppp1pppp/3p4/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A41",
            "Queen's Pawn Game",
        ),
        "r1bqkbnr/ppp2ppp/2np4/4P3/2P5/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A41",
            "Rat Defense: English Rat Defense, Lisbon Gambit",
        ),
        "rnbqkbnr/ppp2ppp/3p4/4p3/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A41",
            "Rat Defense: English Rat Defense",
        ),
        "rn1qk1nr/ppp1ppbp/3p2p1/8/2PPP1b1/5N2/PP3PPP/RNBQKB1R w KQkq -": (
            "A41",
            "Robatsch Defense",
        ),
        "rn1qkbnr/ppp1pppp/3p4/8/3P2b1/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A41",
            "Wade Defense",
        ),
        "1r1qkbnr/pppnpppp/3p4/8/2PP2b1/1Q3N2/PP2PPPP/RNB1KB1R w KQk -": (
            "A41",
            "Zukertort Opening: Wade Defense, Chigorin Plan",
        ),
        "rnbqk1nr/ppp1ppbp/3p2p1/8/2PPP3/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "A42",
            "Modern Defense: Averbakh System",
        ),
        "r1bqk1nr/ppp1ppbp/2np2p1/8/2PPP3/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "A42",
            "Modern Defense: Kotov Variation",
        ),
        "rnbqk1nr/ppp1p1bp/3p2p1/5p2/2PPP3/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "A42",
            "Modern Defense: Randspringer Variation",
        ),
        "rnb1k1nr/pp2ppbp/3p2p1/q1p5/2PPP3/2N5/PP2NPPP/R1BQKB1R w KQkq -": (
            "A42",
            "Pterodactyl Defense: Central Variation, Bogolubovia Variation",
        ),
        "rnb1k1nr/pp2ppbp/3p2p1/q1p5/2PPP3/2N2N2/PP3PPP/R1BQKB1R w KQkq -": (
            "A42",
            "Pterodactyl Defense",
        ),
        "rnbqkbnr/pp1ppppp/8/2P5/8/8/PPP1PPPP/RNBQKBNR b KQkq -": (
            "A43",
            "Benoni Defense: Benoni Gambit Accepted",
        ),
        "r1bqkbnr/pp1ppppp/n7/2P5/8/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A43",
            "Benoni Defense: Benoni Gambit, Schlenker Defense",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2pP4/8/5N2/PPP1PPPP/RNBQKB1R b KQkq -": (
            "A43",
            "Benoni Defense: Benoni-Indian Defense, Kingside Move Order",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2pP4/8/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A43",
            "Benoni Defense: Benoni-Indian Defense",
        ),
        "rnbqkbnr/pp1pp1pp/8/2pP1p2/4P3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "A43",
            "Benoni Defense: Benoni-Staunton Gambit",
        ),
        "rnbqkbnr/p2ppppp/1p6/2P5/8/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A43",
            "Benoni Defense: Cormorant Gambit",
        ),
        "rnbqkb1r/pp1ppppp/5n2/3P4/2p5/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A43",
            "Benoni Defense: Hawk Variation",
        ),
        "rnbqkbnr/pp2pppp/3p4/2pP4/8/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A43",
            "Benoni Defense: Old Benoni Defense",
        ),
        "rnbqkbnr/pp2pp1p/3p2p1/2pP4/8/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "A43",
            "Benoni Defense: Old Benoni Defense, Schmid Variation",
        ),
        "r1bqkbnr/pp1ppppp/n7/2pP4/8/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A43",
            "Benoni Defense: Snail Variation",
        ),
        "rnb1kb1r/pp1ppppp/5n2/q1pP4/8/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "A43",
            "Benoni Defense: Woozle Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/1P1P4/8/P1P1PPPP/RNBQKBNR b KQkq -": (
            "A43",
            "Benoni Defense: Zilbermintz-Benoni Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/8/1P1p4/5N2/P1P1PPPP/RNBQKB1R b KQkq -": (
            "A43",
            "Benoni Defense: Zilbermintz-Benoni Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/8/4p3/1P1p4/5N2/P1P1PPPP/RNBQKB1R w KQkq -": (
            "A43",
            "Benoni Defense: Zilbermintz-Benoni Gambit, Tamarkin Countergambit",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/2pP4/4P3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "A43",
            "Benoni Defense: French Benoni Defense",
        ),
        "rnbqkb1r/p2ppppp/5n2/1ppP4/8/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A43",
            "Indian Game: Pseudo-Benko Variation",
        ),
        "rnbqkbnr/pp1pp1pp/8/2pP1p2/8/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A43",
            "Benoni Defense: Old Benoni Defense, Mujannah Formation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A43",
            "Benoni Defense: Old Benoni Defense",
        ),
        "rnbqkbnr/pp1ppppp/8/2pP4/8/8/PPP1PPPP/RNBQKBNR b KQkq -": (
            "A43",
            "Benoni Defense: Old Benoni Defense",
        ),
        "rnbqkbnr/pp1ppppp/8/8/2Pp4/4P3/PP3PPP/RNBQKBNR b KQkq -": (
            "A43",
            "Queen's Pawn Game: Liedmann Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/8/2pPp3/8/8/PPP1PPPP/RNBQKBNR w KQkq e6": (
            "A44",
            "Benoni Defense: Old Benoni Defense",
        ),
        "rnbqkbnr/pp3ppp/3p4/2pPp3/4P3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "A44",
            "Benoni Defense: Semi-Benoni Defense",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/2NQ4/PPP1PPPP/R1B1KBNR b KQkq -": (
            "A45",
            "Amazon Attack: Siberian Attack",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/8/3Pp3/2N2P2/PPP3PP/R1BQKBNR w KQkq -": (
            "A45",
            "Blackmar-Diemer Gambit Declined: O'Kelly Defense",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/8/3Pp3/2N2P2/PPP3PP/R1BQKBNR w KQkq -": (
            "A45",
            "Blackmar-Diemer Gambit Declined: Weinsbach Declination",
        ),
        "rnbqkb1r/pppppppp/5n2/8/3P2P1/8/PPP1PP1P/RNBQKBNR b KQkq -": (
            "A45",
            "Bronstein Gambit",
        ),
        "rnbqkb1r/pppppppp/5n2/8/3P1P2/8/PPP1P1PP/RNBQKBNR b KQkq -": (
            "A45",
            "Canard Opening",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P2P1/5P2/PPP1P2P/RNBQKBNR b KQkq -": (
            "A45",
            "Indian Game: Paleface Attack, Gedult Attack",
        ),
        "rnbqkb1r/pppppppp/8/8/3P2n1/8/PPP1PP1P/RNBQKBNR w KQkq -": (
            "A45",
            "Indian Game: Gibbins-Wiedenhagen Gambit Accepted",
        ),
        "rnbqkb1r/pppppppp/5n2/8/3PP3/5P2/PPP4P/RNBQKBNR b KQkq -": (
            "A45",
            "Indian Game: Gibbins-Wiedenhagen Gambit, Maltese Falcon Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/3P2P1/8/PPP1PP1P/RNBQKBNR w KQkq -": (
            "A45",
            "Indian Game: Gibbins-Wiedenhagen Gambit, Oshima Defense",
        ),
        "rnbqkb1r/ppp1pppp/3p1n2/8/3PP3/2N5/PPP1BP1P/R1BQK1NR b KQkq -": (
            "A45",
            "Indian Game: Gibbins-Wiedenhagen Gambit, Stummer Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/3P4/8/PPPNPPPP/R1BQKBNR w KQkq -": (
            "A45",
            "Indian Game: Lazard Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "A45",
            "Indian Game: Maddigan Gambit",
        ),
        "rnbqkb1r/pppppppp/5n2/6B1/3P4/3B4/PPP2PPP/RN1QK1NR b KQkq -": (
            "A45",
            "Indian Game: Omega Gambit, Arafat Gambit",
        ),
        "rnbqkb1r/pppppppp/5n2/8/3PP3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "A45",
            "Indian Game: Omega Gambit",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3PP3/5P2/PPP3PP/RNBQKBNR b KQkq -": (
            "A45",
            "Indian Game: Paleface Attack, Deferred Blackmar-Diemer Gambit",
        ),
        "rnbqkb1r/pppppppp/5n2/3P4/8/8/PPP1PPPP/RNBQKBNR b KQkq -": (
            "A45",
            "Indian Game: Pawn Push Variation",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2p5/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "A45",
            "Indian Game: Reversed Chigorin Defense",
        ),
        "rnbqkb1r/pppppppp/5n2/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A45",
            "Indian Game",
        ),
        "rnbqkb1r/pppppppp/5n2/8/3P4/6P1/PPP1PP1P/RNBQKBNR b KQkq -": (
            "A45",
            "Indian Game: Tartakower Attack",
        ),
        "rnbqkb1r/pppppppp/5n2/8/3P4/5P2/PPP1P1PP/RNBQKBNR b KQkq -": (
            "A45",
            "Paleface Attack",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "A45",
            "Queen's Pawn Game: Chigorin Variation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/2N2P2/PPP1P1PP/R1BQKBNR b KQkq -": (
            "A45",
            "Queen's Pawn Game: Chigorin Variation, Richter Attack",
        ),
        "rnbqkb1r/pppppp1p/8/6p1/3PnB2/8/PPP1PPPP/RN1QKBNR w KQkq -": (
            "A45",
            "Trompowsky Attack: Borg Variation",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/6B1/3PP3/8/PPP2PPP/RN1QKBNR b KQkq -": (
            "A45",
            "Trompowsky Attack: Classical Defense, Big Center Variation",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/6B1/3P4/8/PPP1PPPP/RN1QKBNR w KQkq -": (
            "A45",
            "Trompowsky Attack: Classical Defense",
        ),
        "rn1qkb1r/ppp1pppp/5n2/3p1b2/3PP2B/2N2P2/PPP3PP/R2QKBNR b KQkq -": (
            "A45",
            "Trompowsky Attack: Edge Variation, Hergert Gambit",
        ),
        "rnb1kb1r/pp2pppp/2p5/q2p4/3PP2B/2P5/PP1Q1PPP/R3KBNR b KQkq -": (
            "A45",
            "Trompowsky Attack: Edge Variation, Hergert Gambit",
        ),
        "rnbqkb1r/pppppppp/8/8/3Pn2B/8/PPP1PPPP/RN1QKBNR b KQkq -": (
            "A45",
            "Trompowsky Attack: Edge Variation",
        ),
        "rnb1kb1r/pp1ppppp/1q3n2/2pP2B1/8/2N5/PPP1PPPP/R2QKBNR b KQkq -": (
            "A45",
            "Trompowsky Attack: Poisoned Pawn Variation",
        ),
        "rnbqkb1r/pppp1ppp/8/4p1P1/3P4/8/PPP1PPP1/RN1QKBNR w KQkq -": (
            "A45",
            "Trompowsky Attack: Raptor Variation, Hergert Gambit",
        ),
        "rnbqkb1r/pppppppp/8/6B1/3Pn2P/8/PPP1PPP1/RN1QKBNR b KQkq -": (
            "A45",
            "Trompowsky Attack: Raptor Variation",
        ),
        "rnbqkb1r/pppppppp/5n2/6B1/3P4/8/PPP1PPPP/RN1QKBNR b KQkq -": (
            "A45",
            "Trompowsky Attack",
        ),
        "rnbqkb1r/pppppppp/8/8/3Pn3/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A46",
            "Döry Defense",
        ),
        "rnbqkb1r/pp1ppppp/2p2n2/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A46",
            "Indian Game: Czech-Indian",
        ),
        "rnbqkb1r/1ppppppp/p4n2/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A46",
            "Indian Game: Knights Variation, Alburt-Miles Variation",
        ),
        "rnbqkb1r/pppppppp/5n2/8/3P4/5N2/PPP1PPPP/RNBQKB1R b KQkq -": (
            "A46",
            "Indian Game: Knights Variation",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/8/3P1B2/5N2/PPP1PPPP/RN1QKB1R b KQkq -": (
            "A46",
            "Indian Game: London System",
        ),
        "rnbqkb1r/p1pppppp/5n2/1p6/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A46",
            "Indian Game: Polish Variation",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2p5/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A46",
            "Indian Game: Spielmann-Indian",
        ),
        "rnbqkb1r/ppp1pppp/3p1n2/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A46",
            "Indian Game: Wade-Tartakower Defense",
        ),
        "rnbqkb1r/pp2pppp/2pp1n2/8/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "A46",
            "Old Indian Defense: Czech Variation",
        ),
        "rn1qkb1r/ppp1pppp/3p1n2/8/2PP2b1/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "A46",
            "Old Indian Defense: Tartakower-Indian",
        ),
        "rnb1kb1r/pp3ppp/1q2pn2/2pp2B1/3P4/2P1PN2/PP3PPP/RN1QKB1R w KQkq -": (
            "A46",
            "Queen's Pawn Game: Torre Attack, Breyer Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p2B1/3P4/2N2N2/PPP1PPPP/R2QKB1R b KQkq -": (
            "A46",
            "Queen's Pawn Game: Veresov Attack, Classical Defense",
        ),
        "rnbqkb1r/pppp1pp1/4pn1p/6B1/3P4/5N2/PPP1PPPP/RN1QKB1R w KQkq -": (
            "A46",
            "Torre Attack: Classical Defense, Nimzowitsch Variation",
        ),
        "rnbqkb1r/p2p1ppp/1p2pn2/2pP2B1/8/4PN2/PPP2PPP/RN1QKB1R b KQkq -": (
            "A46",
            "Torre Attack: Classical Defense, Petrosian Gambit",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/6B1/3P4/5N2/PPP1PPPP/RN1QKB1R b KQkq -": (
            "A46",
            "Torre Attack",
        ),
        "rnbqkb1r/pp1p1ppp/4pn2/2p3B1/3PP3/5N2/PPP2PPP/RN1QKB1R b KQkq -": (
            "A46",
            "Torre Attack: Wagner Gambit",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/8/3P4/4PN2/PPP2PPP/RNBQKB1R b KQkq -": (
            "A46",
            "Yusupov-Rubinstein System",
        ),
        "rnbqkb1r/p1pp1ppp/1p3n2/4p3/3P4/2P2N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "A47",
            "Indian Game: Schnepper Gambit",
        ),
        "rn1qkb1r/pb1ppppp/1p3n2/2p5/3P4/5NP1/PPP1PPBP/RNBQK2R w KQkq -": (
            "A47",
            "Marienbad System",
        ),
        "rn1qkb1r/pb1ppppp/1p3n2/8/2PQ4/5NP1/PP2PPBP/RNB1K2R b KQkq -": (
            "A47",
            "Queen's Indian Defense: Marienbad System, Berg Variation",
        ),
        "rnbqkb1r/p1pppppp/1p3n2/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A47",
            "Queen's Indian Defense",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A48",
            "East Indian Defense",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/3P1B2/5N2/PPP1PPPP/RN1QKB1R b KQkq -": (
            "A48",
            "London System",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p4/3P1B2/2N1PN2/PPP1BPPP/R2QK2R b KQ -": (
            "A48",
            "Queen's Pawn Game: Barry Attack, Grünfeld Variation",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p2B1/3P4/4PN2/PPPN1PPP/R2QKB1R w KQ -": (
            "A48",
            "Queen's Pawn Game: Torre Attack, Grünfeld Variation, Main Line",
        ),
        "rnbqk2r/pp1pppbp/5np1/2p3B1/3P4/5N2/PPPNPPPP/R2QKB1R w KQkq -": (
            "A48",
            "Torre Attack: Fianchetto Defense, Euwe Variation",
        ),
        "rnbqkb1r/pppppp1p/5np1/6B1/3P4/5N2/PPP1PPPP/RN1QKB1R b KQkq -": (
            "A48",
            "Torre Attack",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/3P4/5NP1/PPP1PP1P/RNBQKB1R b KQkq -": (
            "A49",
            "Indian Game: Przepiórka Variation",
        ),
        "rnb2rk1/pp2ppbp/1qpp1np1/8/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "A49",
            "King's Indian Defense: Fianchetto Variation, Benjamin Defense",
        ),
        "rnbqkb1r/pppppp1p/5n2/6p1/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A50",
            "Indian Game: Medusa Gambit",
        ),
        "rnbqkb1r/pppppppp/5n2/8/2PP4/8/PP2PPPP/RNBQKBNR b KQkq -": (
            "A50",
            "Indian Game: Normal Variation",
        ),
        "rnbqkb1r/p1pppppp/5n2/1p6/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A50",
            "Indian Game: Pyrenees Gambit",
        ),
        "r1bqkb1r/pppppppp/5n2/3Pn3/2P2P2/8/PP2P1PP/RNBQKBNR b KQkq -": (
            "A50",
            "Mexican Defense: Horsefly Gambit",
        ),
        "r1bqkb1r/pppppppp/2n2n2/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A50",
            "Mexican Defense",
        ),
        "rnbqkb1r/p1pppppp/1p3n2/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A50",
            "Queen's Indian Defense: Accelerated Variation",
        ),
        "rnbqkb1r/pp1ppppp/2p2n2/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A50",
            "Slav-Indian Defense",
        ),
        "rnbqkb1r/p1pp1ppp/1p6/4P3/2P1n3/P7/1P2PPPP/RNBQKBNR w KQkq -": (
            "A51",
            "Indian Game: Budapest Defense, Fajarowicz Defense, Bonsdorf Variation",
        ),
        "rnbqkb1r/pppp1ppp/8/4P3/2P1n3/8/PPQ1PPPP/RNB1KBNR b KQkq -": (
            "A51",
            "Indian Game: Budapest Defense, Fajarowicz-Steiner Variation",
        ),
        "rnbqkb1r/pppp1ppp/8/4P3/2P1n3/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A51",
            "Indian Game: Budapest Defense, Fajarowicz Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A51",
            "Indian Game: Budapest Defense",
        ),
        "rnbqkb1r/pppp1ppp/8/4P3/2P3n1/5N2/PP2PPPP/RNBQKB1R b KQkq -": (
            "A52",
            "Indian Game: Budapest Defense, Adler Variation",
        ),
        "rnbqkb1r/pppp1ppp/2n5/8/2P1PP2/8/PP4PP/RNBQKBNR w KQkq -": (
            "A52",
            "Indian Game: Budapest Defense, Alekhine Variation, Abonyi Variation",
        ),
        "rnbqkb1r/pppp1ppp/8/4P3/2P1P1n1/8/PP3PPP/RNBQKBNR b KQkq -": (
            "A52",
            "Indian Game: Budapest Defense, Alekhine Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p4/4P3/2P1P1n1/8/PP3PPP/RNBQKBNR w KQkq -": (
            "A52",
            "Indian Game: Budapest Defense, Alekhine Variation, Tartakower Defense",
        ),
        "rnbqkb1r/pppp1ppp/8/4P3/2P3n1/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A52",
            "Indian Game: Budapest Defense",
        ),
        "rnbqkb1r/pppp1ppp/8/4P3/2P2Bn1/8/PP2PPPP/RN1QKBNR b KQkq -": (
            "A52",
            "Indian Game: Budapest Defense, Rubinstein Variation",
        ),
        "rnbqkb1r/ppp1pppp/3p1n2/8/2PP2P1/8/PP2PP1P/RNBQKBNR b KQkq -": (
            "A53",
            "Old Indian Defense: Aged Gibbon Gambit",
        ),
        "rnbqkb1r/pp2pppp/2pp1n2/8/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "A53",
            "Old Indian Defense: Czech Variation",
        ),
        "rn1qkb1r/ppp1pppp/3p1n2/5b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "A53",
            "Old Indian Defense: Janowski Variation, Fianchetto Variation",
        ),
        "rn1qkb1r/ppp1pppp/3p1n2/5b2/2PP4/2N3P1/PP2PP1P/R1BQKBNR b KQkq -": (
            "A53",
            "Old Indian Defense: Janowski Variation, Fianchetto Variation",
        ),
        "rn1qkb1r/ppp1pppp/3p1n2/5b2/2PPP3/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "A53",
            "Old Indian Defense: Janowski Variation, Grinberg Gambit",
        ),
        "rn1qkb1r/ppp1pppp/3p1n2/5b2/2PP4/2N2P2/PP2P1PP/R1BQKBNR b KQkq -": (
            "A53",
            "Old Indian Defense: Janowski Variation, Main Line",
        ),
        "rn1qkb1r/ppp1pppp/3p1n2/5b2/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "A53",
            "Old Indian Defense: Janowski Variation",
        ),
        "rnbqkb1r/ppp1pppp/3p1n2/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A53",
            "Old Indian Defense",
        ),
        "r1bqkb1r/pppn1ppp/3p1n2/4p3/2PP4/2NBP3/PP3PPP/R1BQK1NR b KQkq -": (
            "A54",
            "Old Indian Defense: Dus-Khotimirsky Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/4p3/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "A54",
            "Old Indian Defense: Two Knights Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/4p3/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "A54",
            "Old Indian Defense: Ukrainian Variation",
        ),
        "r1bqkb1r/pppn1ppp/3p1n2/4p3/2PPP3/2N2N2/PP3PPP/R1BQKB1R b KQkq -": (
            "A55",
            "Old Indian Defense: Normal Variation",
        ),
        "rnbqkb1r/pp1p1ppp/5n2/2pPp3/2P5/8/PP2PPPP/RNBQKBNR w KQkq e6": (
            "A56",
            "Benoni Defense: Czech Benoni Defense",
        ),
        "rnbqkb1r/pp2pppp/3p1n2/2pP4/2P5/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A56",
            "Benoni Defense: Hromádka System",
        ),
        "rnbqkb1r/pp3p1p/3p1np1/2pPp3/2P1P3/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "A56",
            "Benoni Defense: King's Indian System",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2p5/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A56",
            "Benoni Defense",
        ),
        "rnbqkb1r/pp1p1ppp/4pn2/2P5/2P5/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A56",
            "Benoni Defense: Weenink Variation",
        ),
        "r1bq1rk1/pp2ppbp/2n2np1/3p4/2PP4/2N2N2/PP2BPPP/R1BQ1RK1 w - -": (
            "A56",
            "Grünfeld Defense: Three Knights Variation, Burille Variation, Reversed Tarrasch Variation",
        ),
        "rnbqkb1r/pp1ppppp/8/2pP4/2P1n3/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A56",
            "Vulture Defense",
        ),
        "rnbqkb1r/3ppppp/p4n2/1PpP4/8/5P2/PP2P1PP/RNBQKBNR b KQkq -": (
            "A57",
            "Benko Gambit Accepted: Dlugy Variation",
        ),
        "rnbqkb1r/3ppppp/p4n2/1PpP4/8/4P3/PP3PPP/RNBQKBNR b KQkq -": (
            "A57",
            "Benko Gambit Accepted: Modern Variation",
        ),
        "rnbqkb1r/3ppppp/pP3n2/2pP4/8/8/PP2PPPP/RNBQKBNR b KQkq -": (
            "A57",
            "Benko Gambit Accepted: Pawn Return Variation",
        ),
        "rnbqkb1r/3ppppp/p4n2/1PpP4/8/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A57",
            "Benko Gambit Accepted",
        ),
        "rnbqkb1r/p2ppppp/5n2/1ppP2B1/2P5/8/PP2PPPP/RN1QKBNR b KQkq -": (
            "A57",
            "Benko Gambit Declined: Bishop's Attack",
        ),
        "rnbqkb1r/p2ppppp/5n2/1ppP4/2P1P3/8/PP3PPP/RNBQKBNR b KQkq -": (
            "A57",
            "Benko Gambit Declined: Hjørring Countergambit",
        ),
        "rnbqkb1r/p2ppppp/5n2/1ppP4/2P5/5N2/PP2PPPP/RNBQKB1R b KQkq -": (
            "A57",
            "Benko Gambit Declined: Main Line",
        ),
        "rnbqkb1r/p2ppppp/5n2/1ppP4/2P5/5P2/PP2P1PP/RNBQKBNR b KQkq -": (
            "A57",
            "Benko Gambit Declined: Pseudo-Sämisch Variation",
        ),
        "rnbqkb1r/p2ppppp/5n2/1ppP4/2P5/8/PP1NPPPP/R1BQKBNR b KQkq -": (
            "A57",
            "Benko Gambit Declined: Quiet Line",
        ),
        "rnbqkb1r/p2ppppp/5n2/1ppP4/P1P5/8/1P2PPPP/RNBQKBNR b KQkq -": (
            "A57",
            "Benko Gambit Declined: Sosonko Variation",
        ),
        "rnbqkb1r/p2ppppp/5n2/1ppP4/2P3P1/8/PP2PP1P/RNBQKBNR b KQkq -": (
            "A57",
            "Benko Gambit: Mutkin Countergambit",
        ),
        "rnbqkb1r/4pppp/3p1n2/1NpP4/1pB1P3/8/PP3PPP/R1BQK1NR b KQkq -": (
            "A57",
            "Benko Gambit: Nescafé Frappe Attack",
        ),
        "rnbqkb1r/p2ppppp/5n2/1ppP4/2P5/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A57",
            "Benko Gambit",
        ),
        "rnbqkb1r/3ppppp/p4n2/1PpP4/8/2N5/PP2PPPP/R1BQKBNR b KQkq -": (
            "A57",
            "Benko Gambit: Zaitsev System",
        ),
        "rnbqkb1r/3ppppp/5n2/1NpP4/1p2P3/8/PP3PPP/R1BQKBNR b KQkq -": (
            "A57",
            "Benko Gambit: Zaitsev Variation, Nescafé Frappe Attack",
        ),
        "rn1qkb1r/3ppp1p/b4np1/2pP4/5P2/2N5/PP2P1PP/R1BQKBNR b KQkq -": (
            "A58",
            "Benko Gambit Accepted: Central Storming Variation",
        ),
        "rn1qk2r/4ppbp/b2p1np1/2pP4/8/2N2NP1/PP2PPBP/R1BQK2R b KQkq -": (
            "A58",
            "Benko Gambit Accepted: Fianchetto Variation",
        ),
        "rnbqkb1r/3ppppp/P4n2/2pP4/8/8/PP2PPPP/RNBQKBNR b KQkq -": (
            "A58",
            "Benko Gambit Accepted: Fully Accepted Variation",
        ),
        "rn1qkb1r/4pp1p/b2p1np1/2pP4/8/2N2NP1/PP2PP1P/R1BQKB1R b KQkq -": (
            "A58",
            "Benko Gambit: Fianchetto Variation",
        ),
        "rn1qkb1r/4pp1p/b2p1np1/2pP4/8/2N5/PP1NPPPP/R1BQKB1R b KQkq -": (
            "A58",
            "Benko Gambit: Nd2 Variation",
        ),
        "rn1q1rk1/4ppbp/3p1np1/2pP4/4P3/2N2NP1/PP3PKP/R1BQ3R b - -": (
            "A59",
            "Benko Gambit Accepted: King Walk Variation",
        ),
        "rn1qkb1r/4pp1p/3p1np1/2pP4/4P3/2N5/PP2NPPP/R1BQ1K1R b kq -": (
            "A59",
            "Benko Gambit Accepted: Yugoslav Variation",
        ),
        "rn1qkb1r/4pppp/b2p1n2/2pP4/4P3/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "A59",
            "Benko Gambit Accepted: Yugoslav Variation",
        ),
        "rn1qkb1r/4pp1p/3p1np1/2pP4/4P3/2N3P1/PP3P1P/R1BQ1KNR b kq -": (
            "A59",
            "Benko Gambit",
        ),
        "rnbqkb1r/pp1p1ppp/4pn2/2pP4/2P5/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A60",
            "Benoni Defense: Modern Variation",
        ),
        "rnbqk2r/pp1p1ppp/3b1n2/2pP4/8/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "A60",
            "Benoni Defense: Modern Variation, Snake Variation",
        ),
        "rnbqkb1r/pp3p1p/3p1np1/2pP4/8/2N2NP1/PP2PP1P/R1BQKB1R b KQkq -": (
            "A61",
            "Benoni Defense: Fianchetto Variation",
        ),
        "rnbqkb1r/pp3p1p/3p1np1/2pP4/8/2N5/PP1NPPPP/R1BQKB1R b KQkq -": (
            "A61",
            "Benoni Defense: Knight's Tour Variation",
        ),
        "rnbqkb1r/pp3p1p/3p1np1/2pP4/8/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "A61",
            "Benoni Defense",
        ),
        "rnbqkb1r/pp3p1p/3p1np1/2pP2B1/8/2N2N2/PP2PPPP/R2QKB1R b KQkq -": (
            "A61",
            "Benoni Defense: Uhlmann Variation",
        ),
        "rnbq1rk1/pp3pbp/3p1np1/2pP4/8/2N2NP1/PP2PPBP/R1BQK2R w KQ -": (
            "A62",
            "Benoni Defense: Fianchetto Variation",
        ),
        "r1bq1rk1/pp1n1pbp/3p1np1/2pP4/8/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "A63",
            "Benoni Defense: Fianchetto Variation, Hastings Defense",
        ),
        "r1bqr1k1/1p1n1pbp/p2p1np1/2pP4/P7/2N3P1/1P1NPPBP/R1BQ1RK1 w - -": (
            "A64",
            "Benoni Defense: Fianchetto Variation, Hastings Defense, Main Line",
        ),
        "rnbqkb1r/pp3ppp/3p1n2/2pP4/4P3/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "A65",
            "Benoni Defense: King's Pawn Line",
        ),
        "rnbqk2r/pp3pbp/3p1np1/2pPP3/5P2/2N5/PP4PP/R1BQKBNR b KQkq -": (
            "A66",
            "Benoni Defense: Mikėnas Variation",
        ),
        "rnbqkb1r/pp3p1p/3p1np1/2pP4/4PP2/2N5/PP4PP/R1BQKBNR b KQkq -": (
            "A66",
            "Benoni Defense: Pawn Storm Variation",
        ),
        "rnbqk2r/pp3pbp/3p1np1/1BpP4/4PP2/2N5/PP4PP/R1BQK1NR b KQkq -": (
            "A67",
            "Benoni Defense: Taimanov Variation",
        ),
        "rnbq1rk1/pp3pbp/3p1np1/2pP4/4PP2/2N2N2/PP4PP/R1BQKB1R w KQ -": (
            "A68",
            "Benoni Defense: Four Pawns Attack",
        ),
        "rnbqr1k1/pp3pbp/3p1np1/2pP4/4PP2/2N2N2/PP2B1PP/R1BQK2R w KQ -": (
            "A69",
            "Benoni Defense: Four Pawns Attack, Main Line",
        ),
        "rnbqk2r/pp3pbp/3p1np1/2pP4/4P3/2N2N1P/PP3PP1/R1BQKB1R b KQkq -": (
            "A70",
            "Benoni Defense: Classical Variation, New York Variation",
        ),
        "rnbqkb1r/pp3p1p/3p1np1/2pP4/4P3/2N2N2/PP3PPP/R1BQKB1R b KQkq -": (
            "A70",
            "Benoni Defense: Classical Variation",
        ),
        "rnbqk2r/pp3pbp/3p1np1/2pP4/4P3/2N2N2/PP2BPPP/R1BQK2R b KQkq -": (
            "A70",
            "Benoni Defense: Classical Variation, Traditional Variation",
        ),
        "rnbqk2r/pp3pbp/3p1np1/2pP2B1/4P3/2N2N2/PP3PPP/R2QKB1R b KQkq -": (
            "A71",
            "Benoni Defense: Classical Variation, Averbakh-Grivas Attack",
        ),
        "rnbq1rk1/pp3pbp/3p1np1/2pP4/4P3/2N2N2/PP2BPPP/R1BQK2R w KQ -": (
            "A72",
            "Benoni Defense: Classical Variation",
        ),
        "rnbq1rk1/pp3pbp/3p1np1/2pP4/4P3/2N2N2/PP2BPPP/R1BQ1RK1 b - -": (
            "A73",
            "Benoni Defense: Classical Variation, Main Line",
        ),
        "rnbq1rk1/1p3pbp/p2p1np1/2pP4/P3P3/2N2N2/1P2BPPP/R1BQ1RK1 b - -": (
            "A74",
            "Benoni Defense: Classical Variation, Full Line",
        ),
        "rn1q1rk1/1p3pbp/p2p1np1/2pP4/P3P1b1/2N2N2/1P2BPPP/R1BQ1RK1 w - -": (
            "A75",
            "Benoni Defense: Classical Variation, Argentine Counterattack",
        ),
        "rnbqr1k1/pp3pbp/3p1np1/2pP4/4P3/2N2N2/PP2BPPP/R1BQ1RK1 w - -": (
            "A76",
            "Benoni Defense: Classical Variation, Czerniak Defense",
        ),
        "rnbqr1k1/pp3pbp/3p1np1/2pP4/4P3/2N5/PP1NBPPP/R1BQ1RK1 b - -": (
            "A77",
            "Benoni Defense: Classical Variation, Czerniak Defense, Tal Line",
        ),
        "r1bqr1k1/pp3pbp/n2p1np1/2pP4/4P3/2N5/PP1NBPPP/R1BQ1RK1 w - -": (
            "A78",
            "Benoni Defense: Classical Variation, Czerniak Defense",
        ),
        "r1bqr1k1/pp3pbp/n2p1np1/2pP4/4P3/2N2P2/PP1NB1PP/R1BQ1RK1 b - -": (
            "A79",
            "Benoni Defense: Classical Variation, Czerniak Defense",
        ),
        "rnbqkbnr/ppp1p1pp/8/5p2/3Pp3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "A80",
            "Blackmar-Diemer Gambit: Netherlands Variation",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/3P4/3Q4/PPP1PPPP/RNB1KBNR b KQkq -": (
            "A80",
            "Dutch Defense: Alapin Variation",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/3P2P1/8/PPP1PP1P/RNBQKBNR w KQkq -": (
            "A80",
            "Dutch Defense: Hevendehl Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/5pB1/3P4/8/PPP1PPPP/RN1QKBNR b KQkq -": (
            "A80",
            "Dutch Defense: Hopton Attack",
        ),
        "rnbqkb1r/ppppp1pp/5n2/5p2/3P2P1/7P/PPP1PP2/RNBQKBNR b KQkq -": (
            "A80",
            "Dutch Defense: Janzen-Korchnoi Gambit",
        ),
        "rnbqkbnr/ppp1p1pp/8/3p1p2/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "A80",
            "Dutch Defense: Kingfisher Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/3P4/7P/PPP1PPP1/RNBQKBNR b KQkq -": (
            "A80",
            "Dutch Defense: Korchnoi Attack",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/3P2P1/8/PPP1PP1P/RNBQKBNR b KQkq -": (
            "A80",
            "Dutch Defense: Krejcik Gambit",
        ),
        "rnbqkbnr/ppp1p1pp/8/3p4/3PP1p1/2N5/PPP2P1P/R1BQKBNR b KQkq -": (
            "A80",
            "Dutch Defense: Krejcik Gambit, Tate Gambit",
        ),
        "rnbqkbnr/pppp2pp/4p3/5p2/3P2P1/3Q4/PPP1PP1P/RNB1KBNR b KQkq -": (
            "A80",
            "Dutch Defense: Manhattan Gambit, Anti-Classical Line",
        ),
        "rnbqkbnr/ppppp2p/6p1/5p2/3P2P1/3Q4/PPP1PP1P/RNB1KBNR b KQkq -": (
            "A80",
            "Dutch Defense: Manhattan Gambit, Anti-Leningrad Variation",
        ),
        "rnbqkbnr/ppp1p1pp/3p4/5p2/3P2P1/3Q4/PPP1PP1P/RNB1KBNR b KQkq -": (
            "A80",
            "Dutch Defense: Manhattan Gambit, Anti-Modern Variation",
        ),
        "rnbqkbnr/ppp1p1pp/8/3p1p2/3P2P1/3Q4/PPP1PP1P/RNB1KBNR b KQkq -": (
            "A80",
            "Dutch Defense: Manhattan Gambit, Anti-Stonewall Variation",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "A80",
            "Dutch Defense: Omega-Isis Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/3P4/2N5/PPP1PPPP/R1BQKBNR b KQkq -": (
            "A80",
            "Dutch Defense: Raphael Variation",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "A80",
            "Dutch Defense",
        ),
        "rnbqkb1r/ppppp1pp/5n2/5p2/3P2P1/2N5/PPP1PP1P/R1BQKBNR b KQkq -": (
            "A80",
            "Dutch Defense: Spielmann Gambit",
        ),
        "rnbqkbnr/ppp1p1pp/8/3p1p2/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "A80",
            "Queen's Pawn Game: Veresov Attack, Dutch System",
        ),
        "rnbqkb1r/pppp2pp/4pn2/5p2/3P4/6PN/PPP1PPBP/RNBQK2R b KQkq -": (
            "A81",
            "Dutch Defense: Blackburne Variation",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/3P4/6P1/PPP1PP1P/RNBQKBNR b KQkq -": (
            "A81",
            "Dutch Defense: Fianchetto Attack",
        ),
        "rnbqk2r/pp1pp1bp/2p3pn/5p2/3P4/5NP1/PPP1PPBP/RNBQ1RK1 w kq -": (
            "A81",
            "Dutch Defense: Leningrad, Basman System",
        ),
        "rnbqk1nr/ppppp1bp/6p1/5p2/3P4/6PN/PPP1PPBP/RNBQK2R b KQkq -": (
            "A81",
            "Dutch Defense: Leningrad Variation, Karlsbad Variation",
        ),
        "rnbqkb1r/ppppp2p/5np1/5p2/3P4/6P1/PPP1PPBP/RNBQK1NR w KQkq -": (
            "A81",
            "Dutch Defense: Semi-Leningrad Variation",
        ),
        "rnbqkb1r/ppppp1pp/5n2/8/3Pp3/2N2P2/PPP3PP/R1BQKBNR b KQkq -": (
            "A82",
            "Dutch Defense: Blackmar's Second Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/8/3Pp3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "A82",
            "Dutch Defense: Staunton Gambit Accepted",
        ),
        "rnbqkbnr/ppppp1pp/8/8/3Pp3/8/PPPN1PPP/R1BQKBNR b KQkq -": (
            "A82",
            "Dutch Defense: Staunton Gambit, American Attack",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/3PP3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "A82",
            "Dutch Defense: Staunton Gambit",
        ),
        "rnbqkb1r/ppppp1pp/5n2/8/3Pp1P1/2N5/PPP2P1P/R1BQKBNR b KQkq -": (
            "A82",
            "Dutch Defense: Staunton Gambit, Tartakower Variation",
        ),
        "rnbqkbnr/pppp2pp/4p3/5p2/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "A82",
            "French Defense: Franco-Hiva Gambit",
        ),
        "rnbqkbnr/ppp1p1pp/3p4/5p2/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "A82",
            "Rat Defense: Balogh Defense",
        ),
        "rnbqkb1r/ppppp2p/5np1/6B1/3Pp2P/2N5/PPP2PP1/R2QKBNR b KQkq -": (
            "A83",
            "Dutch Defense: Staunton Gambit, Alekhine Variation",
        ),
        "rnbqkb1r/pp1pp1pp/2p2n2/6B1/3Pp3/2N5/PPP2PPP/R2QKBNR w KQkq -": (
            "A83",
            "Dutch Defense: Staunton Gambit, Chigorin Variation",
        ),
        "rnbqkb1r/ppppp2p/5np1/6B1/3Pp3/2N2P2/PPP3PP/R2QKBNR b KQkq -": (
            "A83",
            "Dutch Defense: Staunton Gambit, Lasker Variation",
        ),
        "rnbqkb1r/p1ppp1pp/1p3n2/6B1/3Pp3/2N5/PPP2PPP/R2QKBNR w KQkq -": (
            "A83",
            "Dutch Defense: Staunton Gambit, Nimzowitsch Variation",
        ),
        "rnbqkb1r/ppppp1pp/5n2/6B1/3Pp3/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "A83",
            "Dutch Defense: Staunton Gambit",
        ),
        "rnbqkb1r/ppppp2p/6pn/5p2/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "A84",
            "Dutch Defense: Bladel Variation",
        ),
        "rnbqkbnr/pppp2pp/4p3/5p2/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A84",
            "Dutch Defense: Classical Variation",
        ),
        "rnbqkb1r/ppppp1pp/5n2/5p2/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "A84",
            "Dutch Defense: Normal Variation",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/2PP4/8/PP2PPPP/RNBQKBNR b KQkq -": (
            "A84",
            "Dutch Defense",
        ),
        "rnbqkbnr/pppp2pp/4p3/5p2/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq -": (
            "A84",
            "Dutch Defense: Rubinstein Variation",
        ),
        "rnbqkbnr/pppp2pp/4p3/5p2/2PPP3/8/PP3PPP/RNBQKBNR b KQkq -": (
            "A84",
            "Horwitz Defense: Dutch Defense, Bellon Gambit",
        ),
        "rnbqkb1r/ppppp1pp/5n2/5p2/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq -": (
            "A85",
            "Dutch Defense: Queen's Knight Variation",
        ),
        "rnbqkb1r/ppppp1pp/5n2/5p2/2PP4/6P1/PP2PP1P/RNBQKBNR b KQkq -": (
            "A86",
            "Dutch Defense: Fianchetto Variation",
        ),
        "rnb1kb1r/ppq1p1pp/2pp1n2/5p2/2PP4/2N3P1/PP2PPBP/R1BQK1NR w KQkq -": (
            "A86",
            "Dutch Defense: Hort-Antoshin System",
        ),
        "rnbqkb1r/ppppp2p/5np1/5p2/2PP4/6P1/PP2PP1P/RNBQKBNR w KQkq -": (
            "A86",
            "Dutch Defense: Leningrad Variation",
        ),
        "rnbqk2r/ppppp1bp/5np1/5p2/2PP4/5NP1/PP2PPBP/RNBQK2R b KQkq -": (
            "A87",
            "Dutch Defense: Leningrad Variation",
        ),
        "rnbq1rk1/pp2p1bp/2pp1np1/5p2/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "A88",
            "Dutch Defense: Leningrad Variation, Warsaw Variation",
        ),
        "r1bq1rk1/ppp1p1bp/2np1np1/5p2/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "A89",
            "Dutch Defense: Leningrad Variation, Matulović Variation",
        ),
        "rnbqkb1r/pppp2pp/4pn2/5p2/2PP4/6P1/PP2PPBP/RNBQK1NR b KQkq -": (
            "A90",
            "Dutch Defense: Classical Variation",
        ),
        "rnbqk2r/ppppb1pp/4pn2/5p2/2PP4/6P1/PP1BPPBP/RN1QK1NR w KQkq -": (
            "A90",
            "Dutch Defense: Nimzowitsch-Dutch Variation, Alekhine Variation",
        ),
        "rnbqk2r/pppp2pp/4pn2/5p2/1bPP4/6P1/PP2PPBP/RNBQK1NR w KQkq -": (
            "A90",
            "Dutch Defense: Nimzowitsch-Dutch Variation",
        ),
        "rnbqk2r/ppppb1pp/4pn2/5p2/2PP4/6PN/PP2PPBP/RNBQK2R b KQkq -": (
            "A91",
            "Dutch Defense: Classical Variation, Blackburne Attack",
        ),
        "rnbqk2r/ppppb1pp/4pn2/5p2/2PP4/6P1/PP2PPBP/RNBQK1NR w KQkq -": (
            "A91",
            "Dutch Defense: Classical Variation",
        ),
        "rnbq1rk1/ppppb1pp/4p3/5p2/2PPn3/5NP1/PP2PPBP/RNBQ1RK1 w - -": (
            "A92",
            "Dutch Defense: Alekhine Variation",
        ),
        "rnbq1rk1/ppppb1pp/4pn2/5p2/2PP4/5NP1/PP2PPBP/RNBQK2R w KQ -": (
            "A92",
            "Dutch Defense: Classical Variation",
        ),
        "rnbq1rk1/ppp1b1pp/4pn2/3p1p2/2PP4/5NP1/PP2PPBP/RNBQ1RK1 w - -": (
            "A92",
            "Dutch Defense: Stonewall Variation",
        ),
        "rnbq1rk1/ppp1b1pp/4pn2/3p1p2/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 b - -": (
            "A92",
            "Dutch Defense: Stonewall",
        ),
        "rnbq1rk1/ppp1b1pp/4pn2/3p1p2/2PP4/1P3NP1/P3PPBP/RNBQ1RK1 b - -": (
            "A93",
            "Dutch Defense: Classical Variation, Stonewall Variation, Botvinnik Variation",
        ),
        "rnbq1rk1/pp2b1pp/2p1pn2/3p1p2/2PP4/BP3NP1/P3PPBP/RN1Q1RK1 b - -": (
            "A94",
            "Dutch Defense: Classical Variation, Stonewall Variation",
        ),
        "rnbq1rk1/pp2b1pp/2p1pn2/3p1p2/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "A95",
            "Dutch Defense: Classical Variation, Stonewall Variation",
        ),
        "rnb1qrk1/pp2b1pp/2p1pn2/3p1pB1/2PP4/2N2NP1/PPQ1PPBP/R4RK1 b - -": (
            "A95",
            "Dutch Defense: Stonewall Variation, Chekhover Variation",
        ),
        "rnbq1rk1/1pp1b1pp/3ppn2/p4p2/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "A96",
            "Dutch Defense: Classical Variation, Buenos Aires Variation",
        ),
        "rnbq1rk1/ppp1b1pp/3pp3/5p2/2PPn3/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "A96",
            "Dutch Defense: Classical Variation, Huisl Variation",
        ),
        "rnbq1rk1/ppp1b1pp/3ppn2/5p2/2PP4/5NP1/PP2PPBP/RNBQ1RK1 w - -": (
            "A96",
            "Dutch Defense: Classical Variation",
        ),
        "rnb1qrk1/ppp1b1pp/3ppn2/5p2/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "A97",
            "Dutch Defense: Classical Variation, Ilyin-Zhenevsky Variation",
        ),
        "rnb1qrk1/ppp1b1pp/3ppn2/5p2/2PP4/2N2NP1/PP2PPBP/R1BQR1K1 b - -": (
            "A97",
            "Dutch Defense: Classical Variation, Ilyin-Zhenevsky Variation, Winter Variation",
        ),
        "rnb1qrk1/ppp1b1pp/3ppn2/5p2/2PP4/2N2NP1/PPQ1PPBP/R1B2RK1 b - -": (
            "A98",
            "Dutch Defense: Classical Variation, Ilyin-Zhenevsky Variation, Alatortsev-Lisitsin Line",
        ),
        "rnb1qrk1/ppp1b1pp/3ppn2/5p2/2PP4/1PN2NP1/P3PPBP/R1BQ1RK1 b - -": (
            "A99",
            "Dutch Defense: Classical Variation, Ilyin-Zhenevsky Variation, Modern Main Line",
        ),
        "rnbqkbnr/ppppp1pp/5p2/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Barnes Defense",
        ),
        "rnbqk1nr/ppppppbp/8/6p1/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Borg Defense: Borg Gambit",
        ),
        "rnbqkbnr/p2p1p1p/1p2p3/2P3p1/4P3/2P5/PP3PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Borg Defense: Langhorst Gambit",
        ),
        "rnbqkbnr/pppppp1p/8/6p1/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Borg Defense",
        ),
        "rnbqkbnr/pppppp2/7p/8/3PP1pP/8/PPP2PP1/RNBQKBNR w KQkq -": (
            "B00",
            "Borg Defense: Troon Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/4p1p1/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Borg Opening: Zilbermintz Gambit",
        ),
        "rnbqkbnr/ppppppp1/7p/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Carr Defense",
        ),
        "rnbqkbnr/pppp1pp1/7p/4p3/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Carr Defense: Zilbermintz Gambit",
        ),
        "rnbqkbnr/ppppp1pp/8/5p2/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Duras Gambit",
        ),
        "rnbq1bnr/pppppkpp/5p2/8/3PP3/8/PPP2PPP/RNBQKBNR w KQ -": (
            "B00",
            "Fried Fox Defense",
        ),
        "rnbqkb1r/ppppppp1/5n2/7p/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Goldsmith Defense: Picklepuss Defense",
        ),
        "rnbqkbnr/ppppppp1/8/7p/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Goldsmith Defense",
        ),
        "rn1qkbnr/p1pppppp/bp6/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Guatemala Defense",
        ),
        "rnbqkb1r/ppppp2p/5ppn/8/2PPP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Hippopotamus Defense",
        ),
        "rnbqkb1r/pppppppp/7n/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Hippopotamus Defense",
        ),
        "r1bqkbnr/pppppppp/2n5/8/3PP3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "B00",
            "King's Pawn Game: Nimzowitsch Defense",
        ),
        "r1bqkbnr/pppppppp/2n5/8/3PP3/2P5/P4PPP/RNBQKBNR b KQkq -": (
            "B00",
            "King's Pawn Game: Nimzowitsch Defense, Wheeler Gambit",
        ),
        "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq -": (
            "B00",
            "King's Pawn Game",
        ),
        "r1bqkbnr/pppppppp/n7/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Lemming Defense",
        ),
        "rnbqkb1r/ppp1pppp/3p1n2/8/3PP3/5P2/PPP3PP/RNBQKBNR b KQkq -": (
            "B00",
            "Lion Defense: Lion's Jaw Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Breyer Variation",
        ),
        "r1bqkbnr/pppppppp/2n5/8/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "B00",
            "Nimzowitsch Defense, Declined Variation",
        ),
        "r1bqkb1r/ppp1pppp/2npP2n/8/3P4/5N1P/PPP2PP1/RNBQKB1R b KQkq -": (
            "B00",
            "Nimzowitsch Defense: El Columpio Defense, El Columpio Gambit",
        ),
        "r1bqkb1r/ppp1pppp/2nP3n/8/3P4/5N1P/PPP2PP1/RNBQKB1R b KQkq -": (
            "B00",
            "Nimzowitsch Defense: El Columpio Defense, Exchange Variation",
        ),
        "r1bqkb1r/ppp1pppp/2np3n/1B2P3/3P4/5N1P/PPP2PP1/RNBQK2R b KQkq -": (
            "B00",
            "Nimzowitsch Defense: El Columpio Defense, Pin Variation",
        ),
        "r1bqkb1r/pppppppp/2n5/4P3/6n1/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B00",
            "Nimzowitsch Defense: El Columpio Defense",
        ),
        "r1bqkb1r/pppp2pp/2n1pn2/5P2/3P4/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Franco-Hiva Gambit",
        ),
        "r1bqkb1r/pppp2pp/2n1pn2/5P2/3P4/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Franco-Hiva Gambit",
        ),
        "r1bqkbnr/pppp1ppp/2n1p3/8/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Franco-Nimzowitsch Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n1p3/8/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: French Connection Variation",
        ),
        "r1bqkbnr/ppp1pppp/2n5/3p4/3PP3/4B3/PPP2PPP/RN1QKBNR b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Hornung Gambit",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b1P3/4P3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Kennedy Variation, Bielefelder Gambit",
        ),
        "r1bqkbnr/ppp2ppp/2np4/4P3/4P3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Kennedy Variation, de Smet Gambit",
        ),
        "r1bqkbnr/pppp2pp/2n2p2/4P3/4P3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Kennedy Variation, Hammer Gambit",
        ),
        "r1b1kbnr/pppp1ppp/2n5/4P3/4P2q/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Kennedy Variation, Herford Gambit",
        ),
        "r1bqkbnr/pppp1ppp/8/4n3/4P3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Kennedy Variation, Keres Attack",
        ),
        "r1bqkbnr/pppp1ppp/2n5/3Pp3/4P3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Kennedy Variation, Linksspringer Variation",
        ),
        "r1bqkbnr/pppp1ppp/6n1/8/4PP2/8/PPP3PP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Kennedy Variation, Main Line",
        ),
        "r1bqkbnr/pppp1ppp/8/4n3/4P3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Kennedy Variation, Paulsen Attack",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Kennedy Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/4PP2/8/PPP3PP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Kennedy Variation, Riemann Defense",
        ),
        "r1bqkbnr/ppppp1pp/2n5/5P2/8/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Lean Variation, Colorado Counter Accepted",
        ),
        "r1bqkbnr/ppppp1pp/2n5/5p2/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Lean Variation",
        ),
        "r1bqkbnr/ppp1pppp/2np4/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Mikėnas Variation",
        ),
        "r1bqkbnr/ppppp1pp/2n2p2/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Neo-Mongoloid Defense",
        ),
        "r1bqkbnr/pppppp1p/2n3p1/8/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Pirc Connection Variation",
        ),
        "r1bqkbnr/pppppppp/2n5/1B6/4P3/8/PPPP1PPP/RNBQK1NR b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Pseudo-Spanish Variation",
        ),
        "r1bqkbnr/pppppppp/2n5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense",
        ),
        "r1bqkbnr/ppp1pppp/8/3P4/1n1P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Aachen Gambit",
        ),
        "r1bqkbnr/ppp1pppp/2n5/3pP3/3P4/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Advance Variation",
        ),
        "r1bqkbnr/1pp1pppp/p1n5/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Bogoljubov Variation, Brandics Gambit",
        ),
        "r1bqkbnr/ppp1pp1p/2n3p1/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Bogoljubov Variation, Erben Gambit",
        ),
        "r1bqkbnr/ppp2ppp/2n5/3pp3/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Bogoljubov Variation, Heinola-Deppe Gambit",
        ),
        "r1bqkbnr/ppp1pppp/8/3Pn3/4p3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Bogoljubov Variation, Nimzowitsch Gambit",
        ),
        "r1bqkbnr/ppp1pppp/2n5/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Bogoljubov Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3P4/4p3/2N2P2/PPP3PP/R1BQKBNR b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Bogoljubov Variation, Richter Gambit",
        ),
        "r1bqkb1r/ppp1pppp/2n2n2/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Bogoljubov Variation, Vehre Variation",
        ),
        "r1b1kbnr/ppp1pppp/2n5/3q4/3P4/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Exchange Variation, Marshall Gambit",
        ),
        "r1b1kbnr/ppp1pppp/2n5/3q4/3P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation, Exchange Variation",
        ),
        "r1bqkbnr/ppp1pppp/2n5/3p4/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Scandinavian Variation",
        ),
        "r1bqkbnr/pppppppp/2n5/8/1P2P3/8/P1PP1PPP/RNBQKBNR b KQkq -": (
            "B00",
            "Nimzowitsch Defense: Wheeler Gambit",
        ),
        "r1bqkbnr/ppp1pppp/2np4/8/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Williams Variation",
        ),
        "r1bqkbnr/1ppppppp/p1n5/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Nimzowitsch Defense: Woodchuck Variation",
        ),
        "r1bqkbnr/p2ppppp/1pn5/2P5/4P3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Owen Defense: Hekili-Loa Gambit",
        ),
        "rn1qkbnr/p1ppp2p/1p4p1/5P1Q/3P4/3B4/PPP2PbP/RNB1K1NR w KQkq -": (
            "B00",
            "Owen Defense: Matovinsky Gambit",
        ),
        "rn1qkbnr/pbpppppp/1p6/6B1/3PP3/8/PPP2PPP/RN1QKBNR b KQkq -": (
            "B00",
            "Owen Defense: Naselwaus Gambit",
        ),
        "rnbqkbnr/p1pppppp/1p6/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Owen Defense",
        ),
        "rn1qkbnr/pbpppppp/1p6/8/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B00",
            "Owen Defense: Smith Gambit",
        ),
        "rn1qkbnr/pbppp1pp/1p3p2/8/2PPP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Owen Defense: Unicorn Variation",
        ),
        "rn1qkbnr/pbpp1ppp/1p6/4p3/3PP3/5P2/PPP3PP/RNBQKBNR w KQkq -": (
            "B00",
            "Owen Defense: Wind Gambit",
        ),
        "rnbqkb1r/ppp1pppp/3p1n2/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Pirc Defense",
        ),
        "rnbqkbnr/ppp1pppp/3p4/8/3PP3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "B00",
            "Pirc Defense",
        ),
        "rnbqkbnr/ppp1pppp/3p4/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Pirc Defense",
        ),
        "rnbqkb1r/ppp1pppp/3p1n2/8/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B00",
            "Pirc Defense: Roscher Gambit",
        ),
        "r1bqkbnr/pppnpppp/3p4/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Rat Defense: Antal Defense",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3P4/5P2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "B00",
            "Rat Defense: Fuller Gambit",
        ),
        "rnbqkbnr/ppp1pppp/3p4/8/4PP2/8/PPPP2PP/RNBQKBNR b KQkq -": (
            "B00",
            "Rat Defense: Harmonist Variation",
        ),
        "rnbqkbnr/ppp1pppp/3p4/8/4P2P/8/PPPP1PP1/RNBQKBNR b KQkq -": (
            "B00",
            "Rat Defense: Petruccioli Attack",
        ),
        "rnbqkbnr/ppp1pppp/3p4/8/4P1P1/8/PPPP1P1P/RNBQKBNR b KQkq -": (
            "B00",
            "Rat Defense: Spike Attack",
        ),
        "rnbqkbnr/1ppppppp/p7/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "St. George Defense",
        ),
        "rn1qk1nr/1bp1ppbp/p2p2p1/1p6/3PP3/2PB1N2/PP3PPP/RNBQ1RK1 w kq -": (
            "B00",
            "St. George Defense: San Jorge Variation",
        ),
        "rnbqkbnr/1ppp1ppp/p7/4p3/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "St. George Defense: Zilbermintz Gambit",
        ),
        "r1bqkbnr/ppp1pppp/2n5/3P4/4p3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "B00",
            "van Geet Opening: Berlin Gambit",
        ),
        "rnbqkbnr/1ppppppp/8/p7/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Ware Defense",
        ),
        "r1bqkbnr/1ppppppp/2n5/p7/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B00",
            "Ware Defense: Snagglepuss Defense",
        ),
        "r1bqkbnr/pp1ppppp/n7/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B00",
            "Zukertort Defense: Sicilian Knight Variation",
        ),
        "rn2kbnr/ppp2ppp/8/q3p3/3P2b1/2N2N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "B01",
            "Scandinavian Defense: Anderssen Counterattack, Collijn Variation",
        ),
        "rnb1kbnr/ppp2ppp/8/q3p3/3P4/2N2N2/PPP2PPP/R1BQKB1R b KQkq -": (
            "B01",
            "Scandinavian Defense: Anderssen Counterattack, Göteborg System",
        ),
        "r1b1k1nr/ppp2ppp/2n5/q3P3/1b6/2N2N2/PPPB1PPP/R2QKB1R b KQkq -": (
            "B01",
            "Scandinavian Defense: Anderssen Counterattack, Orthodox Attack",
        ),
        "rnb1kbnr/ppp2ppp/8/q3p3/3P4/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Anderssen Counterattack",
        ),
        "r1bqkbnr/pp2pppp/2n5/8/8/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Blackburne Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/3P4/8/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Blackburne-Kloosterboer Gambit",
        ),
        "rn1qkbnr/ppp2ppp/4b3/8/8/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Boehnke Gambit",
        ),
        "rnb1kb1r/1pp1pppp/p2q1n2/8/3P4/2N2N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "B01",
            "Scandinavian Defense: Bronstein Variation",
        ),
        "rn2kb1r/ppp1pppp/5n2/q4b2/3P4/2N2N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "B01",
            "Scandinavian Defense: Classical Variation",
        ),
        "rn2kb1r/pp2pppp/2p2n2/q3Nb2/3P2P1/2N5/PPP2P1P/R1BQKB1R b KQkq -": (
            "B01",
            "Scandinavian Defense: Grünfeld Variation",
        ),
        "rnb1kbnr/ppp1pppp/3q4/8/8/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Gubinsky-Melts Defense",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3P4/2P5/8/PP1P1PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Icelandic-Palme Gambit",
        ),
        "rnbqkb1r/pp3ppp/2P2n2/4p3/3P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Kádas Gambit",
        ),
        "rnbqkb1r/ppp1pppp/8/8/1nPP4/8/PP3PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Kiel Variation",
        ),
        "rnbqkbnr/pp3ppp/2P5/4p3/8/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Kloosterboer Gambit",
        ),
        "rn2kb1r/ppp1pppp/5n2/q7/3P2b1/2N2N1P/PPP2PP1/R1BQKB1R b KQkq -": (
            "B01",
            "Scandinavian Defense: Lasker Variation",
        ),
        "rnb1kbnr/ppp1pppp/8/q7/1P6/2N5/P1PP1PPP/R1BQKBNR b KQkq -": (
            "B01",
            "Scandinavian Defense: Main Line, Leonhardt Gambit",
        ),
        "rnb1kb1r/ppp1pppp/5n2/q7/3P4/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Main Line, Mieses Variation",
        ),
        "rnb1kbnr/ppp1pppp/8/q7/8/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Main Line",
        ),
        "rnbqkb1r/ppp1pppp/8/3n4/3P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Marshall Variation",
        ),
        "rnb1kbnr/ppp1pppp/8/3q4/8/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Mieses-Kotrč Variation",
        ),
        "rn1qkb1r/ppp1pppp/8/3n4/3P2b1/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B01",
            "Scandinavian Defense: Modern Variation, Gipslis Variation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3P4/3P4/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "B01",
            "Scandinavian Defense: Modern Variation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3P4/8/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Modern Variation",
        ),
        "rnbqkb1r/p1p1pp1p/5np1/1p1P4/2PP4/8/PP3PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Modern Variation, Wing Gambit",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/3P4/2P5/8/PP1P1PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Panov Transfer Variation",
        ),
        "r2qkb1r/pppnpppp/5n2/1B1P1b2/3P4/5P2/PPP3PP/RNBQK1NR w KQkq -": (
            "B01",
            "Scandinavian Defense: Portuguese Variation, Portuguese Gambit",
        ),
        "rn1qkb1r/ppp1pppp/5n2/3P4/3P2b1/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Portuguese Variation",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3P4/3P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Richter Variation",
        ),
        "rnbqkb1r/ppp1pp1p/6p1/3n4/3P4/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B01",
            "Scandinavian Defense: Richter Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/4P3/1P6/P1PP1PPP/RNBQKBNR b KQkq -": (
            "B01",
            "Scandinavian Defense",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense",
        ),
        "rn2kb1r/pp2pppp/2p2n2/5b2/1qBP1B2/2N5/PPP1NPPP/R2QK2R w KQkq -": (
            "B01",
            "Scandinavian Defense: Schiller-Pytel Variation, Modern Variation",
        ),
        "rnb1kbnr/pp2pppp/2pq4/8/3P4/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B01",
            "Scandinavian Defense: Schiller-Pytel Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/1P2P3/8/P1PP1PPP/RNBQKBNR b KQkq -": (
            "B01",
            "Scandinavian Defense: Zilbermintz Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/4N3/8/PPPP1PPP/R1BQKBNR w KQkq -": (
            "B01",
            "van Geet Opening: Grünfeld Defense",
        ),
        "rnbqkbnr/ppppp1pp/8/4Pp2/3P4/8/PPP2PPP/RNBQKBNR w KQkq f6": (
            "B02",
            "Alekhine Defense: Brooklyn Variation, Everglades Variation",
        ),
        "rnbqkbnr/pppppppp/8/4P3/8/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B02",
            "Alekhine Defense: Brooklyn Variation",
        ),
        "rnbqkb1r/pppppppp/8/3nP3/8/N7/PPPP1PPP/R1BQKBNR b KQkq -": (
            "B02",
            "Alekhine Defense: Buckley Attack",
        ),
        "rnbqkb1r/pppp1ppp/4p3/2PnP3/2B5/2N5/PP1P1PPP/R1BQK1NR b KQkq -": (
            "B02",
            "Alekhine Defense: Hunt Variation, Lasker Simul Gambit",
        ),
        "rnbqkb1r/ppp1pppp/3p4/2P1P1B1/8/2P5/PP3PPP/R2QKBNR b KQkq -": (
            "B02",
            "Alekhine Defense: Hunt Variation, Matsukevich Gambit",
        ),
        "rnbqkb1r/ppp2ppp/3p4/2PBP3/8/8/PP1P1PPP/R1BQK1NR b KQkq -": (
            "B02",
            "Alekhine Defense: Hunt Variation, Mikėnas Gambit",
        ),
        "rnbqkb1r/pp1ppppp/1n6/2p1P3/8/1B1P4/PPP2PPP/RNBQK1NR b KQkq -": (
            "B02",
            "Alekhine Defense: Kmoch Variation",
        ),
        "rnbqkb1r/pppppBpp/8/8/4n3/8/PPPP1PPP/RNBQK1NR b KQkq -": (
            "B02",
            "Alekhine Defense: Krejcik Variation, Krejcik Gambit",
        ),
        "rnbqkb1r/pppppppp/5n2/8/2B1P3/8/PPPP1PPP/RNBQK1NR b KQkq -": (
            "B02",
            "Alekhine Defense: Krejcik Variation",
        ),
        "rnbqkb1r/pppppppp/5n2/8/4P3/3P4/PPP2PPP/RNBQKBNR b KQkq -": (
            "B02",
            "Alekhine Defense: Maróczy Variation",
        ),
        "rnbqkb1r/ppppp1pp/5p2/4P3/3Pn3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B02",
            "Alekhine Defense: Mokele Mbembe Variation, Modern Line",
        ),
        "rnbqkb1r/pppppppp/8/4P3/4n3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B02",
            "Alekhine Defense: Mokele Mbembe Variation",
        ),
        "rnbqkb1r/pppp1ppp/4p3/4P3/3Pn3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B02",
            "Alekhine Defense: Mokele Mbembe Variation, Vavra Defense",
        ),
        "rnbqkb1r/pppppppp/8/3nP3/8/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B02",
            "Alekhine Defense: Normal Variation",
        ),
        "rnbqkb1r/pppppppp/5n2/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B02",
            "Alekhine Defense",
        ),
        "rnbqkb1r/pppppppp/8/3nP3/8/2N5/PPPP1PPP/R1BQKBNR b KQkq -": (
            "B02",
            "Alekhine Defense: Sämisch Attack",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/3P4/8/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "B02",
            "Alekhine Defense: Scandinavian Variation, Geschev Gambit",
        ),
        "rnbqkb1r/ppp1pppp/5n2/6B1/4p3/2NP4/PPP2PPP/R2QKBNR b KQkq -": (
            "B02",
            "Alekhine Defense: Scandinavian Variation, Myers Gambit",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "B02",
            "Alekhine Defense: Scandinavian Variation",
        ),
        "rnbqkb1r/pppnpppp/4P3/3p4/8/2N5/PPPP1PPP/R1BQKBNR b KQkq -": (
            "B02",
            "Alekhine Defense: Spielmann Gambit",
        ),
        "rnbqkb1r/pppppppp/1n6/4P3/2P5/1P6/P2P1PPP/RNBQKBNR b KQkq -": (
            "B02",
            "Alekhine Defense: Steiner Variation",
        ),
        "rnbqkb1r/pppppppp/1n6/2P1P3/8/8/PP1P1PPP/RNBQKBNR b KQkq -": (
            "B02",
            "Alekhine Defense: Two Pawns Attack, Lasker Variation",
        ),
        "rnbqkb1r/ppp2ppp/3pp3/2PnP3/2B5/2N5/PP1P1PPP/R1BQK1NR w KQkq -": (
            "B02",
            "Alekhine Defense: Two Pawns Attack, Mikėnas Variation",
        ),
        "rnbqkb1r/pppppppp/8/4P3/2P2n2/8/PP1P1PPP/RNBQKBNR w KQkq -": (
            "B02",
            "Alekhine Defense: Two Pawns Attack, The Squirrel Variation",
        ),
        "rnbqkb1r/pppppppp/8/3nP3/2P5/8/PP1P1PPP/RNBQKBNR b KQkq -": (
            "B02",
            "Alekhine Defense: Two Pawns Attack",
        ),
        "rnbqkb1r/pppppppp/8/3nP3/8/1P6/P1PP1PPP/RNBQKBNR b KQkq -": (
            "B02",
            "Alekhine Defense: Welling Variation",
        ),
        "rnbqkb1r/pppppppp/5n2/8/2P1P3/8/PP1P1PPP/RNBQKBNR b KQkq -": (
            "B02",
            "English Opening: Achilles-Omega Gambit",
        ),
        "rnbqk2r/pppp1ppp/5n2/2b1p3/4PP2/3P4/PPP3PP/RNBQKBNR w KQkq -": (
            "B02",
            "King's Pawn Game: Clam Variation, Radisch Gambit",
        ),
        "rnbqkb1r/ppp1pppp/3p4/3nP3/2BP4/8/PPP2PPP/RNBQK1NR b KQkq -": (
            "B03",
            "Alekhine Defense: Balogh Variation",
        ),
        "r2q1rk1/pp2ppbp/1nnp2p1/5b2/2PP1B2/2N2N1P/PP2BPP1/R2Q1RK1 b - -": (
            "B03",
            "Alekhine Defense: Exchange Variation, Karpov Variation",
        ),
        "rnbqkb1r/ppp1pppp/1n1P4/8/2PP4/8/PP3PPP/RNBQKBNR b KQkq -": (
            "B03",
            "Alekhine Defense: Exchange Variation",
        ),
        "rnbqkb1r/ppp1pp1p/1n1p4/4P1p1/2PP1P2/8/PP4PP/RNBQKBNR w KQkq -": (
            "B03",
            "Alekhine Defense: Four Pawns Attack, Cambridge Gambit",
        ),
        "rnbqkb1r/ppp1pp1p/1n1p2p1/4P3/2PP1P2/8/PP4PP/RNBQKBNR w KQkq -": (
            "B03",
            "Alekhine Defense: Four Pawns Attack, Fianchetto Variation",
        ),
        "r2qkb1r/ppp1p1pp/1nn1p3/2P5/3P2b1/5N2/PP4PP/RNBQKB1R b KQkq -": (
            "B03",
            "Alekhine Defense: Four Pawns Attack, Ilyin-Zhenevsky Variation",
        ),
        "rn1q1rk1/ppp1b1pp/1n2pp2/4Pb2/2PP4/2N2N2/PP2B1PP/R1BQ1RK1 w - -": (
            "B03",
            "Alekhine Defense: Four Pawns Attack, Korchnoi Variation",
        ),
        "r1bqkb1r/ppp1pppp/1nn5/4P3/2PP4/4B3/PP4PP/RN1QKBNR b KQkq -": (
            "B03",
            "Alekhine Defense: Four Pawns Attack, Main Line",
        ),
        "rnbqkb1r/ppp1pppp/1n1p4/4P3/2PP1P2/8/PP4PP/RNBQKBNR b KQkq -": (
            "B03",
            "Alekhine Defense: Four Pawns Attack",
        ),
        "2kr3r/pppqbppp/1nn1p3/4Pb2/2PP4/2N1BN2/PP2B1PP/R2Q1RK1 w - -": (
            "B03",
            "Alekhine Defense: Four Pawns Attack, Tartakower Variation",
        ),
        "rn1qkb1r/ppp1pppp/1n1p4/4Pb2/2PP1P2/8/PP4PP/RNBQKBNR w KQkq -": (
            "B03",
            "Alekhine Defense: Four Pawns Attack, Trifunović Variation",
        ),
        "rnbqkb1r/ppp1pppp/1n1p4/2P1P3/3P4/8/PP3PPP/RNBQKBNR b KQkq -": (
            "B03",
            "Alekhine Defense: Hunt Variation",
        ),
        "rn1qkb1r/ppp1pppp/1n1p4/4P3/2PP2b1/5N2/PP2BPPP/RNBQK2R b KQkq -": (
            "B03",
            "Alekhine Defense: Modern Variation, Alekhine Gambit",
        ),
        "rnbqkb1r/p1pppppp/8/1p1nP3/3P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B03",
            "Alekhine Defense: O'Sullivan Gambit",
        ),
        "rnbqkb1r/ppp1pppp/3p4/3nP3/2PP4/8/PP3PPP/RNBQKBNR b KQkq -": (
            "B03",
            "Alekhine Defense",
        ),
        "rnbqkb1r/ppp1pppp/3p4/3nP3/3P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B03",
            "Alekhine Defense",
        ),
        "rnbqkb1r/pppppppp/8/3nP3/3P4/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "B03",
            "Alekhine Defense",
        ),
        "rnbqkb1r/ppp1pp1p/3p2p1/3nP3/3P4/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B04",
            "Alekhine Defense: Modern Variation, Alburt Variation",
        ),
        "rnbqk2r/ppp1ppbp/1n1p2p1/4P3/P2P4/1B3N2/1PP2PPP/RNBQK2R b KQkq -": (
            "B04",
            "Alekhine Defense: Modern Variation, Keres Variation",
        ),
        "r1bqkb1r/ppp1pppp/2np4/3nP3/3P4/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B04",
            "Alekhine Defense: Modern Variation, Larsen-Haakert Variation",
        ),
        "rnbqkb1r/ppp1pppp/8/3np3/3P4/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B04",
            "Alekhine Defense: Modern Variation, Larsen Variation",
        ),
        "rnbqkb1r/ppp1pppp/3p4/3nP3/3P4/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B04",
            "Alekhine Defense: Modern Variation",
        ),
        "rnbqkb1r/ppp1pppp/1n1p4/4P3/3P4/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B04",
            "Alekhine Defense: Modern Variation, Schmid Variation",
        ),
        "rn1qkb1r/pp2pppp/2pp4/3nP3/3P2b1/5N2/PPP1BPPP/RNBQK2R w KQkq -": (
            "B05",
            "Alekhine Defense: Modern Variation, Flohr Variation",
        ),
        "rn1qkb1r/ppp1pppp/3p4/3nP3/2PP2b1/5N2/PP3PPP/RNBQKB1R b KQkq -": (
            "B05",
            "Alekhine Defense: Modern Variation, Alekhine Variation",
        ),
        "rn1qkb1r/ppp1pppp/3p4/3nP3/3P2b1/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B05",
            "Alekhine Defense: Modern Variation, Main Line",
        ),
        "rn1qkb1r/ppp1pppp/3p4/3nP3/3P2b1/5N1P/PPP2PP1/RNBQKB1R b KQkq -": (
            "B05",
            "Alekhine Defense: Modern Variation, Panov Variation",
        ),
        "rn1qkb1r/ppp1pppp/1n1p4/3PP3/2P3b1/5N2/PP3PPP/RNBQKB1R b KQkq -": (
            "B05",
            "Alekhine Defense: Modern Variation, Vitolins Attack",
        ),
        "rnbqk1nr/pp2ppbp/2pp2p1/8/2BPP3/2N5/PPP1QPPP/R1B1K1NR b KQkq -": (
            "B06",
            "Modern Defense: Anti-Modern Variation",
        ),
        "rnbqk1nr/p1ppppbp/6p1/1p6/2BPP3/8/PPP2PPP/RNBQK1NR w KQkq -": (
            "B06",
            "Modern Defense: Bishop's Attack, Bücker Gambit",
        ),
        "rnbqk1nr/pppp1p1p/4p1p1/8/2BbP3/5Q2/PPP2PPP/RNB1K1NR w KQkq -": (
            "B06",
            "Modern Defense: Bishop's Attack, Monkey's Bum Variation",
        ),
        "rnbqk1nr/ppppppbp/6p1/8/2BPP3/8/PPP2PPP/RNBQK1NR b KQkq -": (
            "B06",
            "Modern Defense: Bishop's Attack",
        ),
        "rnbqk1nr/pp2pp1p/2P3p1/8/2Pb4/8/PP3PPP/RNBQKBNR w KQkq -": (
            "B06",
            "Modern Defense: Dunworthy Variation",
        ),
        "rnbqkbnr/ppppp2p/6p1/5p2/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B06",
            "Modern Defense: Fianchetto Gambit",
        ),
        "rnbqk1nr/pp2ppb1/2p3p1/3pP2p/3P1P2/2N5/PPP3PP/R1BQKBNR w KQkq -": (
            "B06",
            "Modern Defense: Gurgenidze Defense",
        ),
        "rnbqk1nr/ppp1ppbp/6p1/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Modern Defense: Lizard Defense, Mittenberger Gambit",
        ),
        "rnbq1rk1/ppppp2p/6pb/5P2/3P4/2N5/PPP2PPP/R2QKBNR w KQ -": (
            "B06",
            "Modern Defense: Masur Gambit",
        ),
        "rnbqk1nr/pp1pppbp/6p1/2p5/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Modern Defense: Modern Pterodactyl Defense",
        ),
        "rnbqk1nr/p1ppppbp/1p4p1/8/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Modern Defense: Mongredien Defense",
        ),
        "rnbqk1nr/p1ppppbp/1p4p1/8/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B06",
            "Modern Defense: Mongredien Defense",
        ),
        "rnbqkb1r/ppp1pp1p/3p2p1/4P2n/3P4/8/PPP1BPPP/RNBQK1NR w KQkq -": (
            "B06",
            "Modern Defense: Norwegian Defense, Norwegian Gambit",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B06",
            "Modern Defense: Norwegian Defense",
        ),
        "rnbqk1nr/ppp1ppbp/3p2p1/8/3PPP2/2N5/PPP3PP/R1BQKBNR b KQkq -": (
            "B06",
            "Modern Defense: Pseudo-Austrian Attack",
        ),
        "rnbqkbnr/pppppp1p/6p1/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B06",
            "Modern Defense",
        ),
        "rnb1k1nr/pp2ppbp/3p2p1/q1p5/2PPP3/5N2/PP2BPPP/RNBQK2R w KQkq -": (
            "B06",
            "Modern Defense: Semi-Averbakh Variation, Pterodactyl Variation Declined",
        ),
        "rnbqk1nr/ppp1ppbp/3p2p1/8/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Modern Defense: Standard Defense",
        ),
        "rnbqk1nr/ppppppbp/6p1/8/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "B06",
            "Modern Defense: Standard Line",
        ),
        "rnbqk1nr/ppppppbp/6p1/8/3PPP2/8/PPP3PP/RNBQKBNR b KQkq -": (
            "B06",
            "Modern Defense: Three Pawns Attack",
        ),
        "rnbqk1nr/ppp1ppbp/3p2p1/8/3PP3/2N2N2/PPP2PPP/R1BQKB1R b KQkq -": (
            "B06",
            "Modern Defense: Two Knights Variation",
        ),
        "rnbqk1nr/pp2ppbp/2pp2p1/8/3PP3/2N2N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "B06",
            "Modern Defense: Two Knights Variation, Suttles Variation",
        ),
        "rnb1k1nr/pp2ppbp/2pp2p1/6B1/3PP3/2N2N2/PqPQ1PPP/R3KB1R w KQkq -": (
            "B06",
            "Modern Defense: Two Knights Variation, Suttles Variation, Tal Gambit",
        ),
        "rnbqk1nr/ppppppbp/6p1/8/3PP3/8/PPPB1PPP/RN1QKBNR b KQkq -": (
            "B06",
            "Modern Defense: Westermann Gambit",
        ),
        "rnbqk1nr/ppppppbp/6p1/8/3PP3/3B4/PPP2PPP/RNBQK1NR b KQkq -": (
            "B06",
            "Modern Defense: Wind Gambit",
        ),
        "rnbqkb1r/ppppppnp/6p1/4P3/3P2P1/8/PPP2P1P/RNBQKBNR w KQkq -": (
            "B06",
            "Norwegian Defense",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/3PPP2/5N2/PPP3PP/RNBQKB1R w KQkq -": (
            "B06",
            "Pterodactyl Defense: Austrian Variation, Western Austriadactylus Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/4PP2/2N2N2/PPPP2PP/R1BQKB1R w KQkq -": (
            "B06",
            "Pterodactyl Defense: Austrian Variation, Grand Prix Pterodactyl Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/3PPP2/2P5/PP4PP/RNBQKBNR w KQkq -": (
            "B06",
            "Pterodactyl Defense: Austrian Variation, Pteranodon Variation",
        ),
        "rnb1k1nr/pp2ppbp/3p2p1/q1p5/2PPP3/2N1B3/PP3PPP/R2QKBNR w KQkq -": (
            "B06",
            "Pterodactyl Defense: Central Variation, Anhanguera Variation",
        ),
        "rnb1k1nr/pp2ppbp/3p2p1/q1pP4/2P1P3/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Pterodactyl Defense: Central Variation, Benoni Quetzalcoatlus Variation",
        ),
        "rnb1k1nr/pp2ppbp/3p2p1/q1P5/2P1P3/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Pterodactyl Defense: Central Variation, Quetzalcoatlus Gambit",
        ),
        "rnbqk1nr/pp1pppbp/6p1/2p5/3PP3/2N1B3/PPP2PPP/R2QKBNR b KQkq -": (
            "B06",
            "Pterodactyl Defense: Eastern Variation, Anhanguera Variation",
        ),
        "rnb1k1nr/pp1ppp1p/6p1/q1pP4/4P3/2P5/P1P2PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Pterodactyl Defense: Eastern Variation, Benoni Pteranodon Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1pP4/4P3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Pterodactyl Defense: Eastern Variation, Benoni Pterodactyl Variation",
        ),
        "rnbqk1nr/pp1pppbp/6p1/2pP4/4P3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "B06",
            "Pterodactyl Defense: Eastern Variation, Benoni Variation",
        ),
        "rnb1k1nr/pp1ppp1p/6p1/q1P5/4P3/2P5/P1P2PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Pterodactyl Defense: Eastern Variation, Pteranodon Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1P5/4P3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Pterodactyl Defense: Eastern Variation, Pterodactyl Variation",
        ),
        "rnbqk1nr/pp1pppbp/6p1/2P5/4P3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "B06",
            "Pterodactyl Defense: Eastern Variation, Rhamphorhynchus Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/3PP3/5NP1/PPP2P1P/RNBQKB1R w KQkq -": (
            "B06",
            "Pterodactyl Defense: Fianchetto Variation, King's Pterodactyl Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1P5/4P3/6P1/PPP2P1P/RNBQKBNR w KQkq -": (
            "B06",
            "Pterodactyl Defense: Fianchetto Variation, Rhamphorhynchus Variation",
        ),
        "rnb1k1nr/pp2ppbp/3p2p1/q1p5/3PP3/2N2N2/PPP1BPPP/R1BQK2R w KQkq -": (
            "B06",
            "Pterodactyl Defense: Sicilian Variation, Quetzalcoatlus Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/2BPP3/2N2N2/PPP2PPP/R1BQK2R b KQkq -": (
            "B06",
            "Pterodactyl Defense: Sicilian Variation, Siroccopteryx Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/3PP3/4BN2/PPP2PPP/RN1QKB1R w KQkq -": (
            "B06",
            "Pterodactyl Defense: Western Variation, Anhanguera Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q7/2BNP3/8/PPP2PPP/RNBQK2R w KQkq -": (
            "B06",
            "Pterodactyl Defense: Western Variation, Siroccopteryx Variation",
        ),
        "rnbqkbnr/pp2pp1p/2pp2p1/8/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B06",
            "Rat Defense: Accelerated Gurgenidze Variation",
        ),
        "rnbqk1nr/ppppppbp/6p1/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B06",
            "Modern Defense",
        ),
        "rnbqkb1r/pp2pppp/2pp1n2/8/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B07",
            "Czech Defense",
        ),
        "r1bqkb1r/pp1n1ppp/2p2n2/3p4/2BQPP2/2N2N2/PPP3PP/R1B1K2R w KQkq -": (
            "B07",
            "Lion Defense: Anti-Philidor Variation, Lion's Cave Variation, Lion's Claw Gambit",
        ),
        "r1bqkb1r/pppn1ppp/3p1n2/4p3/3PPP2/2N5/PPP3PP/R1BQKBNR w KQkq -": (
            "B07",
            "Lion Defense: Anti-Philidor Variation, Lion's Cave Variation",
        ),
        "r1bqkb1r/pppnpppp/3p1n2/8/3PPP2/2N5/PPP3PP/R1BQKBNR b KQkq -": (
            "B07",
            "Lion Defense: Anti-Philidor Variation",
        ),
        "r1bqkb1r/pppnpppp/3p1n2/8/3PP1P1/2N5/PPP2P1P/R1BQKBNR b KQkq -": (
            "B07",
            "Lion Defense: Bayonet Attack",
        ),
        "rnbqk1nr/ppp1ppbp/3p2p1/8/3PP3/2P2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "B07",
            "Modern Defense: Geller System",
        ),
        "r1bqk2r/pp1nbppp/2pp1n2/4p3/3PP3/2N2N2/PPP1BPPP/R1BQ1RK1 w kq -": (
            "B07",
            "Philidor Defense: Lion Variation, Lion's Claw Gambit",
        ),
        "rn1qkb1r/pp2pp1p/2pp1np1/8/3PP1b1/2N1B3/PPPQ1PPP/R3KBNR w KQkq -": (
            "B07",
            "Pirc Defense: 150 Attack, Inner Doll Defense",
        ),
        "rnbqkb1r/pp2pp1p/2pp1np1/8/3PP3/2N1B3/PPPQ1PPP/R3KBNR b KQkq -": (
            "B07",
            "Pirc Defense: 150 Attack",
        ),
        "rnbqkb1r/pp2pp1p/2pp1np1/8/3PP3/2N1B2P/PPP2PP1/R2QKBNR b KQkq -": (
            "B07",
            "Pirc Defense: 150 Attack, Sveshnikov-Janša Attack",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/3PP2P/2N5/PPP1BPP1/R1BQK1NR b KQkq -": (
            "B07",
            "Pirc Defense: Bayonet Attack",
        ),
        "rnbqkb1r/ppp1pp1p/3p1np1/6B1/3PP3/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "B07",
            "Pirc Defense: Byrne Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/3PP1P1/2N5/PPP1BP1P/R1BQK1NR b KQkq -": (
            "B07",
            "Pirc Defense: Chinese Variation",
        ),
        "rnbqkb1r/ppp1pp1p/3p1np1/8/3PP3/2N5/PPP1BPPP/R1BQK1NR b KQkq -": (
            "B07",
            "Pirc Defense: Classical Variation",
        ),
        "rnbqkb1r/ppp1pp1p/3p1np1/8/2BPP3/2N5/PPP2PPP/R1BQK1NR b KQkq -": (
            "B07",
            "Pirc Defense: Kholmov System",
        ),
        "rnbqkb1r/ppp1pp1p/3p1np1/8/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B07",
            "Pirc Defense",
        ),
        "rnbqkb1r/ppp1pppp/3p1n2/8/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "B07",
            "Pirc Defense",
        ),
        "rnbqkb1r/ppp1pp1p/3p1np1/8/3PP3/2N3P1/PPP2P1P/R1BQKBNR b KQkq -": (
            "B07",
            "Pirc Defense: Sveshnikov System",
        ),
        "r1bq1rk1/ppp1ppbp/2np1np1/8/3PP3/2N2N2/PPP1BPPP/R1BQ1RK1 w - -": (
            "B08",
            "Pirc Defense: Classical Variation, Quiet System, Chigorin Line",
        ),
        "rnbq1rk1/pp2ppbp/2pp1np1/8/3PP3/2N2N2/PPP1BPPP/R1BQ1RK1 w - -": (
            "B08",
            "Pirc Defense: Classical Variation, Quiet System, Czech Defense",
        ),
        "rn1q1rk1/ppp1ppbp/3p1np1/8/3PP1b1/2N2N2/PPP1BPPP/R1BQ1RK1 w - -": (
            "B08",
            "Pirc Defense: Classical Variation, Quiet System, Parma Defense",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/3PP3/2N2N2/PPP1BPPP/R1BQK2R b KQkq -": (
            "B08",
            "Pirc Defense: Classical Variation, Quiet System",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/3PP3/2N2N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "B08",
            "Pirc Defense: Classical Variation",
        ),
        "rnbqkb1r/ppp1pp1p/3p1np1/8/3PP3/2N2N2/PPP2PPP/R1BQKB1R b KQkq -": (
            "B08",
            "Pirc Defense: Classical Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/3PP3/2N2N1P/PPP2PP1/R1BQKB1R b KQkq -": (
            "B08",
            "Pirc Defense: Classical Variation, Schlechter Variation",
        ),
        "rnbqk2r/pp2ppbp/3p1np1/2p5/3PPP2/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "B09",
            "Pirc Defense: Austrian Attack, Dragon Formation",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/3PPP2/2N1BN2/PPP3PP/R2QKB1R b KQ -": (
            "B09",
            "Pirc Defense: Austrian Attack, Kurajica Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2BPPP2/2N5/PPP3PP/R1BQK1NR b KQkq -": (
            "B09",
            "Pirc Defense: Austrian Attack, Ljubojević Variation",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/3PPP2/2N2N2/PPP3PP/R1BQKB1R w KQ -": (
            "B09",
            "Pirc Defense: Austrian Attack",
        ),
        "rnbqkb1r/ppp1pp1p/3p1np1/8/3PPP2/2N5/PPP3PP/R1BQKBNR b KQkq -": (
            "B09",
            "Pirc Defense: Austrian Attack",
        ),
        "rnbq1rk1/pppnppbp/3p2p1/4P3/3P1P1P/2N2N2/PPP3P1/R1BQKB1R b KQ -": (
            "B09",
            "Pirc Defense: Austrian Attack, Unzicker Attack, Bronstein Variation",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/4P3/3P1P2/2N2N2/PPP3PP/R1BQKB1R b KQ -": (
            "B09",
            "Pirc Defense: Austrian Attack, Unzicker Attack",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/3PPP2/2NB1N2/PPP3PP/R1BQK2R b KQ -": (
            "B09",
            "Pirc Defense: Austrian Attack, Weiss Variation",
        ),
        "rnbqkb1r/pp2pppp/5n2/3P4/8/8/PP1P1PPP/RNBQKBNR w KQkq -": (
            "B10",
            "Caro-Kann Defense: Accelerated Panov Attack, Modern Variation",
        ),
        "rnbqkbnr/pp1p1ppp/2p5/4p3/2P1P3/8/PP1P1PPP/RNBQKBNR w KQkq -": (
            "B10",
            "Caro-Kann Defense: Accelerated Panov Attack, Open Variation",
        ),
        "rnb1kbnr/pp2pppp/2p5/3q4/2P5/8/PP1P1PPP/RNBQKBNR w KQkq -": (
            "B10",
            "Caro-Kann Defense: Accelerated Panov Attack, Pseudo-Scandinavian Variation",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/2P1P3/8/PP1P1PPP/RNBQKBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Accelerated Panov Attack",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/2P1P3/8/PP1P1PPP/RNBQKBNR w KQkq -": (
            "B10",
            "Caro-Kann Defense: Accelerated Panov Attack",
        ),
        "rnbqkbnr/pp2pppp/8/3p4/4P3/1Q6/PP1P1PPP/RNB1KBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Accelerated Panov Attack, van Weersel Attack",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/4P3/3P4/PPP2PPP/RNBQKBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Breyer Variation",
        ),
        "rnbq1rk1/pp2npbp/2p3p1/3pp3/1P2P3/3P1NP1/P1PN1PBP/R1BQ1RK1 b - -": (
            "B10",
            "Caro-Kann Defense: Breyer Variation, Stein Attack",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/4P3/1P6/P1PP1PPP/RNBQKBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Euwe Attack",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/4P3/2N2Q2/PPPP1PPP/R1B1KBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Goldman Variation",
        ),
        "rnbqkbnr/pp2pppp/2p5/6N1/4p3/2N5/PPPP1PPP/R1BQKB1R b KQkq -": (
            "B10",
            "Caro-Kann Defense: Hector Gambit",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/2B1P3/8/PPPP1PPP/RNBQK1NR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Hillbilly Attack",
        ),
        "rnbqkbnr/pp2pppp/2p5/7Q/4p3/1B6/PPPP1PPP/RNB1K1NR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Hillbilly Attack, Schaeffer Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/1P1p4/4P3/8/P1PP1PPP/RNBQKBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Labahn Attack, Double Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/2p5/4p3/1P2P3/8/PBPP1PPP/RN1QKBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Labahn Attack, Polish Variation",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B10",
            "Caro-Kann Defense",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "B10",
            "Caro-Kann Defense",
        ),
        "rnbqkbnr/pp2pppp/2p5/6B1/4p3/2NP4/PPP2PPP/R2QKBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Scorpion-Horus Gambit",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/4P1P1/8/PPPP1P1P/RNBQKBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Spike Variation",
        ),
        "rnbqkbnr/pp2pppp/2p5/8/4p1P1/2NP4/PPP2P1P/R1BQKBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Spike Variation, Scorpion-Grob Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/3pP3/2P5/8/PP1P1PPP/RNBQKBNR b KQkq -": (
            "B10",
            "Caro-Kann Defense: Toikkanen Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/4P3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq -": (
            "B10",
            "Caro-Kann Defense: Two Knights Attack",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/2PPP3/8/PP3PPP/RNBQKBNR b KQkq -": (
            "B10",
            "Slav Defense: Diemer Gambit",
        ),
        "rn1qkbnr/pp2pppp/2p5/3p4/4P3/2N2b1P/PPPP1PP1/R1BQKB1R w KQkq -": (
            "B11",
            "Caro-Kann Defense: Two Knights Attack, Mindeno Variation, Exchange Line",
        ),
        "rn1qkbnr/pp2pppp/2p5/3p3b/4P3/2N2N1P/PPPP1PP1/R1BQKB1R w KQkq -": (
            "B11",
            "Caro-Kann Defense: Two Knights Attack, Mindeno Variation, Retreat Line",
        ),
        "rn1qkbnr/pp2pppp/2p5/3p4/4P1b1/2N2N2/PPPP1PPP/R1BQKB1R w KQkq -": (
            "B11",
            "Caro-Kann Defense: Two Knights Attack, Mindeno Variation",
        ),
        "rn1qkbnr/pp3ppp/2p1p3/3pPb2/3P4/2P5/PP2BPPP/RNBQK1NR b KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation, Short Variation",
        ),
        "rn1qkbnr/pp2pppp/2p5/3pPb2/3P2P1/8/PPP2P1P/RNBQKBNR b KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation, Bayonet Attack",
        ),
        "rnbqkbnr/pp2pppp/8/2ppP3/3P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation, Botvinnik-Carls Defense",
        ),
        "rn1qkbnr/pp2pppp/2p5/3pPb2/3P4/8/PPP1NPPP/RNBQKB1R b KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation, Bronstein Variation",
        ),
        "rn1qkbnr/pp2pppp/2p5/3pPb2/1P1P4/8/P1P2PPP/RNBQKBNR b KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation, Prins Attack",
        ),
        "rnbqkbnr/pp2pppp/2p5/3pP3/3P4/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation",
        ),
        "rn1qkbnr/pp2pppp/2p5/3pPb2/3P4/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation, Short Variation",
        ),
        "rn1qkbnr/pp2pppp/2p5/3pPb2/3P3P/8/PPP2PP1/RNBQKBNR b KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation, Tal Variation",
        ),
        "rn2kbnr/pp2pppp/1qp5/3pPb2/3P4/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation, van der Wiel Attack, Dreyev Defense",
        ),
        "rn1qkbnr/pp2pppp/2p5/3pPb2/3P4/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation, van der Wiel Attack",
        ),
        "rn1qkbnr/pp3ppp/4p1b1/2ppP3/3P2PP/2N5/PPP1NP2/R1BQKB1R b KQkq -": (
            "B12",
            "Caro-Kann Defense: Advance Variation, van der Wiel Attack",
        ),
        "r1bqkbnr/pp1ppppp/n1p5/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B12",
            "Caro-Kann Defense: de Bruycker Defense",
        ),
        "r1bqkbnr/ppnppppp/2p5/8/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B12",
            "Caro-Kann Defense: de Bruycker Defense",
        ),
        "rnb1kbnr/pp2pppp/1qp5/3p4/3PP3/8/PPPN1PPP/R1BQKBNR w KQkq -": (
            "B12",
            "Caro-Kann Defense: Edinburgh Variation",
        ),
        "rnbqkbnr/pp3ppp/2p5/8/2BpP3/5N2/PPP3PP/RNBQK2R b KQkq -": (
            "B12",
            "Caro-Kann Defense: Maróczy Variation, Maróczy Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/3PP3/5P2/PPP3PP/RNBQKBNR b KQkq -": (
            "B12",
            "Caro-Kann Defense: Maróczy Variation",
        ),
        "rnbqkb1r/pp1ppppp/2p2n2/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B12",
            "Caro-Kann Defense: Masi Variation",
        ),
        "rnbqkbnr/pp1pp1pp/2p5/5p2/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B12",
            "Caro-Kann Defense: Massachusetts Defense",
        ),
        "rnbqkb1r/pp1npppp/2p1P3/3p4/3P4/3B4/PPP2PPP/RNBQK1NR b KQkq -": (
            "B12",
            "Caro-Kann Defense: Mieses Attack, Landau Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/3PP3/4B3/PPP2PPP/RN1QKBNR b KQkq -": (
            "B12",
            "Caro-Kann Defense: Mieses Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/3PP3/8/PPPN1PPP/R1BQKBNR b KQkq -": (
            "B12",
            "Caro-Kann Defense: Modern Variation",
        ),
        "rnbqkbnr/pp1ppppp/2p5/8/3PP3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "B12",
            "Caro-Kann Defense",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "B12",
            "Caro-Kann Defense",
        ),
        "rnbqkbnr/pp2pppp/2p5/6N1/3Pp3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "B12",
            "Caro-Kann Defense: Ulysses Gambit",
        ),
        "rnbqkbnr/pp2pppp/8/3p4/3P2P1/8/PPP2P1P/RNBQKBNR b KQkq -": (
            "B13",
            "Caro-Kann Defense: Exchange Variation, Bulla Attack",
        ),
        "rnbqkbnr/pp2pppp/2p5/3P4/3P4/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "B13",
            "Caro-Kann Defense: Exchange Variation",
        ),
        "r1bqkb1r/pp2pppp/2n2n2/3p4/3P1B2/2PB4/PP3PPP/RN1QK1NR b KQkq -": (
            "B13",
            "Caro-Kann Defense: Exchange Variation, Rubinstein Variation",
        ),
        "rnbqkb1r/pp2pppp/5n2/2Pp4/3P4/8/PP3PPP/RNBQKBNR b KQkq -": (
            "B13",
            "Caro-Kann Defense: Panov Attack, Gunderam Attack",
        ),
        "r1bqkb1r/pp3ppp/2n1pn2/3p2B1/2PP4/2N5/PP3PPP/R2QKBNR w KQkq -": (
            "B13",
            "Caro-Kann Defense: Panov Attack, Modern Defense, Carlsbad Line",
        ),
        "r1b1kb1r/pp2pppp/2n2n2/q2p2B1/2PP4/2N5/PP3PPP/R2QKBNR w KQkq -": (
            "B13",
            "Caro-Kann Defense: Panov Attack, Modern Defense, Czerniak Line",
        ),
        "r2qkb1r/pp2pppp/2n2n2/3p4/2PP2b1/2N2N2/PP3PPP/R1BQKB1R w KQkq -": (
            "B13",
            "Caro-Kann Defense: Panov Attack, Modern Defense, Mieses Line",
        ),
        "r1bqkb1r/pp2pppp/2n2n2/3p4/2PP4/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "B13",
            "Caro-Kann Defense: Panov Attack, Modern Defense",
        ),
        "r1b1kb1r/pp2pppp/1qn2n2/3p2B1/2PP4/2N5/PP3PPP/R2QKBNR w KQkq -": (
            "B13",
            "Caro-Kann Defense: Panov Attack, Modern Defense, Reifir-Spielmann Line",
        ),
        "rnbqkb1r/pp2pppp/5n2/3p4/2PP4/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "B13",
            "Caro-Kann Defense: Panov Attack",
        ),
        "rnbqkbnr/pp2pppp/8/3p4/2PP4/8/PP3PPP/RNBQKBNR b KQkq -": (
            "B13",
            "Caro-Kann Defense: Panov Attack",
        ),
        "r1bqkb1r/pp2pppp/5n2/n2P2B1/2p5/2N5/PP3PPP/R2QKBNR w KQkq -": (
            "B13",
            "Caro-Kann Defense: Panov-Botvinnik, Herzog Defense",
        ),
        "rnbqk2r/pp2ppbp/5np1/3P4/3P4/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "B14",
            "Caro-Kann Defense: Panov Attack, Fianchetto Defense, Fianchetto Gambit",
        ),
        "rnbqkb1r/pp2pp1p/5np1/3p4/2PP4/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "B14",
            "Caro-Kann Defense: Panov Attack, Fianchetto Defense",
        ),
        "rnbqkb1r/pp3ppp/4pn2/3p4/2PP4/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "B14",
            "Caro-Kann Defense: Panov Attack",
        ),
        "rnbqk2r/pp3ppp/4pn2/3p4/1bPP4/2N2N2/PP3PPP/R1BQKB1R w KQkq -": (
            "B14",
            "Nimzowitsch-Indian Defense: Panov Attack, Main Line",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/8/3PN3/3B4/PPP2PPP/R1BQK1NR b KQkq -": (
            "B15",
            "Caro-Kann Defense: Alekhine Gambit",
        ),
        "rnbqkbnr/pp2ppp1/2p4p/8/3PN3/8/PPP2PPP/R1BQKBNR w KQkq -": (
            "B15",
            "Caro-Kann Defense: Finnish Variation",
        ),
        "rnbqkb1r/pp3ppp/2p2p2/8/2BP4/8/PPP2PPP/R1BQK1NR b KQkq -": (
            "B15",
            "Caro-Kann Defense: Forgacs Variation",
        ),
        "rnbqkbnr/p3pppp/2p5/1p1p4/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B15",
            "Caro-Kann Defense: Gurgenidze Counterattack",
        ),
        "rnbqkbnr/pp2pp1p/2p3p1/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "B15",
            "Caro-Kann Defense: Gurgenidze System",
        ),
        "rnbqkbnr/pp2pppp/2p5/8/3PN3/8/PPP2PPP/R1BQKBNR b KQkq -": (
            "B15",
            "Caro-Kann Defense: Main Line",
        ),
        "rnbqkbnr/pp2pppp/2p5/8/3Pp3/2N2P2/PPP3PP/R1BQKBNR b KQkq -": (
            "B15",
            "Caro-Kann Defense: Rasa-Studier Gambit",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "B15",
            "Caro-Kann Defense",
        ),
        "rnbqkb1r/pp3ppp/2p2p2/8/3P4/8/PPP2PPP/R1BQKBNR w KQkq -": (
            "B15",
            "Caro-Kann Defense: Tartakower Variation",
        ),
        "rnbqkbnr/pp2pppp/2p5/8/2BPp3/2N5/PPP2PPP/R1BQK1NR b KQkq -": (
            "B15",
            "Caro-Kann Defense: von Hennig Gambit",
        ),
        "rnbqkb1r/pp2pp1p/2p2p2/8/3P4/8/PPP2PPP/R1BQKBNR w KQkq -": (
            "B16",
            "Caro-Kann Defense: Bronstein-Larsen Variation",
        ),
        "r1bqk2r/pp1n1pp1/2pbp2p/8/3PQ3/3B1N2/PPP2PPP/R1B1K2R b KQkq -": (
            "B17",
            "Caro-Kann Defense: Karpov Variation, Modern Main Line",
        ),
        "r1bqkbnr/pp2pppp/2p2n2/6N1/3P4/8/PPP2PPP/R1BQKBNR w KQkq -": (
            "B17",
            "Caro-Kann Defense: Karpov Variation, Modern Variation, Ivanchuk Defense",
        ),
        "r1bqkb1r/pp1npppp/2p2n2/8/3P4/5NN1/PPP2PPP/R1BQKB1R b KQkq -": (
            "B17",
            "Caro-Kann Defense: Karpov Variation, Modern Variation, Kasparov Attack",
        ),
        "r1bqkbnr/pp1npppp/2p5/6N1/3P4/8/PPP2PPP/R1BQKBNR b KQkq -": (
            "B17",
            "Caro-Kann Defense: Karpov Variation, Modern Variation",
        ),
        "r1bqkbnr/pp1npppp/2p5/8/3PN3/8/PPP2PPP/R1BQKBNR w KQkq -": (
            "B17",
            "Caro-Kann Defense: Karpov Variation",
        ),
        "r1bqkb1r/pp3ppp/1np1pn2/6N1/3P4/1B6/PPP1QPPP/R1B1K1NR b KQkq -": (
            "B17",
            "Caro-Kann Defense: Karpov Variation, Smyslov Variation, Main Line",
        ),
        "r1bqkb1r/pp3ppp/1np1pn2/6N1/2BP4/8/PPP1QPPP/R1B1K1NR w KQkq -": (
            "B17",
            "Caro-Kann Defense: Karpov Variation, Smyslov Variation",
        ),
        "r1bqkb1r/pp2pppp/2p2n2/8/2BP4/8/PPP2PPP/R1BQK1NR w KQkq -": (
            "B17",
            "Caro-Kann Defense: Karpov Variation, Tiviakov-Fischer Attack",
        ),
        "rn1qkbnr/pp2pppp/2p3b1/8/3P4/6NN/PPP2PPP/R1BQKB1R b KQkq -": (
            "B18",
            "Caro-Kann Defense: Classical Variation, Flohr Variation",
        ),
        "rn1qkbnr/pp2pppp/2p3b1/8/3P3P/6N1/PPP2PP1/R1BQKBNR b KQkq -": (
            "B18",
            "Caro-Kann Defense: Classical Variation, Main Line",
        ),
        "rn1qkbnr/pp2pppp/2p3b1/8/3P1P2/6N1/PPP3PP/R1BQKBNR b KQkq -": (
            "B18",
            "Caro-Kann Defense: Classical Variation, Maróczy Attack",
        ),
        "rn1qkbnr/pp2pppp/2p5/5b2/3PN3/8/PPP2PPP/R1BQKBNR w KQkq -": (
            "B18",
            "Caro-Kann Defense: Classical Variation",
        ),
        "r2qkbnr/pp1nppp1/2p3bp/8/3P3P/5NN1/PPP2PP1/R1BQKB1R w KQkq -": (
            "B19",
            "Caro-Kann Defense: Classical Variation",
        ),
        "r2qkbnr/pp1nppp1/2p3bp/7P/3P4/5NN1/PPP2PP1/R1BQKB1R b KQkq -": (
            "B19",
            "Caro-Kann Defense: Classical Variation, Spassky Variation",
        ),
        "r2qk2r/pp1nbpp1/2p1pn1p/7P/3P4/3Q1NN1/PPPB1PP1/2KR3R w kq -": (
            "B19",
            "Caro-Kann Defense: Classical Variation, Lobron System",
        ),
        "r2qk2r/pp1n1pp1/2pbpn1p/7P/3P4/3Q1NN1/PPPB1PP1/2KR3R w kq -": (
            "B19",
            "Caro-Kann Defense: Classical Variation, Seirawan Variation",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/4P3/1P6/PBPP1PPP/RN1QKBNR b KQkq -": (
            "B20",
            "Caro-Kann Defense: Euwe Attack, Prins Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P1Q1/8/PPPP1PPP/RNB1KBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Amazon Attack",
        ),
        "r1bqkbnr/pp2pppp/2np4/2p5/4PP2/2PP4/PP4PP/RNBQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Big Clamp Formation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/2B1P3/8/PPPP1PPP/RNBQK1NR b KQkq -": (
            "B20",
            "Sicilian Defense: Bowdler Attack",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/7N/PPPP1PPP/RNBQKB1R b KQkq -": (
            "B20",
            "Sicilian Defense: Brick Variation",
        ),
        "r1bqkbnr/pp2ppp1/2np4/2p4p/2P1P3/2N3P1/PP1P1P1P/R1BQKBNR w KQkq -": (
            "B20",
            "Sicilian Defense: Gloria Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P1P1/8/PPPP1P1P/RNBQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Grob Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPPNPPP/RNBQKB1R b KQkq -": (
            "B20",
            "Sicilian Defense: Keres Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPPKPPP/RNBQ1BNR b kq -": (
            "B20",
            "Sicilian Defense: King David Opening",
        ),
        "r1bqkbnr/pp1ppppp/2n5/8/2BpP3/N7/PPP2PPP/R1BQK1NR b KQkq -": (
            "B20",
            "Sicilian Defense: Kronberger Variation, Nemeth Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/N7/PPPP1PPP/R1BQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Kronberger Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/6P1/PPPP1P1P/RNBQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Lasker-Dunne Attack",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/P7/1PPP1PPP/RNBQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Mengarini Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P2P/8/PPPP1PP1/RNBQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Myers Attack",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/P3P3/8/1PPP1PPP/RNBQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Myers Attack",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "B20",
            "Sicilian Defense",
        ),
        "rnbqkbnr/p2ppppp/1p6/2p5/4P3/1P6/P1PP1PPP/RNBQKBNR w KQkq -": (
            "B20",
            "Sicilian Defense: Snyder Variation, Queen's Fianchetto Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/1P6/P1PP1PPP/RNBQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Snyder Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/2P1P3/8/PP1P1PPP/RNBQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Staunton-Cochrane Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/8/1p2P3/8/PBPP1PPP/RN1QKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Wing Gambit, Abrahams Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/8/4P3/p7/2PP1PPP/RNBQKBNR w KQkq -": (
            "B20",
            "Sicilian Defense: Wing Gambit, Carlsbad Variation",
        ),
        "rnb1kbnr/pp2pppp/8/3q4/1p6/P7/1BPP1PPP/RN1QKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Wing Gambit, Marienbad Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/8/1p2P3/P7/2PP1PPP/RNBQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Wing Gambit, Marshall Variation",
        ),
        "rnb1kbnr/pp3ppp/4q3/4p3/1pP5/P2B1N2/3P1PPP/RNBQK2R b KQkq -": (
            "B20",
            "Sicilian Defense: Wing Gambit, Nanu Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/1P2P3/8/P1PP1PPP/RNBQKBNR b KQkq -": (
            "B20",
            "Sicilian Defense: Wing Gambit",
        ),
        "r1b1kbnr/pp3ppp/2n1q3/4p3/1pP5/P4N2/1B1P1PPP/RN1QKB1R w KQkq -": (
            "B20",
            "Sicilian Defense: Wing Gambit, Romanian Defense",
        ),
        "rnbqkbnr/pp1ppppp/8/8/1pP1P3/8/P2P1PPP/RNBQKBNR b KQkq c3": (
            "B20",
            "Sicilian Defense: Wing Gambit, Santasiere Variation",
        ),
        "rnbqkbnr/pp2pppp/8/2p5/4pP2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "B21",
            "Bird Opening: Dutch Variation, Batavo Gambit",
        ),
        "r1bqkb1r/pp1ppppp/2n2n2/8/2B1P3/8/PPP2PPP/RNBQK1NR b KQkq -": (
            "B21",
            "Sicilian Defense: Coles Sicilian Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/8/3pPP2/8/PPP3PP/RNBQKBNR b KQkq -": (
            "B21",
            "Sicilian Defense: Halasz Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4PP2/8/PPPP2PP/RNBQKBNR b KQkq -": (
            "B21",
            "Sicilian Defense: McDonnell Attack",
        ),
        "rnbqkb1r/pp2pppp/5n2/2pP4/5P2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "B21",
            "Sicilian Defense: McDonnell Attack, Tal Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/8/4p3/3pP3/2P2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "B21",
            "Sicilian Defense: Morphy Gambit, Andreaschek Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/8/3pP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B21",
            "Sicilian Defense: Morphy Gambit",
        ),
        "rnbqkb1r/1p3ppp/p2ppn2/8/2B1P3/2N2N2/PP3PPP/R1BQ1RK1 w kq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Chicago Defense",
        ),
        "r1bqkb1r/1p2pppp/p1np1n2/8/2B1P3/2N2N2/PP3PPP/R1BQ1RK1 w kq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Classical Formation",
        ),
        "r1bqkbnr/pp1ppp1p/2n3p1/8/4P3/2N2N2/PP3PPP/R1BQKB1R w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Fianchetto Defense",
        ),
        "rnbqkbnr/1p1p1ppp/p3p3/8/4P3/2N2N2/PP3PPP/R1BQKB1R w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Kan Formation",
        ),
        "r1b1k1nr/1pqp1ppp/p1nbp3/8/2B1P3/2N2N2/PP2QPPP/R1B2RK1 w kq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Larsen Defense",
        ),
        "r1bqk1nr/3p1ppp/p1n1p3/1pb5/4P3/1BN2N2/PP3PPP/R1BQ1RK1 w kq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Deferred Morphy Defense",
        ),
        "r1bqk1nr/pp1p1ppp/2n1p3/2b5/2B1P3/2N2N2/PP3PPP/R1BQK2R w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Morphy Defense",
        ),
        "r1bqkbnr/1p1p1ppp/p1n1p3/8/2B1P3/2N2N2/PP3PPP/R1BQK2R w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Paulsen Formation",
        ),
        "r1bqk1nr/pp1p1ppp/2n1p3/8/1bB1P3/2N2N2/PP3PPP/R1BQK2R w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Pin Defense",
        ),
        "r1bqkbnr/pp3ppp/2npp3/8/2B1P3/2N2N2/PP3PPP/R1BQK2R w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Scheveningen Formation",
        ),
        "r1bqkbnr/5ppp/p1npp3/1p6/2B1P3/2N2N2/PP2QPPP/R1B2RK1 w kq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Sozin Formation",
        ),
        "rnbqkb1r/1p1pnppp/p3p3/8/2B1P3/2N2N2/PP3PPP/R1BQK2R w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Accepted, Taimanov Formation",
        ),
        "2bqkbnr/r4ppp/p1npp3/1p6/4P3/1BN2N2/PP2QPPP/R1B2RK1 w k -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit, Chicago Defense",
        ),
        "rnbqkbnr/pp1ppppp/8/8/4P3/2p2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit, Danish Variation",
        ),
        "rnbqkb1r/pp1ppppp/5n2/8/3pP3/2P5/PP3PPP/RNBQKBNR w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Declined, Alapin Formation",
        ),
        "rnbqkbnr/pp1ppppp/8/8/2P1P3/3p4/PP3PPP/RNBQKBNR b KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Declined, Dubois Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/8/4P3/2Pp4/PP3PPP/RNBQKBNR w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Declined, Push Variation",
        ),
        "rnbqkbnr/pp2pppp/8/3p4/3pP3/2P5/PP3PPP/RNBQKBNR w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Declined, Scandinavian Formation",
        ),
        "rnb1kbnr/pp1ppppp/8/q7/3pP3/2P5/PP3PPP/RNBQKBNR w KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit Declined, Wing Formation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/3PP3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit",
        ),
        "rnbqkbnr/pp1ppppp/8/8/3pP3/2P5/PP3PPP/RNBQKBNR b KQkq -": (
            "B21",
            "Sicilian Defense: Smith-Morra Gambit",
        ),
        "r3kbnr/pp2pppp/2n5/3q4/3P2b1/5N2/PP3PPP/RNBQKB1R w KQkq -": (
            "B22",
            "Sicilian Defense: Alapin Variation, Barmen Defense, Central Exchange",
        ),
        "r3kbnr/pp2pppp/8/8/3n4/2N2P2/PP3P1P/R1B1KB1R w KQkq -": (
            "B22",
            "Sicilian Defense: Alapin Variation, Barmen Defense, Endgame Variation",
        ),
        "r1b1k1nr/pp3ppp/2n5/3qp3/1b1P4/2N2N2/PP2BPPP/R1BQK2R b KQkq -": (
            "B22",
            "Sicilian Defense: Alapin Variation, Barmen Defense, Milner-Barry Attack",
        ),
        "rn2kb1r/pp2pppp/5n2/2pq4/3P2b1/2P2N2/PP3PPP/RNBQKB1R w KQkq -": (
            "B22",
            "Sicilian Defense: Alapin Variation, Barmen Defense, Modern Line",
        ),
        "rnb1kbnr/pp2pppp/8/2pq4/8/2P5/PP1P1PPP/RNBQKBNR w KQkq -": (
            "B22",
            "Sicilian Defense: Alapin Variation, Barmen Defense",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/2P5/PP1P1PPP/RNBQKBNR b KQkq -": (
            "B22",
            "Sicilian Defense: Alapin Variation",
        ),
        "rnbqkb1r/pp1ppppp/8/3nP3/3p4/2P5/PP3PPP/RNBQKBNR w KQkq -": (
            "B22",
            "Sicilian Defense: Alapin Variation, Smith-Morra Gambit Declined",
        ),
        "r1b1kb1r/ppqppp1p/1nn5/4P1p1/2p5/2P2N2/PPBPQPPP/RNB1K2R w KQkq -": (
            "B22",
            "Sicilian Defense: Alapin Variation, Stoltz Attack, Ivanchuk Line",
        ),
        "r1bqkb1r/pp1ppppp/1nn5/2p1P3/8/1BP2N2/PP1P1PPP/RNBQK2R b KQkq -": (
            "B22",
            "Sicilian Defense: Alapin Variation, Stoltz Attack",
        ),
        "r1bqkb1r/pp1ppppp/2n5/2pnP3/8/N1P2N2/PP1P1PPP/R1BQKB1R b KQkq -": (
            "B22",
            "Sicilian Defense: Heidenfeld Variation",
        ),
        "rnbqkbnr/pp1p1ppp/8/4p3/3pP3/2P5/PP3PPP/RNBQKBNR w KQkq -": (
            "B22",
            "Sicilian Defense: Smith-Morra Gambit Declined, Center Formation",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/2p5/4P3/2N3P1/PPPP1P1P/R1BQKBNR b KQkq -": (
            "B23",
            "Sicilian Defense: Closed Defense",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/2p5/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "B23",
            "Sicilian Defense: Closed Defense",
        ),
        "r1bqkbnr/pp1ppppp/2n5/2p5/4P3/2N5/PPPPNPPP/R1BQKB1R b KQkq -": (
            "B23",
            "Sicilian Defense: Closed Defense, Chameleon Variation",
        ),
        "r1bqkbnr/pp1ppppp/2n5/2p5/4P1P1/2N5/PPPP1P1P/R1BQKBNR b KQkq -": (
            "B23",
            "Sicilian Defense: Closed Defense, Grob Attack",
        ),
        "rnbqkbnr/pp3ppp/4p3/2pp4/4P3/2N3P1/PPPP1P1P/R1BQKBNR w KQkq -": (
            "B23",
            "Sicilian Defense: Closed Defense, Korchnoi Defense",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq -": (
            "B23",
            "Sicilian Defense: Closed Defense",
        ),
        "r1bqkbnr/pp1ppppp/2n5/2p5/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "B23",
            "Sicilian Defense: Closed Defense, Traditional Line",
        ),
        "r1bqkbnr/pp1ppppp/2n5/2p5/4PP2/2N5/PPPP2PP/R1BQKBNR b KQkq -": (
            "B23",
            "Sicilian Defense: Grand Prix Attack",
        ),
        "r1bqk1nr/pp1p1pbp/2n1p1p1/2p2P2/2B1P3/2N2N2/PPPP2PP/R1BQK2R b KQkq -": (
            "B23",
            "Sicilian Defense: Grand Prix Attack, Schofman Variation",
        ),
        "r1bqk1nr/pp1pppbp/2n3p1/2p5/4P3/2N3P1/PPPP1PBP/R1BQK1NR w KQkq -": (
            "B24",
            "Sicilian Defense: Closed Defense",
        ),
        "r1bqkbnr/pp1ppp1p/2n3p1/2p5/4P3/2N3P1/PPPP1P1P/R1BQKBNR w KQkq -": (
            "B24",
            "Sicilian Defense: Closed Defense",
        ),
        "r1bqkbnr/pp1ppppp/2n5/2p5/4P3/2N3P1/PPPP1P1P/R1BQKBNR b KQkq -": (
            "B24",
            "Sicilian Defense: Closed Defense, Fianchetto Variation",
        ),
        "r1bqk1nr/pp1p1pbp/4p1p1/2p5/3nP3/3PB1P1/PPP1NPBP/R2QK1NR b KQkq -": (
            "B24",
            "Sicilian Defense: Closed Defense, Smyslov Variation",
        ),
        "r1bqk1nr/pp2ppbp/2np2p1/2p5/4P3/2NP2P1/PPP2PBP/R1BQK1NR w KQkq -": (
            "B25",
            "Sicilian Defense: Closed Defense",
        ),
        "r1bqk2r/pp2npbp/2np2p1/2p1p3/4PP2/2NP2PN/PPP3BP/R1BQK2R w KQkq -": (
            "B25",
            "Sicilian Defense: Closed Defense, Botvinnik Defense, Edge Variation",
        ),
        "r1bqk1nr/pp3pbp/2np2p1/2p1p3/4P3/2NP2P1/PPP1NPBP/R1BQK2R w KQkq -": (
            "B25",
            "Sicilian Defense: Closed Defense, Botvinnik Defense",
        ),
        "r1bqk1nr/pp3pbp/2np2p1/2p1p3/4PP2/2NP2P1/PPP3BP/R1BQK1NR w KQkq -": (
            "B25",
            "Sicilian Defense: Closed Defense, Botvinnik Defense",
        ),
        "r1bqk1nr/pp2ppbp/2np2p1/2p5/4PP2/2NP2P1/PPP3BP/R1BQK1NR b KQkq -": (
            "B25",
            "Sicilian Defense: Closed Defense",
        ),
        "r1bqk1nr/pp2ppbp/2np2p1/2p5/4P3/2NPB1P1/PPP2PBP/R2QK1NR b KQkq -": (
            "B26",
            "Sicilian Defense: Closed Defense",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/3PP3/2N2N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "B27",
            "Modern Defense: Pterodactyl Defense",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/3PP3/2N1BN2/PPP2PPP/R2QKB1R b KQkq -": (
            "B27",
            "Pterodactyl Defense: Sicilian Variation, Anhanguera Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1pP4/4P3/2N2N2/PPP2PPP/R1BQKB1R b KQkq -": (
            "B27",
            "Pterodactyl Defense: Sicilian Variation, Benoni Gambit",
        ),
        "rnb1k1nr/pp1ppp1p/6p1/q1P5/4P3/2P2N2/P1P2PPP/R1BQKB1R b KQkq -": (
            "B27",
            "Pterodactyl Defense: Sicilian Variation, Pteranodon Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1P5/4P3/2N2N2/PPP2PPP/R1BQKB1R b KQkq -": (
            "B27",
            "Pterodactyl Defense: Sicilian Variation, Rhamphorhynchus Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/3PP3/2N2N2/PPPB1PPP/R2QKB1R b KQkq -": (
            "B27",
            "Pterodactyl Defense: Sicilian Variation, Unpin Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1p5/3PP3/2P2N2/PP3PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Pterodactyl Defense: Western Variation, Pterodactyl Variation",
        ),
        "rnb1k1nr/pp1pppbp/6p1/q1P5/4P3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Pterodactyl Defense: Western Variation, Rhamphorhynchus Variation",
        ),
        "rnbqk1nr/pp1ppp1p/6pb/2p5/2P1P3/5N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Acton Extension Variation",
        ),
        "rnbqkbnr/pp1pp1pp/8/2p2p2/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Brussels Gambit",
        ),
        "rnbqkbnr/pp1pppp1/7p/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Bücker Variation",
        ),
        "rnbqkb1r/pp1pp1pp/7n/2p2P2/8/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Double-Dutch Gambit",
        ),
        "rnbqkbnr/pp1pp2p/6p1/2p2p2/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Frederico Variation",
        ),
        "rnbqkbnr/pp1ppp1p/6p1/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Hyperaccelerated Dragon Variation",
        ),
        "rnbqkbnr/pp1ppp1p/6p1/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B27",
            "Sicilian Defense: Hyperaccelerated Fianchetto Variation",
        ),
        "rnb1k1nr/pp1ppp1p/6p1/2P5/4P3/2q2N2/P1P2PPP/R1BQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Hyperaccelerated Pterodactyl Defense, Exchange Variation",
        ),
        "rnbqk1nr/pp1pppbp/6p1/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Hyperaccelerated Pterodactyl Defense",
        ),
        "rnbqkbnr/pp1p1ppp/8/2p1p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Jalalabad Variation",
        ),
        "rnbqkbnr/p2ppppp/1p6/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Katalimov Variation",
        ),
        "rnb1kbnr/pp1ppppp/8/q1p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Mongoose Variation",
        ),
        "rnbqkbnr/p2ppppp/8/1pp5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Polish Gambit",
        ),
        "rnb1kbnr/ppqppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B27",
            "Sicilian Defense: Quinteros Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "B27",
            "Sicilian Defense",
        ),
        "rnbqkbnr/1p1ppppp/p7/2p5/4P3/5N2/PPPPBPPP/RNBQK2R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Aronin System",
        ),
        "rnbqkbnr/1p1ppppp/p7/2p5/4P3/1P3N2/P1PP1PPP/RNBQKB1R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Kieseritzky System",
        ),
        "rnbqkbnr/1p1p1ppp/p3p3/2p5/2P1P3/5N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Maróczy Bind Formation, Paulsen Line",
        ),
        "rnbqkbnr/1p1ppppp/p7/2p5/2P1P3/5N2/PP1P1PPP/RNBQKB1R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Maróczy Bind Formation",
        ),
        "rnbqkbnr/1p2pppp/p2p4/2p5/2P1P3/5N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Maróczy Bind Formation, Robatsch Line",
        ),
        "rnbqkbnr/1p1ppppp/p7/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Normal System, Cortlever Gambit",
        ),
        "rnbqkbnr/1p1ppppp/p7/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Normal System",
        ),
        "rnbqkbnr/1p1ppppp/p7/8/3pP3/2P2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Normal System, Smith-Morra Line",
        ),
        "rnbqkbnr/1p1p1ppp/p7/4p3/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Normal System, Taimanov Line",
        ),
        "rnbqkbnr/1p1ppppp/p7/8/3QP3/5N2/PPP2PPP/RNB1KB1R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Normal System, Zagorovsky Line",
        ),
        "rnbqkbnr/1p1ppppp/p7/2p5/4P3/3P1N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Quiet System",
        ),
        "rnbqkbnr/1p1ppppp/p7/2p5/4P3/5NP1/PPPP1P1P/RNBQKB1R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Réti System",
        ),
        "rnbqkbnr/1p1ppppp/p7/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation",
        ),
        "rnbqkb1r/1p1ppppp/p4n2/2p5/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Venice System, Barcza Line",
        ),
        "rnbqkb1r/1p2pppp/p4n2/2pP4/8/2P2N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Venice System, Gambit Line",
        ),
        "rnbqkbnr/3ppppp/p7/1pp5/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Venice System, Ljubojević Line",
        ),
        "rnbqkbnr/1p1ppppp/p7/2p5/4P3/2P2N2/PP1P1PPP/RNBQKB1R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Venice System",
        ),
        "rnbqkbnr/1p2pppp/p2p4/2p5/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Venice System, Steiner Line",
        ),
        "rnbqkbnr/1p1ppppp/p7/2p5/1P2P3/5N2/P1PP1PPP/RNBQKB1R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Wing Gambit",
        ),
        "rnbqkbnr/1p1ppppp/p7/2p5/4P3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq -": (
            "B28",
            "Sicilian Defense: O'Kelly Variation, Yerevan System",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2p1P3/8/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "B29",
            "Sicilian Defense: Nimzowitsch Variation, Advance Variation",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2p5/4P3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq -": (
            "B29",
            "Sicilian Defense: Nimzowitsch Variation, Closed Variation",
        ),
        "rnbqkb1r/pp1ppppp/8/2p1P3/8/2n2N2/PPPP1PPP/R1BQKB1R w KQkq -": (
            "B29",
            "Sicilian Defense: Nimzowitsch Variation, Exchange Variation",
        ),
        "r1bqkb1r/pp1p1ppp/2n5/2ppP3/3P4/5N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "B29",
            "Sicilian Defense: Nimzowitsch Variation, Main Line",
        ),
        "rnbqkb1r/pp1ppppp/5n2/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B29",
            "Sicilian Defense: Nimzowitsch Variation",
        ),
        "r1bqk1nr/pp3ppp/2np4/2p1p1b1/2B1P3/2NP4/PPPN1PPP/R1BQK2R w KQkq -": (
            "B30",
            "Sicilian Defense: Closed Defense, Anti-Sveshnikov Variation, Kharlov-Kramnik Line",
        ),
        "r1bqkbnr/pp1ppppp/2n5/1Bp5/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "B30",
            "Sicilian Defense: Nezhmetdinov-Rossolimo Attack",
        ),
        "r1bqkbnr/pp1ppppp/8/nBp5/1P2P3/5N2/P1PP1PPP/RNBQK2R b KQkq -": (
            "B30",
            "Sicilian Defense: Nezhmetdinov-Rossolimo Attack, San Francisco Gambit",
        ),
        "r1bqkbnr/pp1ppppp/2n5/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B30",
            "Sicilian Defense: Old Sicilian Variation",
        ),
        "rnbqkbnr/pp1ppppp/8/1Bp5/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "B30",
            "Sicilian Defense: Rossolimo Variation, Brooklyn Retreat Defense",
        ),
        "r1bqk1nr/pp1p1pbp/2n3p1/1Bp1p3/3PP3/2P2N2/PP3PPP/RNBQ1RK1 b kq -": (
            "B31",
            "Sicilian Defense: Nezhmetdinov-Rossolimo Attack, Fianchetto Variation, Gufeld Gambit",
        ),
        "r1bqk2r/pp1pppbp/2n2np1/1Bp5/3PP3/2P2N2/PP3PPP/RNBQ1RK1 b kq -": (
            "B31",
            "Sicilian Defense: Nezhmetdinov-Rossolimo Attack, Fianchetto Variation, Lutikov Gambit",
        ),
        "r1bqkbnr/pp1ppp1p/2n3p1/1Bp5/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "B31",
            "Sicilian Defense: Nezhmetdinov-Rossolimo Attack, Fianchetto Variation",
        ),
        "r1bqk2r/pp1pppbp/2n2np1/1Bp5/Q3P3/2P2N2/PP1P1PPP/RNB2RK1 b kq -": (
            "B31",
            "Sicilian Defense: Nezhmetdinov-Rossolimo Attack, Fianchetto Variation, Totsky Attack",
        ),
        "r1bqk1nr/pp1p1pbp/2n3p1/1Bp1p3/1P2P3/5N2/P1PP1PPP/RNBQR1K1 b kq -": (
            "B31",
            "Sicilian Defense: Nezhmetdinov-Rossolimo Attack, Gurgenidze Variation",
        ),
        "r1bqkbnr/pp1ppp1p/2n3p1/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B32",
            "Sicilian Defense: Accelerated Dragon",
        ),
        "r1b1kbnr/ppqppppp/2n5/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B32",
            "Sicilian Defense: Flohr Variation",
        ),
        "r1bqkbnr/pp1p1ppp/2n1p3/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B32",
            "Sicilian Defense: Franco-Sicilian Variation",
        ),
        "r1b1kbnr/pp1ppppp/1qn5/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B32",
            "Sicilian Defense: Godiva Variation",
        ),
        "r1bqkbnr/pp3ppp/2np4/1N2p3/4P3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B32",
            "Sicilian Defense: Kalashnikov Variation",
        ),
        "r1bqkbnr/pp1p1ppp/2n5/4p3/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B32",
            "Sicilian Defense: Löwenthal Variation",
        ),
        "r1bqkbnr/pp2pppp/2n5/3p4/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B32",
            "Sicilian Defense: Nimzowitsch-American Variation",
        ),
        "r1bqkbnr/1p1p1ppp/p1n5/4p3/2PNP3/8/PP3PPP/RNBQKB1R w KQkq -": (
            "B32",
            "Sicilian Defense: O'Kelly Variation, Maróczy Bind Formation, Geller Line",
        ),
        "r1bqkbnr/pp1ppppp/2n5/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B32",
            "Sicilian Defense: Open Variation",
        ),
        "r1bqkbnr/pp1ppppp/2n5/8/3NP3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "B32",
            "Sicilian Defense: Open Variation",
        ),
        "r1bqkbnr/pp1ppppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B32",
            "Sicilian Defense: Open Variation",
        ),
        "r1bqk2r/pp1p1ppp/2n1pn2/1Nb5/4P3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B33",
            "Sicilian Defense: Four Knights Variation, Cobra Variation",
        ),
        "r2qkb1r/1p3ppp/p1npbn2/4p1B1/4P3/N1N5/PPP2PPP/R2QKB1R w KQkq -": (
            "B33",
            "Sicilian Defense: Lasker-Pelikan Variation, Bird Variation",
        ),
        "r1bqkb1r/pp1p1ppp/2N2n2/4p3/4P3/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "B33",
            "Sicilian Defense: Lasker-Pelikan Variation, Exchange Variation",
        ),
        "r1bqkb1r/pp1p1ppp/2n2n2/4p3/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B33",
            "Sicilian Defense: Lasker-Pelikan Variation",
        ),
        "r1bqkb1r/pp1p1ppp/2n2n2/4p3/4P3/2N2N2/PPP2PPP/R1BQKB1R b KQkq -": (
            "B33",
            "Sicilian Defense: Lasker-Pelikan Variation, Retreat Variation",
        ),
        "r1bqkb1r/pp1p1ppp/2n2n2/4p3/4P3/1NN5/PPP2PPP/R1BQKB1R b KQkq -": (
            "B33",
            "Sicilian Defense: Lasker-Pelikan Variation, Schlechter Variation",
        ),
        "r1bqkb1r/5ppp/p1np1n2/1p1Np1B1/4P3/N7/PPP2PPP/R2QKB1R b KQkq -": (
            "B33",
            "Sicilian Defense: Lasker-Pelikan Variation, Sveshnikov Variation, Chelyabinsk Variation",
        ),
        "r1bqk2r/5pbp/p1np1p2/1p1Np3/4P3/N7/PPP2PPP/R2QKB1R w KQkq -": (
            "B33",
            "Sicilian Defense: Lasker-Pelikan Variation, Sveshnikov Variation, Novosibirsk Variation",
        ),
        "r1bqkb1r/5p1p/p1np4/1B1Npp2/4P3/N7/PPP2PPP/R2QK2R b KQkq -": (
            "B33",
            "Sicilian Defense: Lasker-Pelikan Variation, Sveshnikov Variation, Peresypkin Sacrifice",
        ),
        "r1bqkb1r/5p1p/p1np4/1p1Npp2/4P3/N7/PPP2PPP/R2QKB1R w KQkq -": (
            "B33",
            "Sicilian Defense: Lasker-Pelikan Variation, Sveshnikov Variation",
        ),
        "r1bqkb1r/5ppp/p1np1n2/1p2p1B1/4P3/N1N5/PPP2PPP/R2QKB1R w KQkq -": (
            "B33",
            "Sicilian Defense: Lasker-Pelikan Variation, Sveshnikov Variation",
        ),
        "r1bqkb1r/pp1ppppp/2n2n2/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B33",
            "Sicilian Defense: Open Variation",
        ),
        "r1bqkbnr/pp1ppp1p/2N3p1/8/4P3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "B34",
            "Sicilian Defense: Accelerated Dragon, Exchange Variation",
        ),
        "r1bqkbnr/pp1ppp1p/2n3p1/8/3NP3/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "B34",
            "Sicilian Defense: Accelerated Dragon, Modern Variation",
        ),
        "r1bqk2r/pp1pppbp/2n2np1/8/2BNP3/2N1B3/PPP2PPP/R2QK2R b KQkq -": (
            "B35",
            "Sicilian Defense: Accelerated Dragon, Modern Bc4 Variation",
        ),
        "r1bqk2r/pp2ppbp/2np1np1/8/2BNP3/2N1B3/PPP2PPP/R2QK2R w KQkq -": (
            "B35",
            "Sicilian Defense: Dragon Variation, Modern Bc4 Variation",
        ),
        "r1bqkb1r/pp2pp1p/3p1np1/8/2PQP3/2N5/PP3PPP/R1B1KB1R w KQkq -": (
            "B36",
            "Sicilian Defense: Accelerated Dragon, Maróczy Bind Formation, Gurgenidze Variation",
        ),
        "r1bqkbnr/pp1ppp1p/2n3p1/8/2PNP3/8/PP3PPP/RNBQKB1R b KQkq -": (
            "B36",
            "Sicilian Defense: Accelerated Dragon, Maróczy Bind Formation",
        ),
        "r1bqk1nr/pp1pppbp/2n3p1/8/2PNP3/8/PP3PPP/RNBQKB1R w KQkq -": (
            "B37",
            "Sicilian Defense: Accelerated Fianchetto, Maróczy Bind Formation",
        ),
        "r1bqk2r/pp2ppbp/2np2pn/8/2P1P3/8/PPN1BPPP/RNBQK2R w KQkq -": (
            "B37",
            "Sicilian Defense: Accelerated Fianchetto, Simagin Variation",
        ),
        "r1bqk1nr/pp1pppbp/2n3p1/8/2PNP3/4B3/PP3PPP/RN1QKB1R b KQkq -": (
            "B38",
            "Sicilian Defense: Accelerated Dragon, Maróczy Bind Formation",
        ),
        "r1bqk2r/pp1pppbp/2n3p1/8/2PNP1n1/2N1B3/PP3PPP/R2QKB1R w KQkq -": (
            "B39",
            "Sicilian Defense: Accelerated Dragon, Maróczy Bind Formation, Breyer Variation",
        ),
        "r1bqkb1r/pp1p1ppp/2n1p3/2pnP3/3P4/2P2N2/PP3PPP/RNBQKB1R w KQkq -": (
            "B40",
            "Sicilian Defense: Alapin Variation, Sherzer Variation",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/2p5/4P3/2P2N2/PP1P1PPP/RNBQKB1R b KQkq -": (
            "B40",
            "Sicilian Defense: Delayed Alapin Variation",
        ),
        "r1bqkb1r/pp1p1ppp/2N1pn2/8/4P3/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "B40",
            "Sicilian Defense: Four Knights Variation, Exchange Variation",
        ),
        "r1bqkb1r/pp1p1ppp/2n1pn2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B40",
            "Sicilian Defense: Four Knights Variation",
        ),
        "rnbqkb1r/pp1p1ppp/4pn2/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B40",
            "Sicilian Defense: French Variation, Normal Variation",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B40",
            "Sicilian Defense: French Variation, Open Variation",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B40",
            "Sicilian Defense: French Variation",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/2p5/4P3/1P3N2/P1PP1PPP/RNBQKB1R b KQkq -": (
            "B40",
            "Sicilian Defense: French Variation, Westerinen Attack",
        ),
        "rnb1kb1r/pp1p1ppp/1q2pn2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B40",
            "Sicilian Defense: Gaw-Paw Variation",
        ),
        "rnbqkbnr/3p1ppp/p3p3/1p6/3NP3/2N3P1/PPP2P1P/R1BQKB1R b KQkq -": (
            "B40",
            "Sicilian Defense: Kan Variation, Wing Attack, Fianchetto Variation",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/2p5/2P1P3/5N2/PP1P1PPP/RNBQKB1R b KQkq -": (
            "B40",
            "Sicilian Defense: Kramnik Variation",
        ),
        "rnb1kbnr/pp1p1ppp/1q2p3/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B40",
            "Sicilian Defense: Kveinis Variation",
        ),
        "rnbqkbnr/pp3ppp/4p3/2pp4/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B40",
            "Sicilian Defense: Marshall Counterattack",
        ),
        "rnbqk1nr/pp1p1ppp/4p3/2b5/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B40",
            "Sicilian Defense: Paulsen-Basman Defense",
        ),
        "rnbqk2r/pp1p1ppp/5n2/4p3/1b1NP3/2NB4/PPP2PPP/R1BQK2R w KQkq -": (
            "B40",
            "Sicilian Defense: Pin Variation, Jaffe Variation",
        ),
        "rnbqk2r/pp1p1ppp/4pn2/4P3/1b1N4/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "B40",
            "Sicilian Defense: Pin Variation, Koch Variation",
        ),
        "rnbqk2r/pp1p1ppp/4pn2/8/1b1NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B40",
            "Sicilian Defense: Pin Variation",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/8/3pP3/2P2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "B40",
            "Sicilian Defense: Deferred Smith-Morra Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/2p5/1P2P3/5N2/P1PP1PPP/RNBQKB1R b KQkq -": (
            "B40",
            "Sicilian Defense: Deferred Wing Gambit",
        ),
        "r1bqk2r/1p1p1ppp/p1n1pn2/8/1bPNP3/2N5/PPB2PPP/R1BQK2R b KQkq -": (
            "B41",
            "Sicilian Defense: Kan Variation, Maróczy Bind Formation, Bronstein Variation",
        ),
        "r1bqk2r/1p1p1ppp/p1n1pn2/8/1bPNP3/2NB4/PP3PPP/R1BQK2R w KQkq -": (
            "B41",
            "Sicilian Defense: Kan Variation, Maróczy Bind Formation, Bronstein Variation",
        ),
        "rnbqkbnr/1p1p1p1p/p3p1p1/8/2PNP3/8/PP3PPP/RNBQKB1R w KQkq -": (
            "B41",
            "Sicilian Defense: Kan Variation, Maróczy Bind Formation, Hedgehog Variation",
        ),
        "rnbqkbnr/1p1p1ppp/p3p3/8/2PNP3/8/PP3PPP/RNBQKB1R b KQkq -": (
            "B41",
            "Sicilian Defense: Kan Variation, Maróczy Bind Formation, Réti Variation",
        ),
        "rnbqkbnr/1p1p1ppp/p3p3/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B41",
            "Sicilian Defense: Kan Variation",
        ),
        "rnbqkb1r/1p3p1p/p2ppnp1/8/2PNP3/3B4/PP3PPP/RNBQ1RK1 w kq -": (
            "B42",
            "Sicilian Defense: Kan Variation, Gipslis Variation",
        ),
        "rnbqkbnr/1p1p1ppp/p3p3/8/3NP3/3B4/PPP2PPP/RNBQK2R b KQkq -": (
            "B42",
            "Sicilian Defense: Kan Variation, Modern Variation",
        ),
        "rnbqk1nr/1p1p1ppp/p3p3/2b5/3NP3/3B4/PPP2PPP/RNBQK2R w KQkq -": (
            "B42",
            "Sicilian Defense: Kan Variation, Polugaevsky Variation",
        ),
        "rnbqkbnr/1p1p1p1p/p3p1p1/8/3NP3/3B4/PPP2PPP/RNBQK2R w KQkq -": (
            "B42",
            "Sicilian Defense: Kan Variation, Swiss Cheese Variation",
        ),
        "rnbqkbnr/1p1p1ppp/p3p3/8/3NP3/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "B43",
            "Sicilian Defense: Kan Variation, Knight Variation",
        ),
        "rnb1k1nr/3p1ppp/pq2p3/1pb5/3NP1Q1/2NBB3/PPP2PPP/R3K2R b KQkq -": (
            "B43",
            "Sicilian Defense: Kan Variation, Wing Attack, Christiansen's Dream",
        ),
        "rnbqkbnr/3p1ppp/p3p3/1p6/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B43",
            "Sicilian Defense: Kan Variation, Wing Attack",
        ),
        "rnb1kbnr/3p1ppp/pq2p3/1p6/4P3/2NB1N2/PPP2PPP/R1BQK2R b KQkq -": (
            "B43",
            "Sicilian Defense: Kan Variation, Wing Attack, Spraggett Attack",
        ),
        "r1bqkb1r/1p3ppp/p1n1pn2/3p4/2P1P3/N1N5/PP3PPP/R1BQKB1R w KQkq -": (
            "B44",
            "Sicilian Defense: Paulsen Variation, Gary Gambit",
        ),
        "r1bq1rk1/4bppp/ppnppn2/8/2P1P3/N1N5/PP2BPPP/R1BQ1RK1 w - -": (
            "B44",
            "Sicilian Defense: Paulsen Variation, Modern Line",
        ),
        "r1bqkbnr/pp1p1ppp/2n1p3/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B44",
            "Sicilian Defense: Paulsen Variation",
        ),
        "r1bqkbnr/pp1p1ppp/2n1p3/1N6/4P3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "B44",
            "Sicilian Defense: Paulsen Variation, Szén Variation",
        ),
        "r1bqk2r/pp1p1ppp/2nNpn2/8/1b2P3/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "B45",
            "Sicilian Defense: Paulsen Variation, American Attack",
        ),
        "r1bqkbnr/pp1p1ppp/2n1p3/8/3NP3/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "B45",
            "Sicilian Defense: Paulsen Variation, Normal Variation",
        ),
        "r1bqkbnr/1p1p1ppp/p1n1p3/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B46",
            "Sicilian Defense: Paulsen Variation",
        ),
        "r1bqkb1r/1p1pnppp/p1n1p3/8/3NP3/2N5/PPP1BPPP/R1BQK2R w KQkq -": (
            "B46",
            "Sicilian Defense: Paulsen Variation, Taimanov Variation",
        ),
        "rqb1kbnr/1p1p1ppp/pBn1p3/1N6/4P3/2N5/PPP2PPP/R2QKB1R b KQkq -": (
            "B47",
            "Sicilian Defense: Paulsen Variation, Bastrikov Variation, Ponomariov Gambit",
        ),
        "r1b1kbnr/ppqp1ppp/2n1p3/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B47",
            "Sicilian Defense: Paulsen Variation, Bastrikov Variation",
        ),
        "r1b1kbnr/1pqp1ppp/p1n1p3/8/3NP3/2N1B3/PPPQ1PPP/R3KB1R b KQkq -": (
            "B48",
            "Sicilian Defense: Paulsen Variation, Bastrikov Variation, English Attack",
        ),
        "r1b1kbnr/1pqp1ppp/p1n1p3/8/3NP3/2N1BP2/PPP3PP/R2QKB1R b KQkq -": (
            "B48",
            "Sicilian Defense: Paulsen Variation, Bastrikov Variation, English Attack",
        ),
        "r1b1kbnr/ppqp1ppp/2n1p3/8/3NP3/2N1B3/PPP2PPP/R2QKB1R b KQkq -": (
            "B48",
            "Sicilian Defense: Paulsen Variation, Bastrikov Variation",
        ),
        "r1b1kbnr/1pqp1ppp/p1n1p3/8/3NP3/2N1B3/PPP1BPPP/R2QK2R b KQkq -": (
            "B49",
            "Sicilian Defense: Paulsen Variation, Bastrikov Variation",
        ),
        "r1b1kb1r/pp2pppp/2np4/q2P4/8/2P2N2/P3BPPP/R1BQK2R b KQkq -": (
            "B50",
            "Sicilian Defense: Delayed Alapin Variation, Basman-Palatnik Double Gambit",
        ),
        "r1bqkb1r/pp2pppp/2np4/8/3Pn3/5N2/PP2BPPP/RNBQK2R w KQkq -": (
            "B50",
            "Sicilian Defense: Delayed Alapin Variation, Basman-Palatnik Gambit",
        ),
        "rnbqkbnr/pp2pppp/3p4/2p5/4P3/2P2N2/PP1P1PPP/RNBQKB1R b KQkq -": (
            "B50",
            "Sicilian Defense: Delayed Alapin Variation",
        ),
        "rnbqkbnr/p3pppp/3p4/1pp5/4P3/5NP1/PPPP1P1P/RNBQKB1R w KQkq -": (
            "B50",
            "Sicilian Defense: Kotov Gambit",
        ),
        "rnbqkb1r/pp2pppp/3p4/2P5/4n3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B50",
            "Sicilian Defense: Modern Variations, Anti-Qxd4 Move Order Accepted",
        ),
        "rnbqkb1r/pp2pppp/3p1n2/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B50",
            "Sicilian Defense: Modern Variations, Anti-Qxd4 Move Order",
        ),
        "rnbqkbnr/pp2pppp/3p4/8/3pP3/2P2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "B50",
            "Sicilian Defense: Modern Variations, Tartakower Variation",
        ),
        "rnbqkbnr/pp2pppp/3p4/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "B50",
            "Sicilian Defense",
        ),
        "rnbqkbnr/pp2pppp/3p4/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "B50",
            "Sicilian Defense",
        ),
        "rnbqkbnr/pp2pppp/3p4/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "B50",
            "Sicilian Defense",
        ),
        "rnbqkbnr/pp2pppp/3p4/2p5/1P2P3/5N2/P1PP1PPP/RNBQKB1R b KQkq -": (
            "B50",
            "Sicilian Defense: Wing Gambit, Deferred Variation",
        ),
        "r2qkbnr/pp1bpp1p/2np2p1/1Bp1P3/8/5N2/PPPPQPPP/RNB2RK1 b kq -": (
            "B51",
            "Sicilian Defense: Canal Attack, Dorfman Gambit",
        ),
        "r2qkb1r/1p2pppp/p2p1n2/2p3B1/3Pb3/2P2N2/PP3PPP/RN1QR1K1 b kq -": (
            "B51",
            "Sicilian Defense: Canal Attack, Moscow Gambit",
        ),
        "rnbqkbnr/pp2pppp/3p4/1Bp5/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "B51",
            "Sicilian Defense: Moscow Variation",
        ),
        "r3kb1r/pp1qpppp/2np1n2/2p5/3PP3/2P2N2/PP3PPP/RNBQ1RK1 b kq -": (
            "B52",
            "Sicilian Defense: Canal Attack, Haag Gambit",
        ),
        "rn1qkbnr/pp1bpppp/3p4/1Bp5/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "B52",
            "Sicilian Defense: Canal Attack, Main Line",
        ),
        "rn2kbnr/pp1qpppp/3p4/2p5/2P1P3/5N2/PP1P1PPP/RNBQK2R b KQkq -": (
            "B52",
            "Sicilian Defense: Moscow Variation, Sokolsky Variation",
        ),
        "rnbqkbnr/pp2pppp/3p4/8/3QP3/5N2/PPP2PPP/RNB1KB1R b KQkq -": (
            "B53",
            "Sicilian Defense: Chekhover Variation",
        ),
        "r1b1kbnr/pp1qpppp/2np4/1B6/3QP3/5N2/PPP2PPP/RNB1K2R w KQkq -": (
            "B53",
            "Sicilian Defense: Chekhover Variation, Zaitsev Defense",
        ),
        "rnbqkbnr/pp2pp1p/3p2p1/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B54",
            "Sicilian Defense: Accelerated Dragon",
        ),
        "rnbqkb1r/pp2pppp/3p1n2/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "B54",
            "Sicilian Defense: Modern Variations, Main Line",
        ),
        "rnbqkb1r/pp2pppp/3p1n2/8/3NP3/5P2/PPP3PP/RNBQKB1R b KQkq -": (
            "B54",
            "Sicilian Defense: Prins Variation",
        ),
        "rnbqkb1r/pp3ppp/3p1n2/1B2p3/3NP3/5P2/PPP3PP/RNBQK2R b KQkq -": (
            "B55",
            "Sicilian Defense: Prins Variation, Venice Attack",
        ),
        "r1bqkb1r/pp2pppp/2np1n2/8/3NP3/2N3P1/PPP2P1P/R1BQKB1R b KQkq -": (
            "B56",
            "Sicilian Defense: Classical Variation, Fianchetto Variation",
        ),
        "r1bqkb1r/pp2pppp/2np1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B56",
            "Sicilian Defense: Classical Variation",
        ),
        "rn1qkb1r/pp1bpppp/3p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B56",
            "Sicilian Defense: Kupreichik Variation",
        ),
        "rnbqkb1r/pp2pppp/3p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "B56",
            "Sicilian Defense: Modern Variations",
        ),
        "r1bqkb1r/pp2pppp/2np1n2/8/4P3/2N5/PPP1NPPP/R1BQKB1R b KQkq -": (
            "B56",
            "Sicilian Defense: Spielmann Variation",
        ),
        "rnbqkb1r/pp3ppp/3p1n2/1B2p3/3NP3/2N5/PPP2PPP/R1BQK2R b KQkq -": (
            "B56",
            "Sicilian Defense: Venice Attack",
        ),
        "r1bqkb1r/pp2pppp/2np1n2/8/3NP3/2NB4/PPP2PPP/R1BQK2R b KQkq -": (
            "B56",
            "Sicilian Defense: Yates Variation",
        ),
        "r1b1kb1r/pp2pppp/1qnp1n2/8/2BNP3/2N5/PPP2PPP/R1BQK2R w KQkq -": (
            "B57",
            "Sicilian Defense: Classical Variation, Anti-Sozin Variation",
        ),
        "r1bqkb1r/pp2pppp/2np1n2/8/2BNP3/2N5/PPP2PPP/R1BQK2R b KQkq -": (
            "B57",
            "Sicilian Defense: Classical Variation, Sozin Attack",
        ),
        "r1bqkb1r/p3pp1p/2pp1np1/4P3/2B5/2N5/PPP2PPP/R1BQK2R b KQkq -": (
            "B57",
            "Sicilian Defense: Magnus Smith Trap",
        ),
        "r1bqkb1r/pp3ppp/2Np1n2/4p3/4P3/2N5/PPP1BPPP/R1BQK2R b KQkq -": (
            "B58",
            "Sicilian Defense: Boleslavsky Variation, Louma Variation",
        ),
        "r1bqkb1r/pp3ppp/2np1n2/4p3/3NP3/2N5/PPP1BPPP/R1BQK2R w KQkq -": (
            "B58",
            "Sicilian Defense: Boleslavsky Variation",
        ),
        "r1bqkb1r/pp2pp1p/3p1np1/8/3QP3/2N5/PPP1BPPP/R1B1K2R w KQkq -": (
            "B58",
            "Sicilian Defense: Classical Variation, Dragon Transfer Variation",
        ),
        "r1bqkb1r/pp2pppp/2np1n2/8/3NP3/2N5/PPP1BPPP/R1BQK2R b KQkq -": (
            "B58",
            "Sicilian Defense: Classical Variation",
        ),
        "r1bqkb1r/pp3ppp/2np1n2/4p3/4P3/1NN5/PPP1BPPP/R1BQK2R b KQkq -": (
            "B59",
            "Sicilian Defense: Boleslavsky Variation",
        ),
        "r1bqkb1r/pp2pp1p/2np1np1/6B1/3NP3/2N5/PPP2PPP/R2QKB1R w KQkq -": (
            "B60",
            "Sicilian Defense: Richter-Rauzer Variation, Dragon Variation",
        ),
        "r2qkb1r/pp1bpppp/2np1n2/6B1/3NP3/2N5/PPP2PPP/R2QKB1R w KQkq -": (
            "B60",
            "Sicilian Defense: Richter-Rauzer Variation, Modern Variation",
        ),
        "r1bqkb1r/pp2pppp/2np1n2/6B1/3NP3/2N5/PPP2PPP/R2QKB1R b KQkq -": (
            "B60",
            "Sicilian Defense: Richter-Rauzer Variation",
        ),
        "r2qkb1r/pp1bpppp/2np1n2/6B1/3NP3/2N5/PPPQ1PPP/R3KB1R b KQkq -": (
            "B61",
            "Sicilian Defense: Richter-Rauzer Variation, Modern Variation",
        ),
        "r1bqkb1r/pp3ppp/2nppn2/6B1/3NP3/2NQ4/PPP2PPP/R3KB1R b KQkq -": (
            "B62",
            "Sicilian Defense: Richter-Rauzer Variation",
        ),
        "r1bqkb1r/pp3ppp/2Nppn2/6B1/4P3/2N5/PPP2PPP/R2QKB1R b KQkq -": (
            "B62",
            "Sicilian Defense: Richter-Rauzer Variation, Exchange Variation",
        ),
        "r1bqkb1r/pp3ppp/2nppn2/6B1/4P3/1NN5/PPP2PPP/R2QKB1R b KQkq -": (
            "B62",
            "Sicilian Defense: Richter-Rauzer Variation, Podebrady Variation",
        ),
        "r1bqkb1r/pp3ppp/2nppn2/6B1/3NP3/2N5/PPP2PPP/R2QKB1R w KQkq -": (
            "B62",
            "Sicilian Defense: Richter-Rauzer Variation",
        ),
        "r1bqkb1r/pp3ppp/2nppn2/1B4B1/3NP3/2N5/PPP2PPP/R2QK2R b KQkq -": (
            "B62",
            "Sicilian Defense: Richter-Rauzer Variation, Vitolins Variation",
        ),
        "r1bqk2r/4bppp/p2ppn2/1p4B1/3QPP2/2N5/PPP3PP/2KR1B1R w kq -": (
            "B63",
            "Sicilian Defense: Richter-Rauzer Variation, Classical Variation, Kantscher Line",
        ),
        "r1bqk2r/pp2bppp/2nppn2/6B1/3NP3/2N5/PPPQ1PPP/R3KB1R w KQkq -": (
            "B63",
            "Sicilian Defense: Richter-Rauzer Variation, Classical Variation",
        ),
        "r1b1kb1r/pp3ppp/1qnppn2/6B1/3NP3/2N5/PPPQ1PPP/R3KB1R w KQkq -": (
            "B63",
            "Sicilian Defense: Richter-Rauzer Variation, Ivanov Variation",
        ),
        "r1bqkb1r/pp3ppp/2nppn2/6B1/3NP3/2N5/PPPQ1PPP/R3KB1R b KQkq -": (
            "B63",
            "Sicilian Defense: Richter-Rauzer Variation, Traditional Variation",
        ),
        "r1bq1rk1/pp2bppp/2np1n2/4p1B1/3NPP2/2N5/PPPQ2PP/2KR1B1R w - -": (
            "B64",
            "Sicilian Defense: Richter-Rauzer Variation, Classical Variation",
        ),
        "r1bq1rk1/pp2bppp/2nppn2/6B1/3NPP2/2N5/PPPQ2PP/2KR1B1R b - -": (
            "B64",
            "Sicilian Defense: Richter-Rauzer Variation, Classical Variation",
        ),
        "r1bq1rk1/pp2bppp/3ppn2/6B1/3nPP2/2N5/PPPQ2PP/2KR1B1R w - -": (
            "B65",
            "Sicilian Defense: Richter-Rauzer Variation, Rauzer Attack",
        ),
        "r1bq1rk1/pp2bppp/3ppn2/6B1/3QPP2/2N5/PPP3PP/2KR1B1R b - -": (
            "B65",
            "Sicilian Defense: Richter-Rauzer Variation, Classical Variation",
        ),
        "r1bqkb1r/1p3ppp/p1nppn2/6B1/3NP3/2N5/PPPQ1PPP/R3KB1R w KQkq -": (
            "B66",
            "Sicilian Defense: Richter-Rauzer Variation, Neo-Modern Variation, Early Deviations",
        ),
        "r2qkb1r/1p1b1ppp/p1nppn2/6B1/3NP3/2N5/PPPQ1PPP/2KR1B1R w kq -": (
            "B67",
            "Sicilian Defense: Richter-Rauzer Variation, Neo-Modern Variation",
        ),
        "r2qk2r/1p1bbppp/p1nppn2/6B1/3NPP2/2N5/PPPQ2PP/2KR1B1R w kq -": (
            "B68",
            "Sicilian Defense: Richter-Rauzer Variation, Neo-Modern Variation",
        ),
        "r2qk2r/3bbppp/p1nppB2/1p6/4PP2/2N2N2/PPPQ2PP/2KR1B1R b kq -": (
            "B69",
            "Sicilian Defense: Richter-Rauzer Variation, Neo-Modern Variation, Nezhmetdinov Attack",
        ),
        "rnbqkb1r/pp2pp1p/3p1np1/8/3NP3/2N5/PPP1BPPP/R1BQK2R b KQkq -": (
            "B70",
            "Sicilian Defense: Dragon Variation, Classical Variation",
        ),
        "rnbqkb1r/pp2pp1p/3p1np1/8/3NP3/2N3P1/PPP2P1P/R1BQKB1R b KQkq -": (
            "B70",
            "Sicilian Defense: Dragon Variation, Fianchetto Variation",
        ),
        "rnbqkb1r/pp2pp1p/3p1np1/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B70",
            "Sicilian Defense: Dragon Variation",
        ),
        "r1bqkb1r/pp1npp1p/3p1np1/8/3NPP2/2N5/PPP3PP/R1BQKB1R w KQkq -": (
            "B71",
            "Sicilian Defense: Dragon Variation, Levenfish Variation, Main Line",
        ),
        "rnbqkb1r/pp2pp1p/3p1np1/8/3NPP2/2N5/PPP3PP/R1BQKB1R b KQkq -": (
            "B71",
            "Sicilian Defense: Dragon Variation, Levenfish Variation",
        ),
        "r1bqk2r/pp2ppbp/2np1np1/8/3NP3/2N1B3/PPPQBPPP/R3K2R b KQkq -": (
            "B72",
            "Sicilian Defense: Dragon Variation, Classical Variation, Amsterdam Variation",
        ),
        "rnbqk2r/pp2ppbp/3p1np1/8/3NP3/2N1B3/PPP1BPPP/R2QK2R b KQkq -": (
            "B72",
            "Sicilian Defense: Dragon Variation, Classical Variation",
        ),
        "r1bq1rk1/pp2ppbp/2np1np1/8/3NP3/2N1B3/PPPQBPPP/2KR3R b - -": (
            "B72",
            "Sicilian Defense: Dragon Variation, Classical Variation, Grigoriev Variation",
        ),
        "rnbqkb1r/pp2pp1p/3p1np1/8/3NP3/2N1B3/PPP2PPP/R2QKB1R b KQkq -": (
            "B72",
            "Sicilian Defense: Dragon Variation",
        ),
        "r1bqk2r/pp2ppbp/2np1np1/8/3NP3/2N1B3/PPP1BPPP/R2QK2R w KQkq -": (
            "B72",
            "Sicilian Defense: Dragon Variation, Classical Variation",
        ),
        "r1bqk2r/pp2ppbp/2np1np1/8/4P3/1NN1B3/PPP1BPPP/R2QK2R b KQkq -": (
            "B72",
            "Sicilian Defense: Dragon Variation, Classical Variation",
        ),
        "r1b2rk1/pp2ppbp/1qnp1np1/4P3/3N1P2/2N1B3/PPP1B1PP/R2Q1RK1 b - -": (
            "B73",
            "Sicilian Defense: Dragon Variation, Classical Variation, Zollner Gambit",
        ),
        "r1bq1rk1/pp2ppbp/2np1np1/8/3NP3/2N1B3/PPPQBPPP/R4RK1 b - -": (
            "B73",
            "Sicilian Defense: Dragon Variation, Classical Variation, Battery Variation",
        ),
        "r1bqk2r/pp2ppbp/2np1np1/8/3NP3/2N1B3/PPP1BPPP/R2Q1RK1 b kq -": (
            "B73",
            "Sicilian Defense: Dragon Variation, Classical Variation",
        ),
        "r2q1rk1/pp2ppbp/5np1/n2p1P2/4P3/1NNPB3/PP4PP/R2Q1RK1 w - -": (
            "B74",
            "Sicilian Defense: Dragon Variation, Classical Variation, Bernard Defense",
        ),
        "r2q1rk1/pp2ppbp/3p1np1/n4P2/2b1P3/1NNBB3/PPP3PP/R2Q1RK1 b - -": (
            "B74",
            "Sicilian Defense: Dragon Variation, Classical Variation, Spielmann Variation",
        ),
        "r1bq1rk1/1p2ppbp/2np1np1/p7/4P3/1NN1B3/PPP1BPPP/R2Q1RK1 w - -": (
            "B74",
            "Sicilian Defense: Dragon Variation, Classical Variation, Alekhine Line",
        ),
        "r2q1rk1/pp2ppbp/3pbnp1/n7/4PP2/1NN1B3/PPP1B1PP/R2Q1RK1 w - -": (
            "B74",
            "Sicilian Defense: Dragon Variation, Classical Variation, Maróczy Line",
        ),
        "r1bq1rk1/pp2ppbp/2np1np1/8/4P3/1NN1B3/PPP1BPPP/R2Q1RK1 b - -": (
            "B74",
            "Sicilian Defense: Dragon Variation, Classical Variation, Normal Line",
        ),
        "r4rk1/pp2ppbp/3p1np1/q4P2/4P1P1/2N1B3/PPP1Q2P/R4RK1 b - -": (
            "B74",
            "Sicilian Defense: Dragon Variation, Classical Variation, Stockholm Attack",
        ),
        "r1q2rk1/pp2ppbp/2npbnp1/8/4PP2/1NN1B3/PPP1B1PP/R2Q1RK1 w - -": (
            "B74",
            "Sicilian Defense: Dragon Variation, Classical Variation, Tartakower Line",
        ),
        "r1bqk2r/pp2ppbp/2np1np1/8/3NP3/2N1BP2/PPP3PP/R2QKB1R w KQkq -": (
            "B75",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack, Belezky Line",
        ),
        "rnbqk2r/pp2ppbp/3p1np1/8/3NP3/2N1BP2/PPP3PP/R2QKB1R b KQkq -": (
            "B75",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack, Early Deviations",
        ),
        "r1bq1rk1/pp2ppbp/2np1np1/8/3NP3/2N1BP2/PPPQ2PP/2KR1B1R b - -": (
            "B76",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack, Modern Line",
        ),
        "r1bq1rk1/pp2ppbp/2np1np1/8/3NP1P1/2N1BP2/PPPQ3P/R3KB1R b KQ -": (
            "B76",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack, Panov Variation",
        ),
        "r1bq1rk1/pp2ppbp/2np1np1/8/3NP3/2N1BP2/PPPQ2PP/R3KB1R w KQ -": (
            "B76",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack",
        ),
        "rnbq1rk1/pp2ppbp/3p1np1/8/3NP3/2N1BP2/PPP3PP/R2QKB1R w KQ -": (
            "B76",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack",
        ),
        "r2q1rk1/pp2ppbp/3pbnp1/8/2BBP3/2N2P2/PPPQ2PP/R3K2R w KQ -": (
            "B77",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack, Czerniak Variation",
        ),
        "r1bq1rk1/pp2ppbp/2np1np1/8/2BNP3/2N1BP2/PPPQ2PP/R3K2R b KQ -": (
            "B77",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack, Main Line",
        ),
        "r2q1rk1/pp1bppbp/2np1np1/8/2BNP3/2N1BP2/PPPQ2PP/R3K2R w KQ -": (
            "B77",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack",
        ),
        "r1bq1rk1/pp1nppbp/2np2p1/8/2BNP3/2N1BP2/PPPQ2PP/R3K2R w KQ -": (
            "B77",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack, Sosonko Variation",
        ),
        "r1bq1rk1/1p2ppbp/2np1np1/p7/2BNP3/2N1BP2/PPPQ2PP/R3K2R w KQ -": (
            "B77",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack, Byrne Variation",
        ),
        "2rq1rk1/pp1bppbp/2np1np1/8/2BNP3/2N1BP2/PPPQ2PP/2KR3R w - -": (
            "B78",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack, Old Line",
        ),
        "r2q1rk1/pp1bppbp/2np1np1/8/2BNP3/2N1BP2/PPPQ2PP/2KR3R b - -": (
            "B78",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack",
        ),
        "r1r3k1/pp1bppb1/2np1np1/q6p/3NP2P/1BN1BP2/PPPQ2P1/2KR3R w - -": (
            "B79",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack, Soltis Variation",
        ),
        "r1r3k1/pp1bppbp/2np1np1/q7/3NP2P/1BN1BP2/PPPQ2P1/2KR3R b - -": (
            "B79",
            "Sicilian Defense: Dragon Variation, Yugoslav Attack",
        ),
        "rnbqkb1r/1p3ppp/p2ppn2/8/3NP3/2N1B3/PPPQ1PPP/R3KB1R b KQkq -": (
            "B80",
            "Sicilian Defense: Scheveningen Variation, English Attack",
        ),
        "rnbqkb1r/pp3ppp/3ppn2/8/3NP3/2N3P1/PPP2P1P/R1BQKB1R b KQkq -": (
            "B80",
            "Sicilian Defense: Scheveningen Variation, Fianchetto Variation",
        ),
        "rnbqkb1r/pp3ppp/3ppn2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B80",
            "Sicilian Defense: Scheveningen Variation",
        ),
        "rnbqkb1r/pp3ppp/3ppn2/1B6/3NP3/2N5/PPP2PPP/R1BQK2R b KQkq -": (
            "B80",
            "Sicilian Defense: Scheveningen Variation, Vitolins Variation",
        ),
        "rnbqkb1r/pp3ppp/3ppn2/8/3NP1P1/2N5/PPP2P1P/R1BQKB1R b KQkq -": (
            "B81",
            "Sicilian Defense: Scheveningen Variation, Keres Attack",
        ),
        "rnbqkb1r/pp3ppp/3ppn2/8/3NPP2/2N5/PPP3PP/R1BQKB1R b KQkq -": (
            "B82",
            "Sicilian Defense: Scheveningen Variation, Matanović Attack",
        ),
        "r1bqk2r/pp2bppp/2nppn2/8/3NPP2/2N1BQ2/PPP3PP/R3KB1R b KQkq -": (
            "B82",
            "Sicilian Defense: Scheveningen Variation, Tal Variation",
        ),
        "rnbqkb1r/pp3ppp/3ppn2/8/3NP3/2N5/PPP1BPPP/R1BQK2R b KQkq -": (
            "B83",
            "Sicilian Defense: Scheveningen Variation, Classical Variation",
        ),
        "r1bq1rk1/pp2bppp/2nppn2/8/3NPP2/2N1B3/PPP1B1PP/R2Q1RK1 b - -": (
            "B83",
            "Sicilian Defense: Scheveningen Variation, Modern Variation",
        ),
        "r1bqkb1r/pp3ppp/2nppn2/8/3NP3/2N5/PPP1BPPP/R1BQK2R w KQkq -": (
            "B83",
            "Sicilian Defense: Scheveningen Variation, Modern Variation",
        ),
        "r2q1rk1/pp1bbppp/2nppn2/8/4PP2/1NN1B3/PPP1B1PP/R2Q1RK1 b - -": (
            "B83",
            "Sicilian Defense: Scheveningen Variation, Modern Variation",
        ),
        "r1bqkb1r/1p1n1ppp/p2ppn2/8/3NP3/2N5/PPP1BPPP/R1BQ1RK1 w kq -": (
            "B84",
            "Sicilian Defense: Najdorf Variation, Scheveningen Variation",
        ),
        "rnb1kb1r/1pq2ppp/p2ppn2/8/3NP3/2N5/PPP1BPPP/R1BQ1RK1 w kq -": (
            "B84",
            "Sicilian Defense: Scheveningen Variation, Classical Variation",
        ),
        "rnbqkb1r/1p3ppp/p2ppn2/8/3NP3/2N5/PPP1BPPP/R1BQK2R w KQkq -": (
            "B84",
            "Sicilian Defense: Scheveningen Variation, Classical Variation",
        ),
        "r1b2rk1/1pq1bppp/p1nppn2/8/3NPP2/2N1B3/PPP1B1PP/R3QRK1 w - -": (
            "B85",
            "Sicilian Defense: Scheveningen Variation, Classical Main Line",
        ),
        "r1b1k2r/1pq1bppp/p1nppn2/8/P2NPP2/2N5/1PP1B1PP/R1BQ1R1K b kq -": (
            "B85",
            "Sicilian Defense: Scheveningen Variation, Classical Variation, Paulsen Variation",
        ),
        "r1b1kb1r/1pq2ppp/p1nppn2/8/3NPP2/2N1B3/PPP1B1PP/R2Q1RK1 b kq -": (
            "B85",
            "Sicilian Defense: Scheveningen Variation, Classical Variation, Paulsen Variation",
        ),
        "r1b1kb1r/1pq2ppp/p1nppn2/8/3NPP2/2N5/PPP1B1PP/R1BQ1RK1 w kq -": (
            "B85",
            "Sicilian Defense: Scheveningen Variation, Classical Variation, Paulsen Variation",
        ),
        "rnbqkb1r/pp3ppp/3ppn2/8/2BNP3/2N5/PPP2PPP/R1BQK2R b KQkq -": (
            "B86",
            "Sicilian Defense: Sozin Attack",
        ),
        "rnbqkb1r/5ppp/p2ppn2/1p6/3NP3/1BN5/PPP2PPP/R1BQK2R w KQkq -": (
            "B87",
            "Sicilian Defense: Sozin Attack, Flank Variation",
        ),
        "r1bqkb1r/pp3ppp/2nppn2/8/2BNP3/2N5/PPP2PPP/R1BQK2R w KQkq -": (
            "B88",
            "Sicilian Defense: Sozin Attack, Leonhardt Variation",
        ),
        "r1bq1rk1/pp2bppp/2nppn2/8/3NPP2/1BN1B3/PPP3PP/R2QK2R b KQ -": (
            "B88",
            "Sicilian Defense: Sozin Attack, Fischer Variation",
        ),
        "r1bqkb1r/pp3ppp/2nppn2/8/2BNP3/2N1B3/PPP2PPP/R2QK2R b KQkq -": (
            "B89",
            "Sicilian Defense: Sozin Attack, Main Line",
        ),
        "r1bq1rk1/p3bppp/1p1ppn2/n7/3NPP2/1BN1B3/PPP3PP/R2Q1RK1 w - -": (
            "B89",
            "Sicilian Defense: Sozin Attack, Main Line, Sherbakov Variation",
        ),
        "r1bqk2r/pp2bppp/2nppn2/8/2BNP3/2N1B3/PPP1QPPP/R3K2R b KQkq -": (
            "B89",
            "Sicilian Defense: Velimirović Attack",
        ),
        "rnbqkb1r/1p2pppp/p2p1n2/8/2BNP3/2N5/PPP2PPP/R1BQK2R b KQkq -": (
            "B90",
            "Sicilian Defense: Najdorf Variation, Lipnitsky Attack",
        ),
        "rnbqkb1r/1p2pppp/p2p1n2/8/3NP3/2N4P/PPP2PP1/R1BQKB1R b KQkq -": (
            "B90",
            "Sicilian Defense: Najdorf Variation, Adams Attack",
        ),
        "rnbqkb1r/1p2pppp/p2p1n2/8/3NP1P1/2N5/PPP2P1P/R1BQKB1R b KQkq -": (
            "B90",
            "Sicilian Defense: Najdorf Variation, Dekker Gambit",
        ),
        "rnbqkb1r/1p2pppp/p2p4/8/3NP1n1/2N1B3/PPP2PPP/R2QKB1R w KQkq -": (
            "B90",
            "Sicilian Defense: Najdorf Variation, English Attack, Anti-English Variation",
        ),
        "rnbqkb1r/1p2pppp/p2p1n2/8/3NP3/2N1B3/PPP2PPP/R2QKB1R b KQkq -": (
            "B90",
            "Sicilian Defense: Najdorf Variation, English Attack",
        ),
        "rnbqkb1r/1p2pppp/p2p1n2/8/3NP3/2N5/PPP2PPP/R1BQKBR1 b Qkq -": (
            "B90",
            "Sicilian Defense: Najdorf Variation, Freak Attack",
        ),
        "rnbqkb1r/1p2pppp/p2p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "B90",
            "Sicilian Defense: Najdorf Variation",
        ),
        "rnbqkb1r/1p3p1p/p2p1np1/4pNP1/4P3/2N1B3/PPP2P1P/R2QKB1R b KQkq -": (
            "B90",
            "Sicilian Defense: Scheveningen Variation, Delayed Keres Attack, Perenyi Gambit",
        ),
        "rnbqkb1r/1p3ppp/p2ppn2/8/3NP1P1/2N1B3/PPP2P1P/R2QKB1R b KQkq -": (
            "B90",
            "Sicilian Defense: Scheveningen Variation, Delayed Keres Attack",
        ),
        "rnbqkb1r/1p3ppp/p2ppn2/8/3NP3/2N1BP2/PPP3PP/R2QKB1R b KQkq -": (
            "B90",
            "Sicilian Defense: Scheveningen Variation, English Attack",
        ),
        "rnbqkb1r/1p2pppp/p2p1n2/8/3NP3/2N3P1/PPP2P1P/R1BQKB1R b KQkq -": (
            "B91",
            "Sicilian Defense: Najdorf Variation, Zagreb (Fianchetto) Variation",
        ),
        "rn1qk2r/1p2bppp/p2pbn2/4p3/4P3/1NN5/PPP1BPPP/R1BQ1RK1 w kq -": (
            "B92",
            "Sicilian Defense: Najdorf Variation, Opocensky Variation, Modern Line",
        ),
        "rnbqkb1r/1p2pppp/p2p1n2/8/3NP3/2N5/PPP1BPPP/R1BQK2R b KQkq -": (
            "B92",
            "Sicilian Defense: Najdorf Variation, Opocensky Variation",
        ),
        "rnbq1rk1/1p2bppp/p2p1n2/4p3/4P3/1NN5/PPP1BPPP/R1BQ1RK1 w - -": (
            "B92",
            "Sicilian Defense: Najdorf Variation, Opocensky Variation, Traditional Line",
        ),
        "rnbqkb1r/1p2pppp/p2p1n2/8/3NPP2/2N5/PPP3PP/R1BQKB1R b KQkq -": (
            "B93",
            "Sicilian Defense: Najdorf Variation, Amsterdam Variation",
        ),
        "r3kb1r/1b3ppp/p2ppn2/qpn1P1B1/3N4/1BN5/PPPQ1PPP/2KRR3 b kq -": (
            "B94",
            "Sicilian Defense: Najdorf Variation, Ivkov Variation",
        ),
        "rnbqkb1r/1p2pppp/p2p1n2/6B1/3NP3/2N5/PPP2PPP/R2QKB1R b KQkq -": (
            "B94",
            "Sicilian Defense: Najdorf Variation",
        ),
        "rnbqkb1r/1p3ppp/p2ppn2/6B1/3NP3/2N5/PPP2PPP/R2QKB1R w KQkq -": (
            "B95",
            "Sicilian Defense: Najdorf Variation",
        ),
        "r1bqkb1r/1p3ppp/p1nppn2/6B1/3NPP2/2N5/PPP3PP/R2QKB1R w KQkq -": (
            "B96",
            "Sicilian Defense: Najdorf Variation, Neo-Classical Defense",
        ),
        "rnbqkb1r/5ppp/p2ppn2/1p4B1/3NPP2/2N5/PPP3PP/R2QKB1R w KQkq -": (
            "B96",
            "Sicilian Defense: Najdorf Variation, Polugaevsky Variation",
        ),
        "rnb1kb1r/2q2ppp/p3pn2/1p2P1B1/3N4/2N5/PPP1Q1PP/R3KB1R b KQkq -": (
            "B96",
            "Sicilian Defense: Najdorf Variation, Polugaevsky Variation, Simagin Line",
        ),
        "rnbqkb1r/1p3ppp/p2ppn2/6B1/3NPP2/2N5/PPP3PP/R2QKB1R b KQkq -": (
            "B96",
            "Sicilian Defense: Najdorf Variation",
        ),
        "rnb1kb1r/1p3ppp/p2ppn2/6B1/3NPP2/q1N5/P1PQ2PP/1R2KB1R w Kkq -": (
            "B97",
            "Sicilian Defense: Najdorf Variation, Poisoned Pawn Accepted",
        ),
        "rnb1kb1r/1p3ppp/pq1ppn2/6B1/3NPP2/2N5/PPP3PP/R2QKB1R w KQkq -": (
            "B97",
            "Sicilian Defense: Najdorf Variation, Poisoned Pawn Variation",
        ),
        "rnb1k2r/1pq1bpp1/p2ppn1p/8/3NPP1B/2N2Q2/PPP3PP/R3KB1R w KQkq -": (
            "B98",
            "Sicilian Defense: Najdorf Variation, Browne Variation",
        ),
        "rnbqk2r/1p2bp2/p2ppn1p/6p1/3NPP1B/2N2Q2/PPP3PP/R3KB1R w KQkq -": (
            "B98",
            "Sicilian Defense: Najdorf Variation, Göteborg (Argentine) Variation",
        ),
        "rnbqk2r/1p2bppp/p2ppn2/6B1/3NPP2/2N5/PPP3PP/R2QKB1R w KQkq -": (
            "B98",
            "Sicilian Defense: Najdorf Variation",
        ),
        "rnb1k2r/1pq1bppp/p2ppn2/6B1/3NPP2/2N2Q2/PPP3PP/R3KB1R w KQkq -": (
            "B98",
            "Sicilian Defense: Najdorf Variation, Traditional Line",
        ),
        "r1b1k2r/1pqnbppp/p2ppn2/6B1/3NPP2/2N2Q2/PPP3PP/2KR1B1R w kq -": (
            "B99",
            "Sicilian Defense: Najdorf Variation, Main Line",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/4B3/PPP2PPP/RN1QKBNR b KQkq -": (
            "C00",
            "French Defense: Alapin Gambit",
        ),
        "rnbqkbnr/p1pp1ppp/4p3/1p6/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C00",
            "French Defense: Baeuerle Gambit",
        ),
        "rnbqk1nr/pppp1ppp/4p3/4P3/1b6/8/P1PP1PPP/RNBQKBNR b KQkq -": (
            "C00",
            "French Defense: Banzai-Leong Gambit, Pinova Gambit",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/1P2P3/8/P1PP1PPP/RNBQKBNR b KQkq -": (
            "C00",
            "French Defense: Banzai-Leong Gambit",
        ),
        "rnbqkbnr/pppp1ppp/4p3/1B6/4P3/8/PPPP1PPP/RNBQK1NR b KQkq -": (
            "C00",
            "French Defense: Bird Invitation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/4N3/3Pp3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C00",
            "French Defense: Carlson Gambit",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPPQPPP/RNB1KBNR b KQkq -": (
            "C00",
            "French Defense: Chigorin Variation",
        ),
        "rnbqkb1r/pppp2pp/4pn2/5P2/3P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C00",
            "French Defense: Franco-Hiva Gambit Accepted",
        ),
        "rnbqkbnr/pppp2pp/4p3/5p2/4P3/3P4/PPP2PPP/RNBQKBNR w KQkq -": (
            "C00",
            "French Defense: Franco-Hiva Gambit",
        ),
        "rnbqkbnr/pppp2pp/4p3/5p2/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C00",
            "French Defense: Franco-Hiva Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3p4/3PPp2/8/PPP1Q1PP/RNB1KBNR w KQkq -": (
            "C00",
            "French Defense: Hoffmann Gambit",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/4P3/1P6/PBPP1PPP/RN1QKBNR b KQkq -": (
            "C00",
            "French Defense: Horwitz Attack, Papa-Ticulat Gambit",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/4P3/1P6/P1PP1PPP/RNBQKBNR b KQkq -": (
            "C00",
            "French Defense: Horwitz Attack",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/4P3/3P4/PPP2PPP/RNBQKBNR b KQkq -": (
            "C00",
            "French Defense: King's Indian Attack",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C00",
            "French Defense: Knight's Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/8/4pP2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C00",
            "French Defense: La Bourdonnais Variation, Reuter Gambit",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/4PP2/8/PPPP2PP/RNBQKBNR b KQkq -": (
            "C00",
            "French Defense: La Bourdonnais Variation",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C00",
            "French Defense: Mediterranean Defense",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/7N/PPP2PPP/RNBQKB1R b KQkq -": (
            "C00",
            "French Defense: Morphy Gambit",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/3PP3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "C00",
            "French Defense: Normal Variation",
        ),
        "rnbqkbnr/ppp2ppp/8/3p4/4P3/1Q6/PP1P1PPP/RNB1KBNR b KQkq -": (
            "C00",
            "French Defense: Orthoschnapp Gambit",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/4PP2/2N5/PPPP2PP/R1BQKBNR b KQkq -": (
            "C00",
            "French Defense: Pelikan Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C00",
            "French Defense: Perseus Gambit",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq -": (
            "C00",
            "French Defense: Queen's Knight",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/4P3/6P1/PPPP1P1P/RNBQKBNR b KQkq -": (
            "C00",
            "French Defense: Réti-Spielmann Attack",
        ),
        "r1bqkb1r/ppp2ppp/2n1pn2/3p4/4P3/3P1N2/PPPNBPPP/R1BQK2R b KQkq -": (
            "C00",
            "French Defense: Reversed Philidor Formation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C00",
            "French Defense",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "C00",
            "French Defense",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/3B4/PPP2PPP/RNBQK1NR b KQkq -": (
            "C00",
            "French Defense: Schlechter Variation",
        ),
        "rnbqkbnr/pppp1ppp/4p3/8/2P1P3/8/PP1P1PPP/RNBQKBNR b KQkq -": (
            "C00",
            "French Defense: Steiner Variation",
        ),
        "rnbqkbnr/pppp1ppp/4p3/4P3/8/8/PPPP1PPP/RNBQKBNR b KQkq -": (
            "C00",
            "French Defense: Steinitz Attack",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/4P3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq -": (
            "C00",
            "French Defense: Two Knights Variation",
        ),
        "rnbqkbnr/pp3ppp/4p3/2ppP3/1P6/5N2/P1PP1PPP/RNBQKB1R b KQkq -": (
            "C00",
            "French Defense: Wing Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/4p3/2p5/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C00",
            "Queen's Pawn Game: Franco-Sicilian Defense",
        ),
        "rnbqkbnr/ppp2ppp/3pp3/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C00",
            "Rat Defense: Small Center Defense",
        ),
        "rnbqkbnr/1p1p1ppp/p3p3/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C00",
            "Sicilian Defense: Dražić Variation",
        ),
        "rnbqkbnr/2pp1ppp/p3p3/1p6/2PPP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "C00",
            "St. George Defense: Three Pawns Attack, Sanky-George Gambit",
        ),
        "rnbqkbnr/1ppp1ppp/p3p3/8/2PPP3/8/PP3PPP/RNBQKBNR b KQkq -": (
            "C00",
            "St. George Defense: Three Pawns Attack",
        ),
        "rn1qkb1r/1b1p1ppp/p3pn2/1pp5/3PP3/2PB1N2/PP3PPP/RNBQ1RK1 w kq -": (
            "C00",
            "St. George Defense: Traditional Line",
        ),
        "rnbqkbnr/1ppp1ppp/p3p3/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C00",
            "St. George Defense",
        ),
        "rnbqkbnr/2pp1ppp/4p3/1p6/3PP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "C00",
            "St. George Defense: St. George Gambit",
        ),
        "r1bqkb1r/ppp2ppp/2n2n2/3p2B1/3P4/2N5/PPP2PPP/R2QKBNR w KQkq -": (
            "C01",
            "French Defense: Exchange Variation, Bogoljubov Variation",
        ),
        "rnbqkbnr/ppp2ppp/8/3p4/2PP4/8/PP3PPP/RNBQKBNR b KQkq -": (
            "C01",
            "French Defense: Exchange Variation, Monte Carlo Variation",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3p2B1/3P4/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "C01",
            "French Defense: Exchange Variation, Svenonius Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3P4/3P4/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "C01",
            "French Defense: Exchange Variation",
        ),
        "r2qkbnr/pp1b1ppp/2n1p3/2ppP3/3P4/2P2N2/PP3PPP/RNBQKB1R w KQkq -": (
            "C02",
            "French Defense: Advance Variation, Euwe Variation",
        ),
        "rn1qkbnr/pppb1ppp/4p3/3pP3/3P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C02",
            "French Defense: Advance Variation, Extended Bishop Swap Variation",
        ),
        "rnbqkbnr/pp3ppp/4p3/2ppP3/1P1P4/8/P1P2PPP/RNBQKBNR b KQkq -": (
            "C02",
            "French Defense: Advance Variation, Frenkel Gambit",
        ),
        "r1b1kb1r/pp3ppp/1qn1p2n/2ppP3/3P4/P1P2N2/1P3PPP/RNBQKB1R w KQkq -": (
            "C02",
            "French Defense: Advance Variation, Lputian Variation",
        ),
        "r1b1kbnr/pp3ppp/1qn1p3/2ppP3/3P4/P1P2N2/1P3PPP/RNBQKB1R b KQkq -": (
            "C02",
            "French Defense: Advance Variation, Main Line",
        ),
        "r1b1kbnr/pp3ppp/1qn1p3/2ppP3/3P4/2PB1N2/PP3PPP/RNBQK2R b KQkq -": (
            "C02",
            "French Defense: Advance Variation, Milner-Barry Gambit",
        ),
        "rnbqkbnr/pp3ppp/4p3/2ppP3/3P2Q1/8/PPP2PPP/RNB1KBNR b KQkq -": (
            "C02",
            "French Defense: Advance Variation, Nimzowitsch Attack",
        ),
        "rnbqkbnr/pp3ppp/4p3/3pP3/3p2Q1/5N2/PPP2PPP/RNB1KB1R b KQkq -": (
            "C02",
            "French Defense: Advance Variation, Nimzowitsch Gambit",
        ),
        "rnbqkbnr/pp3ppp/4p3/2ppP3/3P4/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C02",
            "French Defense: Advance Variation, Nimzowitsch System",
        ),
        "r1bqkbnr/pp3ppp/2n1p3/2ppP3/3P4/2P2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "C02",
            "French Defense: Advance Variation, Paulsen Attack",
        ),
        "rnbqkbnr/pp3ppp/4p3/3pP3/3p4/3B1N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C02",
            "French Defense: Advance Variation, Ruisdonk Gambit",
        ),
        "rnbqkbnr/pp3ppp/4p3/2PpP3/8/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "C02",
            "French Defense: Advance Variation, Steinitz Variation",
        ),
        "rn2kbnr/pp1b1ppp/1q2p3/2ppP3/3P4/2P2N2/PP3PPP/RNBQKB1R w KQkq -": (
            "C02",
            "French Defense: Advance Variation, Wade Variation",
        ),
        "r1bqkbnr/pp3ppp/2n1p3/2ppP3/3P4/2P5/PP3PPP/RNBQKBNR w KQkq -": (
            "C02",
            "French Defense: Advance Variation",
        ),
        "rnbqkbnr/pp3ppp/4p3/2ppP3/3P4/2P5/PP3PPP/RNBQKBNR b KQkq -": (
            "C02",
            "French Defense: Advance Variation",
        ),
        "rnbqkbnr/pp3ppp/4p3/2ppP3/3P4/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C02",
            "French Defense: Advance Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3pP3/3P4/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "C02",
            "French Defense: Advance Variation",
        ),
        "r1bqkbnr/ppp2ppp/2n5/4p3/3PN3/2P5/PP3PPP/R1BQKBNR w KQkq -": (
            "C03",
            "French Defense: Guimard Variation, Thunderbunny Variation",
        ),
        "r1bqkbnr/ppp2ppp/2n1p3/3p4/3PP3/8/PPPN1PPP/R1BQKBNR w KQkq -": (
            "C03",
            "French Defense: Tarrasch Variation, Guimard Defense",
        ),
        "rnbqkbnr/ppp3pp/4p3/3p1p2/3PP3/8/PPPN1PPP/R1BQKBNR w KQkq -": (
            "C03",
            "French Defense: Tarrasch Variation, Haberditz Variation",
        ),
        "rnbqkbnr/1pp2ppp/p3p3/3p4/3PP3/8/PPPN1PPP/R1BQKBNR w KQkq -": (
            "C03",
            "French Defense: Tarrasch Variation, Modern System",
        ),
        "rnbqk1nr/ppp1bppp/4p3/3p4/3PP3/8/PPPN1PPP/R1BQKBNR w KQkq -": (
            "C03",
            "French Defense: Tarrasch Variation, Morozevich Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/8/PPPN1PPP/R1BQKBNR b KQkq -": (
            "C03",
            "French Defense: Tarrasch Variation",
        ),
        "r1bqkb1r/ppp2ppp/2n1pn2/3p4/3PP3/5N2/PPPN1PPP/R1BQKB1R w KQkq -": (
            "C04",
            "French Defense: Tarrasch Variation, Guimard Defense, Main Line",
        ),
        "rnbqkb1r/p2n1ppp/1p2p3/2ppP3/3P4/2PB4/PP1N1PPP/R1BQK1NR w KQkq -": (
            "C05",
            "French Defense: Tarrasch Variation, Botvinnik Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2n1p3/2ppP3/3P4/2PB4/PP1N1PPP/R1BQK1NR w KQkq -": (
            "C05",
            "French Defense: Tarrasch Variation, Closed Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/3PP3/8/PPPN1PPP/R1BQKBNR w KQkq -": (
            "C05",
            "French Defense: Tarrasch Variation, Closed Variation",
        ),
        "rnbqkb1r/pppn1ppp/4p3/3pP3/3P1P2/8/PPPN2PP/R1BQKBNR b KQkq -": (
            "C05",
            "French Defense: Tarrasch Variation, Pawn Center Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2n1p3/3pP3/3P4/3B4/PP1NNPPP/R1BQK2R b KQkq -": (
            "C06",
            "French Defense: Tarrasch Variation, Closed Variation, Main Line",
        ),
        "r1bqkb1r/pp3ppp/1nn1p3/3pP3/3P4/3B4/PP1NNPPP/R1BQK2R w KQkq -": (
            "C06",
            "French Defense: Tarrasch Variation, Leningrad Variation",
        ),
        "rnbqkbnr/pp3ppp/4p3/8/2Bp4/5N2/PPPN1PPP/R1BQK2R w KQkq -": (
            "C07",
            "French Defense: Tarrasch Variation, Eliskases Variation",
        ),
        "r1b1kb1r/1p3ppp/p2qpn2/8/2BN4/8/PPP2PPP/R1BQ1RK1 w kq -": (
            "C07",
            "French Defense: Tarrasch Variation, Chistyakov Defense, Modern Line",
        ),
        "rnb1kbnr/pp3ppp/4p3/2pq4/3P4/8/PPPN1PPP/R1BQKBNR w KQkq -": (
            "C07",
            "French Defense: Tarrasch Variation, Chistyakov Defense",
        ),
        "rnbqkbnr/pp3ppp/4p3/2pp4/3PP3/5N2/PPPN1PPP/R1BQKB1R b KQkq -": (
            "C07",
            "French Defense: Tarrasch Variation, Open System, Euwe-Keres Line",
        ),
        "rnbqkbnr/pp3ppp/4p3/2pp4/3PP3/8/PPPN1PPP/R1BQKBNR w KQkq -": (
            "C07",
            "French Defense: Tarrasch Variation, Open System",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2pP4/3P4/8/PPPN1PPP/R1BQKBNR w KQkq -": (
            "C07",
            "French Defense: Tarrasch Variation, Open System, Shaposhnikov Gambit",
        ),
        "rnbqkbnr/pp3ppp/4p3/2pp4/3PP3/2P5/PP1N1PPP/R1BQKBNR b KQkq -": (
            "C07",
            "French Defense: Tarrasch Variation, Open System, Süchting Line",
        ),
        "rnbqkbnr/pp3ppp/8/2pp4/3P4/8/PPPN1PPP/R1BQKBNR w KQkq -": (
            "C08",
            "French Defense: Tarrasch Variation, Open System",
        ),
        "rnbqkbnr/pp3ppp/8/3p4/2pP4/5N2/PPPN1PPP/R1BQKB1R w KQkq -": (
            "C08",
            "French Defense: Tarrasch Variation, Open System, Advance Line",
        ),
        "r1bqkbnr/pp3ppp/2n5/2pp4/3P4/5N2/PPPN1PPP/R1BQKB1R w KQkq -": (
            "C09",
            "French Defense: Tarrasch Variation, Open System, Main Line",
        ),
        "r1bqkbnr/ppp2ppp/2n1p3/3P4/3P4/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "C10",
            "French Defense: Classical Variation, Svenonius Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "C10",
            "French Defense: Paulsen Variation",
        ),
        "r1bqkbnr/pppn1ppp/4p3/8/3PN3/8/PPP2PPP/R1BQKBNR w KQkq -": (
            "C10",
            "French Defense: Rubinstein Variation, Blackburne Defense",
        ),
        "r1bqkb1r/ppp2ppp/4pn2/4N3/3P4/8/PPP2PPP/R1BQKB1R b KQkq -": (
            "C10",
            "French Defense: Rubinstein Variation, Capablanca Line",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/3PN3/8/PPP2PPP/R1BQKBNR w KQkq -": (
            "C10",
            "French Defense: Rubinstein Variation, Ellis Gambit",
        ),
        "rn1qkbnr/ppp2ppp/2b1p3/8/3PN3/5N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "C10",
            "French Defense: Rubinstein Variation, Fort Knox Variation",
        ),
        "r1bqkb1r/ppp2ppp/4pn2/8/3P4/2P2N2/PP3PPP/R1BQKB1R b KQkq -": (
            "C10",
            "French Defense: Rubinstein Variation, Kasparov Attack",
        ),
        "rnb1kbnr/ppp2ppp/4p3/3q4/3PN3/8/PPP2PPP/R1BQKBNR w KQkq -": (
            "C10",
            "French Defense: Rubinstein Variation, Marić Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/8/3Pp3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "C10",
            "French Defense: Rubinstein Variation",
        ),
        "rnbqkbnr/pp3ppp/4p3/2pp4/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "C10",
            "Sicilian Defense: Marshall Gambit",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p2B1/3PP3/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "C11",
            "French Defense: Burn Variation",
        ),
        "rnbq1rk1/ppp2ppp/4pb2/8/3PN3/5N2/PPP2PPP/R2QKB1R w KQ -": (
            "C11",
            "French Defense: Classical Variation, Burn Variation, Main Line",
        ),
        "rnbqk2r/ppp1bp1p/4pp2/8/3PN3/8/PPP2PPP/R2QKBNR w KQkq -": (
            "C11",
            "French Defense: Classical Variation, Burn Variation, Morozevich Line",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3P4/3P4/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "C11",
            "French Defense: Classical Variation, Delayed Exchange Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "C11",
            "French Defense: Classical Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3pP3/3P4/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "C11",
            "French Defense: Classical Variation, Steinitz Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/3PP3/2NB4/PPP2PPP/R1BQK1NR b KQkq -": (
            "C11",
            "French Defense: Classical Variation, Swiss Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/3PP3/2N1B3/PPP2PPP/R2QKBNR b KQkq -": (
            "C11",
            "French Defense: Henneberger Variation",
        ),
        "r1bq1rk1/pp1n2pp/2n1pp2/2bpP3/5PQ1/P1N2N2/1PP3PP/R1B1KB1R w KQ -": (
            "C11",
            "French Defense: Steinitz Variation, Brodsky-Jones Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2n1p3/2ppP3/3P1P2/2N1BN2/PPP3PP/R2QKB1R b KQkq -": (
            "C11",
            "French Defense: Steinitz Variation, Boleslavsky Variation",
        ),
        "rnbqk2r/pp1n1ppp/4p3/2bpP3/5PQ1/2N5/PPP3PP/R1B1KBNR b KQkq -": (
            "C11",
            "French Defense: Steinitz Variation, Bradford Attack Variation",
        ),
        "rnbqkb1r/pppn1ppp/4p3/3pP3/3P2Q1/2N5/PPP2PPP/R1B1KBNR b KQkq -": (
            "C11",
            "French Defense: Steinitz Variation, Gledhill Attack",
        ),
        "r1bqkb1r/pp1n1ppp/2n1p3/2PpP3/5P2/2N5/PPP3PP/R1BQKBNR w KQkq -": (
            "C11",
            "French Defense: Steinitz Variation",
        ),
        "rnbqkb1r/pp1n1ppp/4p3/2ppP3/3P1P2/2N2N2/PPP3PP/R1BQKB1R b KQkq -": (
            "C11",
            "French Defense: Steinitz Variation",
        ),
        "rnbqk2r/ppp2ppp/4pn2/3pP1B1/1b1P4/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Advance Variation",
        ),
        "rnb1k2r/ppp2p1p/4pp2/q7/1b1P4/2N5/PPPQ1PPP/R3KBNR w KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Bogoljubov Variation",
        ),
        "rnbqk2r/ppp2pp1/4pn1p/3pP3/1b1P3B/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Bernstein Variation",
        ),
        "rnbqk2r/ppp2pp1/4pP1p/3p2B1/1b1P4/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Chigorin Variation",
        ),
        "rnbqk2r/ppp2pp1/4pn1p/3pP3/1b1P4/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Dr. Olland (Dutch) Variation",
        ),
        "rnbq1k1r/ppp2pp1/4p2p/3pP3/3Pn1Q1/2P5/P1P2PPP/R1B1KBNR b KQ -": (
            "C12",
            "French Defense: MacCutcheon Variation, Duras Variation",
        ),
        "rnbqk2r/ppp2ppp/4pn2/3P2B1/1b1P4/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Exchange Variation",
        ),
        "rnbqk1r1/ppp2pP1/4p3/3p4/1b1P2Qp/2N5/PPP2PP1/R3KBNR b KQq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Grigoriev Variation",
        ),
        "rnbqk2r/ppp2pp1/4pn1p/3pP3/1b1P4/2N1B3/PPP2PPP/R2QKBNR b KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Janowski Variation",
        ),
        "rnbqk2r/ppp2p2/4p1pp/3pP3/3Pn1Q1/2P5/P1PB1PPP/R3KBNR w KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Lasker Variation",
        ),
        "rnbqk2r/ppp2pp1/4pn1p/3pP3/3P4/2b5/PPPB1PPP/R2QKBNR w KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Lasker Variation",
        ),
        "rnbqk2r/ppp2ppp/4pn2/3p2B1/1b1PP3/2N5/PPP2PPP/R2QKBNR w KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation",
        ),
        "rnbqk2r/pppn1pp1/4p2p/3pP3/1b1P4/2N5/PPPB1PPP/R2QKBNR w KQkq -": (
            "C12",
            "French Defense: MacCutcheon Variation, Tartakower Variation",
        ),
        "rnb1k2r/pppn1ppp/4p3/3pP1q1/3P4/2N5/PPP2PP1/R2QKBNR w KQkq -": (
            "C13",
            "French Defense: Alekhine-Chatard Attack, Albin-Chatard Gambit",
        ),
        "rnbqk2r/pp1nbppp/4p3/2ppP1B1/3P3P/2N5/PPP2PP1/R2QKBNR w KQkq -": (
            "C13",
            "French Defense: Alekhine-Chatard Attack, Breyer Variation",
        ),
        "rnbqk2r/1ppnbppp/p3p3/3pP1B1/3P3P/2N5/PPP2PP1/R2QKBNR w KQkq -": (
            "C13",
            "French Defense: Alekhine-Chatard Attack, Maróczy Variation",
        ),
        "rnbqk2r/pppnbppp/4p3/3pP1B1/3P3P/2N5/PPP2PP1/R2QKBNR b KQkq -": (
            "C13",
            "French Defense: Alekhine-Chatard Attack",
        ),
        "rnbq1rk1/pppnbppp/4p3/3pP1B1/3P3P/2N5/PPP2PP1/R2QKBNR w KQ -": (
            "C13",
            "French Defense: Alekhine-Chatard Attack, Spielmann Variation",
        ),
        "rnbqk2r/pppnb1pp/4pp2/3pP1B1/3P3P/2N5/PPP2PP1/R2QKBNR w KQkq -": (
            "C13",
            "French Defense: Alekhine-Chatard Attack, Teichmann Variation",
        ),
        "rnbqk1nr/p1p1bppp/1p2p3/3pP3/3P4/2N1B3/PPP2PPP/R2QKBNR w KQkq -": (
            "C13",
            "French Defense: Classical Variation, Frankfurt Variation",
        ),
        "rnbqk2r/ppp1bppp/4pn2/3p2B1/3PP3/2N5/PPP2PPP/R2QKBNR w KQkq -": (
            "C13",
            "French Defense: Classical Variation, Normal Variation",
        ),
        "rnbqk2r/ppp1bppp/4p3/3pP3/3P2Q1/2N5/PPP2PPP/R3KBNR b KQkq -": (
            "C13",
            "French Defense: Classical Variation, Richter Attack",
        ),
        "rnbqk2r/ppp1bppp/4pB2/3p4/3PP3/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "C13",
            "French Defense: Classical Variation, Richter Attack",
        ),
        "rnbqk2r/ppp1bppp/4p3/3pP1B1/3Pn3/2N5/PPP2PPP/R2QKBNR w KQkq -": (
            "C13",
            "French Defense: Classical Variation, Tartakower Variation",
        ),
        "rnbqk1nr/ppp1bppp/4p3/3pP1B1/3P4/2N5/PPP2PPP/R2QKBNR w KQkq -": (
            "C13",
            "French Defense: Classical Variation, Vistaneckis (Nimzowitsch) Variation",
        ),
        "r1b2rk1/pp1nqppp/2n1p3/3pP3/2pP1P2/2N2N2/PPPQ2PP/2KR1B1R w - -": (
            "C14",
            "French Defense: Classical Variation, Stahlberg Variation",
        ),
        "rnb1k2r/pppnqppp/4p3/1N1pP3/3P4/8/PPP2PPP/R2QKBNR b KQkq -": (
            "C14",
            "French Defense: Classical Variation, Alapin Variation",
        ),
        "rnb1k2r/pppnqppp/4p3/3pP3/3P2Q1/2N5/PPP2PPP/R3KBNR b KQkq -": (
            "C14",
            "French Defense: Classical Variation, Pollock Variation",
        ),
        "rnb1k2r/pppnqppp/4p3/3pP3/3P4/2N5/PPPQ1PPP/R3KBNR b KQkq -": (
            "C14",
            "French Defense: Classical Variation, Rubinstein Variation",
        ),
        "rnb1k2r/pppnqppp/4p3/3pP3/3P1P2/2N5/PPP3PP/R2QKBNR b KQkq -": (
            "C14",
            "French Defense: Classical Variation, Steinitz Variation",
        ),
        "rnb1k2r/pppnqppp/4p3/3pP3/3P4/2NB4/PPP2PPP/R2QK1NR b KQkq -": (
            "C14",
            "French Defense: Classical Variation, Tarrasch Variation",
        ),
        "rnb1k2r/pppnqppp/4p3/3pP3/3P4/2N5/PPP2PPP/R2QKBNR w KQkq -": (
            "C14",
            "French Defense: Classical Variation",
        ),
        "rnbqk2r/ppp2ppp/4pn2/3p2B1/1b1PP3/2N5/PPP1NPPP/R2QKB1R b KQkq -": (
            "C15",
            "French Defense: MacCutcheon Variation, Wolf Gambit",
        ),
        "r1bq1rk1/ppp1bppp/2n1pn2/8/3PN3/P5N1/1PP1BPPP/R1BQK2R w KQ -": (
            "C15",
            "French Defense: Winawer Variation, Alekhine Gambit, Alatortsev Variation",
        ),
        "rnbqk1nr/ppp2ppp/4p3/8/3Pp3/P1b5/1PP1NPPP/R1BQKB1R w KQkq -": (
            "C15",
            "French Defense: Winawer Variation, Alekhine Gambit Accepted",
        ),
        "r1bqk1nr/ppp2ppp/2n1p3/8/3Pp3/P1N5/1PP2PPP/R1BQKB1R w KQkq -": (
            "C15",
            "French Defense: Winawer Variation, Alekhine Gambit, Kan Variation",
        ),
        "rnbqk1nr/ppp2ppp/4p3/3p4/1b1PP3/2N5/PPP1NPPP/R1BQKB1R b KQkq -": (
            "C15",
            "French Defense: Winawer Variation, Alekhine-Maróczy Gambit",
        ),
        "rnbqk1nr/ppp2ppp/4p3/3P4/1b1P4/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "C15",
            "French Defense: Winawer Variation, Delayed Exchange Variation",
        ),
        "rnbqk2r/ppp1nppp/8/3p3Q/1b1P4/2NB4/PPP2PPP/R1B1K1NR b KQkq -": (
            "C15",
            "French Defense: Winawer Variation, Exchange Variation, Canal Attack",
        ),
        "rnb1k1nr/ppp2ppp/4p3/8/1b1qp1Q1/2N5/PPPB1PPP/R3KBNR w KQkq -": (
            "C15",
            "French Defense: Winawer Variation, Fingerslip Variation, Kunin Double Gambit",
        ),
        "rnbqk1r1/ppp2p1p/4pn1Q/8/1b1Pp3/2N5/PPPB1PPP/R3KBNR b KQq -": (
            "C15",
            "French Defense: Winawer Variation, Fingerslip Variation, Main Line",
        ),
        "rnbqk1nr/ppp2ppp/4p3/3p4/1b1PP3/2N5/PPPB1PPP/R2QKBNR b KQkq -": (
            "C15",
            "French Defense: Winawer Variation, Fingerslip Variation",
        ),
        "rnbqk2r/ppp1nppp/4p3/3p4/1b1PP3/8/PPPB1PPP/RN1QKBNR b KQkq -": (
            "C15",
            "French Defense: Winawer Variation, Fingerslip Variation, Schwarz Line",
        ),
        "rnb1k1nr/pp3ppp/4p3/2pq4/1b1P4/2NB4/PPPB1PPP/R2QK1NR b KQkq -": (
            "C15",
            "French Defense: Winawer Variation, Kondratiyev Variation",
        ),
        "rnbqk1nr/ppp2ppp/4p3/3p4/1b1PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "C15",
            "French Defense: Winawer Variation",
        ),
        "rnbqk1nr/ppp2ppp/4p3/3p4/1b1PP3/P1N5/1PP2PPP/R1BQKBNR b KQkq -": (
            "C15",
            "French Defense: Winawer Variation, Winckelmann-Riemer Gambit",
        ),
        "rnbqk1nr/ppp2ppp/4p3/3pP3/1b1P4/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "C16",
            "French Defense: Winawer Variation, Advance Variation",
        ),
        "rnb1k1nr/pppq1ppp/4p3/3pP3/1b1P4/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "C16",
            "French Defense: Winawer Variation, Petrosian Variation",
        ),
        "rnbqk1nr/pp3ppp/4p3/2ppP3/1b1P2Q1/2N5/PPP2PPP/R1B1KBNR b KQkq -": (
            "C17",
            "French Defense: Winawer Variation, Advance Variation, Moscow Variation",
        ),
        "rnbqk1nr/pp3ppp/4p3/2ppP3/1b1P4/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "C17",
            "French Defense: Winawer Variation, Advance Variation",
        ),
        "rnbqk1nr/pp3ppp/4p3/2ppP3/1b1P4/P1N5/1PP2PPP/R1BQKBNR b KQkq -": (
            "C17",
            "French Defense: Winawer Variation, Advance Variation",
        ),
        "rnbqk1nr/pp3ppp/4p3/3pP3/1P6/2p2N2/1PP2PPP/R1BQKB1R b KQkq -": (
            "C17",
            "French Defense: Winawer Variation, Advance Variation",
        ),
        "rnbqk2r/pp2nppp/4p3/2ppP3/1b1P1P2/2N5/PPPB2PP/R2QKBNR b KQkq -": (
            "C17",
            "French Defense: Winawer Variation, Bogoljubov Variation, Icelandic Defense",
        ),
        "rnbqk1nr/pp3ppp/4p3/2ppP3/1b1P4/2N5/PPPB1PPP/R2QKBNR b KQkq -": (
            "C17",
            "French Defense: Winawer Variation, Bogoljubov Variation",
        ),
        "rnbqk1nr/pp3ppp/4p3/3pP3/1P6/2p5/1PP2PPP/R1BQKBNR w KQkq -": (
            "C17",
            "French Defense: Winawer Variation, Maróczy-Wallis Variation",
        ),
        "rnbqk1nr/pp3ppp/4p3/b2pP3/1P1p4/P1N5/2P2PPP/R1BQKBNR w KQkq -": (
            "C17",
            "French Defense: Winawer Variation, Retreat Variation, Armenian Line",
        ),
        "rnbqk1nr/pp3ppp/4p3/b1ppP3/3P4/P1N5/1PP2PPP/R1BQKBNR w KQkq -": (
            "C17",
            "French Defense: Winawer Variation, Retreat Variation",
        ),
        "rnbqk1nr/pp3ppp/4p3/2ppP3/3P4/P1P5/2P2PPP/R1BQKBNR b KQkq -": (
            "C18",
            "French Defense: Winawer Variation, Advance Variation",
        ),
        "rnb1k1nr/ppq2ppp/4p3/2ppP3/3P4/P1P5/2P2PPP/R1BQKBNR w KQkq -": (
            "C18",
            "French Defense: Winawer Variation, Classical Variation",
        ),
        "rnbqk2r/pp2nppp/4p3/2ppP3/3P4/P1P5/2P2PPP/R1BQKBNR w KQkq -": (
            "C19",
            "French Defense: Winawer Variation, Advance Variation",
        ),
        "rnbqk2r/pp2nppp/4p3/2ppP3/P2P4/2P5/2P2PPP/R1BQKBNR b KQkq -": (
            "C19",
            "French Defense: Winawer Variation, Advance Variation",
        ),
        "rnb1k1r1/ppq1np1Q/4p3/3pP3/3p4/P1P5/2P1NPPP/R1B1KB1R b KQq -": (
            "C19",
            "French Defense: Winawer Variation, Poisoned Pawn Variation, Main Line",
        ),
        "rnb1k1r1/ppq1np1Q/4p3/3pP3/3p4/P1P5/2P2PPP/R1BK1BNR b q -": (
            "C19",
            "French Defense: Winawer Variation, Poisoned Pawn Variation, Paoli Variation",
        ),
        "rnbqk2r/pp2nppp/4p3/2ppP3/3P2Q1/P1P5/2P2PPP/R1B1KBNR b KQkq -": (
            "C19",
            "French Defense: Winawer Variation, Poisoned Pawn Variation",
        ),
        "rnbqk2r/pp2nppp/4p3/2ppP3/3P4/P1P2N2/2P2PPP/R1BQKB1R b KQkq -": (
            "C19",
            "French Defense: Winawer Variation, Positional Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2B1P3/5P2/PPPP2PP/RNBQK1NR b KQkq -": (
            "C20",
            "Barnes Opening: Walkerling Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPPKPPP/RNBQ1BNR b kq -": (
            "C20",
            "Bongcloud Attack",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/3PP3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "C20",
            "Center Game",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/2P1P3/8/PP1P1PPP/RNBQKBNR b KQkq -": (
            "C20",
            "English Opening: The Whale Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPPNPPP/RNBQKB1R b KQkq -": (
            "C20",
            "King's Pawn Game: Alapin Opening",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/2P1P3/8/PP1P1PPP/RNBQKBNR w KQkq -": (
            "C20",
            "King's Pawn Game: Bavarian Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/3PP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C20",
            "King's Pawn Game: Beyer Gambit",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/4P3/3P4/PPP2PPP/RNBQKBNR w KQkq -": (
            "C20",
            "King's Pawn Game: Clam Variation, Reversed King's Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N2P2/PPPP2PP/R1BQKBNR b KQkq -": (
            "C20",
            "King's Pawn Game: King's Head Opening",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/5P2/PPPP2PP/RNBQKBNR b KQkq -": (
            "C20",
            "King's Pawn Game: King's Head Opening",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/3P4/PPP2PPP/RNBQKBNR b KQkq -": (
            "C20",
            "King's Pawn Game: Leonardis Variation",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/4P3/2P5/PP1P1PPP/RNBQKBNR w KQkq -": (
            "C20",
            "King's Pawn Game: MacLeod Attack, Lasa Gambit",
        ),
        "rnbqk1nr/ppp2ppp/3b4/3pp2Q/4P3/2P5/PP1P1PPP/RNB1KBNR w KQkq -": (
            "C20",
            "King's Pawn Game: MacLeod Attack, Norwalde Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/2P5/PP1P1PPP/RNBQKBNR b KQkq -": (
            "C20",
            "King's Pawn Game: MacLeod Attack",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/P7/1PPP1PPP/RNBQKBNR b KQkq -": (
            "C20",
            "King's Pawn Game: Mengarini Opening",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/5Q2/PPPP1PPP/RNB1KBNR b KQkq -": (
            "C20",
            "King's Pawn Game: Napoleon Attack",
        ),
        "rn1qkbnr/pppb1ppp/3p4/4P3/4P3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C20",
            "King's Pawn Game: Philidor Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq -": (
            "C20",
            "King's Pawn Game",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/3B4/PPPP1PPP/RNBQK1NR b KQkq -": (
            "C20",
            "King's Pawn Game: Tortoise Opening",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p2Q/4P3/8/PPPP1PPP/RNB1KBNR w KQkq -": (
            "C20",
            "King's Pawn Game: Wayward Queen's Attack, Kiddie Countergambit",
        ),
        "r1bqkb1r/ppp4p/2n2ppn/3pp3/2B1P3/3P1Q2/PPP1NPPP/RNB1K2R w KQkq -": (
            "C20",
            "King's Pawn Game: Wayward Queen's Attack, Mellon Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p2Q/4P3/8/PPPP1PPP/RNB1KBNR b KQkq -": (
            "C20",
            "King's Pawn Game: Wayward Queen's Attack",
        ),
        "r1bqkbnr/pp3ppp/2n5/4p3/8/3P4/PPP2PPP/RNBQKBNR w KQkq -": (
            "C20",
            "King's Pawn Game: Weber Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/1P6/P1PP1PPP/RNBQKBNR b KQkq -": (
            "C20",
            "King's Pawn Opening",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4pQ2/4P3/8/PPPP1PPP/RNB1KBNR b KQkq -": (
            "C20",
            "King's Pawn Opening: Speers Variation",
        ),
        "r1bqk2r/pppp1ppp/5n2/2b5/3nP3/5N2/PP2QPPP/RNB1KB1R w KQkq -": (
            "C20",
            "King's Pawn Opening: van Hooydoon Gambit",
        ),
        "rnbqk1nr/pppp1ppp/8/1Bb1p3/1P2P3/8/P1PP1PPP/RNBQK1NR b KQkq -": (
            "C20",
            "Portuguese Opening: Miguel Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/1B2p3/3PP3/8/PPP2PPP/RNBQK1NR b KQkq -": (
            "C20",
            "Portuguese Opening: Portuguese Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/1B2p3/4P3/8/PPPP1PPP/RNBQK1NR b KQkq -": (
            "C20",
            "Portuguese Opening",
        ),
        "rnbqkbnr/pppp1ppp/8/8/3pP3/8/PPP2PPP/RNBQKBNR w KQkq -": (
            "C21",
            "Center Game Accepted",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b5/3pPP2/2P2N2/PP4PP/RNBQKB1R b KQkq -": (
            "C21",
            "Center Game: Halasz-McDonnell Gambit, Crocodile Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/8/3pPP2/8/PPP3PP/RNBQKBNR b KQkq -": (
            "C21",
            "Center Game: Halasz-McDonnell Gambit",
        ),
        "rnbqkbnr/p2p1ppp/8/1pp5/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C21",
            "Center Game: Kieseritzky Variation",
        ),
        "rnbqkbnr/pp1p1ppp/8/2p5/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C21",
            "Center Game: Kieseritzky Variation",
        ),
        "rnbqkbnr/pp1p1ppp/8/2p5/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C21",
            "Center Game: Kieseritzky Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/8/3pP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C21",
            "Center Game: Kieseritzky Variation",
        ),
        "rnbqk1nr/pppp1ppp/8/2b5/3pP3/2P2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "C21",
            "Center Game: Lanc-Arnold Gambit",
        ),
        "rnbqk1nr/pppp1ppp/8/2b5/2B1P3/2p2N2/PP3PPP/RNBQK2R b KQkq -": (
            "C21",
            "Center Game: Lanc-Arnold Gambit, Schippler Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/3QP3/8/PPP2PPP/RNB1KBNR b KQkq -": (
            "C21",
            "Center Game",
        ),
        "rnbqkbnr/pppp1ppp/8/8/3pP3/3B4/PPP2PPP/RNBQK1NR b KQkq -": (
            "C21",
            "Center Game: Ross Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/2BpP3/8/PPP2PPP/RNBQK1NR b KQkq -": (
            "C21",
            "Center Game: von der Lasa Gambit",
        ),
        "rnb1kbnr/ppppqppp/8/8/2B1P3/8/PB3PPP/RN1QK1NR w KQkq -": (
            "C21",
            "Danish Gambit Accepted: Chigorin Defense",
        ),
        "rnbqkb1r/pppp1ppp/5n2/8/2B1P3/8/PB3PPP/RN1QK1NR w KQkq -": (
            "C21",
            "Danish Gambit Accepted: Classical Defense",
        ),
        "rnbqk1nr/pppp1ppp/8/8/1bB1P3/8/PB3PPP/RN1QK1NR w KQkq -": (
            "C21",
            "Danish Gambit Accepted: Copenhagen Defense",
        ),
        "rnbqkbnr/pppp1ppp/8/8/2B1P3/8/PB3PPP/RN1QK1NR b KQkq -": (
            "C21",
            "Danish Gambit Accepted",
        ),
        "rnbqkbnr/ppp2ppp/8/3p4/2B1P3/8/PB3PPP/RN1QK1NR w KQkq -": (
            "C21",
            "Danish Gambit Accepted: Schlechter Defense",
        ),
        "rnbqkb1r/ppppnppp/8/8/3pP3/2P5/PP3PPP/RNBQKBNR w KQkq -": (
            "C21",
            "Danish Gambit Accepted: Svenonius Defense",
        ),
        "rnbqkbnr/ppp2ppp/8/3p4/3pP3/2P5/PP3PPP/RNBQKBNR w KQkq -": (
            "C21",
            "Danish Gambit Declined: Sorensen Defense",
        ),
        "rnbqkbnr/pppp1ppp/8/8/3pP3/2P5/PP3PPP/RNBQKBNR b KQkq -": (
            "C21",
            "Danish Gambit",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/8/4P3/4Q3/PPP2PPP/RNB1KBNR w KQkq -": (
            "C22",
            "Center Game: Berger Variation",
        ),
        "r1bqk1nr/ppppbppp/2n5/8/4P3/2P1Q3/PP3PPP/RNB1KBNR w KQkq -": (
            "C22",
            "Center Game: Charousek Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/2Q1P3/8/PPP2PPP/RNB1KBNR b KQkq -": (
            "C22",
            "Center Game: Hall Variation",
        ),
        "r1bqr1k1/ppp2ppp/2np1n2/8/1bB1P3/2N1Q2N/PPPB1PPP/2KR3R b - -": (
            "C22",
            "Center Game: Kupreichik Variation",
        ),
        "r1bqkbnr/pppp2pp/2n5/5p2/4P3/4Q3/PPP2PPP/RNB1KBNR w KQkq -": (
            "C22",
            "Center Game: l'Hermet Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/3QP3/8/PPP2PPP/RNB1KBNR w KQkq -": (
            "C22",
            "Center Game: Normal Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/4P3/4Q3/PPP2PPP/RNB1KBNR b KQkq -": (
            "C22",
            "Center Game: Paulsen Attack Variation",
        ),
        "rnbqkbnr/p2p1ppp/2p5/1B2p3/4P3/8/PPPP1PPP/RNBQK1NR w KQkq -": (
            "C23",
            "Bishop's Opening: Anderssen Gambit",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/2B1P3/8/PPPP1PPP/RNBQK1NR w KQkq -": (
            "C23",
            "Bishop's Opening: Boi Variation",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/2B1P3/3P4/PPP2PPP/RNBQK1NR b KQkq -": (
            "C23",
            "Bishop's Opening: Calabrese Countergambit, Jaenisch Variation",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/2B1P3/8/PPPP1PPP/RNBQK1NR w KQkq -": (
            "C23",
            "Bishop's Opening: Calabrese Countergambit",
        ),
        "rnb1k1nr/pppp1ppp/8/2b1p1q1/2B1P3/2P5/PP1P1PPP/RNBQK1NR w KQkq -": (
            "C23",
            "Bishop's Opening: del Rio Variation",
        ),
        "rnbqk1nr/pppp1ppp/8/8/2BPP2b/5N2/P1P4p/RNBQ1R1K b kq -": (
            "C23",
            "Bishop's Opening: Four Pawns Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/2B1P3/8/PPPP1PPP/RNBQK1NR w KQkq -": (
            "C23",
            "Bishop's Opening: Khan Gambit",
        ),
        "rnbqk1nr/ppp2ppp/8/2bpp3/2B1P3/2P5/PP1P1PPP/RNBQK1NR w KQkq -": (
            "C23",
            "Bishop's Opening: Lewis Countergambit",
        ),
        "rnbqk2r/ppp2ppp/5n2/2bBp3/4P3/2P5/PP1P1PPP/RNBQK1NR w KQkq -": (
            "C23",
            "Bishop's Opening: Lewis Countergambit",
        ),
        "rnbqk2r/ppp2ppp/5n2/2bBp3/3PP3/2P5/PP3PPP/RNBQK1NR b KQkq -": (
            "C23",
            "Bishop's Opening: Lewis Countergambit, Walker Variation",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/2BPP3/8/PPP2PPP/RNBQK1NR b KQkq -": (
            "C23",
            "Bishop's Opening: Lewis Gambit",
        ),
        "r2qkbnr/pp3ppp/8/3pn3/8/8/PPP1NPPP/RNBQK2R b KQkq -": (
            "C23",
            "Bishop's Opening: Lisitsin Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1PP2/2P5/PP1PQ1PP/RNB1K1NR b KQkq -": (
            "C23",
            "Bishop's Opening: López Gambit",
        ),
        "rnbqk2r/pppp1ppp/5n2/2b1p3/2B1PP2/8/PPPPQ1PP/RNB1K1NR b KQkq -": (
            "C23",
            "Bishop's Opening: López Variation, López Gambit",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/2B1P3/8/PPPPQPPP/RNB1K1NR b KQkq -": (
            "C23",
            "Bishop's Opening: López Variation",
        ),
        "rnbqk1nr/pppp1ppp/8/4p3/1bB1P3/2P5/P2P1PPP/RNBQK1NR b KQkq -": (
            "C23",
            "Bishop's Opening: McDonnell Gambit, La Bourdonnais-Denker Gambit",
        ),
        "rnbqk1nr/pppp1ppp/8/4p3/1bB1PP2/8/P1PP2PP/RNBQK1NR b KQkq -": (
            "C23",
            "Bishop's Opening: McDonnell Gambit, McDonnell Double Gambit",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/1PB1P3/8/P1PP1PPP/RNBQK1NR b KQkq -": (
            "C23",
            "Bishop's Opening: McDonnell Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/2p5/4p3/2B1P3/8/PPPP1PPP/RNBQK1NR w KQkq -": (
            "C23",
            "Bishop's Opening: Philidor Counterattack",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/2B1P3/2P5/PP1P1PPP/RNBQK1NR b KQkq -": (
            "C23",
            "Bishop's Opening: Philidor Variation",
        ),
        "rnbq1rk1/ppp2ppp/5P2/2b4Q/2pp4/2P5/PP3PPP/RNB1K1NR w KQ -": (
            "C23",
            "Bishop's Opening: Pratt Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/2B1P3/8/PPPP1PPP/RNBQK1NR b KQkq -": (
            "C23",
            "Bishop's Opening",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/2B1PP2/8/PPPP2PP/RNBQK1NR b KQkq -": (
            "C23",
            "Bishop's Opening: Stein Gambit",
        ),
        "rnbqkbnr/p1pp2pp/8/1B2pp2/4P3/8/PPPP1PPP/RNBQK1NR w KQkq -": (
            "C23",
            "Bishop's Opening: Thorold Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2B1PP2/8/PPPP2PP/RNBQK1NR b KQkq -": (
            "C24",
            "Bishop's Opening: Berlin Defense, Greco Gambit",
        ),
        "rnbq1rk1/ppppbppp/5n2/4p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQ -": (
            "C24",
            "Bishop's Opening: Berlin Defense, Kitchener's Folly Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2B1P3/8/PPPP1PPP/RNBQK1NR w KQkq -": (
            "C24",
            "Bishop's Opening: Berlin Defense",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/1PB1P3/5P2/P1PPN1PP/RNBQK2R b KQkq -": (
            "C24",
            "Bishop's Opening: Krejcik Gambit",
        ),
        "rnbqkb1r/pppp1ppp/8/4p3/2B1n3/2N5/PPPP1PPP/RNBQK2R b KQkq -": (
            "C24",
            "Bishop's Opening: Pachman Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2BPP3/8/PPP2PPP/RNBQK1NR b KQkq -": (
            "C24",
            "Bishop's Opening: Ponziani Gambit",
        ),
        "rnb1k2r/ppp1qppp/5n2/3P4/1bBp4/2P2N2/PP3PPP/RNBQK2R w KQkq -": (
            "C24",
            "Bishop's Opening: Urusov Gambit, Panov Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/2NP4/PPP2PPP/R1BQK1NR b KQkq -": (
            "C24",
            "Bishop's Opening: Vienna Hybrid Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/8/2BpP3/2P5/PP3PPP/RNBQK1NR b KQkq -": (
            "C24",
            "Bishop's Opening: Warsaw Gambit",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "C25",
            "Vienna Game: Anderssen Defense",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "C25",
            "Vienna Game: Fyfe Gambit",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/4P1Q1/2N5/PPPP1PPP/R1B1KBNR b KQkq -": (
            "C25",
            "Vienna Game: Giraffe Attack",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/N3P3/8/PPPP1PPP/R1BQKBNR b KQkq -": (
            "C25",
            "Vienna Game: Hamppe-Meitner Variation",
        ),
        "r1b1kbnr/pppp1p1p/5q2/4n3/2B1PQ2/2N5/PPPP2PP/R1B2RK1 w kq -": (
            "C25",
            "Vienna Game: Hamppe-Muzio Gambit, Dubois Variation",
        ),
        "r1bqkbnr/pppp1p1p/2n5/8/2B1Ppp1/2N2N2/PPPP2PP/R1BQ1RK1 b kq -": (
            "C25",
            "Vienna Game: Hamppe-Muzio Gambit",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "C25",
            "Vienna Game: Max Lange Defense",
        ),
        "rnbqkbnr/ppp2ppp/3p4/4p3/4PP2/2N5/PPPP2PP/R1BQKBNR b KQkq -": (
            "C25",
            "Vienna Game: Omaha Gambit",
        ),
        "r1bqk1nr/pppp1pp1/2n5/2b1p3/4P2p/2N2NP1/PPPP1PBP/R1BQK2R w KQkq -": (
            "C25",
            "Vienna Game: Paulsen Variation, Mariotti Gambit",
        ),
        "r1bqk2r/ppp2ppp/2n2n2/2bpp3/4P3/2N3P1/PPPPNPBP/R1BQK2R w KQkq -": (
            "C25",
            "Vienna Game: Paulsen Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2N3P1/PPPP1P1P/R1BQKBNR b KQkq -": (
            "C25",
            "Vienna Game: Paulsen Variation",
        ),
        "r1bqkbnr/pppp2pp/2n5/4pp2/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "C25",
            "Vienna Game: Philidor Countergambit",
        ),
        "r2qkbnr/ppp2p1p/2P5/8/2BP1pb1/2N2p2/PPP3PP/R1BQ1RK1 b kq -": (
            "C25",
            "Vienna Game: Pierce Gambit, Rushmere Attack",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq -": (
            "C25",
            "Vienna Game",
        ),
        "r1b1k1nr/pppp1ppp/2n2q2/2bNp3/2B1P1Q1/8/PPPP1PPP/R1B1K1NR b KQkq -": (
            "C25",
            "Vienna Game: Stanley Variation, Meitner-Mieses Gambit",
        ),
        "r1bqk1nr/ppppbppp/2n5/8/4Pp2/2N2N2/PPPP2PP/R1BQKB1R w KQkq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Cunningham Defense",
        ),
        "r1bqkbnr/ppp2p1p/2np4/6N1/4PppP/2N5/PPPP2P1/R1BQKB1R w KQkq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Hamppe-Allgaier Gambit, Alapin Variation",
        ),
        "r1bq1bnr/pppp1k2/2n4p/8/3PPppP/2N5/PPP3P1/R1BQKB1R b KQ -": (
            "C25",
            "Vienna Game: Vienna Gambit, Hamppe-Allgaier Gambit, Thorold Variation",
        ),
        "r1bqkbnr/pppp1p1p/2n5/6N1/4PppP/2N5/PPPP2P1/R1BQKB1R b KQkq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Hamppe-Allgaier Gambit",
        ),
        "r1bqkbnr/pppp1p1p/2n5/8/2B1Pp2/2N2p2/PPPP2PP/R1BQ1RK1 w kq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Hamppe-Muzio Gambit",
        ),
        "r1bqkbnr/pppp1p1p/2n5/6p1/3PPp2/2N2N2/PPP3PP/R1BQKB1R b KQkq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Pierce Gambit",
        ),
        "r1bqk1nr/ppp2ppp/2np4/2b1P3/4P3/2N5/PPPP2PP/R1BQKBNR w KQkq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Quelle Gambit",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/4PP2/2N5/PPPP2PP/R1BQKBNR b KQkq -": (
            "C25",
            "Vienna Game: Vienna Gambit",
        ),
        "r1b1kbnr/p1pp1ppp/1pn5/8/3PPp1q/2N5/PPP1K1PP/R1BQ1BNR w kq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Steinitz Gambit, Fraser-Minckwitz Defense",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/4Pp2/2N2N2/PPPP2PP/R1BQKB1R b KQkq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Steinitz Gambit, Knight Variation",
        ),
        "r1b1kbnr/pppp1ppp/2n5/8/3PPp1q/2N5/PPP1K1PP/R1BQ1BNR b kq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Steinitz Gambit, Main Line",
        ),
        "r1b1kbnr/ppp2ppp/2np4/8/3PPp1q/2N5/PPP1K1PP/R1BQ1BNR w kq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Steinitz Gambit, Paulsen Defense",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/3PPp2/2N5/PPP3PP/R1BQKBNR b KQkq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Steinitz Gambit",
        ),
        "r1b1kbnr/pppp1p1p/2n5/6p1/3PPp1q/2N5/PPP1K1PP/R1BQ1BNR w kq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Steinitz Gambit, Sörensen Defense",
        ),
        "r1b1kbnr/ppp2ppp/2n5/3p4/3PPp1q/2N5/PPP1K1PP/R1BQ1BNR w kq -": (
            "C25",
            "Vienna Game: Vienna Gambit, Steinitz Gambit, Zukertort Defense",
        ),
        "rnbqk2r/pppp1ppp/5n2/4p3/1b2P1Q1/2N5/PPPP1PPP/R1B1KBNR w KQkq -": (
            "C25",
            "Vienna Game: Zhuravlev Countergambit",
        ),
        "rnbqkb1r/p1pp1ppp/5n2/1p2p3/2B1P3/2N5/PPPP1PPP/R1BQK1NR w KQkq -": (
            "C26",
            "Bishop's Opening: Horwitz Gambit",
        ),
        "rnbqk2r/pppp1ppp/5n2/2b1p3/2B1P3/2NP4/PPP2PPP/R1BQK1NR b KQkq -": (
            "C26",
            "Bishop's Opening: Vienna Hybrid Variation, Spielmann Attack",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq -": (
            "C26",
            "Vienna Game: Falkbeer Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/P1N5/1PPP1PPP/R1BQKBNR b KQkq -": (
            "C26",
            "Vienna Game: Mengarini Variation",
        ),
        "rnbqkb1r/pp3ppp/2p2n2/3Pp3/8/2N3P1/PPPP1P1P/R1BQKBNR w KQkq -": (
            "C26",
            "Vienna Game: Mieses Variation, Erben Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N3P1/PPPP1P1P/R1BQKBNR b KQkq -": (
            "C26",
            "Vienna Game: Mieses Variation",
        ),
        "r1bqk2r/ppp2ppp/2n2n2/2bPp3/8/2N3P1/PPPPNPBP/R1BQK2R b KQkq -": (
            "C26",
            "Vienna Game: Paulsen Variation, Pollock Gambit",
        ),
        "rnbqk2r/p1pp1ppp/5n2/1pb1p3/2B1P3/2N5/PPPPNPPP/R1BQK2R w KQkq -": (
            "C26",
            "Vienna Game: Stanley Variation, Eifel Gambit",
        ),
        "rnbqk2r/pppp1ppp/5n2/4p3/1bB1P3/2N5/PPPP1PPP/R1BQK1NR w KQkq -": (
            "C26",
            "Vienna Game: Stanley Variation, Reversed Spanish Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2B1P3/2N5/PPPP1PPP/R1BQK1NR b KQkq -": (
            "C26",
            "Vienna Game: Stanley Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/4PP2/2N5/PPPP2PP/R1BQKBNR b KQkq -": (
            "C26",
            "Vienna Game: Vienna Gambit",
        ),
        "rnbqkb1r/pppp1ppp/8/4p3/2B1n3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -": (
            "C27",
            "Bishop's Opening: Boden-Kieseritzky Gambit",
        ),
        "rnbqkb1r/ppp2ppp/8/3pp3/2B1n3/2N2N2/PPPP1PPP/R1BQK2R w KQkq -": (
            "C27",
            "Bishop's Opening: Boden-Kieseritzky Gambit, Lichtenhein Defense",
        ),
        "r1bqkb1r/pppp1ppp/2nn4/4p2Q/3P4/1BN5/PPP2PPP/R1B1K1NR b KQkq -": (
            "C27",
            "Vienna Game: Adams Gambit",
        ),
        "rnbqkb1r/pppp1ppp/8/4p3/2B1n3/2N5/PPPP1PPP/R1BQK1NR w KQkq -": (
            "C27",
            "Vienna Game: Frankenstein-Dracula Variation",
        ),
        "r1bqk2r/ppppbppp/2nn4/4N2Q/8/1BN5/PPPP1PPP/R1B1K2R b KQkq -": (
            "C27",
            "Vienna Game: Stanley Variation, Alekhine Variation",
        ),
        "N1bk1b1r/p2pq2p/1pnn2p1/3Qpp2/8/1B6/PPPP1PPP/R1B1K1NR w KQ -": (
            "C27",
            "Vienna Game: Stanley Variation, Frankenstein-Dracula Variation",
        ),
        "rnbqk2r/ppppbppp/3n4/4p2Q/8/1BN5/PPPP1PPP/R1B1K1NR w KQkq -": (
            "C27",
            "Vienna Game: Stanley Variation, Monster Gambit Declined",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/4p3/1bB1P3/2NP4/PPP1NPPP/R1BQK2R b KQkq -": (
            "C28",
            "Bishop's Opening: Vienna Hybrid Variation, Hromádka Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n5/4p3/2B1nP2/2N2N2/PPPP2PP/R1BQK2R b KQkq -": (
            "C28",
            "Vienna Game: Stanley Variation, Bronstein Gambit",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/2N5/PPPP1PPP/R1BQK1NR w KQkq -": (
            "C28",
            "Vienna Game: Stanley Variation, Three Knights Variation",
        ),
        "rnbqkb1r/ppp3pp/8/3pPp2/3Pn3/2N2Q2/PPP3PP/R1B1KBNR b KQkq -": (
            "C29",
            "Vienna Game: Heyde Variation",
        ),
        "rnbqkb1r/ppp3pp/8/3pPp2/4n3/2N2Q2/PPPP2PP/R1B1KBNR w KQkq f6": (
            "C29",
            "Vienna Game: Vienna Gambit, Bardeleben Variation",
        ),
        "rnbqk2r/ppp1bppp/8/3pP3/4n3/2N2N2/PPPP2PP/R1BQKB1R w KQkq -": (
            "C29",
            "Vienna Game: Vienna Gambit, Breyer Variation",
        ),
        "rn1qkb1r/ppp2ppp/8/3pP3/4n1b1/2N2N2/PPPPQ1PP/R1B1KB1R b KQkq -": (
            "C29",
            "Vienna Game: Vienna Gambit, Kaufmann Variation",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3pp3/4PP2/2N5/PPPP2PP/R1BQKBNR w KQkq -": (
            "C29",
            "Vienna Game: Vienna Gambit, Main Line",
        ),
        "rnbqkb1r/ppp2ppp/8/3pP3/4n3/2NP4/PPP3PP/R1BQKBNR b KQkq -": (
            "C29",
            "Vienna Game: Vienna Gambit, Modern Variation",
        ),
        "rnbqkb1r/ppp2ppp/8/3pP3/4n3/2N2Q2/PPPP2PP/R1B1KBNR b KQkq -": (
            "C29",
            "Vienna Game: Vienna Gambit, Paulsen Attack",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3pp3/4PP2/2NP4/PPP3PP/R1BQKBNR b KQkq -": (
            "C29",
            "Vienna Game: Vienna Gambit, Steinitz Variation",
        ),
        "rnb1kb1r/ppp2ppp/8/3NP2q/8/3P1Nn1/PPP4P/R1BQKB1R b KQkq -": (
            "C29",
            "Vienna Game: Vienna Gambit, Würzburger Trap",
        ),
        "r1bqk1nr/pppn1ppp/3p4/2b1p3/4PP2/2N2N2/PPPP2PP/R1BQKB1R w KQkq -": (
            "C30",
            "King's Gambit Declined: Classical Variation, Hanham Variation",
        ),
        "rnbqk1nr/ppp3pp/8/2b2p2/2BpP3/2P2N2/PP4PP/RNBQK2R b KQkq -": (
            "C30",
            "King's Gambit Declined: Classical Variation, Réti Variation",
        ),
        "rnbqk1nr/ppp2ppp/3p4/2b1P3/4P3/5N2/PPPP2PP/RNBQKB1R b KQkq -": (
            "C30",
            "King's Gambit Declined: Classical Variation, Soldatenkov Variation",
        ),
        "r2qk2r/ppp2ppp/2np1n2/2b5/2B1Pp2/2NP1Q1P/PPP3P1/R1B1K2R w KQkq -": (
            "C30",
            "King's Gambit Declined: Classical Variation, Svenonius Variation",
        ),
        "rn1qk1nr/ppp2ppp/8/2b1p3/Q3P1b1/2P2N2/PP1P2PP/RNB1KB1R b KQkq -": (
            "C30",
            "King's Gambit Declined: Classical Variation, Euwe Attack",
        ),
        "rnbqk1nr/ppp2ppp/3p4/2b1p3/4PP2/2P2N2/PP1P2PP/RNBQKB1R b KQkq -": (
            "C30",
            "King's Gambit Declined: Classical Variation",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/4PP2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Classical Variation",
        ),
        "rnbqk1nr/ppp2ppp/3p4/2b1p3/1P2PP2/5N2/P1PP2PP/RNBQKB1R b KQkq -": (
            "C30",
            "King's Gambit Declined: Classical Variation, Rotlewi Countergambit",
        ),
        "rnbqk1nr/ppp3pp/3p4/2b1pp2/4PP2/2P2N2/PP1P2PP/RNBQKB1R w KQkq -": (
            "C30",
            "King's Gambit Declined: Classical Variation, Rubinstein Countergambit",
        ),
        "r1bqkbnr/pppp1p2/2n4p/4p1P1/4P3/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C30",
            "King's Gambit Declined: Hobbs-Zilbermintz Gambit",
        ),
        "rnb1kbnr/ppppqppp/8/4p3/4PP2/6P1/PPPP3P/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Keene Defense",
        ),
        "rnb1kbnr/pppp1ppp/8/4p3/4PP1q/6P1/PPPP3P/RNBQKBNR b KQkq -": (
            "C30",
            "King's Gambit Declined: Keene Defense",
        ),
        "rnb1kbnr/pppp1ppp/8/4p3/4PP1q/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Keene Defense",
        ),
        "rnbqkbnr/pp1p1ppp/8/2p1p3/4PP2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Mafia Defense",
        ),
        "r1bqkbnr/pppp2pp/2n5/4pp2/4PP2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C30",
            "King's Gambit Declined: Miles Defense",
        ),
        "rnb1k1nr/pppp1ppp/8/4p3/1bB1Pq2/2N2N2/PPPP2PP/R1BQK2R b KQkq -": (
            "C30",
            "King's Gambit Declined: Norwalde Variation, Bücker Gambit",
        ),
        "rnb1kbnr/pppp1ppp/5q2/4p3/4PP2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Norwalde Variation",
        ),
        "rnb1kbnr/pppp1ppp/8/4p3/3PPq2/2N5/PPP3PP/R1BQKBNR b KQkq -": (
            "C30",
            "King's Gambit Declined: Norwalde Variation, Schubert Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/4PP2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Petrov Defense",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/4PP2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Queen's Knight Defense",
        ),
        "rnbqk1nr/pppp1p1p/8/2b1p1p1/4PP2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C30",
            "King's Gambit Declined: Senechaud Countergambit",
        ),
        "r1bqkbnr/pppp2pp/2n2p2/4P3/4P3/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Soller-Zilbermintz Gambit",
        ),
        "r1bqkbnr/pppp1p1p/2n5/4p1p1/4PP2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C30",
            "King's Gambit Declined: Zilbermintz Double Gambit",
        ),
        "rnb1kbnr/pppp2pp/8/4pP2/5P1q/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Panteldakis Countergambit, Greco Variation",
        ),
        "rnb1kbnr/ppppq2p/6P1/7Q/5p2/8/PPPP2PP/RNBK1BNR b kq -": (
            "C30",
            "King's Gambit Declined: Panteldakis Countergambit, Pawn Sacrifice Line",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/4PP2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Panteldakis Countergambit",
        ),
        "rnbqk1nr/pppp2pp/8/2b1pP2/5P2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit Declined: Panteldakis Countergambit, Schiller Defense",
        ),
        "rnbq1bnr/ppppk1pp/8/5P1Q/5p2/8/PPPP2PP/RNB1KBNR w KQ -": (
            "C30",
            "King's Gambit Declined: Panteldakis Countergambit, Shirazi Line",
        ),
        "rnbqk1nr/ppp3pp/3b4/3p1P2/3P1p2/3B1N2/PPP3PP/RNBQK2R b KQkq -": (
            "C30",
            "King's Gambit Declined: Panteldakis Countergambit, Symmetrical Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4PP2/8/PPPP2PP/RNBQKBNR b KQkq -": (
            "C30",
            "King's Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/4p1p1/4PP2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C30",
            "King's Gambit: Zilbermintz Double Countergambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/4PP2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/4PP2/2N5/PPPP2PP/R1BQKBNR b KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Milner-Barry Variation",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3P4/4pP2/2N5/PPPPQ1PP/R1B1KBNR b KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Rubinstein Variation",
        ),
        "rnbqkbnr/ppp2ppp/8/3Pp3/5P2/8/PPPP2PP/RNBQKBNR b KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit Accepted",
        ),
        "rnbqkbnr/ppp2ppp/8/1B1P4/4pP2/8/PPPP2PP/RNBQK1NR b KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Anderssen Attack",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/4PP2/5N2/PPPP2PP/RNBQKB1R b KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Blackburne Attack",
        ),
        "rnbqk2r/ppp2ppp/5n2/3P4/1b3P2/2NPp3/PPPB2PP/R2QKBNR w KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Charousek Gambit, Morphy Defense",
        ),
        "rnbqkbnr/ppp2ppp/8/3P4/4pP2/3P4/PPP3PP/RNBQKBNR b KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Charousek Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/3PPP2/8/PPP3PP/RNBQKBNR b KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Hinrichsen Gambit",
        ),
        "rnbqk1nr/ppp2ppp/8/2bPp3/5P2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Miles Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3P4/5p2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Modern Transfer",
        ),
        "rnbqkbnr/pp3ppp/2p5/3Pp3/5P2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Nimzowitsch-Marshall Countergambit",
        ),
        "rnbqk1nr/pp3ppp/2P5/2b1p3/5P2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Pickler Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3P4/4pP2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C31",
            "King's Gambit Declined: Falkbeer Countergambit, Staunton Line",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/4NP2/8/PPPP2PP/R1BQKBNR b KQkq -": (
            "C31",
            "van Geet Opening: Grünfeld Defense, Steiner Gambit",
        ),
        "rnb1k2r/ppp2ppp/8/3q4/4nP2/8/PPPNQbPP/RNBK1B1R b kq -": (
            "C32",
            "King's Gambit Declined: Falkbeer Countergambit, Alapin Variation",
        ),
        "rnbqkb1r/ppp2ppp/8/3P4/4nP2/8/PPP1Q1PP/RNB1KBNR b KQkq -": (
            "C32",
            "King's Gambit Declined: Falkbeer Countergambit, Charousek Gambit",
        ),
        "rnb1kb1r/ppp3pp/8/3q1p2/4nPP1/8/PPPNQ2P/R1B1KBNR b KQkq -": (
            "C32",
            "King's Gambit Declined: Falkbeer Countergambit, Charousek Variation",
        ),
        "rn1q1rk1/ppp2ppp/8/2bP1b2/4nPP1/5N2/PPP1Q2P/RNB1KB1R w KQ -": (
            "C32",
            "King's Gambit Declined: Falkbeer Countergambit, Tarrasch Variation",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3P4/4PP2/8/PPP3PP/RNBQKBNR b KQkq -": (
            "C32",
            "King's Gambit Declined: Falkbeer Countergambit, Charousek Gambit Accepted",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3P4/4pP2/3P4/PPPN2PP/R1BQKBNR b KQkq -": (
            "C32",
            "King's Gambit Declined: Falkbeer Countergambit, Charousek Gambit, Keres Variation",
        ),
        "rn1qk2r/ppp2ppp/8/2bP1b2/4nP2/5N2/PPP1Q1PP/RNB1KB1R w KQkq -": (
            "C32",
            "King's Gambit Declined: Falkbeer Countergambit, Charousek Gambit, Main Line",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3P4/4pP2/3P4/PPP1Q1PP/RNB1KBNR b KQkq -": (
            "C32",
            "King's Gambit Declined: Falkbeer Countergambit, Charousek Gambit, Old Line",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/8/PPPPQ1PP/RNB1KBNR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Basman Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/6p1/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Anderssen Defense",
        ),
        "rnbqkbnr/pp3ppp/2p5/3B4/4Pp2/8/PPPP2PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Anderssen Variation",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3B4/4Pp2/8/PPPP2PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Bledow Countergambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3p4/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Bledow Variation",
        ),
        "r1b1kbnr/pppp1ppp/2n5/8/2B1Pp1q/8/PPPP2PP/RNBQ1KNR w kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Boden Variation",
        ),
        "rnbqkb1r/pp1p1ppp/2p2n2/8/2B1Pp2/2N5/PPPP2PP/R1BQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Bogoljubov Defense",
        ),
        "rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/2N5/PPPP2PP/R1BQK1NR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Bogoljubov Variation",
        ),
        "rnb1k1nr/ppp2ppp/3b4/3B4/4Pp1q/8/PPPP2PP/RNBQ1KNR w kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Boren-Svenonius Variation",
        ),
        "rnb1kbnr/p1pp1ppp/8/1p6/2B1Pp1q/8/PPPP2PP/RNBQ1KNR w kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Bryan Countergambit",
        ),
        "rnb1kbnr/ppp2p1p/8/3B2p1/4Pp1q/6P1/PPPP3P/RNBQ1KNR b kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Chigorin Attack",
        ),
        "rnb1kbnr/pppp1p1p/8/6p1/2B1Pp1q/5Q2/PPPP2PP/RNB2KNR b kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Classical Defense, Cozio Attack",
        ),
        "rnb1k2r/ppppnpbp/8/6p1/2BPPp1q/2N5/PPP3PP/R1BQ1KNR w kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Classical Defense",
        ),
        "rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Cozio Defense",
        ),
        "rnb1kbnr/ppp2ppp/3p4/8/2B1Pp1q/8/PPPP2PP/RNBQ1KNR w kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Cozio Variation",
        ),
        "rnb1kb1r/pppp1ppp/5n2/8/2B1Pp1q/8/PPPP2PP/RNBQ1KNR w kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, First Jaenisch Variation",
        ),
        "rnb1k1nr/pppp1pbp/8/6p1/2B1P2q/2N2Qp1/PPPP3P/R1B2KNR b kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Fraser Variation",
        ),
        "rnbqkbnr/pppp2pp/8/5p2/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Gianutio Gambit",
        ),
        "rnb1k1nr/pppp1ppp/8/2b5/2B1Pp1q/8/PPPP2PP/RNBQ1KNR w kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Greco Variation",
        ),
        "rnb1k1nr/ppp2pbp/3p4/4P1p1/2BP1p1q/2N5/PPP3PP/R1BQ1KNR b kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Grimm Attack",
        ),
        "rnbqkbnr/p1pp1ppp/8/1p6/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Kieseritzky Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/2p5/8/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, López Defense",
        ),
        "rnb1kbnr/pppp1p1p/8/6p1/2B1Pp1q/8/PPPP2PP/RNBQ1KNR w kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, López Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Maurian Defense",
        ),
        "rnb1k1nr/pppp1pbp/8/6p1/2B1Pp1q/2N3P1/PPPP3P/R1BQ1KNR b kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, McDonnell Attack",
        ),
        "rnb1k2r/ppppnpbp/8/6p1/2BPPp1q/2N3P1/PPP4P/R1BQ1KNR b kq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, McDonnell Attack",
        ),
        "rnbqk2r/pppp1ppp/5n2/4P3/1bB2p2/2N5/PPPP2PP/R1BQK1NR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Paulsen Attack",
        ),
        "rnbqkbnr/pppp1ppp/8/8/2B1Pp2/8/PPPP2PP/RNBQK1NR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit",
        ),
        "rnbqkb1r/ppppnppp/8/8/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Bishop's Gambit, Steinitz Defense",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/5Q2/PPPP2PP/RNB1KBNR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Breyer Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/7Q/4Pp2/8/PPPP2PP/RNB1KBNR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Carrera Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4PpQ1/8/PPPP2PP/RNB1KBNR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Dodo Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/7N/PPPP2PP/RNBQKB1R b KQkq -": (
            "C33",
            "King's Gambit Accepted: Eisenberg Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/6P1/PPPP3P/RNBQKBNR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Gaga Gambit",
        ),
        "rnbk1bnr/pppp2pp/8/8/2B1pp1q/2N5/PPPPQ1PP/R1BK2NR w - -": (
            "C33",
            "King's Gambit Accepted: López-Gianutio Countergambit, Hein Variation",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/1P6/P1PP2PP/RNBQKBNR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Orsini Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/8/PPPPN1PP/RNBQKB1R b KQkq -": (
            "C33",
            "King's Gambit Accepted: Paris Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/3PPp2/8/PPP3PP/RNBQKBNR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Polerio Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/8/PPPP2PP/RNBQKBNR w KQkq -": (
            "C33",
            "King's Gambit Accepted",
        ),
        "rnbqkbnr/pppp1ppp/8/1B6/4Pp2/8/PPPP2PP/RNBQK1NR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Schurig Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/3B4/PPPP2PP/RNBQK1NR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Schurig Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp1P/8/PPPP2P1/RNBQKBNR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Stamma Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/8/PPPPB1PP/RNBQK1NR b KQkq -": (
            "C33",
            "King's Gambit Accepted: Tartakower Gambit",
        ),
        "rnbqkbnr/ppp3pp/3p4/5P2/5p2/8/PPPPB1PP/RNBQK1NR w KQkq -": (
            "C33",
            "King's Gambit Accepted: Tartakower Gambit, Weiss Defense",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/8/PPPP1KPP/RNBQ1BNR b kq -": (
            "C33",
            "King's Gambit Accepted: Tumbleweed",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/2N5/PPPP2PP/R1BQKBNR b KQkq -": (
            "C33",
            "van Geet Opening: Nowokunski Gambit",
        ),
        "rnbqkbnr/pppp1pp1/7p/8/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C34",
            "King's Gambit Accepted: Becker Defense",
        ),
        "rnbqkb1r/ppppnppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C34",
            "King's Gambit Accepted: Bonsch-Osmolovsky Variation",
        ),
        "rnbqkbnr/ppp2ppp/3p4/8/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C34",
            "King's Gambit Accepted: Fischer Defense",
        ),
        "rnbqkbnr/ppp2ppp/3p4/8/1P2Pp2/5N2/P1PP2PP/RNBQKB1R b KQkq -": (
            "C34",
            "King's Gambit Accepted: Fischer Defense, Schulder Gambit",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/8/3PPp2/3B1N2/PPP3PP/RNBQK2R b KQkq -": (
            "C34",
            "King's Gambit Accepted: Fischer Defense, Spanish Variation",
        ),
        "rnbqkbnr/pppp2pp/8/5p2/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C34",
            "King's Gambit Accepted: Gianutio Countergambit",
        ),
        "rnbqk1nr/ppp2pb1/3p3p/6p1/2BPPp1P/5N2/PPP3P1/RNBQK2R w KQkq -": (
            "C34",
            "King's Gambit Accepted: Greco Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/6p1/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C34",
            "King's Gambit Accepted: King's Knight Gambit",
        ),
        "rnbqkbnr/pppp1ppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R b KQkq -": (
            "C34",
            "King's Gambit Accepted: King's Knight Gambit",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C34",
            "King's Gambit Accepted: MacLeod Defense",
        ),
        "rnbqkb1r/pppp1ppp/5n2/8/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C34",
            "King's Gambit Accepted: Schallopp Defense",
        ),
        "rnbqkb1r/pppp1ppp/8/4P2n/5pP1/5N2/PPPP3P/RNBQKB1R b KQkq g3": (
            "C34",
            "King's Gambit Accepted: Schallopp Defense, Tashkent Attack",
        ),
        "rnbqk1nr/pppp1ppp/8/8/2B1Pp1b/5NP1/PPPP3P/RNBQK2R b KQkq -": (
            "C35",
            "King's Gambit Accepted: Cunningham Defense, Bertin Gambit",
        ),
        "rnbqk1nr/pppp1ppp/8/8/2B1P2b/5N2/PPPP3p/RNBQ1R1K b kq -": (
            "C35",
            "King's Gambit Accepted: Cunningham Defense, Bertin Gambit",
        ),
        "rnbqk2r/ppppbppp/5n2/8/2B1Pp2/5N2/PPPP2PP/RNBQK2R w KQkq -": (
            "C35",
            "King's Gambit Accepted: Cunningham Defense, McCormick Defense",
        ),
        "rnbqk1nr/ppppbppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C35",
            "King's Gambit Accepted: Cunningham Defense",
        ),
        "rnbqkb1r/p4ppp/2p5/3n4/2B2p2/5N2/PPPP2PP/RNBQK2R w KQkq -": (
            "C36",
            "King's Gambit Accepted: Abbazia Defense, Main Line",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3P4/5p2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C36",
            "King's Gambit Accepted: Abbazia Defense",
        ),
        "rnbqkbnr/ppp2ppp/8/3p4/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq -": (
            "C36",
            "King's Gambit Accepted: Modern Defense",
        ),
        "rnbqkbnr/ppp2ppp/8/3P4/5p2/5N2/PPPP2PP/RNBQKB1R b KQkq -": (
            "C36",
            "King's Gambit Accepted: Modern Defense",
        ),
        "rnbqkbnr/pppp1p1p/8/8/2B1PppP/5N2/PPPP2P1/RNBQK2R b KQkq h3": (
            "C37",
            "King's Gambit Accepted: Australian Gambit",
        ),
        "r1bqkbnr/pppp1p1p/2n5/6p1/2B1Pp2/5N2/PPPP2PP/RNBQK2R w KQkq -": (
            "C37",
            "King's Gambit Accepted: Blachly Gambit",
        ),
        "rnb1kbnr/pppp1p1p/8/3N4/2q1Pp2/5Q2/PPPP2PP/R1B2R1K b kq -": (
            "C37",
            "King's Gambit Accepted: Double Muzio Gambit, Baldwin Gambit",
        ),
        "rnb1kbnr/pppp1p1p/5q2/8/2B1Pp2/2N2Q2/PPPP2PP/R1B2RK1 b kq -": (
            "C37",
            "King's Gambit Accepted: Double Muzio Gambit, Bello Gambit",
        ),
        "r1b1k2r/ppppnp1p/2n4b/4q3/2B2p2/2NP1Q2/PPPB2PP/4RRK1 b kq -": (
            "C37",
            "King's Gambit Accepted: Double Muzio Gambit, Paulsen Defense",
        ),
        "rnb1kbnr/pppp1B1p/8/4q3/5p2/5Q2/PPPP2PP/RNB2RK1 b kq -": (
            "C37",
            "King's Gambit Accepted: Double Muzio Gambit",
        ),
        "rnb2bnr/pppp1k1p/5q2/8/4P3/2N1pQ2/PPP3PP/R4RK1 w - -": (
            "C37",
            "King's Gambit Accepted: Double Muzio Gambit, Young Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/8/2BPPp2/5Q2/PPP3PP/RNB1K2R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Ghulam-Kassim Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/8/2BPPpp1/5N2/PPP3PP/RNBQK2R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Ghulam-Kassim Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/6p1/2B1Pp2/5N2/PPPP2PP/RNBQK2R b KQkq -": (
            "C37",
            "King's Gambit Accepted: King's Knight Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/8/2BPPB2/5p2/PPP3PP/RN1QK2R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Kotov Gambit",
        ),
        "rnbqkbnr/pppp1B1p/8/8/4Ppp1/5N2/PPPP2PP/RNBQK2R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Lolli Gambit",
        ),
        "rnb2bnr/pppp1k1p/5q2/8/4Pp2/2N1BQ2/PPP3PP/R4RK1 b - -": (
            "C37",
            "King's Gambit Accepted: Lolli Gambit, Young Variation",
        ),
        "rnbqkbnr/pppp1p1p/8/8/2B1Ppp1/2N2N2/PPPP2PP/R1BQK2R b KQkq -": (
            "C37",
            "King's Gambit Accepted: McDonnell Gambit",
        ),
        "rn1qkbnr/ppp2p2/3p4/6p1/2B1Ppp1/5N2/PPPP2P1/RNBQ1RK1 w kq -": (
            "C37",
            "King's Gambit Accepted: Middleton Countergambit",
        ),
        "rnb1kbnr/ppppqp1p/8/8/2B1Pp2/5Q2/PPPP2PP/RNB2RK1 w kq -": (
            "C37",
            "King's Gambit Accepted: Muzio Gambit Accepted, From Defense",
        ),
        "rnbqkbnr/ppp2p1p/8/3p4/2B1Ppp1/5N2/PPPP2PP/RNBQ1RK1 w kq -": (
            "C37",
            "King's Gambit Accepted: Muzio Gambit, Brentano Defense",
        ),
        "r1bqkbnr/pppp1p1p/2n5/8/2B1Pp2/5Q2/PPPP2PP/RNB2RK1 w kq -": (
            "C37",
            "King's Gambit Accepted: Muzio Gambit, Holloway Defense",
        ),
        "rnb1kbnr/ppppqp1p/8/8/2B1Ppp1/5N2/PPPP2PP/RNBQ1RK1 w kq -": (
            "C37",
            "King's Gambit Accepted: Muzio Gambit, Kling and Horwitz Counterattack",
        ),
        "rnb1kbnr/pppp1p1p/5q2/8/2B1Pp2/5Q2/PPPP2PP/RNB2RK1 w kq -": (
            "C37",
            "King's Gambit Accepted: Muzio Gambit, Sarratt Defense",
        ),
        "rnbqkbnr/pppp1p1p/8/8/2B1Ppp1/5N2/PPPP2PP/RNBQ1RK1 b kq -": (
            "C37",
            "King's Gambit Accepted: Muzio Gambit, Wild Muzio Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/6p1/4Pp2/2N2N2/PPPP2PP/R1BQKB1R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Quade Gambit",
        ),
        "rnb1kbnr/pppp1p1p/8/4N3/3PPppq/6P1/PPP4P/RNBQKB1R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Rosentreter Gambit, Bird Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/6p1/3PPp2/5N2/PPP3PP/RNBQKB1R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Rosentreter Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/8/3PPpp1/2N2N2/PPP3PP/R1BQKB1R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Rosentreter Gambit, Sörensen Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/8/3PPBp1/5N2/PPP3PP/RN1QKB1R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Rosentreter Gambit, Testa Variation",
        ),
        "rnb1kb1r/ppp2p1p/3p3n/4N3/2BPPppq/8/PPP3PP/RNBQ1K1R w kq -": (
            "C37",
            "King's Gambit Accepted: Salvio Gambit, Anderssen Counterattack",
        ),
        "rnb1kbnr/pppp1p1p/8/4N3/2B1P1pq/5p2/PPPP2PP/RNBQ1K1R w kq -": (
            "C37",
            "King's Gambit Accepted: Salvio Gambit, Cochrane Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/4N3/2B1Ppp1/8/PPPP2PP/RNBQK2R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Salvio Gambit",
        ),
        "rnb1kb1r/pppp1p1p/5n2/4N3/2B1Pppq/8/PPPP2PP/RNBQ1K1R w kq -": (
            "C37",
            "King's Gambit Accepted: Salvio Gambit, Santa Maria Defense",
        ),
        "rnb1kb1r/pppp1p1p/7n/4N3/2B1Pppq/8/PPPP2PP/RNBQ1K1R w kq -": (
            "C37",
            "King's Gambit Accepted: Salvio Gambit, Silberschmidt Defense",
        ),
        "r1b1kbnr/pppp1p1p/2n5/4N3/2B1Pppq/8/PPPP2PP/RNBQ1K1R w kq -": (
            "C37",
            "King's Gambit Accepted: Salvio Gambit, Viennese Variation",
        ),
        "rnb1kb1r/pppp1p1p/7n/4N3/2BPP1pq/5p2/PPP3PP/RNBQ1K1R w kq -": (
            "C37",
            "King's Gambit Accepted: Silberschmidt Gambit",
        ),
        "rnbqkbnr/pppp1p1p/8/4N3/3PPpp1/8/PPP3PP/RNBQKB1R b KQkq -": (
            "C37",
            "King's Gambit Accepted: Sörensen Gambit",
        ),
        "rnbqk1nb/pp3p2/2pp4/4N1p1/2BPPp2/2N5/PPP3P1/R1BQK3 b Qq -": (
            "C38",
            "King's Gambit Accepted: Greco Gambit",
        ),
        "rnbqk1nr/pppp1pbp/8/6p1/2B1Pp2/5N2/PPPP2PP/RNBQ1RK1 b kq -": (
            "C38",
            "King's Gambit Accepted: Hanstein Gambit",
        ),
        "rnbqk1nr/ppp2pbp/3p4/6p1/2BPPp2/2P2N2/PP4PP/RNBQK2R b KQkq -": (
            "C38",
            "King's Gambit Accepted: Mayet Gambit",
        ),
        "rnbqk1nr/pppp1pbp/8/6p1/2B1Pp1P/5N2/PPPP2P1/RNBQK2R b KQkq -": (
            "C38",
            "King's Gambit Accepted: Philidor Gambit",
        ),
        "rnbqk1nr/ppp2pb1/3p3p/6p1/2BPPp1P/3Q1N2/PPP3P1/RNB1K2R b KQkq -": (
            "C38",
            "King's Gambit Accepted: Philidor Gambit, Schultz Variation",
        ),
        "rnbqk1nr/pppp1pbp/8/6p1/2B1Pp2/5N2/PPPP2PP/RNBQK2R w KQkq -": (
            "C38",
            "King's Gambit Accepted: Traditional Variation",
        ),
        "rnbq1bnr/pppp1k2/7p/8/4PppP/2N5/PPPP2P1/R1BQKB1R b KQ -": (
            "C39",
            "King's Gambit Accepted: Allgaier Gambit, Blackburne Gambit",
        ),
        "rnbq1bnr/ppp3k1/7p/4B3/2BPp1pP/8/PPP3P1/RN1QK2R b KQ -": (
            "C39",
            "King's Gambit Accepted: Allgaier Gambit, Cook Variation",
        ),
        "rnbqkbnr/pppp1p1p/8/6N1/4PppP/8/PPPP2P1/RNBQKB1R b KQkq -": (
            "C39",
            "King's Gambit Accepted: Allgaier Gambit",
        ),
        "rnbq1bnr/pppp1k2/7p/8/3PPppP/8/PPP3P1/RNBQKB1R b KQ -": (
            "C39",
            "King's Gambit Accepted: Allgaier Gambit, Thorold Attack",
        ),
        "rnbq1bnr/pppp1k2/7p/8/2B1PppP/8/PPPP2P1/RNBQK2R b KQ -": (
            "C39",
            "King's Gambit Accepted: Allgaier Gambit, Urusov Attack",
        ),
        "rnbq3r/pppp1k2/3b1n1p/8/4PQ1P/8/PPPP2P1/RNB1KB1R w KQ -": (
            "C39",
            "King's Gambit Accepted: Allgaier Gambit, Horny Defense",
        ),
        "rnbqkb1r/pppp1p1p/5n2/6N1/4PppP/8/PPPP2P1/RNBQKB1R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Allgaier Gambit, Schlechter Defense",
        ),
        "rnbq1bnr/ppp3k1/7p/3B4/3PPppP/8/PPP3P1/RNBQK2R b KQ -": (
            "C39",
            "King's Gambit Accepted: Allgaier Gambit, Urusov Attack",
        ),
        "rnbqk2r/ppp2p1p/3b4/3PN3/2BP1npP/8/PPP3P1/RN1QK2R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Anderssen-Cordel Gambit",
        ),
        "rnbqk2r/ppp2p1p/3b1n2/3PN3/2B2ppP/8/PPPP2P1/RNBQK2R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Anderssen Defense",
        ),
        "rnbqkb1r/ppp2p1p/5n2/3p4/4PpNP/8/PPPP2P1/RNBQKB1R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Berlin Defense, de Riviere Variation",
        ),
        "rnbqkb1r/pppp1p1p/5n2/4N3/3PPppP/8/PPP3P1/RNBQKB1R b KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Berlin Defense, Rubinstein Variation",
        ),
        "rnbqkb1r/pppp1p1p/5n2/4N3/4PppP/8/PPPP2P1/RNBQKB1R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Berlin Defense",
        ),
        "rnbqkb1r/ppp2p1p/8/3pN3/3PnBpP/8/PPPN2P1/R2QKB1R b KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Brentano Defense, Caro Variation",
        ),
        "rnb1k2r/ppp2p1p/5n2/3qN3/1b1P1ppP/2N5/PPP2KP1/R1BQ1B1R b kq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Brentano Defense, Kaplanek Variation",
        ),
        "rnbqkb1r/ppp2p1p/5n2/3pN3/3PPBpP/8/PPP3P1/RN1QKB1R b KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Brentano Defense",
        ),
        "rnbqkbnr/ppp2p1p/8/3pN3/4PppP/8/PPPP2P1/RNBQKB1R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Brentano Defense",
        ),
        "rnbqkbnr/pppp1N2/7p/8/4PppP/8/PPPP2P1/RNBQKB1R b KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Cotter Gambit",
        ),
        "rnbqkbnr/ppp2p1p/3p4/4N3/4PppP/8/PPPP2P1/RNBQKB1R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Kolisch Defense",
        ),
        "rnbqkbnr/pppp1p2/8/4N2p/4PppP/8/PPPP2P1/RNBQKB1R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Long Whip Defense",
        ),
        "r1bqkbnr/pppp1p1p/2n5/4N3/4PppP/8/PPPP2P1/RNBQKB1R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Neumann Defense",
        ),
        "rnbqk2r/ppp2pbp/5n2/3PN3/2B2ppP/8/PPPP2P1/RNBQK2R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Deferred Paulsen Defense",
        ),
        "rnbqk1nr/pppp1pbp/8/4N3/4PppP/8/PPPP2P1/RNBQKB1R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Paulsen Defense",
        ),
        "rnbqk2r/ppp2p1p/5n2/3Pb3/2B2ppP/8/PPPP2P1/RNBQ1RK1 w kq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Rice Gambit",
        ),
        "rnb1kbnr/ppppqp1p/8/4N3/4PppP/8/PPPP2P1/RNBQKB1R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Rosenthal Defense",
        ),
        "rnbqkbnr/pppp1p1p/8/4N3/4PppP/8/PPPP2P1/RNBQKB1R b KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit",
        ),
        "rnbqk1n1/pppp1p1r/7b/4N2p/2BPPppP/2N5/PPP3P1/R1BQK2R b KQq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Long Whip Defense, Jaenisch Variation",
        ),
        "rnbqk1nr/ppppbp1p/8/4N3/4PppP/8/PPPP2P1/RNBQKB1R w KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Polerio Defense",
        ),
        "rnbqk2r/ppp2p1p/3b1n2/3PN3/2B2ppP/8/PPPP2P1/RNBQ1RK1 b kq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Rice Gambit",
        ),
        "rnb1kbnr/ppppq2p/8/4Np2/2BPPppP/8/PPP3P1/RNBQK2R b KQkq -": (
            "C39",
            "King's Gambit Accepted: Kieseritzky Gambit, Salvio Defense, Cozio Variation",
        ),
        "rnbqkbnr/pppp1p1p/8/6p1/4Pp1P/5N2/PPPP2P1/RNBQKB1R b KQkq -": (
            "C39",
            "King's Gambit Accepted: King's Knight Gambit",
        ),
        "rnbqk1nr/ppp2ppp/3b4/3Pp3/8/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "Elephant Gambit: Maróczy Gambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3P4/4p3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "Elephant Gambit: Paulsen Countergambit",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "Elephant Gambit",
        ),
        "rnb1kbnr/ppp2ppp/8/4N1q1/2B1p3/8/PPPP1PPP/RNBQK2R w KQkq -": (
            "C40",
            "Elephant Gambit: Wasp Variation",
        ),
        "rnb1kbnr/ppppqppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "Gunderam Defense",
        ),
        "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C40",
            "King's Knight Opening",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b1N3/4P3/8/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "King's Pawn Game: Busch-Gass Gambit, Chiodini Gambit",
        ),
        "rnbqk1nr/pppp1ppp/8/2b1p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "King's Pawn Game: Busch-Gass Gambit",
        ),
        "rnb1kbnr/ppp1q1pp/5p2/3p4/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "King's Pawn Game: Damiano Defense, Damiano Gambit, Chigorin Gambit",
        ),
        "rnb1kbnQ/ppppq2p/6p1/8/4P3/8/PPPP1PPP/RNB1KB1R b KQq -": (
            "C40",
            "King's Pawn Game: Damiano Defense, Damiano Gambit",
        ),
        "rnbqkbnr/pppp2pp/5p2/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "King's Pawn Game: Damiano Defense",
        ),
        "rnb1kbnr/ppppq1pp/8/4pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C40",
            "King's Pawn Game: Gunderam Defense, Gunderam Gambit",
        ),
        "rnbqkbnr/pp1p1ppp/2p5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "King's Pawn Game: Gunderam Gambit",
        ),
        "rnb1kbnr/pppp1ppp/6q1/4p3/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 b kq -": (
            "C40",
            "King's Pawn Game: La Bourdonnais Gambit",
        ),
        "rnb1kbnr/pppp1ppp/5q2/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "King's Pawn Game: McConnell Defense",
        ),
        "rnb1kbnr/ppp3pp/3p1q2/5p2/2NPP3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit Accepted: Bilguer Variation",
        ),
        "rnb1kbnr/ppp3pp/3p1q2/8/2NPp3/8/PPP1BPPP/RNBQK2R b KQkq -": (
            "C40",
            "Latvian Gambit Accepted: Bronstein Attack",
        ),
        "rnb1kbnr/ppp4p/3p1qp1/8/2NPp3/8/PPP1QPPP/RNB1KB1R b KQkq -": (
            "C40",
            "Latvian Gambit Accepted: Bronstein Gambit",
        ),
        "rnb1kbnr/pppp2pp/5q2/5p2/2N1P3/8/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit Accepted: Foltys-Leonhardt Variation",
        ),
        "rnb1kbnr/pppp2pp/5q2/8/2N1p3/3P4/PPP2PPP/RNBQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit Accepted: Foltys Variation",
        ),
        "rnb1kbnr/pppp2pp/5q2/8/2N1p3/2N5/PPPP1PPP/R1BQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit Accepted: Leonhardt Variation",
        ),
        "rnb1kbnr/pppp2pp/5q2/4Np2/3PP3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit Accepted: Main Line",
        ),
        "rnb1kbnr/ppp3pp/3p1q2/8/3Pp3/4N3/PPP2PPP/RNBQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit Accepted: Nimzowitsch Attack",
        ),
        "rnbqkbnr/pppp2pp/8/4pP2/8/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit Accepted",
        ),
        "rnb1kb1N/ppp3pp/5n2/3p4/2B1p3/8/PPPP1PqP/RNBQKR2 w Qq -": (
            "C40",
            "Latvian Gambit: Behting Variation",
        ),
        "rnbqkb1r/pppp2pp/5n2/4N3/2B1p3/8/PPPP1PPP/RNBQK2R w KQkq -": (
            "C40",
            "Latvian Gambit: Corkscrew Countergambit",
        ),
        "rnb1kb1N/ppp1q1pp/5n2/3p4/2B1p3/8/PPPP1PPP/RNBQK2R w KQq -": (
            "C40",
            "Latvian Gambit: Corkscrew Gambit",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/2P1P3/5N2/PP1P1PPP/RNBQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit: Diepstraten Countergambit",
        ),
        "r1bqkbnr/pppp2pp/2n5/4Np2/4P3/8/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "Latvian Gambit: Fraser Defense",
        ),
        "rnb1kbnr/ppppq1pp/8/4Np2/4P3/8/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "Latvian Gambit: Greco Variation",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/4P1P1/5N2/PPPP1P1P/RNBQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit: Lobster Gambit",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit: Mason Countergambit",
        ),
        "rnbqkb1r/pppp2pp/5n2/4pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C40",
            "Latvian Gambit: Mayet Attack, Morgado Defense",
        ),
        "rnb1kbnr/pppp2pp/8/4N3/2BPp3/8/PPP2PqP/RNBQK2R w KQkq -": (
            "C40",
            "Latvian Gambit: Mayet Attack, Poisoned Pawn Variation",
        ),
        "rnbqkbnr/ppp3pp/8/3pN3/2B1p3/8/PPPP1PPP/RNBQK2R w KQkq -": (
            "C40",
            "Latvian Gambit: Mayet Attack, Polerio-Svedenborg Variation",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C40",
            "Latvian Gambit: Mayet Attack",
        ),
        "rnbqkbnr/p1pp2pp/8/1p2pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C40",
            "Latvian Gambit: Mayet Attack, Strautins Gambit",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/4P3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit: Mlotkowski Variation",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C40",
            "Latvian Gambit",
        ),
        "rnbqkbnr/pppp2pp/8/4pp2/1P2P3/5N2/P1PP1PPP/RNBQKB1R b KQkq -": (
            "C40",
            "Latvian Gambit: Senechaud Gambit",
        ),
        "r2qkbnr/pppn1ppp/3p4/4P3/4P1b1/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C41",
            "Philidor Defense: Alapin-Blackburne Gambit",
        ),
        "r2q1rk1/pp2bppp/2npbn2/2p3B1/4P3/2N2N2/PPP1BPPP/R2QR1K1 b - -": (
            "C41",
            "Philidor Defense: Berger Variation",
        ),
        "rnbqkbnr/ppp2ppp/3p4/8/3pP3/2P2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "C41",
            "Philidor Defense: Bird Gambit",
        ),
        "rn1qkbnr/pppb1ppp/3p4/8/3QP3/5N2/PPP2PPP/RNB1KB1R w KQkq -": (
            "C41",
            "Philidor Defense: Boden Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "C41",
            "Philidor Defense: Exchange Variation",
        ),
        "rnbqkbnr/ppp2ppp/3p4/8/3NP3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C41",
            "Philidor Defense: Exchange Variation",
        ),
        "rnbqkbnr/ppp2ppp/3p4/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C41",
            "Philidor Defense: Exchange Variation",
        ),
        "r1bq1rk1/pp1nbppp/2p4n/3pp1N1/2BPPP2/2P5/PP4PP/RNBQ1RK1 w - -": (
            "C41",
            "Philidor Defense: Hanham, Berger Variation",
        ),
        "r1bqkbnr/pp1n1ppp/2pp4/4p1N1/2BPP3/8/PPP2PPP/RNBQK2R b KQkq -": (
            "C41",
            "Philidor Defense: Hanham, Kmoch Variation",
        ),
        "r1bqkbnr/pp1n1ppp/2pp4/4p3/2BPP3/2P2N2/PP3PPP/RNBQK2R b KQkq -": (
            "C41",
            "Philidor Defense: Hanham Variation, Delmar Variation",
        ),
        "r1bqkbnr/pp1n1ppp/2pp4/4p3/2BPP3/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C41",
            "Philidor Defense: Hanham Variation, Krause Variation",
        ),
        "r1bqkbnr/pppn1ppp/3p4/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C41",
            "Philidor Defense: Hanham Variation",
        ),
        "r1bqkbnr/pp1n1ppp/2pp4/4p3/2BPP3/2N2N2/PPP2PPP/R1BQK2R b KQkq -": (
            "C41",
            "Philidor Defense: Hanham Variation, Schlechter Variation",
        ),
        "r1bqkbnr/ppp2ppp/1n1p4/4p3/2BPP3/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C41",
            "Philidor Defense: Hanham Variation, Sharp Variation",
        ),
        "r1bqk1nr/pp1nbppp/2pp4/4P3/2B1P3/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C41",
            "Philidor Defense: Hanham Variation, Steiner Variation",
        ),
        "rnbqkbnr/ppp2p1p/3p2p1/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "C41",
            "Philidor Defense: Larsen Variation",
        ),
        "r1bqk2r/pppnbBpp/3p1n2/4p3/3PP3/2N2N2/PPP2PPP/R1BQK2R b KQkq -": (
            "C41",
            "Philidor Defense: Lion Variation, Bishop's Sacrifice Variation",
        ),
        "r1bqk2r/pppnbBpp/5n2/4p3/4P3/2N2N2/PPP2PPP/R1BQK2R b KQkq -": (
            "C41",
            "Philidor Defense: Lion Variation, Delayed Bishop's Sacrifice Variation",
        ),
        "r1bq2k1/pppnbrpp/3pNn2/4p3/3PP3/2N5/PPP2PPP/R1BQK2R b KQ -": (
            "C41",
            "Philidor Defense: Lion Variation, Forcing Line",
        ),
        "r1bqk2r/pppnbpp1/3p1n1p/4p3/2BPP3/2N2N2/PPP2PPP/R1BQ1RK1 w kq -": (
            "C41",
            "Philidor Defense: Lion Variation, Lion's Claw Variation",
        ),
        "r1bqkb1r/pppn1ppp/3p1n2/4p3/3PP3/2N2N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "C41",
            "Philidor Defense: Lion Variation",
        ),
        "r1bqkb1r/pppn1ppp/3p1n2/4p3/3PP1P1/2N2N2/PPP2P1P/R1BQKB1R b KQkq -": (
            "C41",
            "Philidor Defense: Lion Variation, Shirov Gambit",
        ),
        "r1bq1rk1/pp1nbppp/2pp1n2/8/P1BpP3/2N2N2/1PP1QPPP/R1B2RK1 w - -": (
            "C41",
            "Philidor Defense: Lion Variation, Sozin Variation",
        ),
        "rnbqkb1r/ppp3pN/3p3n/5p2/2BpP3/8/PPP2PPP/RNBQK2R b KQkq -": (
            "C41",
            "Philidor Defense: López Countergambit, Jaenisch Variation",
        ),
        "rnbqkbnr/ppp3pp/3p4/4pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C41",
            "Philidor Defense: López Countergambit",
        ),
        "rnbqkbnr/ppp2ppp/3p4/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C41",
            "Philidor Defense: Morphy Gambit",
        ),
        "r1bq1rk1/pppnbBpp/3p1n2/4p1N1/3PP3/2N5/PPP2PPP/R1BQK2R b KQ -": (
            "C41",
            "Philidor Defense: Nimzowitsch Variation, Lärobok Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/4p1N1/3PP3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C41",
            "Philidor Defense: Nimzowitsch Variation, Locock Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/4p3/2BPP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C41",
            "Philidor Defense: Nimzowitsch Variation, Klein Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p4/3QP3/4n3/5N2/PPP2PPP/RNB1KB1R b KQkq -": (
            "C41",
            "Philidor Defense: Nimzowitsch Variation, Rellstab Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C41",
            "Philidor Defense: Nimzowitsch Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/4P3/4P3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C41",
            "Philidor Defense: Nimzowitsch Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p4/4P3/4n3/5N2/PPPN1PPP/R1BQKB1R b KQkq -": (
            "C41",
            "Philidor Defense: Nimzowitsch Variation, Sokolsky Variation",
        ),
        "rnbqkbnr/ppp2ppp/8/3P4/3N4/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C41",
            "Philidor Defense: Paulsen Attack",
        ),
        "rnbqk1nr/ppp3pp/4P3/2bp2N1/4p3/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "C41",
            "Philidor Defense: Philidor Countergambit, Berger Variation",
        ),
        "rnbqkbnr/ppp3pp/4P3/3p2N1/4p3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C41",
            "Philidor Defense: Philidor Countergambit, del Rio Attack",
        ),
        "rnbqkbnr/ppp3pp/3p4/4pp2/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C41",
            "Philidor Defense: Philidor Countergambit",
        ),
        "rnbqkbnr/ppp3pp/3p4/4pp2/3PP3/2N2N2/PPP2PPP/R1BQKB1R b KQkq -": (
            "C41",
            "Philidor Defense: Philidor Countergambit, Zukertort Variation",
        ),
        "rn1qkbnr/pppb1ppp/3p4/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C41",
            "Philidor Defense: Philidor Gambit",
        ),
        "rnbqk1nr/ppp1bppp/3p4/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C41",
            "Philidor Defense",
        ),
        "rnbqkbnr/ppp2ppp/3p4/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C41",
            "Philidor Defense",
        ),
        "rnbqkbnr/ppp2ppp/3p4/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C41",
            "Philidor Defense",
        ),
        "rnbqkbnr/ppp2ppp/3p4/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C41",
            "Philidor Defense",
        ),
        "rnbqk1nr/ppp1bppp/3p4/4p3/2B1P3/2P2N2/PP1P1PPP/RNBQK2R b KQkq -": (
            "C41",
            "Philidor Defense: Steinitz Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/4N3/4P3/8/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C42",
            "Russian Game",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/8/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C42",
            "Russian Game",
        ),
        "rnbqkb1r/ppp2ppp/3p4/8/4n3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C42",
            "Russian Game",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4N3/4P3/8/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C42",
            "Russian Game",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C42",
            "Russian Game",
        ),
        "r2qk2r/ppp1b1pp/2n5/3p1p2/3Pn1b1/2PB1N2/PP1N1PPP/R1BQR1K1 b kq -": (
            "C42",
            "Russian Game: Classical Attack, Berger Variation",
        ),
        "r1bqk2r/ppp1bppp/8/3P4/1n1Pn3/3B1N2/PP3PPP/RNBQ1RK1 b kq -": (
            "C42",
            "Russian Game: Classical Attack, Chigorin Variation, Browne Attack",
        ),
        "r1bqk2r/ppp1bppp/8/3p4/1nPPn3/5N2/PP2BPPP/RNBQ1RK1 b kq -": (
            "C42",
            "Russian Game: Classical Attack, Chigorin Variation, Main Line",
        ),
        "r1bqk2r/ppp1bppp/2n5/3p4/3Pn3/3B1N2/PPP2PPP/RNBQR1K1 b kq -": (
            "C42",
            "Russian Game: Classical Attack, Chigorin Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/8/3P4/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C42",
            "Russian Game: Classical Attack, Closed Variation",
        ),
        "r1bqk2r/ppp1bppp/2n5/3p4/2PPn3/3B1N2/PP3PPP/RNBQ1RK1 b kq -": (
            "C42",
            "Russian Game: Classical Attack, Jaenisch Variation",
        ),
        "r2qk2r/ppp1b1pp/2n5/3p1p2/2PPn1b1/3B1N2/PP3PPP/RNBQR1K1 b kq -": (
            "C42",
            "Russian Game: Classical Attack, Krause Variation",
        ),
        "r2qk2r/ppp3pp/2n5/3p1p2/2PPn1bb/3B1N2/PP3PPP/RNBQR1K1 w kq -": (
            "C42",
            "Russian Game: Classical Attack, Maróczy Variation",
        ),
        "rn1q1rk1/ppp3pp/8/3P1p2/3Pn1b1/3B1N2/PP3PPb/RNBQR1K1 w - -": (
            "C42",
            "Russian Game: Classical Attack, Marshall Trap",
        ),
        "rn1q1rk1/pp3ppp/2pb4/3p4/2PPn1b1/3B1N2/PP3PPP/RNBQR1K1 w - -": (
            "C42",
            "Russian Game: Classical Attack, Marshall Variation, Chinese Gambit",
        ),
        "rnbqk2r/ppp2ppp/3b4/3p4/3Pn3/3B1N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C42",
            "Russian Game: Classical Attack, Marshall Variation",
        ),
        "r1bqkb1r/ppp2ppp/2n5/3p4/3Pn3/3B1N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C42",
            "Russian Game: Classical Attack, Mason-Showalter Variation",
        ),
        "rnbq1rk1/ppp1bppp/8/3p4/3Pn3/3B1N2/PPP2PPP/RNBQ1RK1 w - -": (
            "C42",
            "Russian Game: Classical Attack, Mason Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p4/8/3Pn3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C42",
            "Russian Game: Classical Attack",
        ),
        "rnbq1rk1/pp3ppp/2pb4/3p4/2PPn3/3B1N2/PP3PPP/RNBQ1RK1 w - -": (
            "C42",
            "Russian Game: Classical Attack, Staunton Variation",
        ),
        "rn1q1rk1/ppp2ppp/3b4/3p4/2PPn1b1/3B1N2/PP3PPP/RNBQ1RK1 w - -": (
            "C42",
            "Russian Game: Classical Attack, Tarrasch Variation",
        ),
        "rnbq1b1r/ppp2kpp/3p1n2/8/2B1P3/8/PPPP1PPP/RNBQK2R b KQ -": (
            "C42",
            "Russian Game: Cochrane Gambit, Bishop's Check Line",
        ),
        "rnbq1b1r/ppp2kpp/3p1n2/8/3PP3/8/PPP2PPP/RNBQKB1R b KQ -": (
            "C42",
            "Russian Game: Cochrane Gambit, Center Variation",
        ),
        "rnbqkb1r/ppp2Npp/3p1n2/8/4P3/8/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C42",
            "Russian Game: Cochrane Gambit",
        ),
        "rnbqkb1r/ppp2ppp/3p4/8/4n3/5N2/PPPPQPPP/RNB1KB1R b KQkq -": (
            "C42",
            "Russian Game: Cozio (Lasker) Attack",
        ),
        "rnb1kb1r/ppppqppp/8/4N3/4n3/8/PPPPQPPP/RNB1KB1R w KQkq -": (
            "C42",
            "Russian Game: Damiano Variation, Kholmov Gambit",
        ),
        "rnbqkb1r/pppp1ppp/8/4N3/4n3/8/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C42",
            "Russian Game: Damiano Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p4/8/4n3/3P1N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C42",
            "Russian Game: French Attack",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C42",
            "Russian Game: Italian Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/8/4P3/3N4/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C42",
            "Russian Game: Karklins-Martinovsky Variation",
        ),
        "rnbqkb1r/ppp2ppp/3p4/8/2P1n3/5N2/PP1P1PPP/RNBQKB1R b KQkq -": (
            "C42",
            "Russian Game: Kaufmann Attack",
        ),
        "rnbqkb1r/ppp2ppp/3p4/8/4n3/3B1N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C42",
            "Russian Game: Millennium Attack",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/3PP3/5N2/PPP1QPPP/RNB1KB1R b KQkq -": (
            "C42",
            "Russian Game: Moody Gambit",
        ),
        "rnbqkb1r/ppp2ppp/3p4/8/4n3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq -": (
            "C42",
            "Russian Game: Nimzowitsch Attack",
        ),
        "rnbqkb1r/ppp2ppp/3p1n2/8/2N1P3/8/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C42",
            "Russian Game: Paulsen Attack",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4N3/4P3/8/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C42",
            "Russian Game: Stafford Gambit",
        ),
        "r1bqkb1r/ppp2ppp/2p2n2/8/4P3/8/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C42",
            "Russian Game: Stafford Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq -": (
            "C42",
            "Russian Game: Three Knights Game",
        ),
        "rnbqkb1r/pppp1ppp/8/8/2BQn3/5N2/PPP2PPP/RNB1K2R b KQkq -": (
            "C43",
            "Bishop's Opening: Urusov Gambit, Keidansky Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C43",
            "Bishop's Opening: Urusov Gambit",
        ),
        "rnbqkb1r/pppp1ppp/5n2/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C43",
            "Russian Game: Modern Attack",
        ),
        "r1bqkb1r/pppp1ppp/2n5/2n1P3/3N4/8/PPP1QPPP/RNB1KB1R w KQkq -": (
            "C43",
            "Russian Game: Modern Attack, Bardeleben Variation",
        ),
        "rnbqkb1r/pppp1ppp/8/4P3/3Qn3/5N2/PPP2PPP/RNB1KB1R b KQkq -": (
            "C43",
            "Russian Game: Modern Attack, Center Attack",
        ),
        "rnbqkb1r/pppp1ppp/8/4p3/3Pn3/3B1N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C43",
            "Russian Game: Modern Attack, Center Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n5/4p3/3Pn3/3B1N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C43",
            "Russian Game: Modern Attack, Murrey Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C43",
            "Russian Game: Modern Attack",
        ),
        "rnbqkb1r/pppp1ppp/8/4P3/3pn3/5N2/PPP1QPPP/RNB1KB1R b KQkq -": (
            "C43",
            "Russian Game: Modern Attack, Steinitz Variation",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3pp3/3PP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C43",
            "Russian Game: Modern Attack, Symmetrical Variation",
        ),
        "rnbqkb1r/pppp1ppp/8/4p3/3Pn3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C43",
            "Russian Game: Modern Attack, Symmetrical Variation",
        ),
        "rnbqkb1r/pppp1ppp/8/1B2P3/3pn3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C43",
            "Russian Game: Modern Attack, Tal Gambit",
        ),
        "rnbq1rk1/ppp2ppp/8/3pb3/2PPn3/3B4/PP3PPP/RNBQ1RK1 w - -": (
            "C43",
            "Russian Game: Modern Attack, Trifunović Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4N3/2P1P3/8/PP1P1PPP/RNBQKB1R b KQkq -": (
            "C44",
            "Dresden Opening: The Goblin Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4N3/4P3/8/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C44",
            "Irish Gambit",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5NP1/PPPP1P1P/RNBQKB1R b KQkq -": (
            "C44",
            "King's Knight Opening: Konstantinopolsky Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq -": (
            "C44",
            "King's Knight Opening: Normal Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/2P1P3/5N2/PP1P1PPP/RNBQKB1R b KQkq -": (
            "C44",
            "King's Pawn Game: Dresden Opening",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/1P2P3/5N2/P1PP1PPP/RNBQKB1R b KQkq -": (
            "C44",
            "King's Pawn Game: Pachman Wing Gambit",
        ),
        "r1bqkbnr/pppp1ppp/8/4n3/3PP3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C44",
            "King's Pawn Game: Schulze-Müller Gambit",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4P3/3p4/5N2/PPP1BPPP/RNBQK2R b KQkq -": (
            "C44",
            "King's Pawn Game: Tayler Opening, Basman Gambit",
        ),
        "r1bqkb1r/ppp2ppp/2n2n2/3pp3/4P3/3P1N2/PPPNBPPP/R1BQK2R b KQkq -": (
            "C44",
            "King's Pawn Game: Tayler Opening, Inverted Hanham Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPPBPPP/RNBQK2R b KQkq -": (
            "C44",
            "King's Pawn Game: Tayler Opening",
        ),
        "r1bqkbnr/pppp2pp/2n5/4pP2/8/3P1N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C44",
            "Latvian Gambit: Clam Gambit",
        ),
        "r2qkbnr/pppb1ppp/2n5/3pp3/Q3P3/2P2N2/PP1P1PPP/RNB1KB1R w KQkq -": (
            "C44",
            "Ponziani Opening: Caro Gambit",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "C44",
            "Ponziani Opening: Jaenisch Counterattack",
        ),
        "r1bqkb1r/ppp2ppp/2n2n2/3pp3/Q3P3/2P2N2/PP1P1PPP/RNB1KB1R w KQkq -": (
            "C44",
            "Ponziani Opening: Leonhardt Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/2P2N2/PP1P1PPP/RNBQK2R b KQkq -": (
            "C44",
            "Ponziani Opening: Neumann Gambit",
        ),
        "rnbqk2r/ppp1b1pp/3p1n2/3Pp3/4N3/2PB4/PP3PPP/RNBQK2R w KQkq -": (
            "C44",
            "Ponziani Opening: Ponziani Countergambit, Cordel Variation",
        ),
        "r1bqkbnr/pppp2pp/2n5/4pp2/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "C44",
            "Ponziani Opening: Ponziani Countergambit",
        ),
        "r1bqkbnr/ppp3pp/2np4/3Ppp2/4P3/2P2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "C44",
            "Ponziani Opening: Ponziani Countergambit, Schmidt Attack",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R b KQkq -": (
            "C44",
            "Ponziani Opening",
        ),
        "r1bqkb1r/ppppnppp/2n5/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "C44",
            "Ponziani Opening: Réti Variation",
        ),
        "r1bqk1nr/ppppbppp/2n5/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq -": (
            "C44",
            "Ponziani Opening: Romanishin Variation",
        ),
        "r1b1kbnr/ppp2ppp/2n5/1B1qN3/Q3p3/2P5/PP1P1PPP/RNB1K2R b KQkq -": (
            "C44",
            "Ponziani Opening: Spanish Variation, Harrwitz Attack, Nikitin Gambit",
        ),
        "r1bqkbnr/ppp2ppp/2n5/1B1pp3/4P3/2P2N2/PP1P1PPP/RNBQK2R b KQkq -": (
            "C44",
            "Ponziani Opening: Spanish Variation",
        ),
        "r1bqkbnr/ppp3pp/2n2p2/3pp3/Q3P3/2P2N2/PP1P1PPP/RNB1KB1R w KQkq -": (
            "C44",
            "Ponziani Opening: Steinitz Variation",
        ),
        "r1bqk2r/pppp1ppp/2n5/2bPp3/4n3/2P2N2/PP3PPP/RNBQKB1R w KQkq -": (
            "C44",
            "Ponziani Opening: Vuković Gambit",
        ),
        "r1bqkb1r/pp1p1Npp/2p1nn2/8/2B1P3/8/PPP2PPP/RNBQ1RK1 b kq -": (
            "C44",
            "Scotch Game: Cochrane Variation",
        ),
        "r1bqk1nr/ppppbppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C44",
            "Scotch Game: Benima Defense",
        ),
        "r1bq3r/ppp2k1p/2n3p1/2Qp4/3pP3/8/PPP2PPP/RNB1K2R w KQ -": (
            "C44",
            "Scotch Game: Cochrane-Shumov Defense",
        ),
        "r1bqk1nr/pppp1ppp/2n5/b3P3/2B5/2P2N2/P4PPP/RNBQK2R b KQkq -": (
            "C44",
            "Scotch Game: Cochrane Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/8/1bB1P3/2N2N2/PP3PPP/R1BQK2R w KQkq -": (
            "C44",
            "Scotch Game: Göring Gambit, Bardeleben Variation",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/2B1P3/2p2N2/PP3PPP/RNBQK2R b KQkq -": (
            "C44",
            "Scotch Game: Göring Gambit, Double Pawn Sacrifice",
        ),
        "r1bqk1nr/pppp1ppp/2n5/8/1b2P3/2N2N2/PP3PPP/R1BQKB1R w KQkq -": (
            "C44",
            "Scotch Game: Göring Gambit, Main Line",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/3pP3/2P2N2/PP3PPP/RNBQKB1R b KQkq -": (
            "C44",
            "Scotch Game: Göring Gambit",
        ),
        "r1bq1rk1/pppp1ppp/5n2/4n1N1/1bB5/8/PB3PPP/RN1Q1RK1 w - -": (
            "C44",
            "Scotch Game: Hanneken Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b5/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C44",
            "Scotch Game: Haxo Gambit",
        ),
        "r1bqkbnr/pppp1ppp/8/4p3/3nP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C44",
            "Scotch Game: Lolli Variation",
        ),
        "r1bqkbnr/pppp1ppp/8/8/2BpP3/8/PPP2PPP/RNBQK2R b KQkq -": (
            "C44",
            "Scotch Game: Napoleon Gambit",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C44",
            "Scotch Game",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq -": (
            "C44",
            "Scotch Game",
        ),
        "r1bqkbnr/pppp1ppp/2n5/1B6/3pP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C44",
            "Scotch Game: Relfsson Gambit",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4P3/2Bp4/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C44",
            "Scotch Game: Scotch Gambit, Advance Variation",
        ),
        "r2qk1nr/ppp2ppp/2np4/2b5/2BpP1b1/2P2N2/PP3PPP/RNBQ1RK1 w kq -": (
            "C44",
            "Scotch Game: Scotch Gambit, Cochrane-Anderssen Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/8/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C44",
            "Scotch Game: Scotch Gambit, Dubois Réti Defense",
        ),
        "r1bqkbnr/ppp2ppp/2n5/3p4/3pP3/2P2N2/PP3PPP/RNBQKB1R w KQkq -": (
            "C44",
            "Scotch Game: Scotch Gambit, Göring Gambit Declined",
        ),
        "r1bqkb1r/pppp1ppp/2n5/4P3/2Bp2n1/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C44",
            "Scotch Game: Scotch Gambit, Kingside Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/8/1bBpP3/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C44",
            "Scotch Game: Scotch Gambit, London Defense",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C44",
            "Scotch Game: Scotch Gambit",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b3N1/2BpP3/8/PPP2PPP/RNBQK2R b KQkq -": (
            "C44",
            "Scotch Game: Scotch Gambit, Sarratt Variation",
        ),
        "r1bqk2r/pppp1ppp/2n4n/2b3NQ/2BpP3/8/PPP2PPP/RNB1K2R b KQkq -": (
            "C44",
            "Scotch Game: Vitzthum Attack",
        ),
        "r2q1bnr/ppp1kBpp/3p4/3NN3/4P3/8/PP3PPP/R1Bb1RK1 b - -": (
            "C44",
            "Scotch Game: Sea-Cadet Mate",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/3PP3/5N2/PPP1BPPP/RNBQK2R b KQkq -": (
            "C44",
            "Tayler Opening",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4P3/3N4/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C45",
            "Scotch Game: Alekhine Gambit",
        ),
        "N1bk3r/pp1p1ppp/2n2n2/8/1b6/P4B1q/1PPN1P1P/R1BQK2R b KQ -": (
            "C45",
            "Scotch Game: Berger Variation",
        ),
        "r1b1k1nr/pppp1ppp/2n2q2/1Nb5/4P3/4B3/PPP2PPP/RN1QKB1R b KQkq -": (
            "C45",
            "Scotch Game: Blumenfeld Attack",
        ),
        "r1b1kbnr/pppp1ppp/2n5/8/3NP2q/4B3/PPP2PPP/RN1QKB1R b KQkq -": (
            "C45",
            "Scotch Game: Braune Variation",
        ),
        "r1b1k2r/ppppnppp/2n2q2/2b5/3NP3/2P1B3/PP1Q1PPP/RN2KB1R b KQkq -": (
            "C45",
            "Scotch Game: Classical Variation, Blackburne Attack",
        ),
        "r1b1k1nr/pppp1ppp/2N2q2/2b5/4P3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "C45",
            "Scotch Game: Classical Variation, Intermezzo Variation",
        ),
        "r1b1k1nr/pppp1ppp/2n3q1/2b5/3NP3/2P1B3/PP3PPP/RN1QKB1R w KQkq -": (
            "C45",
            "Scotch Game: Classical Variation, Millennium Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b5/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "C45",
            "Scotch Game: Classical Variation",
        ),
        "r1b1kbnr/pppp1ppp/2n5/8/4P2q/5N2/PPP2PPP/RNBQKB1R b KQkq -": (
            "C45",
            "Scotch Game: Fraser Variation",
        ),
        "r1bqkbnr/ppp2ppp/3p4/8/3QP3/3B4/PPP2PPP/RNB1K2R b KQkq -": (
            "C45",
            "Scotch Game: Ghulam-Kassim Variation",
        ),
        "1rb2rk1/pp3ppp/5q2/3P4/1n6/2P1Q3/PP3PPP/RN2KB1R w KQ -": (
            "C45",
            "Scotch Game: Gottschall Variation",
        ),
        "r1bk2nr/pppp1ppp/2n5/1N6/4q3/8/PPPQBPPP/RN3RK1 b - -": (
            "C45",
            "Scotch Game: Horwitz Attack, Blackburne Variation",
        ),
        "r1bk2nr/pppp1ppp/2n5/1N6/P4q2/8/1PPNBPPP/R2Q1RK1 b - -": (
            "C45",
            "Scotch Game: Horwitz Attack, McDonnell Variation",
        ),
        "r1b1kbnr/pppp1ppp/2n5/1N6/4P2q/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C45",
            "Scotch Game: Horwitz Attack",
        ),
        "r1bk2nr/pppp1ppp/2n5/1N6/2P2q2/8/PP1NBPPP/R2Q1RK1 b - -": (
            "C45",
            "Scotch Game: Horwitz Attack, Vienna Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/8/1b1NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "C45",
            "Scotch Game: Malaniuk Variation",
        ),
        "r1b1k2r/ppppnppp/2n2q2/2b5/4P3/2P1B3/PPN2PPP/RN1QKB1R b KQkq -": (
            "C45",
            "Scotch Game: Meitner Variation",
        ),
        "r1bqkb1r/p1pp1ppp/2p2n2/4P3/8/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C45",
            "Scotch Game: Mieses Variation",
        ),
        "r1b1k1nr/pppp1ppp/2n5/8/1b1NP2q/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "C45",
            "Scotch Game: Modern Defense",
        ),
        "r1b1k2r/ppppnppp/2n2q2/1Bb5/3NP3/2P1B3/PP3PPP/RN1QK2R b KQkq -": (
            "C45",
            "Scotch Game: Paulsen Attack",
        ),
        "r1bnk2r/ppppnppp/5q2/1Bb5/3NP3/2P1B3/PP3PPP/RN1QK2R w KQkq -": (
            "C45",
            "Scotch Game: Paulsen, Gunsberg Defense",
        ),
        "r1b1kbnr/pppp1ppp/2n5/5N2/4P2q/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C45",
            "Scotch Game: Paulsen Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b5/4P3/1N6/PPP2PPP/RNBQKB1R b KQkq -": (
            "C45",
            "Scotch Game: Potter Variation",
        ),
        "r1b1k1nr/pppp1ppp/2n5/1N6/1b2P2q/8/PPPB1PPP/RN1QKB1R b KQkq -": (
            "C45",
            "Scotch Game",
        ),
        "r1bqkbnr/pppp1ppp/2n5/8/3NP3/8/PPP2PPP/RNBQKB1R b KQkq -": (
            "C45",
            "Scotch Game",
        ),
        "r1bqk1nr/pppp1ppp/2n5/8/1b2P3/1N6/PPP2PPP/RNBQKB1R w KQkq -": (
            "C45",
            "Scotch Game: Romanishin Variation",
        ),
        "r1bk2nr/pppp1ppp/2n3q1/1N6/8/8/PPPNBPPP/R2Q1RK1 w - -": (
            "C45",
            "Scotch Game: Rosenthal Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/8/3NP3/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "C45",
            "Scotch Game: Schmidt Variation",
        ),
        "r1b1kbnr/pppp1ppp/2n5/8/3NP2q/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "C45",
            "Scotch Game: Steinitz Variation",
        ),
        "r1b1kbnr/pppp1ppp/2n5/8/3NP2q/8/PPP2PPP/RNBQKB1R w KQkq -": (
            "C45",
            "Scotch Game: Steinitz Variation",
        ),
        "r1bqkb1r/p1pp1ppp/2p2n2/8/4P3/8/PPPN1PPP/R1BQKB1R b KQkq -": (
            "C45",
            "Scotch Game: Tartakower Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/P1N2N2/1PPP1PPP/R1BQKB1R b KQkq -": (
            "C46",
            "Four Knights Game: Gunsberg Variation",
        ),
        "r1bqk1nr/pppp2pp/6n1/4Pp2/1bBP4/2N2Q2/PPP2PPP/R1B1K2R w KQkq f6": (
            "C46",
            "Four Knights Game: Halloween Gambit, Oldtimer Variation",
        ),
        "1rb1kbnr/pp1p1ppp/3P1qn1/1N6/5P2/8/PPP3PP/R1BQKB1R w KQk -": (
            "C46",
            "Four Knights Game: Halloween Gambit, Plasma Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4N3/4P3/2N5/PPPP1PPP/R1BQKB1R b KQkq -": (
            "C46",
            "Four Knights Game: Halloween Gambit",
        ),
        "r1bqkb1r/pppp1Bpp/2n5/4p3/4n3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -": (
            "C46",
            "Four Knights Game: Italian Variation, Noa Gambit",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -": (
            "C46",
            "Four Knights Game: Italian Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq -": (
            "C46",
            "Four Knights Game",
        ),
        "r1bqk1nr/pppp1ppp/2n5/4p3/1b2P3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq -": (
            "C46",
            "Three Knights Opening",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq -": (
            "C46",
            "Three Knights Opening",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/3Np3/1b2P3/5N2/PPPP1PPP/R1BQKB1R w KQkq -": (
            "C46",
            "Three Knights Opening: Schlechter Variation",
        ),
        "r1bqkbnr/pppp1p1p/2n3p1/4p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq -": (
            "C46",
            "Three Knights Opening: Steinitz Defense",
        ),
        "r1bqkbnr/pppp1p1p/2n3p1/3N4/3pP3/5N2/PPP2PPP/R1BQKB1R b KQkq -": (
            "C46",
            "Three Knights Opening: Steinitz-Rosenthal Variation",
        ),
        "r1bqkbnr/pppp2pp/2n5/4pp2/4P3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq -": (
            "C46",
            "Three Knights Opening: Winawer Defense",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/8/3pP3/2N2N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "C47",
            "Four Knights Game: Scotch Variation Accepted",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/3N4/3pP3/5N2/PPP2PPP/R1BQKB1R b KQkq -": (
            "C47",
            "Four Knights Game: Scotch Variation, Belgrade Gambit",
        ),
        "r1b1k2r/ppppqppp/2n2n2/4N3/1b1PP3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "C47",
            "Four Knights Game: Scotch Variation, Krause Gambit, Leonhardt Defense",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/4N3/1b1PP3/2N5/PPP2PPP/R1BQKB1R b KQkq -": (
            "C47",
            "Four Knights Game: Scotch Variation, Krause Gambit",
        ),
        "r1bqk2r/pppp1ppp/5n2/3Pp3/1b1nP3/2N2N2/PPP2PPP/R1BQKB1R w KQkq -": (
            "C47",
            "Four Knights Game: Scotch Variation, Oxford Gambit",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/3PP3/2N2N2/PPP2PPP/R1BQKB1R b KQkq -": (
            "C47",
            "Four Knights Game: Scotch Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n5/8/3Nn3/2N5/PPP2PPP/R1BQKB1R w KQkq -": (
            "C47",
            "Four Knights Game: Scotch Variation, Schmid Defense",
        ),
        "r1bqkb1r/pppp2pp/2n5/3N1p2/3pn3/5N2/PPP1QPPP/R1B1KB1R w KQkq -": (
            "C47",
            "Four Knights Game: Scotch Variation, Belgrade Gambit, Modern Defense",
        ),
        "r1bq1rk1/pppp1ppp/2n2n2/1B2P3/1b1P1P2/2N5/PPP3PP/R1BQ1RK1 w - -": (
            "C48",
            "Four Knights Game: Bardeleben Variation",
        ),
        "r1bq1rk1/pppp1ppp/5n2/1Bb1N3/3nP3/2N5/PPPP1PPP/R1BQ1RK1 w - -": (
            "C48",
            "Four Knights Game: Marshall Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1B2n2/4p3/4P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -": (
            "C48",
            "Four Knights Game: Ranken Variation",
        ),
        "r1bqkb1r/pppp1ppp/5n2/1B2p3/3nP3/2N2N2/PPPP1PPP/R1BQ1RK1 b kq -": (
            "C48",
            "Four Knights Game: Rubinstein Countergambit, Henneberger Variation",
        ),
        "r1bq1rk1/ppp2ppp/1b1p1n2/4p3/N3P3/3P1B2/PPP2PPP/R1BQ1RK1 w - -": (
            "C48",
            "Four Knights Game: Rubinstein Countergambit, Maróczy Variation",
        ),
        "r1bqkb1r/pppp1ppp/5n2/4p3/3nP3/2N2N2/PPPPBPPP/R1BQK2R b KQkq -": (
            "C48",
            "Four Knights Game: Rubinstein Countergambit",
        ),
        "r1bq1rk1/pppp1ppp/5n2/2b1N3/B2nP3/2N5/PPPP1PPP/R1BQK2R w KQ -": (
            "C48",
            "Four Knights Game: Spanish Variation, Classical Variation, Marshall Gambit",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/1Bb1p3/4P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq -": (
            "C48",
            "Four Knights Game: Spanish Variation, Classical Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/1B2p3/4P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -": (
            "C48",
            "Four Knights Game: Spanish Variation",
        ),
        "r1bqkb1r/pppp1ppp/5n2/1B2p3/3NP3/2N5/PPPP1PPP/R1BQK2R b KQkq -": (
            "C48",
            "Four Knights Game: Spanish Variation, Rubinstein Variation Accepted",
        ),
        "r1b1kb1r/ppppqppp/5n2/1B2N3/3nPP2/2N5/PPPP2PP/R1BQK2R b KQkq -": (
            "C48",
            "Four Knights Game: Spanish Variation, Rubinstein Variation",
        ),
        "r1bqkb1r/pppp1ppp/5n2/1B2p3/3nP3/2N2N2/PPPP1PPP/R1BQK2R w KQkq -": (
            "C48",
            "Four Knights Game: Spanish Variation, Rubinstein Variation",
        ),
        "r3kb1r/1pp2ppp/p1p1b3/3q4/3PN3/8/PPP2PPP/R1BQR1K1 w kq -": (
            "C48",
            "Four Knights Game: Spielmann Variation",
        ),
        "r1b2rk1/ppp1qppp/2n2n2/1B1pp3/1b2P3/3P1N2/PPP1NPPP/R1BQ1RK1 w - -": (
            "C49",
            "Four Knights Game: Alatortsev Variation",
        ),
        "r1bq1rk1/pppp1ppp/2n2n2/1B2p3/1b2P3/2NP1N2/PPP2PPP/R1BQ1RK1 b - -": (
            "C49",
            "Four Knights Game: Double Spanish",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/1B2p3/1b2P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq -": (
            "C49",
            "Four Knights Game: Double Spanish",
        ),
        "r1bq1rk1/pppp1ppp/2n5/1B1P4/1b2p3/5N2/PPPP1PPP/R1BQ1RK1 w - -": (
            "C49",
            "Four Knights Game: Gunsberg Counterattack",
        ),
        "r1bq1rk1/ppp2ppp/2np1n2/1B2p3/4P3/2PP1N2/P1P2PPP/R1BQR1K1 b - -": (
            "C49",
            "Four Knights Game: Janowski Variation",
        ),
        "r1bq1rk1/pppp1ppp/2B2n2/4p3/1b2P3/2N2N2/PPPP1PPP/R1BQ1RK1 b - -": (
            "C49",
            "Four Knights Game: Nimzowitsch (Paulsen)",
        ),
        "r1bq1rk1/pppp1ppp/2n2n2/1B2p3/4P3/2bP1N2/PPP2PPP/R1BQ1RK1 w - -": (
            "C49",
            "Four Knights Game: Spanish Variation",
        ),
        "r1bq1rk1/ppp1nppp/3p1n2/1B2p1B1/1b2P3/2NP1N2/PPP2PPP/R2Q1RK1 w - -": (
            "C49",
            "Four Knights Game: Spanish Variation, Symmetrical Variation",
        ),
        "r1bq1rk1/ppp2ppp/2np1n2/1B2p3/1b2P3/2NP1N2/PPP2PPP/R1BQ1RK1 w - -": (
            "C49",
            "Four Knights Game: Spanish Variation, Symmetrical Variation",
        ),
        "r1bq1rk1/ppp2ppp/2np1n2/1B2p3/1b2P3/3P1N2/PPP1NPPP/R1BQ1RK1 b - -": (
            "C49",
            "Four Knights Game: Spanish Variation, Symmetrical Variation",
        ),
        "r2n1rk1/ppp1qppp/3p1n2/1B2p1B1/3PP1b1/2P2N2/P1P2PPP/R2QR1K1 w - -": (
            "C49",
            "Four Knights Game: Spanish Variation, Symmetrical Variation",
        ),
        "r1bq1rk1/ppp2ppp/2n2n2/1B1pp3/4P3/2PP1N2/P1P2PPP/R1BQ1RK1 w - -": (
            "C49",
            "Four Knights Game: Svenonius Variation",
        ),
        "r1b2rk1/pp2nppp/2pq1n2/3pp1B1/1b2P2N/1BNP4/PPP2PPP/R2Q1RK1 w - -": (
            "C49",
            "Four Knights Game: Symmetrical, Blake Variation",
        ),
        "r1b2rk1/ppp1qppp/2np1n2/1B2p1B1/4P3/2PP1N2/P1P2PPP/R2Q1RK1 w - -": (
            "C49",
            "Four Knights Game: Symmetrical, Metger Unpin",
        ),
        "r2q1rk1/ppp2ppp/2npbn2/1B2p1B1/1b2P3/2NP1N2/PPP2PPP/R2Q1RK1 w - -": (
            "C49",
            "Four Knights Game: Symmetrical, Tarrasch Variation",
        ),
        "r1b1kbnr/pppp1Npp/8/8/4q3/5n2/PPPPBP1P/RNBQKR2 w Qkq -": (
            "C50",
            "Blackburne Shilling Gambit",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq -": (
            "C50",
            "Four Knights Game: Italian Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C50",
            "Giuoco Piano Game",
        ),
        "r1bqkbnr/pppp1pp1/2n4p/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C50",
            "Italian Game: Anti-Fried Liver Defense",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/2P2N2/PP1P1PPP/RNBQ1RK1 b kq -": (
            "C50",
            "Italian Game: Classical Variation, Albin Gambit",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2BPP3/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C50",
            "Italian Game: Deutz Gambit",
        ),
        "r1bqk2r/ppp2ppp/2np1n2/2b1p1B1/2B1P3/2NP1N2/PPP2PPP/R2QK2R b KQkq -": (
            "C50",
            "Italian Game: Giuoco Pianissimo Variation, Canal Variation",
        ),
        "r1bqk1nr/pppp2pp/2n5/2b1p1N1/2B1Pp2/3P4/PPP2PPP/RNBQK2R w KQkq -": (
            "C50",
            "Italian Game: Giuoco Pianissimo Variation, Dubois Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/2NP1N2/PPP2PPP/R1BQK2R b KQkq -": (
            "C50",
            "Italian Game: Giuoco Pianissimo Variation, Italian Four Knights Variation",
        ),
        "r1bqk1nr/pppp2pp/2n5/2b1pp2/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C50",
            "Italian Game: Giuoco Pianissimo Variation, Lucchini Gambit",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C50",
            "Italian Game: Giuoco Pianissimo Variation, Normal Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C50",
            "Italian Game: Giuoco Pianissimo Variation",
        ),
        "r1bqk1nr/ppppbppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C50",
            "Italian Game: Hungarian Defense",
        ),
        "r1bqk2r/ppppbppp/2n5/4P3/2Bpn3/2P2N2/PP3PPP/RNBQK2R w KQkq -": (
            "C50",
            "Italian Game: Hungarian Defense, Tartakower Variation",
        ),
        "r1bqk1nr/pppp1Bpp/2n5/2b1p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C50",
            "Italian Game: Jerome Gambit",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C50",
            "Italian Game",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b1p3/2BPP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C50",
            "Italian Game: Rosentreter Gambit",
        ),
        "r1bqkbnr/pppp2pp/2n5/4pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C50",
            "Italian Game: Rousseau Gambit",
        ),
        "r1bqkbnr/pppp1ppp/8/4p3/2BnP3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C50",
            "Italian Game: Schilling-Kostić Gambit",
        ),
        "r1bqk1nr/pppp1ppp/2n5/4p3/1bB1P3/5N2/P1PP1PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit Accepted",
        ),
        "r1bqk1nr/ppppbppp/8/n3p3/2BPP3/2P2N2/P4PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit, Anderssen Variation, Cordel Line",
        ),
        "r1bqk1nr/ppppbppp/2n5/4p3/2B1P3/2P2N2/P2P1PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit, Anderssen Variation",
        ),
        "r1bqk1nr/pppp1ppp/1bn5/4p3/1PB1P3/5N2/PBPP1PPP/RN1QK2R b KQkq -": (
            "C51",
            "Italian Game: Evans Gambit Declined, Cordel Variation",
        ),
        "r1bk2nr/pppp1Qpp/1b6/nP2q3/2B1P3/8/PBPP1PPP/RN2K2R b KQ -": (
            "C51",
            "Italian Game: Evans Gambit Declined, Hicken Variation",
        ),
        "r1b1k1nr/pppp1ppp/1b6/nP2N1q1/2B1P3/8/P1PP1PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit Declined, Hirschbach Variation",
        ),
        "r1bqk2r/pppp1ppp/1b5n/nP2N3/2B1P3/8/P1PP1PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit Declined, Lange Variation",
        ),
        "r1b3r1/ppp2k1p/1b6/nP2B1q1/3PP3/8/P1PN1PPP/R2QK2R b KQ -": (
            "C51",
            "Italian Game: Evans Gambit Declined, Pavlov Variation",
        ),
        "r1bqk1nr/pppp1ppp/1bn5/4p3/1PB1P3/5N2/P1PP1PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit Declined",
        ),
        "r1bqk1nr/pppp1ppp/1bn5/4p3/PPB1P3/5N2/2PP1PPP/RNBQK2R b KQkq -": (
            "C51",
            "Italian Game: Evans Gambit Declined",
        ),
        "r1bqk1nr/1ppp1ppp/pbn5/4p3/PPB1P3/2N2N2/2PP1PPP/R1BQK2R b KQkq -": (
            "C51",
            "Italian Game: Evans Gambit Declined, Showalter Variation",
        ),
        "r1b3nr/ppppkBpp/1b6/nP2N1qQ/4P3/8/P1PP1PPP/RNB1K2R b KQ -": (
            "C51",
            "Italian Game: Evans Gambit Declined, Vasquez Variation",
        ),
        "r1bqk1nr/p1pp1ppp/2n5/1pb1p3/1PB1P3/5N2/P1PP1PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit, Fontaine Countergambit",
        ),
        "r2qk1nr/ppp2ppp/1bnp4/8/Q1BPP1b1/2N2N2/P4PPP/R1B2RK1 b kq -": (
            "C51",
            "Italian Game: Evans Gambit, Fraser Attack",
        ),
        "r2q1knr/pppb1Bpp/1b1p4/n7/3PP3/2N2N2/P1Q2PPP/R1B2RK1 b - -": (
            "C51",
            "Italian Game: Evans Gambit, Fraser-Mortimer Attack",
        ),
        "r1bqk1nr/ppp2ppp/1b1p4/n5B1/2BPP3/2N2N2/P4PPP/R2Q1RK1 b kq -": (
            "C51",
            "Italian Game: Evans Gambit, Göring Attack",
        ),
        "r1bqk1nr/pppp1ppp/2n5/8/1bBPP3/5N2/P2B1PPP/RN1QK2R b KQkq -": (
            "C51",
            "Italian Game: Evans Gambit, Harding Variation",
        ),
        "r1bqk1nr/ppp2ppp/2n5/2bpp3/1PB1P3/5N2/P1PP1PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit, Hein Countergambit",
        ),
        "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/2P2N2/P2P1PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit, Mayet Defense",
        ),
        "r1bqk1nr/ppp2ppp/1bnp4/8/2BPP3/5N2/P4PPP/RNBQ1RK1 w kq -": (
            "C51",
            "Italian Game: Evans Gambit, McDonnell Defense, Main Line",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/2P2N2/P2P1PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit, McDonnell Defense",
        ),
        "r1bqk1nr/ppp2ppp/1bnp4/8/2BPP3/2N2N2/P4PPP/R1BQ1RK1 b kq -": (
            "C51",
            "Italian Game: Evans Gambit, Morphy Attack",
        ),
        "r2q2nr/pppb1kpp/1b1p4/n7/3PP3/2N2N2/P1Q2PPP/R1B2RK1 w - -": (
            "C51",
            "Italian Game: Evans Gambit, Mortimer-Evans Gambit",
        ),
        "r1bqk2r/ppp1nppp/1b1p4/n2P4/2B1P3/5N2/PB3PPP/RN1Q1RK1 w kq -": (
            "C51",
            "Italian Game: Evans Gambit, Paulsen Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b1p3/1PB1P3/5N2/P1PP1PPP/RNBQK2R b KQkq -": (
            "C51",
            "Italian Game: Evans Gambit",
        ),
        "r2qk1nr/ppp2ppp/1bnp4/8/2BPP1b1/2N2N2/P4PPP/R1BQ1RK1 w kq -": (
            "C51",
            "Italian Game: Evans Gambit",
        ),
        "r1bqk1nr/ppp3pp/1b1p1p2/n7/2BPP3/2N1BN2/P4PPP/R2Q1RK1 b kq -": (
            "C51",
            "Italian Game: Evans Gambit, Steinitz Variation",
        ),
        "r1bqk1nr/pppp1ppp/2nb4/4p3/2B1P3/2P2N2/P2P1PPP/RNBQK2R w KQkq -": (
            "C51",
            "Italian Game: Evans Gambit, Stone-Ware Variation",
        ),
        "r1bqk1nr/ppp2ppp/1b1p4/n2P4/2B1P3/5N2/PB3PPP/RN1Q1RK1 b kq -": (
            "C51",
            "Italian Game: Evans Gambit, Ulvestad Variation",
        ),
        "r2qk1nr/ppp2ppp/2np4/b3p3/2BPP1b1/2P2N2/P4PPP/RNBQ1RK1 w kq -": (
            "C52",
            "Italian Game: Evans Gambit, Alapin-Steinitz Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/b7/2BpP3/2P2N2/P4PPP/RNBQ1RK1 w kq -": (
            "C52",
            "Italian Game: Evans Gambit, Anderssen Defense",
        ),
        "r1bqk1nr/ppp2ppp/2np4/b3p3/2BPP3/2P2N2/P4PPP/RNBQK2R w KQkq -": (
            "C52",
            "Italian Game: Evans Gambit, Bronstein Defense",
        ),
        "r1b1k2r/ppppnppp/2n3q1/b3P3/2B5/BQN2N2/P4PPP/R4RK1 b kq -": (
            "C52",
            "Italian Game: Evans Gambit, Compromised Defense, Main Line",
        ),
        "r1b1k2r/ppppnppp/2n3q1/b3P3/2B5/1QN2N2/P4PPP/R1BR2K1 b kq -": (
            "C52",
            "Italian Game: Evans Gambit, Compromised Defense, Potter Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/b7/2B1P3/2p2N2/P4PPP/RNBQ1RK1 w kq -": (
            "C52",
            "Italian Game: Evans Gambit, Compromised Defense",
        ),
        "r1bqk1nr/pppp1ppp/2n5/b7/2B1P3/2Pp1N2/P4PPP/RNBQ1RK1 w kq -": (
            "C52",
            "Italian Game: Evans Gambit, Dufresne Defense",
        ),
        "r1bqk1nr/p1pp1ppp/2n5/bp6/2BpP3/2P2N2/P4PPP/RNBQ1RK1 w kq -": (
            "C52",
            "Italian Game: Evans Gambit, Johner Defense",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/b3p3/2BPP3/2P2N2/P4PPP/RNBQK2R w KQkq -": (
            "C52",
            "Italian Game: Evans Gambit, Laroche Variation",
        ),
        "r1bqk1nr/ppp2ppp/1bnp4/4p3/2BPP3/2P2N2/P4PPP/RNBQ1RK1 w kq -": (
            "C52",
            "Italian Game: Evans Gambit, Lasker Defense",
        ),
        "r1bqk1nr/p1pp1ppp/2n5/bp2p3/2BPP3/2P2N2/P4PPP/RNBQK2R w KQkq -": (
            "C52",
            "Italian Game: Evans Gambit, Leonhardt Countergambit",
        ),
        "r1b1k1nr/pppq1ppp/1b6/n3N3/2B1P3/BQP5/P4PPP/RN3RK1 b kq -": (
            "C52",
            "Italian Game: Evans Gambit, Levenfish Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/b3p3/2B1P3/2P2N2/P2P1PPP/RNBQK2R w KQkq -": (
            "C52",
            "Italian Game: Evans Gambit, Main Line",
        ),
        "r1bqk2r/ppppnppp/2n5/b7/2BpP3/2P2N2/P4PPP/RNBQ1RK1 w kq -": (
            "C52",
            "Italian Game: Evans Gambit, Mieses Defense",
        ),
        "r1bqk1nr/pppp1ppp/2n5/b7/2BpP3/2P2N2/P4PPP/RNBQK2R w KQkq -": (
            "C52",
            "Italian Game: Evans Gambit, Pierce Defense",
        ),
        "r1bqk1nr/ppp2ppp/2np4/b3p3/2B1P3/2P2N2/P2P1PPP/RNBQ1RK1 w kq -": (
            "C52",
            "Italian Game: Evans Gambit",
        ),
        "r1bq1rk1/pppp1ppp/2n2n2/b3N3/2BPP3/2P5/P4PPP/RNBQ1RK1 b - -": (
            "C52",
            "Italian Game: Evans Gambit, Richardson Attack",
        ),
        "r2qk1nr/pppb1ppp/2np4/b3p3/2BPP3/2P2N2/P4PPP/RNBQ1RK1 w kq -": (
            "C52",
            "Italian Game: Evans Gambit, Sanders-Alapin Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/b3p3/2B1P3/2P2N2/P2P1PPP/RNBQ1RK1 b kq -": (
            "C52",
            "Italian Game: Evans Gambit, Slow Variation",
        ),
        "r1bqk1nr/ppp2ppp/2np4/b3p1B1/2BPP3/2P2N2/P4PPP/RN1QK2R b KQkq -": (
            "C52",
            "Italian Game: Evans Gambit, Sokolsky Variation",
        ),
        "r1bqk1nr/ppp2ppp/2np4/b3p3/2BPP3/1QP2N2/P4PPP/RNB1K2R b KQkq -": (
            "C52",
            "Italian Game: Evans Gambit, Tartakower Attack",
        ),
        "r1bqk1nr/ppp2ppp/2np4/b7/2BpP3/1QP2N2/P4PPP/RNB2RK1 b kq -": (
            "C52",
            "Italian Game: Evans Gambit, Waller Attack",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/1PB1P3/2P2N2/P2P1PPP/RNBQK2R b KQkq -": (
            "C53",
            "Italian Game: Bird Attack",
        ),
        "r1bqk1nr/pppp2pp/2n5/2b1pp2/2B1P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C53",
            "Italian Game: Classical Variation, Alexandre Gambit",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2BPP3/2P2N2/PP3PPP/RNBQK2R b KQkq -": (
            "C53",
            "Italian Game: Classical Variation, Center Attack",
        ),
        "r1b1k1nr/ppppqppp/1bn5/4p3/2BPP3/2P2N2/PP3PPP/RNBQK2R w KQkq -": (
            "C53",
            "Italian Game: Classical Variation, Center Holding Variation",
        ),
        "r1b1k1nr/ppppqppp/2n5/2b1p3/2B1P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C53",
            "Italian Game: Classical Variation, Closed Variation",
        ),
        "r1bq1rk1/bpp2ppp/p1np1n2/4p3/4P3/1BPP1N1P/PP3PP1/RNBQR1K1 b - -": (
            "C53",
            "Italian Game: Classical Variation, Giuoco Pianissimo Variation, Main Line",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/2PP1N2/PP3PPP/RNBQK2R b KQkq -": (
            "C53",
            "Italian Game: Classical Variation, Giuoco Pianissimo Variation",
        ),
        "r1bqk2r/ppp2ppp/2n5/1B1pP3/1b1Pn3/5N2/PP3PPP/RNBQK2R w KQkq -": (
            "C53",
            "Italian Game: Classical Variation, Greco Gambit, Anderssen Variation",
        ),
        "r1bqk2r/ppp2ppp/2n2n2/2bpP3/2Bp4/2P2N2/PP3PPP/RNBQK2R w KQkq d6": (
            "C53",
            "Italian Game: Classical Variation, Greco Gambit",
        ),
        "r1bqk1nr/ppp2ppp/1bnp4/8/2BPP3/5N2/PP3PPP/RNBQK2R w KQkq -": (
            "C53",
            "Italian Game: Classical Variation, La Bourdonnais Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/2P2N2/PP1P1PPP/RNBQK2R b KQkq -": (
            "C53",
            "Italian Game: Classical Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C53",
            "Italian Game: Classical Variation",
        ),
        "r1b1k2r/1pp1qppp/pbnp1n2/4p3/P1BPP3/2P2N1P/1P3PP1/RNBQR1K1 b kq -": (
            "C53",
            "Italian Game: Classical Variation, Tarrasch Variation",
        ),
        "rnb1k1nr/ppppqppp/1b1P4/4p3/2B1P3/2P2N2/PP3PPP/RNBQK2R b KQkq -": (
            "C53",
            "Italian Game: Giuoco Piano Game, Eisinger Variation",
        ),
        "r1bqk2r/pppp1ppp/2n5/2bBP3/8/2p2NK1/PP4PP/RNBQ3R b kq -": (
            "C53",
            "Italian Game: Giuoco Piano Game, Ghulam-Kassim Variation",
        ),
        "r1b1k1nr/ppppqppp/1bn5/4p1B1/2BPP3/2P2N2/PP3PPP/RN1QK2R b KQkq -": (
            "C53",
            "Italian Game: Giuoco Piano Game, Mestel Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b5/2BpP3/2P2N2/PP3PPP/RNBQ1RK1 b kq -": (
            "C53",
            "Italian Game: Scotch Gambit, Walbrodt-Baird Gambit",
        ),
        "r1bqk2r/pppp1ppp/2n5/8/1bBP4/2n2N2/PP3PPP/R1BQ1RK1 w kq -": (
            "C54",
            "Italian Game: Classical Variation, Greco Gambit, Greco Variation",
        ),
        "r1bqk2r/pppp1ppp/2n5/8/2BPn3/2b2N2/PP3PPP/R1BQ1RK1 w kq -": (
            "C54",
            "Italian Game: Classical Variation, Greco Gambit, Main Line",
        ),
        "r1bqk2r/ppp1nppp/3p1b2/3P4/2B1R1P1/5N2/PP3P1P/R1BQ2K1 b kq -": (
            "C54",
            "Italian Game: Classical Variation, Greco Gambit, Møller-Bayonet Attack",
        ),
        "r1bqk2r/pppp1ppp/2n5/3P4/2B1n3/2b2N2/PP3PPP/R1BQ1RK1 b kq -": (
            "C54",
            "Italian Game: Classical Variation, Greco Gambit, Møller-Therkatz Attack",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b5/2BPP3/5N2/PP3PPP/RNBQK2R b KQkq -": (
            "C54",
            "Italian Game: Classical Variation, Greco Gambit, Traditional Line",
        ),
        "r1bqk2r/pppp1ppp/2n5/8/2BP4/B1b2N2/P4PPP/R2Q1RK1 b kq -": (
            "C54",
            "Italian Game: Giuoco Piano Game, Aitken Variation",
        ),
        "r1bqk2r/ppp2ppp/2n5/3p4/2BP4/1Qb2N2/P4PPP/R1B2RK1 w kq -": (
            "C54",
            "Italian Game: Giuoco Piano Game, Bernstein Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/8/1bBPP3/5N2/PP3PPP/RNBQ1K1R b kq -": (
            "C54",
            "Italian Game: Giuoco Piano Game, Cracow Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/8/1bBPP3/2N2N2/PP3PPP/R1BQK2R b KQkq -": (
            "C54",
            "Italian Game: Giuoco Piano Game, Greco Attack",
        ),
        "r1bq3r/ppp3pp/5k2/3pN3/1n1Pn3/1Q3P2/PP4PP/RN2K2R b KQ -": (
            "C54",
            "Italian Game: Giuoco Piano Game, Krause Variation",
        ),
        "r1bqk2r/ppp2ppp/2n5/3p4/2BPn3/B1P2N2/P4PPP/R2Q1RK1 b kq -": (
            "C54",
            "Italian Game: Giuoco Piano Game, Steinitz Variation",
        ),
        "r1bq1rk1/ppp1nppN/3p4/3P4/2B1R3/8/PP3PPP/R2Q2K1 b - -": (
            "C54",
            "Italian Game: Giuoco Piano Game, Therkatz-Herzog Variation",
        ),
        "r1b1k2r/ppp1qppp/5n2/4p1B1/2BnP3/2N5/PPP3PP/R2Q1RK1 b kq -": (
            "C55",
            "Italian Game: Giuoco Piano Game, Holzhausen Attack",
        ),
        "r1bqk2r/ppp2ppp/3p1n2/4p1B1/2BnP3/8/PPP2PPP/RN1Q1RK1 w kq -": (
            "C55",
            "Italian Game: Giuoco Piano Game",
        ),
        "r1bqk2r/pppp1p2/5n1p/4p1p1/2BnPP1B/8/PPP3PP/RN1Q1RK1 b kq -": (
            "C55",
            "Italian Game: Giuoco Piano Game, Rosentreter Variation",
        ),
        "r1bqk2r/pppp1ppp/2nb1n2/4p3/2BPP3/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C55",
            "Italian Game: Scotch Gambit Declined",
        ),
        "r1bqkb1r/ppp2ppp/2np1n2/4p3/2BPP3/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C55",
            "Italian Game: Scotch Gambit Declined",
        ),
        "r1bqk2r/ppppbppp/2n2n2/8/2BpP3/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C55",
            "Italian Game: Scotch Gambit, de Riviere Defense",
        ),
        "r1bqkb1r/ppp2ppp/2np1n2/8/2BpP3/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C55",
            "Italian Game: Scotch Gambit, Janowski Defense",
        ),
        "r2qk2r/ppp2pPp/2n1b3/2b5/2pp4/5N2/PPP2PPP/RNBQR1K1 b kq -": (
            "C55",
            "Italian Game: Scotch Gambit, Max Lange Attack Accepted",
        ),
        "r3k2r/ppp2ppp/2n1bP2/2b2qN1/2ppN3/8/PPP2PPP/R1BQR1K1 b kq -": (
            "C55",
            "Italian Game: Scotch Gambit, Max Lange Attack, Long Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b5/2BpP3/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C55",
            "Italian Game: Scotch Gambit, Max Lange Attack",
        ),
        "r1bqk2r/pppp1ppp/2n5/2b1P3/2Bp2n1/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C55",
            "Italian Game: Scotch Gambit, Max Lange Attack, Spielmann Defense",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/8/2BpP3/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C55",
            "Italian Game: Scotch Gambit",
        ),
        "r1b1k2r/ppp2ppp/2N5/1B1pP3/4n2q/8/PPP2bPP/RNBQ1K1R w kq -": (
            "C55",
            "Italian Game: Two Knights Defense, Keidansky Variation",
        ),
        "2kr3r/ppp2ppp/1bn1bPq1/6N1/2ppNPP1/8/PPP4P/R1BQR1K1 w - -": (
            "C55",
            "Italian Game: Two Knights Defense, Max Lange Attack, Berger Variation",
        ),
        "r1bqk2r/pppp1ppp/2n5/2b1P3/2Bp2n1/2P2N2/PP3PPP/RNBQ1RK1 b kq -": (
            "C55",
            "Italian Game: Two Knights Defense, Max Lange Attack, Krause Variation",
        ),
        "r2qk2r/ppp2p1p/2n1bPp1/2b3N1/2pp4/8/PPP2PPP/RNBQR1K1 w kq -": (
            "C55",
            "Italian Game: Two Knights Defense, Max Lange Attack, Loman Defense",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1P3/2Bp4/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C55",
            "Italian Game: Two Knights Defense, Max Lange Attack",
        ),
        "r3kb1r/ppp2ppp/2n1bP2/5qN1/2ppN3/8/PPP2PPP/R1BQR1K1 w kq -": (
            "C55",
            "Italian Game: Two Knights Defense, Max Lange Attack, Rubinstein Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C55",
            "Italian Game: Two Knights Defense, Modern Bishop's Opening",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2BPP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C55",
            "Italian Game: Two Knights Defense, Open Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/6N1/2BpP3/8/PPP2PPP/RNBQK2R b KQkq -": (
            "C55",
            "Italian Game: Two Knights Defense, Perreux Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C55",
            "Italian Game: Two Knights Defense",
        ),
        "r1bqkb1r/pppp1ppp/2n5/4p3/2BPn3/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C55",
            "Italian Game: Two Knights Defense",
        ),
        "r3kb1r/ppp2ppp/2n1b3/3q2B1/3pN3/5N2/PPP2PPP/R2QR1K1 b kq -": (
            "C56",
            "Italian Game: Scotch Gambit, Anderssen Attack, Main Line",
        ),
        "r1b1kb1r/ppp2ppp/2n5/3q4/3pn3/2N2N2/PPP2PPP/R1BQR1K1 b kq -": (
            "C56",
            "Italian Game: Scotch Gambit, Anderssen Attack",
        ),
        "r1bqkb1r/ppp2ppp/2n5/3p4/2Bpn3/2N2N2/PPP2PPP/R1BQR1K1 b kq -": (
            "C56",
            "Italian Game: Scotch Gambit, Canal Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n5/8/2Bpn3/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C56",
            "Italian Game: Scotch Gambit, Double Gambit Accepted",
        ),
        "r1bqkb1r/pppp1ppp/2n5/8/2Bpn3/2N2N2/PPP2PPP/R1BQ1RK1 b kq -": (
            "C56",
            "Italian Game: Scotch Gambit, Nakhmanson Gambit",
        ),
        "r4b1r/ppp1kp2/2n1bN1p/q5p1/1P1p3B/5N2/P1P2PPP/R2QR1K1 b - -": (
            "C56",
            "Italian Game: Two Knights Defense, Yurdansky Attack",
        ),
        "r1bq1b1r/ppn3pp/2p1k3/3np3/2BPQ3/P1N5/1PP2PPP/R1B1K2R w KQ -": (
            "C57",
            "Italian Game: Two Knights Defense, Fegatello Attack, Leonhardt Variation",
        ),
        "r1bqkb1r/ppp2Npp/2n5/3np3/2B5/8/PPPP1PPP/RNBQK2R b KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Fried Liver Attack",
        ),
        "r1bqkb1r/p1p2ppp/8/1p1np3/3nN3/2P5/PP1P1PPP/RNBQKB1R b KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Fritz Variation, Gruber Variation",
        ),
        "r1bqkb1r/ppp2ppp/5n2/3Pp1N1/2Bn4/8/PPPP1PPP/RNBQK2R w KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Fritz Variation",
        ),
        "r1bqkb1r/ppp2ppp/5n2/3Pp1N1/1nB5/8/PPPP1PPP/RNBQK2R w KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Kloss Gambit",
        ),
        "r1bqkb1r/ppp2ppp/2n2n2/3pp1N1/2B1P3/8/PPPP1PPP/RNBQK2R w KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Knight's Attack, Normal Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/4p1N1/2B1P3/8/PPPP1PPP/RNBQK2R b KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Knight's Attack",
        ),
        "r1bqkb1r/ppp2ppp/2n5/3np1N1/2BP4/8/PPP2PPP/RNBQK2R b KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Lolli Attack",
        ),
        "r1bqk2r/ppp2ppp/2n5/3np1N1/1bBP4/8/PPP2PPP/RNBQK2R w KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Pincus Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n5/4p1N1/2B1n3/8/PPPP1PPP/RNBQK2R w KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Ponziani-Steinitz Gambit",
        ),
        "r1bqk2r/pppp1Bpp/2n2n2/2b1p1N1/4P3/8/PPPP1PPP/RNBQK2R b KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Traxler Counterattack, Bishop's Sacrifice Line",
        ),
        "r1bqk2r/pppp1Npp/2n5/4p3/2B1n3/4K3/PPPP2PP/RNBQ3R b kq -": (
            "C57",
            "Italian Game: Two Knights Defense, Traxler Counterattack, King's March Line",
        ),
        "r1bqk2r/pppp1Npp/2n2n2/2b1p3/2B1P3/8/PPPP1PPP/RNBQK2R b KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Traxler Counterattack, Knight's Sacrifice Line",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/2b1p1N1/2B1P3/8/PPPP1PPP/RNBQK2R w KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Traxler Counterattack",
        ),
        "r1bq3r/ppppkBpp/2n2n2/2b1p1N1/3PP3/8/PPP2PPP/RNBQK2R b KQ -": (
            "C57",
            "Italian Game: Two Knights Defense, Traxler Counterattack, Trenčianske Teplice Gambit",
        ),
        "r1bqkb1r/p1p2Np1/2n2n1p/1p1Pp3/8/8/PPPP1PPP/RNBQKB1R b KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Ulvestad Variation, Kurkin Gambit",
        ),
        "r1bqkb1r/p1p2ppp/2n2n2/1p1Pp1N1/2B5/8/PPPP1PPP/RNBQK2R w KQkq -": (
            "C57",
            "Italian Game: Two Knights Defense, Ulvestad Variation",
        ),
        "r1bqkb1r/p4ppp/5n2/np2p1N1/8/5Q2/PPPP1PPP/RNB1K2R w KQkq -": (
            "C58",
            "Italian Game: Two Knights Defense, Blackburne Variation",
        ),
        "1rbqkb1r/p4ppp/2p2n2/nB2p1N1/8/5Q2/PPPP1PPP/RNB1K2R w KQk -": (
            "C58",
            "Italian Game: Two Knights Defense, Colman Variation",
        ),
        "r1bqk2r/ppp1bpp1/5n1p/3P4/2P1p3/5N2/PPP1QPPP/RNB1K2R w KQkq -": (
            "C58",
            "Italian Game: Two Knights Defense, Maróczy Variation",
        ),
        "r1b1kb1r/p1q2ppp/2p2n2/n3p1N1/8/3B1Q2/PPPP1PPP/RNB1K2R b KQkq -": (
            "C58",
            "Italian Game: Two Knights Defense, Paoli Variation",
        ),
        "r1bqkb1r/ppp2ppp/5n2/nB1Pp1N1/8/8/PPPP1PPP/RNBQK2R b KQkq -": (
            "C58",
            "Italian Game: Two Knights Defense, Polerio Defense, Bishop's Check Line",
        ),
        "r1bqkb1r/p4ppp/2p2n2/nB2p1N1/8/5Q2/PPPP1PPP/RNB1K2R b KQkq -": (
            "C58",
            "Italian Game: Two Knights Defense, Polerio Defense, Bogoljubov Variation",
        ),
        "r1bqkb1r/ppp2ppp/5n2/n2Pp1N1/2B5/3P4/PPP2PPP/RNBQK2R b KQkq -": (
            "C58",
            "Italian Game: Two Knights Defense, Polerio Defense, Kieseritzky Variation",
        ),
        "r1bqkb1r/ppp2ppp/5n2/n2Pp1N1/2B5/8/PPPP1PPP/RNBQK2R w KQkq -": (
            "C58",
            "Italian Game: Two Knights Defense, Polerio Defense",
        ),
        "r1bqk2r/ppp2pp1/5n1p/2bP4/2P1p3/8/PPPNQPPP/RNB1K2R b KQkq -": (
            "C58",
            "Italian Game: Two Knights Defense, Polerio Defense, Yankovich Variation",
        ),
        "r1bqkb1r/p4ppp/2p2n2/n3p1N1/8/8/PPPPBPPP/RNBQK2R b KQkq -": (
            "C58",
            "Italian Game: Two Knights Defense",
        ),
        "r1b1k2r/p1q2pp1/2pb1n1p/n3N3/3Pp3/8/PPPBBPPP/RN1QK2R b KQkq -": (
            "C59",
            "Italian Game: Two Knights Defense, Knorre Variation",
        ),
        "r1b1kb1r/p1q2pp1/2p2n1p/n3N3/4p3/8/PPPPBPPP/RNBQK2R w KQkq -": (
            "C59",
            "Italian Game: Two Knights Defense, Polerio Defense, Göring Variation",
        ),
        "r1bqkb1r/p4pp1/2p2n1p/n3p1N1/8/8/PPPPBPPP/RNBQK2R w KQkq -": (
            "C59",
            "Italian Game: Two Knights Defense, Polerio Defense, Suhle Defense",
        ),
        "r1bqkb1r/p4pp1/2p2n1p/n3p3/8/7N/PPPPBPPP/RNBQK2R b KQkq -": (
            "C59",
            "Italian Game: Two Knights Defense, Steinitz Variation",
        ),
        "r1bqk1nr/ppp2ppp/2p5/b3p3/4P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Alapin Defense, Alapin Gambit",
        ),
        "r1bqk1nr/pppp1ppp/2n5/1B2p3/1b2P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Alapin Defense",
        ),
        "r1bqkbnr/pppp1p1p/2n5/1B2p1p1/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Brentano Gambit",
        ),
        "r1bqkbnr/1ppp1ppp/2n5/pB2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Bulgarian Variation",
        ),
        "r1bqkb1r/ppppnp1p/2n3p1/1B2p3/4P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Cozio Defense, Paulsen Variation",
        ),
        "r1bqkb1r/ppppnppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Cozio Defense",
        ),
        "r1bq1rk1/ppp1npbp/2n3p1/1B1p4/3NP3/2N1B3/PPPQ1PPP/R3K2R w KQ -": (
            "C60",
            "Ruy López Opening: Cozio Defense, Tartakower Gambit",
        ),
        "r1bqkbnr/pppp1p1p/2n3p1/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Fianchetto Defense",
        ),
        "r1bqk1nr/ppppbppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Lucena Variation",
        ),
        "r1bqkbnr/pppp2pp/2n2p2/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Nürnberg Variation",
        ),
        "r1bqkbnr/pppp1ppp/8/nB2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Pollock Defense",
        ),
        "r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C60",
            "Ruy López Opening",
        ),
        "rnbqkbnr/pppp1ppp/8/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Retreat Variation",
        ),
        "r1bqkbnr/p1pp1ppp/1pn5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Rotary-Albany Gambit",
        ),
        "r1b1kbnr/ppp2ppp/2n5/1B1pN1q1/4P3/8/PPPP1PPP/RNBQ1RK1 b kq -": (
            "C60",
            "Ruy López Opening: Spanish Countergambit, Harding Countergambit, Fricke Gambit",
        ),
        "r1b1kbnr/ppp2ppp/2N5/1B1p2q1/4P3/8/PPPP1PPP/RNBQK2R b KQkq -": (
            "C60",
            "Ruy López Opening: Spanish Countergambit, Harding Gambit",
        ),
        "r1bqkbnr/ppp2ppp/2n5/1B1pp3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Spanish Countergambit",
        ),
        "r1b1kbnr/ppppqppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Vinogradov Variation",
        ),
        "r1bqkbnr/pppp3p/2n3p1/1B2pp2/4P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C60",
            "Ruy López Opening: Fianchetto Defense, Kevitz Gambit",
        ),
        "r1bqkb1r/ppppnppp/8/1B6/3pP3/8/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C61",
            "Ruy López Opening: Bird Variation, Paulsen Variation",
        ),
        "r1bqkbnr/pppp1ppp/8/1B2p3/3nP3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C61",
            "Ruy López Opening: Bird Variation",
        ),
        "r2qkbnr/pppb1ppp/2np4/1B2p3/2PPP3/5N2/PP3PPP/RNBQK2R b KQkq -": (
            "C62",
            "Ruy López Opening: Old Steinitz Defense, Semi-Duras Variation",
        ),
        "r1bqkbnr/ppp2ppp/2np4/1B6/3pP3/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C62",
            "Ruy López Opening: Steinitz Defense, Center Gambit",
        ),
        "r2qkb1r/pppb1ppp/2Bp1n2/4p3/3PP3/2N2N2/PPP2PPP/R1BQK2R b KQkq -": (
            "C62",
            "Ruy López Opening: Steinitz Defense, Nimzowitsch Attack",
        ),
        "r1bqkbnr/ppp2ppp/2np4/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C62",
            "Ruy López Opening: Steinitz Defense",
        ),
        "r1b1kbnr/ppp3pp/2N5/1B4q1/4p3/8/PPPP1PPP/R1BQK2R w KQkq -": (
            "C63",
            "Ruy López Opening: Schliemann Defense, Classical Variation",
        ),
        "r1bqkbnr/pppp2pp/2n5/1B2pp2/4P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -": (
            "C63",
            "Ruy López Opening: Schliemann Defense, Dyckhoff Variation",
        ),
        "r1bqkbnr/pppp2pp/2B5/4pp2/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C63",
            "Ruy López Opening: Schliemann Defense, Exchange Variation",
        ),
        "r1bqkbnr/pppp2pp/2n5/1B2pP2/8/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C63",
            "Ruy López Opening: Schliemann Defense, Jaenisch Gambit Accepted",
        ),
        "r1bqk1nr/ppppb1pp/2n5/1B2p3/4N3/5N2/PPPP1PPP/R1BQK2R w KQkq -": (
            "C63",
            "Ruy López Opening: Schliemann Defense, Kostić Defense",
        ),
        "r1b1kbnr/ppp3pp/2N5/1B1q4/4p3/8/PPPP1PPP/R1BQK2R w KQkq -": (
            "C63",
            "Ruy López Opening: Schliemann Defense, Möhring Variation",
        ),
        "r1bqkbnr/pppp2pp/2n5/1B2pp2/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C63",
            "Ruy López Opening: Schliemann Defense",
        ),
        "r1bqkbnr/pppp2pp/2n5/1B2pp2/3PP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C63",
            "Ruy López Opening: Schliemann Defense, Schönemann Attack",
        ),
        "r1bqkb1r/pppp2pp/2n2n2/1B2p3/4N3/5N2/PPPP1PPP/R1BQK2R w KQkq -": (
            "C63",
            "Ruy López Opening: Schliemann Defense, Tartakower Variation",
        ),
        "r1bq1rk1/pppp1ppp/1bn2n2/1B2p3/3PP3/2P2N2/PP3PPP/RNBQ1RK1 w - -": (
            "C64",
            "Ruy López Opening: Classical Defense, Benelux Variation",
        ),
        "r1b1k1nr/ppppqppp/2n5/1Bb1p3/4P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C64",
            "Ruy López Opening: Classical Defense, Boden Variation",
        ),
        "r1bqk1nr/pppp1ppp/8/1Bb1p3/1P1nP3/5N2/P1PP1PPP/RNBQ1RK1 b kq -": (
            "C64",
            "Ruy López Opening: Classical Defense, Zaitsev Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/1Bb1p3/4P3/2P2N2/PP1P1PPP/RNBQK2R b KQkq -": (
            "C64",
            "Ruy López Opening: Classical Variation, Central Variation",
        ),
        "r1bqk1nr/pppp1ppp/1bn5/1B2p3/4P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C64",
            "Ruy López Opening: Classical Variation, Charousek Variation",
        ),
        "r1bqk1nr/pppp2pp/2n5/1Bb1pp2/4P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C64",
            "Ruy López Opening: Classical Variation, Cordel Gambit",
        ),
        "r1bqk1nr/ppp2ppp/2n5/1Bbpp3/4P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C64",
            "Ruy López Opening: Classical Variation, Konikowski Gambit",
        ),
        "r1bq1rk1/pppp1ppp/1bn2n2/1B2p1B1/3PP3/2P2N2/PP3PPP/RN1Q1RK1 b - -": (
            "C64",
            "Ruy López Opening: Classical Variation, Modern Main Line",
        ),
        "r1bqk1nr/pppp1ppp/2n5/1Bb1p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C64",
            "Ruy López Opening: Classical Variation",
        ),
        "r1bqk1nr/pppp1ppp/2n5/1Bb1p3/1P2P3/5N2/P1PP1PPP/RNBQK2R b KQkq -": (
            "C64",
            "Ruy López Opening: Classical Variation, Spanish Wing Gambit",
        ),
        "r1bqkb1r/ppp2ppp/2Bp1n2/4p3/4P3/3P1N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C65",
            "Ruy López Opening: Berlin Defense, Anderssen Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/1Bb1p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C65",
            "Ruy López Opening: Berlin Defense, Beverwijk Variation",
        ),
        "r1bqkb1r/ppp2ppp/2np1n2/1B2p3/2P1P3/3P1N2/PP3PPP/RNBQK2R b KQkq -": (
            "C65",
            "Ruy López Opening: Berlin Defense, Duras Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n5/1B2p3/4P1n1/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C65",
            "Ruy López Opening: Berlin Defense, Fishing Pole Variation",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/1Bb1p3/4P3/3PBN2/PPP2PPP/RN1QK2R b KQkq -": (
            "C65",
            "Ruy López Opening: Berlin Defense, Kaufmann Variation",
        ),
        "r1bqkb1r/pp1pnppp/2p2n2/1B2N3/4P3/3P4/PPP2PPP/RNBQK2R w KQkq -": (
            "C65",
            "Ruy López Opening: Berlin Defense, Mortimer Trap",
        ),
        "r1bqkb1r/ppppnppp/5n2/1B2p3/4P3/3P1N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C65",
            "Ruy López Opening: Berlin Defense, Mortimer Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/1B6/3pP3/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C65",
            "Ruy López Opening: Berlin Defense, Nyholm Attack",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 b kq -": (
            "C65",
            "Ruy López Opening: Berlin Defense",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C65",
            "Ruy López Opening: Berlin Defense",
        ),
        "r1bqk2r/pppp1ppp/2n2n2/1Bb1p3/4P3/2P2N2/PP1P1PPP/RNBQ1RK1 b kq -": (
            "C65",
            "Ruy López Opening: Classical Variation, Zukertort Gambit",
        ),
        "r1bqkb1r/pppp1ppp/2n2n2/1B2N3/4P3/8/PPPP1PPP/RNBQK2R b KQkq -": (
            "C65",
            "Ruy López Opening: Halloween Attack",
        ),
        "r2qk2r/pppbbppp/2np1n2/1B2p1B1/3PP3/2N2N2/PPP2PPP/R2Q1RK1 b kq -": (
            "C66",
            "Ruy López Opening: Berlin Defense, Closed Bernstein Variation",
        ),
        "r2qk2r/pppbbppp/2Bp1n2/4p3/3PP3/2N2N2/PPP2PPP/R1BQ1RK1 b kq -": (
            "C66",
            "Ruy López Opening: Berlin Defense, Closed Showalter Variation",
        ),
        "r2qkb1r/pppb1ppp/2np1n2/1B6/3pP3/2N2N2/PPP2PPP/R1BQ1RK1 w kq -": (
            "C66",
            "Ruy López Opening: Berlin Defense, Closed Wolf Variation",
        ),
        "r2qk2r/pppbbppp/2np1n2/1B2p3/3PP3/2N2N2/PPP2PPP/R1BQ1RK1 w kq -": (
            "C66",
            "Ruy López Opening: Berlin Defense, Hedgehog Variation",
        ),
        "r1bqkb1r/ppp2ppp/2np1n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C66",
            "Ruy López Opening: Berlin Defense, Improved Steinitz Defense",
        ),
        "r2q1rk1/pppbbppp/2np1n2/1B2p3/3PP3/2N2N2/PPP2PPP/R1BQR1K1 w - -": (
            "C66",
            "Ruy López Opening: Berlin Defense, Tarrasch Trap",
        ),
        "r1bqkb1r/pppn1ppp/2np4/1B2p3/3PP3/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C66",
            "Ruy López Opening: Closed Berlin Defense, Chigorin Variation",
        ),
        "r2k1b1r/pppb1ppp/2p5/4Pn2/8/2N2N2/PPP2PPP/R1B2RK1 w - -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Berlin Wall",
        ),
        "r1bqk2r/p1ppbppp/2p5/4Pn2/8/5N2/PPP1QPPP/RNB2RK1 w kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Cordel Variation",
        ),
        "r1bk1b1r/ppp2ppp/2p5/4Pn2/8/5N2/PPP2PPP/RNB2RK1 w - -": (
            "C67",
            "Ruy López Opening: Berlin Defense, l'Hermet Variation, Berlin Wall Defense",
        ),
        "r1bqkb1r/pppp1ppp/2nn4/1B2p3/3P4/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, l'Hermet Variation",
        ),
        "r1bqkb1r/ppp2ppp/2p5/4P3/4n3/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, l'Hermet Variation, Westerinen Line",
        ),
        "r1bqk2r/ppppbppp/2n5/1B2P3/4n3/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Minckwitz Variation",
        ),
        "r1bqk2r/pnppbppp/2p5/4P3/8/1P3N2/P1P1QPPP/RNB2RK1 b kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Pillsbury Variation",
        ),
        "r1bq1rk1/p1ppbppp/8/2p1P3/3B4/2N5/PPP1QPPP/R3R1K1 w - -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Rio de Janeiro Variation",
        ),
        "r1bqk2r/ppppbppp/2n5/1B2p3/3Pn3/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Rio de Janeiro Variation",
        ),
        "r1bqkb1r/pppp1ppp/2n5/1B2p3/4n3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Rio Gambit Accepted",
        ),
        "r1bqkb1r/1ppp1ppp/p1n5/1B2p3/3Pn3/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Rosenthal Variation",
        ),
        "r1bqk2r/ppp1bppp/2n5/1B1pp3/3Pn3/5N2/PPP1QPPP/RNB2RK1 w kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Trifunović Variation",
        ),
        "r1bqk2r/pnppbppp/2p5/4P3/3N4/8/PPP1QPPP/RNB2RK1 b kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Winawer Attack",
        ),
        "r1bqk2r/pnppbppp/2p5/4P3/2P5/5N2/PP2QPPP/RNB2RK1 b kq -": (
            "C67",
            "Ruy López Opening: Berlin Defense, Zukertort Variation",
        ),
        "r1bqkb1r/pppp1ppp/2nn4/1B2P3/8/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C67",
            "Ruy López Opening: Open Berlin Defense, l'Hermet Variation",
        ),
        "r1bqkb1r/pppp1ppp/2nn4/4p3/B2P4/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C67",
            "Ruy López Opening: Open Berlin Defense, Showalter Variation",
        ),
        "r3kbnr/1ppb1ppp/p1p5/8/3NP3/8/PPP2PPP/RNB1K2R w KQkq -": (
            "C68",
            "Ruy López Opening: Exchange, Alekhine Variation",
        ),
        "r1b1k1nr/1pp2ppp/p1pb4/8/3NP3/8/PPP2PPP/RNB1K2R w KQkq -": (
            "C68",
            "Ruy López Opening: Exchange Variation, Alekhine Variation",
        ),
        "r1bqkbnr/1pp2ppp/p1p5/4p3/4P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -": (
            "C68",
            "Ruy López Opening: Exchange Variation, Keres Variation",
        ),
        "r1bqkbnr/2pp1ppp/p1p5/4p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C68",
            "Ruy López Opening: Exchange Variation, Lutikov Variation",
        ),
        "r1bqkbnr/1ppp1ppp/p1B5/4p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C68",
            "Ruy López Opening: Exchange Variation",
        ),
        "r1bqkbnr/1pp3pp/p1p2p2/4p3/4P3/2NP1N2/PPP2PPP/R1BQK2R b KQkq -": (
            "C68",
            "Ruy López Opening: Exchange Variation, Romanovsky Variation",
        ),
        "r2qkbnr/1pp2pp1/p1p5/4p2p/4P1b1/5N1P/PPPP1PP1/RNBQ1RK1 w kq -": (
            "C69",
            "Ruy López Opening: Exchange Variation, Alapin Gambit",
        ),
        "r1b1kbnr/1pp2ppp/p1pq4/4p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C69",
            "Ruy López Opening: Exchange Variation, Bronstein Variation",
        ),
        "r1bqkbnr/1pp3pp/p1p2p2/4p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C69",
            "Ruy López Opening: Exchange Variation, Gligorić Variation",
        ),
        "r1bqk1nr/1pp2ppp/p1pb4/4p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C69",
            "Ruy López Opening: Exchange Variation, King's Bishop Variation",
        ),
        "r1bqkbnr/1pp2ppp/p1p5/4p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 b kq -": (
            "C69",
            "Ruy López Opening: Exchange Variation, Normal Variation",
        ),
        "r1bqkbnr/1ppp1ppp/p7/4p3/B2nP3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C70",
            "Ruy López Opening: Deferred Bird Defense",
        ),
        "r1bqkbnr/1ppp1ppp/p1n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense",
        ),
        "r1bqk1nr/1ppp1ppp/p1n5/4p3/Bb2P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense, Deferred Alapin Defense",
        ),
        "r1bqkbnr/2pp1ppp/p1n5/1p2p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense, Caro Variation",
        ),
        "r1bqk1nr/1ppp1ppp/p1n5/2b1p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense, Deferred Classical Defense",
        ),
        "r1bqkb1r/1pppnppp/p1n5/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense, Cozio Defense",
        ),
        "r1bqkbnr/1ppp1p1p/p1n3p1/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense, Deferred Fianchetto Defense",
        ),
        "r1bqk1nr/2pp1ppp/p1n5/1pb1p3/4P3/1B3N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense, Graz Variation",
        ),
        "r1bqkbnr/2pp1Bpp/p7/np2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense, Norwegian Variation, Nightingale Gambit",
        ),
        "r1bqkbnr/2pp1ppp/p7/np2p3/4P3/1B3N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense, Norwegian Variation",
        ),
        "r1bqkbnr/1ppp2pp/p1n5/4pP2/B7/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense, Deferred Schliemann Defense, Deferred Jaenisch Gambit",
        ),
        "r1bqkbnr/1ppp2pp/p1n5/4pp2/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C70",
            "Ruy López Opening: Morphy Defense, Deferred Schliemann Defense",
        ),
        "r1bqkbnr/1pp2ppp/p1np4/4p3/B1P1P3/5N2/PP1P1PPP/RNBQK2R b KQkq -": (
            "C71",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense",
        ),
        "r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -": (
            "C71",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense",
        ),
        "r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq -": (
            "C71",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense",
        ),
        "r1bqkbnr/5ppp/p2p4/1pp5/3QP3/1B6/PPP2PPP/RNB1K2R w KQkq -": (
            "C71",
            "Ruy López Opening: Noah's Ark Trap",
        ),
        "r2qbrk1/1pp1bppp/p1np1n2/4p3/B2PP3/2P2N2/PP1N1PPP/R1BQR1K1 w - -": (
            "C72",
            "Ruy López Opening: Closed Defense, Kecskemet Variation",
        ),
        "r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/5N2/PPPP1PPP/RNBQ1RK1 b kq -": (
            "C72",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense",
        ),
        "r1bqkbnr/2p2ppp/p1pp4/4p3/3PP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C73",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense",
        ),
        "r1bqkbnr/2p3pp/p1pp1p2/4p3/3PP3/5N2/PPP2PPP/RNBQK2R w KQkq -": (
            "C73",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense",
        ),
        "r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/2P2N2/PP1P1PPP/RNBQK2R b KQkq -": (
            "C74",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense",
        ),
        "r2qkbnr/1pp3pp/p1np4/4pb2/B7/2P2N2/PP1P1PPP/RNBQ1RK1 b kq -": (
            "C74",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense",
        ),
        "r1bqkbnr/1pp3pp/p1np4/4pp2/B3P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C74",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense, Siesta Variation",
        ),
        "r2qkb1r/1ppbnppp/p1np4/4p3/B2PP3/2P2N2/PP3PPP/RNBQK2R w KQkq -": (
            "C75",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense",
        ),
        "r2qkbnr/1ppb1ppp/p1np4/4p3/B3P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq -": (
            "C75",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense",
        ),
        "r2qkbnr/1ppb1p1p/p1np2p1/4p3/B2PP3/2P2N2/PP3PPP/RNBQK2R w KQkq -": (
            "C76",
            "Ruy López Opening: Morphy Defense, Modern Steinitz Defense, Fianchetto Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/3P1N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C77",
            "Ruy López Opening: Morphy Defense, Anderssen Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1B2n2/4p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq -": (
            "C77",
            "Ruy López Opening: Morphy Defense, Bayreuth Variation",
        ),
        "r1bqkb1r/1pp2ppp/p1np1n2/4p3/B1P1P3/3P1N2/PP3PPP/RNBQK2R b KQkq -": (
            "C77",
            "Ruy López Opening: Morphy Defense, Duras Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/2P2N2/PP1P1PPP/RNBQK2R b KQkq -": (
            "C77",
            "Ruy López Opening: Morphy Defense, Jaffe Gambit",
        ),
        "r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B2PP3/5N2/PPP2PPP/RNBQK2R b KQkq -": (
            "C77",
            "Ruy López Opening: Morphy Defense, Mackenzie Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -": (
            "C77",
            "Ruy López Opening: Morphy Defense, Tarrasch Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/5N2/PPPPQPPP/RNB1K2R b KQkq -": (
            "C77",
            "Ruy López Opening: Morphy Defense, Wormald Attack",
        ),
        "r2qk2r/2p1bppp/p1np1n2/1p2p3/3PP1b1/1BP2N2/PP2QPPP/RNB1K2R w KQkq -": (
            "C77",
            "Ruy López Opening: Wormald Attack, Grünfeld Variation",
        ),
        "r1bqkb1r/1ppp1p1p/p1n2np1/4p3/B3P3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C78",
            "Ruy López Opening: Brix Variation",
        ),
        "r1bqkb1r/1pp2ppp/p1n2n2/3pp3/B3P3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C78",
            "Ruy López Opening: Central Countergambit",
        ),
        "r2qkb1r/1bpp1ppp/p1n2n2/1p2p3/4P3/1B3N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C78",
            "Ruy López Opening: Morphy Defense, Arkhangelsk Variation",
        ),
        "r1bqk2r/1ppp1ppp/p1n2n2/2b1p3/B3P3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C78",
            "Ruy López Opening: Morphy Defense, Neo-Arkhangelsk Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/5N2/PPPP1PPP/RNBQ1RK1 b kq -": (
            "C78",
            "Ruy López Opening: Morphy Defense",
        ),
        "r1bqkb1r/2p2ppp/p1np1n2/1p2p3/4P3/1B3N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C78",
            "Ruy López Opening: Morphy Defense",
        ),
        "r1bqk2r/2ppbppp/p1n2n2/1p2p3/P3P3/1B3N2/1PPP1PPP/RNBQ1RK1 b kq -": (
            "C78",
            "Ruy López Opening: Morphy Defense, Wing Attack",
        ),
        "r1bq1k1r/2p2ppp/p4n2/1pbPR1N1/3n4/1B6/PPPP1PPP/RNBQ2K1 w - -": (
            "C78",
            "Ruy López Opening: Rabinovich Variation",
        ),
        "r1bqkb1r/1pp2ppp/p1np1n2/4p3/B3P3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C79",
            "Ruy López Opening: Morphy Defense, Deferred Steinitz Defense",
        ),
        "r1bqkb1r/2p2ppp/p1pp4/4p3/3Pn3/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C79",
            "Ruy López Opening: Morphy Defense, Deferred Steinitz Defense",
        ),
        "r1bqkb1r/2p3pp/p1p5/3pPp2/4n3/2N2N2/PPP2PPP/R1BQR1K1 b kq -": (
            "C79",
            "Ruy López Opening: Deferred Steinitz Defense, Boleslavsky Variation",
        ),
        "r2qkb1r/2p2ppp/p1pp1n2/4p3/3PP1b1/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C79",
            "Ruy López Opening: Deferred Steinitz Defense, Lipnitsky Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1n5/4p3/B3n3/5N2/PPPPQPPP/RNB2RK1 b kq -": (
            "C80",
            "Ruy López Opening: Morphy Defense, Tartakower Variation",
        ),
        "r1bqkb1r/2p2ppp/p7/1p1p4/P2pn3/1BN5/1PP2PPP/R1BQ1RK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Berger Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1n5/4p3/B3n3/2N2N2/PPPP1PPP/R1BQ1RK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Knorre Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1n5/4p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Variation",
        ),
        "r2qk2r/2p2ppp/p1n1b3/1pbpP3/4n3/1B3N2/PPPN1PPP/R1B1QRK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Bernstein Variation, Luther Line",
        ),
        "r2qkb1r/2p2ppp/p1n1b3/1p1pP3/4n3/1B3N2/PPPN1PPP/R1BQ1RK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Bernstein Variation",
        ),
        "r1bqkb1r/2pp1ppp/p1n5/1p2N3/B2Pn3/8/PPP2PPP/RNBQ1RK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Friess Attack",
        ),
        "r1bqkb1r/2p2ppp/p1n5/1p1pp3/2PPn3/1B3N2/PP3PPP/RNBQ1RK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Harksen Gambit",
        ),
        "r2qkb1r/2p2ppp/p1n1b3/1pn1P1N1/3p4/1BP5/PP1N1PPP/R1BQ1RK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Karpov Gambit",
        ),
        "r1bqkb1r/1pp2ppp/p1n5/3pp3/B3n3/5N2/PPPP1PPP/RNBQR1K1 w kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Skipworth Gambit",
        ),
        "r2qkb1r/2p2ppp/p1n1b3/1p1pP3/4n3/1B3N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Main Line",
        ),
        "r1bqkb1r/1ppp1ppp/p1n5/4p3/B3n3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C80",
            "Ruy López Opening: Open Variation",
        ),
        "r1bqkb1r/2p2ppp/p1n5/1p1pP3/4n3/1B3N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Variation",
        ),
        "r1bqkb1r/2pp1ppp/p1n5/1p2p3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Variation",
        ),
        "r1bqkb1r/2pp1ppp/p1n5/1p1Pp3/B3n3/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Richter Variation",
        ),
        "r1bqkb1r/1ppp1ppp/p1n5/8/B2pn3/5N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Riga Variation",
        ),
        "r1bqkb1r/2p2ppp/p7/1p1pp3/P2nn3/1B3N2/1PP2PPP/RNBQ1RK1 w kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Schlechter Defense",
        ),
        "r1bqkb1r/2p1nppp/p7/1p1pP3/4n3/1B3N2/PPP2PPP/RNBQ1RK1 w kq -": (
            "C80",
            "Ruy López Opening: Open Defense, Zukertort Variation",
        ),
        "r4rk1/2pqbppp/p1n1b3/3pP3/2B1n3/5N2/PP2QPPP/RNBR2K1 w - -": (
            "C81",
            "Ruy López Opening: Open Defense, Howell Attack, Ekstrom Variation",
        ),
        "r2qk2r/2p1bppp/p1n1b3/1p1pP3/2P1n3/1B3N2/PP2QPPP/RNB2RK1 b kq -": (
            "C81",
            "Ruy López Opening: Open Defense, Howell Attack",
        ),
        "r2qkb1r/2p2ppp/p1n1b3/1p1pP3/4n3/1B3N2/PPP1QPPP/RNB2RK1 b kq -": (
            "C81",
            "Ruy López Opening: Open Defense, Howell Attack",
        ),
        "r2qk2r/2p1nppp/p3b3/1pbpP3/4n3/1BPQ1N2/PP3PPP/RNB2RK1 w kq -": (
            "C82",
            "Ruy López Opening: Open Defense, Motzko Attack, Nenarokov Variation",
        ),
        "r2qkb1r/2p2ppp/p1n1b3/1p1pP3/4n3/1BP2N2/PP3PPP/RNBQ1RK1 b kq -": (
            "C82",
            "Ruy López Opening: Open Variation",
        ),
        "r2qkb1r/2p2ppp/p1n1b3/1pnpP3/8/1BP2N2/PP3PPP/RNBQ1RK1 w kq -": (
            "C82",
            "Ruy López Opening: Open Defense, Berlin Variation",
        ),
        "r2q1rk1/2p2ppp/p1n1b3/1pbpP3/8/2P2N2/PPBN1nPP/R1BQ1RK1 w - -": (
            "C82",
            "Ruy López Opening: Open Defense, Dilworth Variation",
        ),
        "r2qk2r/2p2ppp/p1n1b3/1pbpP3/4n3/1BP2N2/PP3PPP/RNBQ1RK1 w kq -": (
            "C82",
            "Ruy López Opening: Open Defense, Italian Variation",
        ),
        "r2qk2r/2p2ppp/p1n1b3/1pbpP3/4n3/1BPQ1N2/PP3PPP/RNB2RK1 b kq -": (
            "C82",
            "Ruy López Opening: Open Defense, Motzko Attack",
        ),
        "r2qk2r/2p2ppp/p1n1b3/1pbpP3/4n3/1BP2N2/PP1N1PPP/R1BQ1RK1 b kq -": (
            "C82",
            "Ruy López Opening: Open Defense, St. Petersburg Variation",
        ),
        "r4rk1/2pqb1pp/p1n1p3/1p1pP3/4R3/1BP5/PP3PPP/RNBQ2K1 b - -": (
            "C83",
            "Ruy López Opening: Open Defense, Tarrasch Trap",
        ),
        "r2q1rk1/2p1bppp/p3b3/1p1pn3/3Nn3/1BP5/PP3PPP/RNBQR1K1 w - -": (
            "C83",
            "Ruy López Opening: Open Defense, Breslau Variation",
        ),
        "r2qk2r/2p1bppp/p1n1b3/1p1pP3/4n3/1BP2N2/PP3PPP/RNBQR1K1 b kq -": (
            "C83",
            "Ruy López Opening: Open Defense, Classical Defense, Main Line",
        ),
        "r2qk2r/2p1bppp/p1n1b3/1p1pP3/4n3/1BP2N2/PP3PPP/RNBQ1RK1 w kq -": (
            "C83",
            "Ruy López Opening: Open Defense, Classical Defense",
        ),
        "r2q1rk1/2p1bppp/p1n1b3/1p1pP3/4n3/1BP2N2/PP1NQPPP/R1B2RK1 b - -": (
            "C83",
            "Ruy López Opening: Open Defense, Malkin Variation",
        ),
        "r1bqk2r/1pppbppp/p1n5/4P3/B2pn3/2P2N2/PP3PPP/RNBQ1RK1 b kq -": (
            "C84",
            "Ruy López Opening: Closed Defense, Basque Gambit (North Spanish Variation)",
        ),
        "r1bqk2r/1pppbppp/p1n5/4P3/B3n3/2p2N2/PP3PPP/RNBQ1RK1 w kq -": (
            "C84",
            "Ruy López Opening: Closed Defense, Center Attack, Basque Gambit",
        ),
        "r1bqk2r/1pppbppp/p1n2n2/4p3/B2PP3/5N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C84",
            "Ruy López Opening: Closed Defense, Center Attack",
        ),
        "r1bqk2r/1pppbppp/p1n2n2/4p3/B3P3/3P1N2/PPP2PPP/RNBQ1RK1 b kq -": (
            "C84",
            "Ruy López Opening: Closed Defense, Martinez Variation",
        ),
        "r1bqk2r/1pppbppp/p1n2n2/4p3/B3P3/2N2N2/PPPP1PPP/R1BQ1RK1 b kq -": (
            "C84",
            "Ruy López Opening: Closed Defense, Morphy Attack",
        ),
        "r1bqk2r/1pppbppp/p1n2n2/4p3/B3P3/5N2/PPPP1PPP/RNBQ1RK1 w kq -": (
            "C84",
            "Ruy López Opening: Closed Defense",
        ),
        "r1bqk2r/1pppbppp/p1B2n2/4p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 b kq -": (
            "C85",
            "Ruy López Opening: Closed Defense, Delayed Exchange Variation",
        ),
        "r1bq1rk1/2ppbppp/p1n2n2/1p2p3/4P3/1B3N2/PPPPQPPP/RNB2RK1 w - -": (
            "C86",
            "Ruy López Opening: Closed Defense, Worrall Attack, Castling Line",
        ),
        "r1bqk2r/2p1bppp/p1np1n2/1p2p3/4P3/1B3N2/PPPPQPPP/RNB2RK1 w kq -": (
            "C86",
            "Ruy López Opening: Closed Defense, Worrall Attack, Delayed Castling Line",
        ),
        "r1bqk2r/1pppbppp/p1n2n2/4p3/B3P3/5N2/PPPPQPPP/RNB2RK1 b kq -": (
            "C86",
            "Ruy López Opening: Closed Defense, Worrall Attack",
        ),
        "r1bqk2r/1pp1bppp/p1np1n2/4p3/B3P3/5N2/PPPP1PPP/RNBQR1K1 w kq -": (
            "C87",
            "Ruy López Opening: Closed Defense, Averbakh Variation",
        ),
        "r1bq1rk1/2ppbppp/p1n2n2/1p2p3/P3P3/1B3N2/1PPP1PPP/RNBQR1K1 b - -": (
            "C88",
            "Ruy López Opening: Closed Defense, Anti-Marshall Variation",
        ),
        "r4rk1/2q1bppp/p2p1n2/npp1p3/3PP3/2P1NQ2/PPB2PPP/R1B1R1K1 b - -": (
            "C88",
            "Ruy López Opening: Closed Defense, Alekhine Gambit",
        ),
        "rnb1k2r/2q1bp1p/p2p1n2/1ppPp1p1/4P3/2P2N1P/PPBN1PP1/R1BQR1K1 w kq -": (
            "C88",
            "Ruy López Opening: Closed Defense, Leonhardt Variation",
        ),
        "r1bq1rk1/2ppbppp/p1n2n2/1p2p3/4P3/1B3N2/PPPP1PPP/RNBQR1K1 w - -": (
            "C88",
            "Ruy López Opening: Closed Defense",
        ),
        "r1bqk2r/2ppbppp/p1n2n2/1p2p3/4P3/1B3N2/PPPP1PPP/RNBQR1K1 b kq -": (
            "C88",
            "Ruy López Opening: Closed Defense",
        ),
        "r1b1k2r/2q1bppp/p2p1n2/npp1p3/P2PP3/2P2N2/1PB2PPP/RNBQR1K1 b kq -": (
            "C88",
            "Ruy López Opening: Closed Defense, Balla Variation",
        ),
        "r1bqk2r/2p1bppp/p1np1n2/1p2p3/3PP3/1B3N2/PPP2PPP/RNBQR1K1 b kq -": (
            "C88",
            "Ruy López Opening: Closed Defense, Rosen Attack",
        ),
        "r2qk2r/1bppbppp/p1n2n2/1p2p3/4P3/1B3N2/PPPP1PPP/RNBQR1K1 w kq -": (
            "C88",
            "Ruy López Opening: Closed Defense, Trajković Counterattack",
        ),
        "r1bqk2r/4bppp/p2p1n2/1pp5/3QP3/1B6/PPP2PPP/RNB1R1K1 w kq -": (
            "C88",
            "Ruy López Opening: Noah's Ark Trap",
        ),
        "r1bq1rk1/4bppp/p1p5/1p1nR3/3P4/1BP5/PP3PPP/RNBQ2K1 b - -": (
            "C89",
            "Ruy López Opening: Marshall Attack, Main Line",
        ),
        "r1b2rk1/5ppp/p1pb4/1p1n4/3P4/1BP3Pq/PP3P1P/RNBQR1K1 w - -": (
            "C89",
            "Ruy López Opening: Marshall Attack, Modern Main Line",
        ),
        "r1bq1rk1/4bppp/p1p5/1p1nR3/8/1BP5/PP1P1PPP/RNBQ2K1 w - -": (
            "C89",
            "Ruy López Opening: Marshall Attack, Modern Variation",
        ),
        "r1bq1rk1/2p1bppp/p4n2/1p2R3/8/1BP5/PP1P1PPP/RNBQ2K1 w - -": (
            "C89",
            "Ruy López Opening: Marshall Attack, Original Marshall Attack",
        ),
        "r1bq1rk1/2p1bppp/p1n2n2/1p1pp3/4P3/1BP2N2/PP1P1PPP/RNBQR1K1 w - -": (
            "C89",
            "Ruy López Opening: Marshall Attack",
        ),
        "r1bq1rk1/5ppp/p2b4/1p1p4/3P4/2P1R3/PP3PPP/RNBQ2K1 b - -": (
            "C89",
            "Ruy López Opening: Marshall Attack, Re3 Variation",
        ),
        "r1bq1rk1/2p1bppp/p1n2n2/1p1P4/4p3/1BP2N2/PP1P1PPP/RNBQR1K1 w - -": (
            "C89",
            "Ruy López Opening: Marshall Attack, Steiner Variation",
        ),
        "5rk1/5ppp/p1pbr3/1p1n3q/P2P2b1/1BPQB1P1/1P1N1P1P/R3R1K1 w - -": (
            "C89",
            "Ruy López Opening: Marshall Attack, Main Line, Spassky Variation",
        ),
        "r1bq1rk1/2p1bppp/p1np1n2/1p2p3/4P3/1BP2N2/PP1P1PPP/RNBQR1K1 w - -": (
            "C90",
            "Ruy López Opening: Closed Defense, Closed Variation",
        ),
        "r1bq1rk1/2p1bppp/p1np1n2/1p2p3/4P3/2P2N2/PPBP1PPP/RNBQR1K1 b - -": (
            "C90",
            "Ruy López Opening: Closed Defense, Lutikov Variation",
        ),
        "r1bq1rk1/2p1bppp/p1np1n2/1p2p3/4P3/1BPP1N2/PP3PPP/RNBQR1K1 b - -": (
            "C90",
            "Ruy López Opening: Closed Defense, Pilnik Variation",
        ),
        "r1bq1rk1/2p1bppp/p1np1n2/1p2p3/4P3/PBP2N2/1P1P1PPP/RNBQR1K1 b - -": (
            "C90",
            "Ruy López Opening: Closed Defense, Suetin Variation",
        ),
        "r2q1rk1/2p1bppp/p1np1n2/1p2p3/3PP1b1/1BP2N2/PP3PPP/RNBQR1K1 w - -": (
            "C91",
            "Ruy López Opening: Closed Defense, Bogoljubov Variation",
        ),
        "r1bq1rk1/2p1bppp/p1np1n2/1p2p3/3PP3/1BP2N2/PP3PPP/RNBQR1K1 b - -": (
            "C91",
            "Ruy López Opening: Closed Defense, Yates Variation",
        ),
        "r2q1rk1/2p1bppp/p1np1n2/1p2p3/P2PP1b1/1BP2N2/1P3PPP/RNBQR1K1 b - -": (
            "C91",
            "Ruy López Opening: Closed Defense, Yates Variation, Short Attack",
        ),
        "r2q1rk1/1bp1bppp/p1np1n2/1p2p3/4P3/1BP2N1P/PP1P1PP1/RNBQR1K1 w - -": (
            "C92",
            "Ruy López Opening: Closed Defense, Flohr System",
        ),
        "r1bq1rk1/2p1bppp/2np1n2/pp2p3/4P3/1BP2N1P/PP1P1PP1/RNBQR1K1 w - -": (
            "C92",
            "Ruy López Opening: Closed Defense, Keres Defense",
        ),
        "r1bq1rk1/2pnbppp/p1np4/1p2p3/4P3/1BP2N1P/PP1P1PP1/RNBQR1K1 w - -": (
            "C92",
            "Ruy López Opening: Closed Defense, Keres Defense",
        ),
        "r2q1rk1/2p1bppp/p1npbn2/1p2p3/4P3/1BP2N1P/PP1P1PP1/RNBQR1K1 w - -": (
            "C92",
            "Ruy López Opening: Closed Defense, Kholmov Variation",
        ),
        "r1bq1rk1/2p1bppp/p1np1n2/1p2p3/4P3/1BP2N1P/PP1P1PP1/RNBQR1K1 b - -": (
            "C92",
            "Ruy López Opening: Closed Defense",
        ),
        "r2qrbk1/1bp2pp1/p1np1n1p/1p2p3/3PP3/PBP2N1P/1P1N1PP1/R1BQR1K1 w - -": (
            "C92",
            "Ruy López Opening: Closed Defense, Smyslov-Breyer-Zaitsev Hybrid Variation",
        ),
        "r1bqr1k1/2p1bppp/p1np1n2/1p2p3/4P3/1BP2N1P/PP1P1PP1/RNBQR1K1 w - -": (
            "C92",
            "Ruy López Opening: Closed Defense, Zaitsev System",
        ),
        "r1bq1rk1/2p1bpp1/p1np1n1p/1p2p3/4P3/1BP2N1P/PP1P1PP1/RNBQR1K1 w - -": (
            "C93",
            "Ruy López Opening: Closed Defense, Smyslov Defense",
        ),
        "rnbq1rk1/2p1bppp/p2p1n2/1p2p3/4P3/1BPP1N1P/PP3PP1/RNBQR1K1 b - -": (
            "C94",
            "Ruy López Opening: Morphy Defense, Breyer Defense, Quiet Variation",
        ),
        "rnbq1rk1/2p1bppp/p2p1n2/1p2p3/4P3/1BP2N1P/PP1P1PP1/RNBQR1K1 w - -": (
            "C94",
            "Ruy López Opening: Morphy Defense, Breyer Defense",
        ),
        "rnbq1rk1/2p1bppp/p2p1n2/1p2p3/3PP3/1BP2N1P/PP3PP1/RNBQR1K1 b - -": (
            "C95",
            "Ruy López Opening: Closed Defense, Breyer",
        ),
        "r1bq1rk1/2pnbppp/p2p1n2/1p2p3/3PP2N/1BP4P/PP3PP1/RNBQR1K1 b - -": (
            "C95",
            "Ruy López Opening: Closed Defense, Breyer Defense",
        ),
        "r2q1rk1/1b1nbppp/p2p1n2/1pp1p3/3PP3/2P2N1P/PPBN1PP1/R1BQR1K1 w - -": (
            "C95",
            "Ruy López Opening: Closed Defense, Breyer Defense",
        ),
        "r1bq1rk1/2pnbppp/p2p1n2/1p2p3/3PP3/1BP2N1P/PP3PP1/RNBQR1K1 w - -": (
            "C95",
            "Ruy López Opening: Morphy Defense, Breyer Defense, Zaitsev Hybrid Variation",
        ),
        "r1b2rk1/2q1bppp/p1pp1n2/np2p3/3PP3/2P2N1P/PPB2PP1/RNBQR1K1 w - -": (
            "C96",
            "Ruy López Opening: Closed Defense, Rossolimo Defense",
        ),
        "r1bq1rk1/4bppp/p1np1n2/1pp1p3/3PP3/2P2N1P/PPB2PP1/RNBQR1K1 w - -": (
            "C96",
            "Ruy López Opening: Closed Defense, Borisenko Variation",
        ),
        "r1bq1rk1/2p1bppp/p2p1n2/np2p3/4P3/2P2N1P/PPBP1PP1/RNBQR1K1 b - -": (
            "C96",
            "Ruy López Opening: Closed Defense, Closed Variation",
        ),
        "r1bq1rk1/4bppp/p2p1n2/npp1p3/4P3/2P2N1P/PPBP1PP1/RNBQR1K1 w - -": (
            "C96",
            "Ruy López Opening: Closed Defense, Closed Variation",
        ),
        "r1bq1rk1/3nbppp/p2p4/npp1p3/3PP3/2P2N1P/PPB2PP1/RNBQR1K1 w - -": (
            "C96",
            "Ruy López Opening: Closed Defense, Keres Defense",
        ),
        "r3r1k1/2qbbp1p/p2p1np1/npp1p3/3PP3/2P1NN1P/PPB2PP1/R1BQR1K1 w - -": (
            "C97",
            "Ruy López Opening: Closed Defense, Chigorin, Yugoslav System",
        ),
        "r1b2rk1/2q1bppp/p2p1n2/npp1p3/3PP3/2P2N1P/PPB2PP1/RNBQR1K1 w - -": (
            "C97",
            "Ruy López Opening: Closed Defense, Chigorin Defense",
        ),
        "r1b2rk1/2q1bppp/p1np1n2/1pp1p3/3PP3/2P2N1P/PPBN1PP1/R1BQR1K1 w - -": (
            "C98",
            "Ruy López Opening: Closed Defense, Chigorin Defense",
        ),
        "r1b2rk1/2q1bppp/p1np1n2/1pP1p3/4P3/2P2N1P/PPBN1PP1/R1BQR1K1 b - -": (
            "C98",
            "Ruy López Opening: Closed Defense, Chigorin Defense",
        ),
        "r1b2rk1/2q1bppp/p2p1n2/np2p3/3PP3/5N1P/PPBN1PP1/R1BQR1K1 b - -": (
            "C99",
            "Ruy López Opening: Morphy Defense, Chigorin Defense, Panov System",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/3P4/3Q4/PPP1PPPP/RNB1KBNR b KQkq -": (
            "D00",
            "Amazon Attack",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/3PP3/8/PPP2PPP/RNBQKBNR b KQkq -": (
            "D00",
            "Blackmar Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/8/3Pp3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3PP3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit",
        ),
        "rnbqk2r/ppp1ppbp/5np1/8/2BP3P/2N2N2/PPP3P1/R1BQK2R b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Bogoljubov Defense, Mad Dog Attack",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/8/2BP4/2N2N2/PPP3PP/R1BQ1R1K b - -": (
            "D00",
            "Blackmar-Diemer Gambit: Bogoljubov Variation, Kloss Attack",
        ),
        "rnbqk2r/ppp1ppbp/5np1/4N3/2BP4/2N5/PPP3PP/R1BQK2R b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Bogoljubov Variation, Nimzowitsch Attack",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/8/3P4/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Bogoljubov Variation",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/8/2BP4/2N2N2/PPP3PP/R1B1QRK1 b - -": (
            "D00",
            "Blackmar-Diemer Gambit: Bogoljubov Variation, Studier Attack",
        ),
        "rnbqkb1r/pp2pppp/5n2/2p5/3Pp3/2N2P2/PPP3PP/R1BQKBNR w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit Declined: Brombacher Countergambit",
        ),
        "rnbqkb1r/ppp2ppp/5n2/4p3/3Pp3/2N2P2/PPP3PP/R1BQKBNR w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit Declined: Elbert Countergambit",
        ),
        "rn1qkbnr/pppbpppp/8/8/3Pp3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit Declined: Grosshans Defense",
        ),
        "r1bqkb1r/ppp1pppp/2n2n2/8/3Pp3/2N2P2/PPP3PP/R1BQKBNR w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit Declined: Lamb Defense",
        ),
        "rnbqkb1r/ppp1pppp/5n2/8/3P4/2N1pP2/PPP3PP/R1BQKBNR w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit Declined: Langeheinecke Defense",
        ),
        "rnbqkbnr/ppp1pppp/8/8/3Pp3/4B3/PPP2PPP/RN1QKBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Diemer-Rosenberg Attack",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/8/3P4/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Euwe Defense",
        ),
        "r1bqk2r/ppp1bppp/4pn2/6B1/3n4/2NB1N2/PPP3PP/R2Q1R1K b kq -": (
            "D00",
            "Blackmar-Diemer Gambit: Euwe Defense, Zilbermintz Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/8/2BPp3/8/PPP2PPP/RNBQK1NR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Fritz Attack",
        ),
        "rnbqkbnr/ppp1pppp/8/8/3Pp3/5P2/PPP3PP/RNBQKBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Gedult Gambit",
        ),
        "rnbqkb1r/pp2pppp/5n2/2p5/3P4/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Kaulich Defense",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/3Pp3/2N1B3/PPP2PPP/R2QKBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Lemberger Countergambit, Diemer Attack",
        ),
        "rnbqkbnr/ppp2ppp/8/4P3/4p3/2N5/PPP2PPP/R1BQKBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Lemberger Countergambit, Endgame Variation",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/3Pp3/2N5/PPP1NPPP/R1BQKB1R b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Lemberger Countergambit, Rassmussen Attack",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/3PN3/8/PPP2PPP/R1BQKBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Lemberger Countergambit, Simple Variation",
        ),
        "rnbqkbnr/ppp2ppp/8/4p2Q/3Pp3/2N5/PPP2PPP/R1B1KBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Lemberger Countergambit, Sneider Attack",
        ),
        "r1bqkb1r/ppp1pppp/2n2n2/8/3P4/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Pietrowsky Defense",
        ),
        "rnbqkb1r/ppp1pppp/5n2/8/3Pp3/2N1B3/PPP2PPP/R2QKBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Rasa-Studier Gambit",
        ),
        "rnbqkb1r/p1p1pppp/1p3n2/8/3P4/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Ritter Defense",
        ),
        "rnbqkb1r/ppp1ppp1/5n2/7p/3P4/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Rook Pawn Defense",
        ),
        "rnbqkb1r/ppp1pppp/5n2/8/3P4/2N2Q2/PPP3PP/R1B1KBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Ryder Gambit",
        ),
        "r1bqkb1r/pppnpppp/5n2/8/3P4/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Schlutter Defense",
        ),
        "rn1qkb1r/ppp1pppp/5n2/5b2/3P4/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Tartakower Variation",
        ),
        "rn1qkb1r/ppp1pppp/5n2/8/3P2b1/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Teichmann Variation",
        ),
        "rn1qkb1r/ppp1pppp/5n2/5b2/3Pp3/2N2P2/PPP3PP/R1BQKBNR w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Vienna Variation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/6B1/3Pp3/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: von Popiel Gambit",
        ),
        "rn1qk2r/ppp2ppp/5pb1/1Q6/1b1Pp1P1/2N5/PPP2P1P/R3KBNR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: von Popiel Gambit, Zilbermintz Variation",
        ),
        "rn1qkbnr/ppp1pppp/8/5b2/3Pp3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Zeller Defense",
        ),
        "rn1qkb1r/ppp1pppp/5n2/5b2/2BPp3/2N2P2/PPP3PP/R1BQK1NR b KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Zeller Defense, Soller Attack",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/8/3P4/2N2N2/PPP3PP/R1BQKB1R w KQkq -": (
            "D00",
            "Blackmar-Diemer Gambit: Ziegler Defense",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3pp3/3PP3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "D00",
            "Blackmar-Diemer, Lemberger Countergambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/3P4/2N5/PPP1PPPP/R1BQKBNR b KQkq -": (
            "D00",
            "Queen's Pawn Game: Chigorin Variation",
        ),
        "rnbqkb1r/ppp1pppp/8/3p4/3Pn3/2N5/PPP2PPP/R1BQKBNR w KQkq -": (
            "D00",
            "Queen's Pawn Game: Hübsch Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p2B1/3P4/8/PPP1PPPP/RN1QKBNR b KQkq -": (
            "D00",
            "Queen's Pawn Game: Levitsky Attack",
        ),
        "rn1qkbnr/ppp1pppp/8/3p2B1/3P2b1/8/PPP1PPPP/RN1QKBNR w KQkq -": (
            "D00",
            "Queen's Pawn Game: Levitsky Attack, Welling Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/3P1B2/8/PPP1PPPP/RN1QKBNR b KQkq -": (
            "D00",
            "Queen's Pawn Game: Mason Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/3P1P2/8/PPP1P1PP/RNBQKBNR b KQkq -": (
            "D00",
            "Queen's Pawn Game: Mason Attack",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/3PPB2/8/PPP2PPP/RN1QKBNR b KQkq -": (
            "D00",
            "Queen's Pawn Game: Morris Countergambit",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4P3/PPP2PPP/RNBQKBNR w KQkq -": (
            "D00",
            "Queen's Pawn Game",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/3P4/4P3/PPP2PPP/RNBQKBNR b KQkq -": (
            "D00",
            "Queen's Pawn Game",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq -": (
            "D00",
            "Queen's Pawn Game",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/3P1B2/8/PPP1PPPP/RN1QKBNR w KQkq -": (
            "D00",
            "Queen's Pawn Game: Steinitz Countergambit",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/3BP3/PPP2PPP/RNBQK1NR b KQkq -": (
            "D00",
            "Queen's Pawn Game: Stonewall Attack",
        ),
        "rn1qkbnr/ppp1pppp/8/3p1b2/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "D00",
            "Queen's Pawn Game: Veresov Attack, Alburt Defense",
        ),
        "rn1qkbnr/ppp1pppp/8/3p4/3P2b1/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "D00",
            "Queen's Pawn Game: Veresov Attack, Anti-Veresov",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "D00",
            "Queen's Pawn Game: Veresov Attack, Shaviliuk Gambit",
        ),
        "rnbqkbnr/ppp1ppp1/8/3p3p/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "D00",
            "Queen's Pawn Game: Veresov Attack, Shropshire Defense",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/3P2P1/8/PPP1PP1P/RNBQKBNR b KQkq -": (
            "D00",
            "Queen's Pawn Game: Zurich Gambit",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/3P4/2N5/PPP1PPPP/R1BQKBNR w KQkq -": (
            "D00",
            "Queen's Pawn Game: Veresov Attack, Irish Gambit",
        ),
        "rnbqkb1r/ppp1pppp/8/3p2B1/3Pn3/2N5/PPP1PPPP/R2QKBNR w KQkq -": (
            "D01",
            "Queen's Pawn Game: Veresov Attack, Boyce Defense",
        ),
        "rn1qkb1r/ppp1pppp/5n2/3p1bB1/3P4/2N2P2/PPP1P1PP/R2QKBNR b KQkq -": (
            "D01",
            "Queen's Pawn Game: Veresov Attack, Richter Variation",
        ),
        "r1bqkb1r/pppnpp1p/5np1/3p2B1/3P4/2N2N2/PPP1PPPP/R2QKB1R w KQkq -": (
            "D01",
            "Queen's Pawn Game: Veresov Attack, Two Knights System, Grünfeld Defense",
        ),
        "r1bqkb1r/pppnpppp/5n2/3p2B1/3P4/2N2N2/PPP1PPPP/R2QKB1R b KQkq -": (
            "D01",
            "Queen's Pawn Game: Veresov Attack, Two Knights System",
        ),
        "rn1qkb1r/ppp1pppp/5B2/3p1b2/3P4/2N5/PPP1PPPP/R2QKBNR b KQkq -": (
            "D01",
            "Queen's Pawn Game: Veresov Attack, Veresov Variation",
        ),
        "rn1qkb1r/ppp1pppp/5n2/3p1bB1/3P4/2N5/PPP1PPPP/R2QKBNR w KQkq -": (
            "D01",
            "Richter-Veresov Attack",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p2B1/3P4/2N5/PPP1PPPP/R2QKBNR b KQkq -": (
            "D01",
            "Richter-Veresov Attack",
        ),
        "rnbqkb1r/pp2pp1p/5p2/2pP4/4p3/2N5/PPP2PPP/R2QKBNR b KQkq -": (
            "D01",
            "Veresov Opening: Malich Gambit",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P1B2/2N5/PPP1PPPP/R2QKBNR b KQkq -": (
            "D01",
            "Rapport-Jobava System",
        ),
        "rnb1kb1r/pp2pppp/1q3n2/2pp4/3P1B2/2N1PN2/PPP2PPP/R2QKB1R b KQkq -": (
            "D02",
            "London System: Poisoned Pawn Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/8/2pP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D02",
            "Queen's Gambit Accepted: Rosenthal Variation",
        ),
        "rn1qkbnr/pp3ppp/2p1p3/3p1b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D02",
            "Queen's Gambit Declined: Baltic Defense, Pseudo-Slav",
        ),
        "rn1qkbnr/ppp1pppp/8/3p4/3P2b1/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "D02",
            "Queen's Pawn Game: Anti-Torre",
        ),
        "rnbqkbnr/pp2pppp/8/3p4/3p4/5NP1/PPP1PPBP/RNBQK2R b KQkq -": (
            "D02",
            "Queen's Pawn Game: Chandler Gambit",
        ),
        "r1bqkbnr/ppp1pppp/2n5/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "D02",
            "Queen's Pawn Game: Chigorin Variation",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "D02",
            "Queen's Pawn Game: Krause Variation",
        ),
        "rnb1kbnr/pp2ppp1/1qp4p/3p4/3P3B/5N2/PPP1PPPP/RN1QKB1R w KQkq -": (
            "D02",
            "Queen's Pawn Game: Levitsky Attack, Euwe Variation, Modern Line",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P1B2/5N2/PPP1PPPP/RN1QKB1R b KQkq -": (
            "D02",
            "Queen's Pawn Game: London System",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/5NP1/PPP1PP1P/RNBQKB1R b KQkq -": (
            "D02",
            "Queen's Pawn Game: Symmetrical Variation, Pseudo-Catalan",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R w KQkq -": (
            "D02",
            "Queen's Pawn Game: Symmetrical Variation",
        ),
        "rnbqkb1r/p1p1pppp/5n2/1p1p4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D02",
            "Queen's Pawn Game: Zilbermintz Countergambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R b KQkq -": (
            "D02",
            "Queen's Pawn Game: Zukertort Variation",
        ),
        "rnbqkb1r/ppp1pppp/8/3p2B1/3Pn3/5N2/PPP1PPPP/RN1QKB1R w KQkq -": (
            "D03",
            "Queen's Pawn Game: Torre Attack, Gossip Variation",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p2B1/3P4/5N2/PPP1PPPP/RN1QKB1R w KQkq -": (
            "D03",
            "Queen's Pawn Game: Torre Attack, Grünfeld Variation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p2B1/3P4/5N2/PPP1PPPP/RN1QKB1R b KQkq -": (
            "D03",
            "Queen's Pawn Game: Torre Attack",
        ),
        "rn1qkb1r/ppp1pppp/5n2/3p1b2/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq -": (
            "D04",
            "Queen's Pawn Game: Colle System, Anti-Colle",
        ),
        "rnbqk2r/ppp1ppbp/5np1/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R w KQkq -": (
            "D04",
            "Queen's Pawn Game: Colle System, Grünfeld Formation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R b KQkq -": (
            "D04",
            "Queen's Pawn Game: Colle System",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R b KQkq -": (
            "D05",
            "Queen's Pawn Game: Colle System",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq -": (
            "D05",
            "Queen's Pawn Game: Colle System",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/2PBPN2/PP3PPP/RNBQK2R b KQkq -": (
            "D05",
            "Queen's Pawn Game: Colle System, Traditional Colle",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/1P2PN2/P1PN1PPP/R1BQKB1R b KQkq -": (
            "D05",
            "Queen's Pawn Game, Zukertort Variation",
        ),
        "r1bq1rk1/pp3ppp/2nbpn2/2pp4/3P4/1P1BPN2/PBP2PPP/RN1Q1RK1 w - -": (
            "D05",
            "Rubinstein Opening: Bogoljubov Defense",
        ),
        "r1bq1rk1/pp2bppp/2n1pn2/2pp4/3P4/1P1BPN2/PBP2PPP/RN1Q1RK1 w - -": (
            "D05",
            "Rubinstein Opening: Classical Defense",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/1P1BPN2/P1P2PPP/RNBQK2R b KQkq -": (
            "D05",
            "Rubinstein Opening",
        ),
        "r1bq1rk1/pppn1ppp/3bpn2/3p4/3P4/1P1BPN2/PBP2PPP/RN1Q1RK1 b - -": (
            "D05",
            "Rubinstein Opening: Semi-Slav Defense",
        ),
        "rnbqkbnr/pp2pppp/8/2P5/2Pp4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D06",
            "Queen's Gambit Declined: Austrian Attack, Salvio Countergambit",
        ),
        "rnbqkb1r/pp2pppp/5n2/2pP4/3P4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D06",
            "Queen's Gambit Declined: Austrian Defense, Gusev Countergambit",
        ),
        "rnb1kb1r/pp2pppp/8/q1PP4/4n3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "D06",
            "Queen's Gambit Declined: Austrian Defense, Haberditz Variation",
        ),
        "rnbqkbnr/pp2pppp/8/2pp4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D06",
            "Queen's Gambit Declined: Austrian Defense",
        ),
        "r2qkbnr/pp2pppp/2n5/8/Q2P4/8/PP2PPPP/RbB1KBNR w KQkq -": (
            "D06",
            "Queen's Gambit Declined: Baltic Defense, Argentinian Gambit",
        ),
        "r2qkbnr/ppp2ppp/2n1p3/3p1b2/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D06",
            "Queen's Gambit Declined: Baltic Defense, Pseudo-Chigorin",
        ),
        "rn1qkbnr/ppp2ppp/4p3/3p1b2/2PP4/1QN5/PP2PPPP/R1B1KBNR b KQkq -": (
            "D06",
            "Queen's Gambit Declined: Baltic Defense, Deferred Queen's Attack",
        ),
        "rn1qkbnr/ppp1pppp/8/3p1b2/2PP4/1Q6/PP2PPPP/RNB1KBNR b KQkq -": (
            "D06",
            "Queen's Gambit Declined: Baltic Defense, Queen's Attack",
        ),
        "rn1qkbnr/ppp1pppp/8/3p1b2/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D06",
            "Queen's Gambit Declined: Baltic Defense",
        ),
        "rnbqkb1r/ppp1pppp/5n2/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D06",
            "Queen's Gambit Declined: Marshall Defense",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/3P4/3P4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D06",
            "Queen's Gambit Declined: Marshall Defense, Tan Gambit",
        ),
        "rnbqkbnr/p1p1pppp/8/1p1p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D06",
            "Queen's Gambit Declined: Zilbermintz Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq -": (
            "D06",
            "Queen's Gambit",
        ),
        "r1b1k1nr/ppp2ppp/2n5/3q4/3p4/2B1P3/PP2NPPP/R2QKB1R b KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense, Exchange Variation, Costa Line",
        ),
        "r1b1kbnr/ppp1pppp/2n5/3q4/3P4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense, Exchange Variation",
        ),
        "r1bqkbnr/ppp1pppp/2n5/8/2pP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense, Janowski Variation",
        ),
        "r1bqkbnr/ppp2ppp/2n5/3pp3/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense, Lazard Gambit",
        ),
        "r2qkbnr/ppp1pppp/2n5/3p4/Q1PP2b1/5N2/PP2PPPP/RNB1KB1R b KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense, Main Line, Alekhine Variation",
        ),
        "r2qkbnr/ppp1pppp/2n5/3p4/2PP2b1/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense, Main Line",
        ),
        "r1bqkb1r/ppp1pppp/2n2n2/8/2pP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense, Modern Gambit",
        ),
        "r1bqkbnr/ppp1pppp/2n5/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense",
        ),
        "r1bqkbnr/ppp1pppp/2n5/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense",
        ),
        "r1bqkbnr/ppp1pppp/2n5/8/2pP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense",
        ),
        "r1bqkbnr/ppp2ppp/2n5/3pp3/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D07",
            "Queen's Gambit Declined: Chigorin Defense, Tartakower Gambit",
        ),
        "r1b1kbnr/ppp1qppp/2n5/4P3/2Pp4/5N2/PP1NPPPP/R1BQKB1R w KQkq -": (
            "D08",
            "Queen's Gambit Declined: Albin Countergambit, Balogh Variation",
        ),
        "r1bqkbnr/ppp3pp/2n2p2/4P3/2Pp4/5N2/PP1NPPPP/R1BQKB1R w KQkq -": (
            "D08",
            "Queen's Gambit Declined: Albin Countergambit, Janowski Variation",
        ),
        "r3k1nr/ppp1qppp/2n5/4P3/1bPp4/5N1P/PP1BPPP1/R2QKB1R w KQkq -": (
            "D08",
            "Queen's Gambit Declined: Albin Countergambit, Krenosz Variation",
        ),
        "rnbqk1nr/ppp2ppp/8/4P3/1bP5/4p3/PP1B1PPP/RN1QKBNR w KQkq -": (
            "D08",
            "Queen's Gambit Declined: Albin Countergambit, Lasker Trap",
        ),
        "r1bqkbnr/ppp2ppp/2n5/4P3/2Pp4/5N2/PP1NPPPP/R1BQKB1R b KQkq -": (
            "D08",
            "Queen's Gambit Declined: Albin Countergambit, Modern Line",
        ),
        "rnbqkbnr/ppp2ppp/8/4P3/2Pp4/5N2/PP2PPPP/RNBQKB1R b KQkq -": (
            "D08",
            "Queen's Gambit Declined: Albin Countergambit, Normal Line",
        ),
        "rnbqkbnr/ppp2ppp/8/3pp3/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D08",
            "Queen's Gambit Declined: Albin Countergambit",
        ),
        "rnbqkbnr/pp3ppp/8/2p1P3/2Pp4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D08",
            "Queen's Gambit Declined: Albin Countergambit, Tartakower Defense",
        ),
        "r2qkbnr/ppp2ppp/2n1b3/4P3/2Pp4/5NP1/PP2PP1P/RNBQKB1R w KQkq -": (
            "D09",
            "Queen's Gambit Declined: Albin Countergambit, Fianchetto Variation, Be6 Line",
        ),
        "r2qkbnr/ppp2ppp/2n5/4Pb2/2Pp4/5NP1/PP2PP1P/RNBQKB1R w KQkq -": (
            "D09",
            "Queen's Gambit Declined: Albin Countergambit, Fianchetto Variation, Bf5 Line",
        ),
        "r2qkbnr/ppp2ppp/2n5/4P3/2Pp2b1/5NP1/PP2PP1P/RNBQKB1R w KQkq -": (
            "D09",
            "Queen's Gambit Declined: Albin Countergambit, Fianchetto Variation, Bg4 Line",
        ),
        "r1bqkbnr/ppp2ppp/2n5/4P3/2Pp4/5NP1/PP2PP1P/RNBQKB1R b KQkq -": (
            "D09",
            "Queen's Gambit Declined: Albin Countergambit, Fianchetto Variation",
        ),
        "rnbqkbnr/pp2pppp/2p5/3P4/3P4/8/PP2PPPP/RNBQKBNR b KQkq -": (
            "D10",
            "Slav Defense: Exchange Variation",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq -": (
            "D10",
            "Slav Defense",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D10",
            "Slav Defense",
        ),
        "rnbqkbnr/pp2pppp/2p5/8/2pP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D10",
            "Slav Defense",
        ),
        "rnbqkbnr/pp2pppp/2p5/8/2pPP3/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "D10",
            "Slav Defense: Slav Gambit, Alekhine Attack",
        ),
        "rnbqkbnr/pp3ppp/2p5/3pp3/2PPP3/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "D10",
            "Slav Defense: Winawer Countergambit, Anti-Winawer Gambit",
        ),
        "rnbqkbnr/pp3ppp/2p5/3pp3/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D10",
            "Slav Defense: Winawer Countergambit",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/3p2B1/2PP4/5N2/PP2PPPP/RN1QKB1R b KQkq -": (
            "D11",
            "Slav Defense: Bonet Gambit",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/3p4/2PP4/5N2/PP1NPPPP/R1BQKB1R b KQkq -": (
            "D11",
            "Slav Defense: Breyer Variation",
        ),
        "rnbqkbnr/pp2pppp/2p5/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R b KQkq -": (
            "D11",
            "Slav Defense: Modern Line",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D11",
            "Slav Defense: Modern",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/3p4/2PP2b1/4PN2/PP3PPP/RNBQKB1R w KQkq -": (
            "D11",
            "Slav Defense: Quiet Variation, Pin Defense",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/3p4/2PP4/4PN2/PP3PPP/RNBQKB1R b KQkq -": (
            "D11",
            "Slav Defense: Quiet Variation",
        ),
        "rn1qkb1r/pp1n1ppp/4p3/3pNb2/3P4/2N1P3/PP3PPP/R1BQKB1R w KQkq -": (
            "D12",
            "Queen's Gambit Declined: Slav, Amsterdam Variation",
        ),
        "rnq1kb1r/pp3ppp/4pn2/3p1b2/3P4/NQ2PN2/PP1B1PPP/R3KB1R b KQkq -": (
            "D12",
            "Queen's Gambit Declined: Slav, Landau Variation",
        ),
        "rn1qkb1r/pp2pppp/5n2/3p1b2/3P4/2N1PN2/PP3PPP/R1BQKB1R b KQkq -": (
            "D12",
            "Slav Defense: Exchange Variation, Schallopp Variation",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/3p1b2/2PP4/4PN2/PP3PPP/RNBQKB1R w KQkq -": (
            "D12",
            "Slav Defense: Quiet Variation, Schallopp Defense",
        ),
        "rnbqkb1r/pp2pppp/5n2/3p4/3P4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D13",
            "Slav Defense: Exchange Variation",
        ),
        "r2qkb1r/pp2pppp/2n2n2/3p1b2/3P1B2/2N2N2/PP2PPPP/R2QKB1R w KQkq -": (
            "D14",
            "Slav Defense: Exchange Variation, Symmetrical Line",
        ),
        "r2qk2r/pp3ppp/2n1pn2/3p1b2/1b1P1B2/1QN1PN2/PP3PPP/R3KB1R w KQkq -": (
            "D14",
            "Slav Defense: Exchange Variation, Trifunović Variation",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/8/2pP4/2N1PN2/PP3PPP/R1BQKB1R b KQkq -": (
            "D15",
            "Slav Defense: Alekhine Variation",
        ),
        "rnbqkb1r/1p2pppp/p1p2n2/2Pp4/3P4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "D15",
            "Slav Defense: Chameleon Variation, Advance System",
        ),
        "rnbqkb1r/1p2pppp/p1p2n2/3p4/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D15",
            "Slav Defense: Chameleon Variation",
        ),
        "rnbqkb1r/p3pppp/2p2n2/1p2P3/2pP4/2N2N2/PP3PPP/R1BQKB1R b KQkq -": (
            "D15",
            "Slav Defense: Geller Gambit",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/8/2pPP3/2N2N2/PP3PPP/R1BQKB1R b KQkq -": (
            "D15",
            "Slav Defense: Geller Gambit",
        ),
        "rnb1kb1r/pp2pppp/1qp2n2/3p4/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D15",
            "Slav Defense: Süchting Variation",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/3p4/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "D15",
            "Slav Defense: Three Knights Variation",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/8/2pP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D15",
            "Slav Defense: Two Knights Attack",
        ),
        "r2qkb1r/pp2pppp/n1p2n2/8/P1pPP1b1/2N2N2/1P3PPP/R1BQKB1R w KQkq -": (
            "D16",
            "Queen's Gambit Declined: Slav, Smyslov Variation",
        ),
        "rnbqkb1r/pp2pppp/2p2n2/8/P1pP4/2N2N2/1P2PPPP/R1BQKB1R b KQkq -": (
            "D16",
            "Slav Defense: Alapin Variation",
        ),
        "r1bqkb1r/pp2pppp/n1p2n2/8/P1pP4/2N2N2/1P2PPPP/R1BQKB1R w KQkq -": (
            "D16",
            "Slav Defense: Smyslov Variation",
        ),
        "rnbqkb1r/pp3ppp/2p1pn2/8/P1pP4/2N2N2/1P2PPPP/R1BQKB1R w KQkq -": (
            "D16",
            "Slav Defense: Soultanbeieff Variation",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/8/P1pP2b1/2N2N2/1P2PPPP/R1BQKB1R w KQkq -": (
            "D16",
            "Slav Defense: Steiner Variation",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/5b2/P1pP3N/2N5/1P2PPPP/R1BQKB1R b KQkq -": (
            "D17",
            "Slav Defense: Czech Variation, Bled Attack",
        ),
        "r3kb1r/ppqn1p1p/2p5/4nbp1/P1N2B2/2N3P1/1P2PPBP/R2QK2R w KQkq -": (
            "D17",
            "Slav Defense: Czech Variation, Carlsbad Variation, Morozevich Variation",
        ),
        "r3kb1r/ppqn1ppp/2p2n2/4pb2/P1NP4/2N3P1/1P2PP1P/R1BQKB1R w KQkq -": (
            "D17",
            "Slav Defense: Czech Variation, Carlsbad Variation",
        ),
        "r2qkb1r/pp2pppp/n1p2n2/4Nb2/P1pPP3/2N5/1P3PPP/R1BQKB1R b KQkq -": (
            "D17",
            "Slav Defense: Czech Variation, Krause Attack, Fazekas Gambit",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/4Nb2/P1pP4/2N5/1P2PPPP/R1BQKB1R b KQkq -": (
            "D17",
            "Slav Defense: Czech Variation, Krause Attack",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/5b2/P1pP4/2N2N2/1P2PPPP/R1BQKB1R w KQkq -": (
            "D17",
            "Slav Defense: Czech Variation",
        ),
        "rn1qkb1r/pp3ppp/2p1pn2/4Nb2/P1pP4/2N5/1P2PPPP/R1BQKB1R w KQkq -": (
            "D17",
            "Slav Defense: Czech Variation, Wiesbaden Variation",
        ),
        "rn1qk2r/pp3ppp/2p1pn2/4Nb2/PbpPP3/2N2P2/1P4PP/R1BQKB1R b KQkq -": (
            "D17",
            "Slav Defense: Czech Variation, Wiesbaden Variation, Sharp Line",
        ),
        "rn1qkb1r/pp2pppp/2p2n2/5b2/P1pP4/2N1PN2/1P3PPP/R1BQKB1R b KQkq -": (
            "D18",
            "Slav Defense: Czech Variation, Classical System",
        ),
        "r2qkb1r/pp2pppp/n1p2n2/5b2/P1pP4/2N1PN2/1P3PPP/R1BQKB1R w KQkq -": (
            "D18",
            "Slav Defense: Czech Variation, Lasker Variation",
        ),
        "rn1q1rk1/pp3ppp/2p1p3/5b2/PbBPn1P1/2N1PN2/1P2QP1P/R1B2RK1 b - -": (
            "D19",
            "Queen's Gambit Declined: Slav, Dutch, Sämisch Variation",
        ),
        "rn1qk2r/pp3ppp/2p1pn2/5b2/PbBP4/2N1PN2/1P3PPP/R1BQ1RK1 b kq -": (
            "D19",
            "Queen's Gambit Declined: Slav, Dutch Variation",
        ),
        "rn1q1rk1/pp3ppp/2p1pn2/5b2/PbBP4/2N1PN2/1P2QPPP/R1B2RK1 b - -": (
            "D19",
            "Slav Defense: Czech Variation, Classical System, Main Line",
        ),
        "rnbqkbnr/ppp1pppp/8/8/Q1pP4/8/PP2PPPP/RNB1KBNR b KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Accelerated Mannheim Variation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/8/2pPP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Central Variation, Alekhine System",
        ),
        "rnbqkbnr/p1p1pppp/8/1p6/2pPP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Central Variation, Greco Variation",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/2pPP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Central Variation, McDonnell Defense",
        ),
        "rnbqkbnr/ppp2ppp/8/4p3/2BPP3/8/PP3PPP/RNBQK1NR b KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Central Variation, McDonnell Defense, Somov Gambit",
        ),
        "r1bqkbnr/ppp1pppp/2n5/8/2pPP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Central Variation, Modern Defense",
        ),
        "rnbqkbnr/pp2pppp/8/2p5/2pPP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Central Variation, Rubinstein Defense",
        ),
        "rnbqkbnr/p3pppp/8/1ppP4/2p1P3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Central Variation, Rubinstein Defense, Yefimov Gambit",
        ),
        "rnbqkb1r/p3pppp/5n2/1ppP4/2p1P3/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Linares Variation",
        ),
        "rnb1kbnr/ppp1qppp/8/8/2Bp4/PQ2P3/1P3PPP/RNB1K1NR b KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Old Variation, Billinger Gambit",
        ),
        "rnb1kbnr/ppp1qppp/8/8/2Bp4/1Q2PN2/PP3PPP/RNB1K2R b KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Old Variation, Christensen Gambit",
        ),
        "rnb1kbnr/ppp1qppp/8/8/2Bp4/1Q2P3/PP3PPP/RNB2KNR b kq -": (
            "D20",
            "Queen's Gambit Accepted: Old Variation, Korchnoi Gambit",
        ),
        "rnb1kbnr/ppp1qppp/8/8/2Bp4/1Q2P3/PP1N1PPP/R1B1K1NR b KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Old Variation, Novikov Gambit",
        ),
        "rnbqkbnr/ppp1pppp/8/8/2pP4/4P3/PP3PPP/RNBQKBNR b KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Old Variation",
        ),
        "rnbqkbnr/ppp1pppp/8/8/2pP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D20",
            "Queen's Gambit Accepted",
        ),
        "rnbqkbnr/ppp1pppp/8/8/2pPP3/8/PP3PPP/RNBQKBNR b KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Saduleto Variation",
        ),
        "rnbqkbnr/ppp1p1pp/8/5p2/2pPP3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "D20",
            "Queen's Gambit Accepted: Schwartz Defense",
        ),
        "rnbqkbnr/1pp1pppp/p7/8/2pPP3/5N2/PP3PPP/RNBQKB1R b KQkq -": (
            "D21",
            "Queen's Gambit Accepted: Alekhine Defense, Borisenko-Furman Variation",
        ),
        "r1bqkbnr/pppnpppp/8/8/2pP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D21",
            "Queen's Gambit Accepted: Godes Variation",
        ),
        "rnbqkbnr/pp2pppp/8/2p5/2pP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D21",
            "Queen's Gambit Accepted: Gunsberg Defense",
        ),
        "rnbqkbnr/ppp1pppp/8/8/2pP4/5N2/PP2PPPP/RNBQKB1R b KQkq -": (
            "D21",
            "Queen's Gambit Accepted: Normal Variation",
        ),
        "rnbqkbnr/p1p1pppp/8/1p6/2pP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D21",
            "Queen's Gambit Accepted: Slav Gambit",
        ),
        "rn1qkbnr/1pp2ppp/p3p3/3P4/2B3b1/4PN2/PP3PPP/RNBQK2R b KQkq -": (
            "D22",
            "Queen's Gambit Accepted: Alekhine Defense, Alatortsev Variation",
        ),
        "rnbqkbnr/2p1pppp/p7/1p6/2pP4/4PN2/PP3PPP/RNBQKB1R w KQkq -": (
            "D22",
            "Queen's Gambit Accepted: Alekhine Defense, Haberditz Variation",
        ),
        "rnbqkbnr/1pp1pppp/p7/8/2pP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D22",
            "Queen's Gambit Accepted: Alekhine Defense",
        ),
        "rnbqkb1r/ppp1pppp/5n2/8/Q1pP4/5N2/PP2PPPP/RNB1KB1R b KQkq -": (
            "D23",
            "Queen's Gambit Accepted: Mannheim Variation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/8/2pP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D23",
            "Queen's Gambit Accepted",
        ),
        "rnbqkb1r/1pp1pppp/p4n2/8/2pPP3/2N2N2/PP3PPP/R1BQKB1R b KQkq -": (
            "D24",
            "Queen's Gambit Accepted: Bogoljubov Defense",
        ),
        "rnbqkb1r/pp3ppp/5n2/2ppP3/2p5/2N2N2/PP3PPP/R1BQKB1R b KQkq -": (
            "D24",
            "Queen's Gambit Accepted: Gunsberg Defense, Prianishenmo Gambit",
        ),
        "rnbqkb1r/ppp1pppp/5n2/8/2pP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "D24",
            "Queen's Gambit Accepted: Showalter Variation",
        ),
        "rn1qkb1r/ppp1pppp/5n2/8/2pP2b1/4PN2/PP3PPP/RNBQKB1R w KQkq -": (
            "D25",
            "Queen's Gambit Accepted: Janowski-Larsen Variation",
        ),
        "rnbqkb1r/ppp1pppp/5n2/8/2pP4/4PN2/PP3PPP/RNBQKB1R b KQkq -": (
            "D25",
            "Queen's Gambit Accepted: Normal Variation",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/8/2pP4/4PN2/PP3PPP/RNBQKB1R w KQkq -": (
            "D25",
            "Queen's Gambit Accepted: Smyslov Variation",
        ),
        "rn1qkb1r/ppp1pppp/4bn2/8/2pP4/4PN2/PP3PPP/RNBQKB1R w KQkq -": (
            "D25",
            "Queen's Gambit Accepted: Winawer Defense",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2p5/2BP4/4PN2/PP3PPP/RNBQ1RK1 b kq -": (
            "D26",
            "Queen's Gambit Accepted: Classical Defense, Normal Line",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2p5/2BP4/4PN2/PP3PPP/RNBQK2R w KQkq -": (
            "D26",
            "Queen's Gambit Accepted: Classical Defense",
        ),
        "r1bqkb1r/pp3ppp/2n1pn2/2p5/2BP4/4PN2/PP3PPP/RNBQ1RK1 w kq -": (
            "D26",
            "Queen's Gambit Accepted: Classical Defense, Steinitz Variation, Development Variation",
        ),
        "rnbqkb1r/pp3ppp/4pn2/8/2Bp4/4PN2/PP3PPP/RNBQ1RK1 w kq -": (
            "D26",
            "Queen's Gambit Accepted: Classical Defense, Steinitz Variation, Exchange Variation",
        ),
        "r1bqk2r/5ppp/p1n1pn2/1pb1P3/2B5/5N2/PP2QPPP/RNB2RK1 b kq -": (
            "D26",
            "Queen's Gambit Accepted: Classical Variation, Furman Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/8/2pP4/4PN2/PP3PPP/RNBQKB1R w KQkq -": (
            "D26",
            "Queen's Gambit Accepted: Normal Variation, Traditional System",
        ),
        "rnbqkb1r/1p3ppp/p3pn2/2p5/2BP4/4PN2/PP3PPP/RNBQ1RK1 w kq -": (
            "D27",
            "Queen's Gambit Accepted: Classical Defense, Main Line",
        ),
        "rnbqkb1r/1p3ppp/p3pn2/2p5/P1BP4/4PN2/1P3PPP/RNBQ1RK1 b kq -": (
            "D27",
            "Queen's Gambit Accepted: Classical Defense, Rubinstein Variation",
        ),
        "rnbqkb1r/1p3ppp/p3pn2/2p5/2BPP3/5N2/PP3PPP/RNBQ1RK1 b kq -": (
            "D27",
            "Queen's Gambit Accepted: Classical Defense, Russian Gambit",
        ),
        "rnbqk2r/1p3ppp/p3pn2/2b5/2B5/4PN2/PP3PPP/RNBQ1RK1 w kq -": (
            "D27",
            "Queen's Gambit Accepted: Furman Variation",
        ),
        "rnbqkb1r/5ppp/p3pn2/1pp5/2BP4/4PN2/PP2QPPP/RNB2RK1 w kq -": (
            "D28",
            "Queen's Gambit Accepted: Classical Defense, Alekhine System (Except Main Line)",
        ),
        "rnbqkb1r/1p3ppp/p3pn2/2p5/2BP4/4PN2/PP2QPPP/RNB2RK1 b kq -": (
            "D28",
            "Queen's Gambit Accepted: Classical Defense, Alekhine System",
        ),
        "r3kb1r/1bq2ppp/p3pn2/1p1P4/2p5/2N1PN2/PPQ2PPP/R1BR2K1 w kq -": (
            "D28",
            "Queen's Gambit Accepted: Classical Variation, Flohr Variation",
        ),
        "rn1qkb1r/1b3ppp/p3pn2/1pp5/3P4/1B2PN2/PP2QPPP/RNB2RK1 w kq -": (
            "D29",
            "Queen's Gambit Accepted: Classical Defense, Alekhine System, Main Line",
        ),
        "r2qk2r/1b1n1ppp/p2bpn2/1pp5/3P4/1BN1PN2/PP2QPPP/R1BR2K1 w kq -": (
            "D29",
            "Queen's Gambit Accepted: Classical Defense, Alekhine System, Smyslov Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/8/2PPp3/8/PP3PPP/RNBQKBNR w KQkq -": (
            "D30",
            "French Defense: Diemer-Duhm Gambit",
        ),
        "rnbqkb1r/ppp2pp1/4pn1p/3p2B1/2PP4/5N2/PP2PPPP/RN1QKB1R w KQkq -": (
            "D30",
            "Queen's Gambit Declined: Capablanca Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/3p2B1/2PP4/4PN2/PP1N1PPP/R2QKB1R b KQkq -": (
            "D30",
            "Queen's Gambit Declined: Capablanca Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "D30",
            "Queen's Gambit Declined",
        ),
        "r1bqkb1r/pp1n1ppp/4pn2/2pp4/2PP4/3BPN2/PP1N1PPP/R1BQK2R w KQkq -": (
            "D30",
            "Queen's Gambit Declined: Semmering Variation",
        ),
        "rnbqkb1r/pp3p1p/2p1pnp1/3p4/2PP4/4PN2/PP1N1PPP/R1BQKB1R w KQkq -": (
            "D30",
            "Queen's Gambit Declined: Spielmann Variation",
        ),
        "rnbqkb1r/pp4pp/2p1p3/3p1p2/2PPn3/3BPN2/PP1N1PPP/R1BQK2R w KQkq -": (
            "D30",
            "Queen's Gambit Declined: Stonewall Variation",
        ),
        "rnbqkbnr/pp3ppp/8/2pp2B1/3P4/5N2/PP2PPPP/RN1QKB1R b KQkq -": (
            "D30",
            "Queen's Gambit Declined: Tarrasch Defense, Pseudo-Tarrasch Defense, Bishop's Attack",
        ),
        "rnbqkbnr/pp3ppp/4p3/2pp4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "D30",
            "Queen's Gambit Declined: Tarrasch Defense, Pseudo-Tarrasch Defense",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p2B1/2PP4/5N2/PP2PPPP/RN1QKB1R b KQkq -": (
            "D30",
            "Queen's Gambit Declined: Traditional Variation",
        ),
        "rnbqk2r/ppp2ppp/4pn2/3p2B1/1bPP4/5N2/PP2PPPP/RN1QKB1R w KQkq -": (
            "D30",
            "Queen's Gambit Declined: Vienna Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/3p4/2PP4/4PN2/PP1N1PPP/R1BQKB1R w KQkq -": (
            "D30",
            "Semi-Slav Defense: Quiet Variation",
        ),
        "rnbqkb1r/pp3ppp/2p1pn2/3p4/2PP4/4PN2/PP1N1PPP/R1BQKB1R b KQkq -": (
            "D30",
            "Semi-Slav Defense: Quiet Variation",
        ),
        "rnbqkbnr/p1p2ppp/1p2p3/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D31",
            "Queen's Gambit Declined: Alapin Variation",
        ),
        "rnbqk1nr/ppp1bppp/4p3/8/2PPp3/2N2P2/PP4PP/R1BQKBNR b KQkq -": (
            "D31",
            "Queen's Gambit Declined: Charousek (Petrosian) Variation, Miladinović Gambit",
        ),
        "rnbqk1nr/ppp1bppp/4p3/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D31",
            "Queen's Gambit Declined: Charousek (Petrosian) Variation",
        ),
        "rnbqkbnr/1pp2ppp/p3p3/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D31",
            "Queen's Gambit Declined: Janowski Variation",
        ),
        "rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq -": (
            "D31",
            "Queen's Gambit Declined: Queen's Knight Variation",
        ),
        "rnbqk1nr/5ppp/2p1p3/pp6/PbpP4/2N1PN2/1P1B1PPP/R2QKB1R w KQkq -": (
            "D31",
            "Queen's Gambit Declined: Semi-Slav, Abrahams Variation",
        ),
        "rnb1k1nr/p4ppp/1qp1p3/1p6/PbpP4/2N1PN2/1P1B1PPP/R2QKB1R w KQkq -": (
            "D31",
            "Queen's Gambit Declined: Semi-Slav, Junge Variation",
        ),
        "rnb1k1nr/p3qppp/2p1p3/1p6/PbpP4/2N1PN2/1P1B1PPP/R2QKB1R w KQkq -": (
            "D31",
            "Queen's Gambit Declined: Semi-Slav, Koomen Variation",
        ),
        "rnbq1rk1/ppp1bpp1/4pn1p/8/2pP3B/2N2N2/PP2PPPP/2RQKB1R w K -": (
            "D31",
            "Queen's Gambit Declined: Uhlmann Variation",
        ),
        "rnbqkbnr/pp3ppp/2p1p3/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D31",
            "Semi-Slav Defense: Accelerated Move Order",
        ),
        "rnbqkbnr/pp4pp/2p1p3/3p1p2/2PP2P1/2N1P3/PP3P1P/R1BQKBNR b KQkq -": (
            "D31",
            "Semi-Slav Defense: Anti-Noteboom, Stonewall Variation, Portisch Gambit",
        ),
        "rnbqkbnr/pp3ppp/2p1p3/8/2PPp3/2N2P2/PP4PP/R1BQKBNR b KQkq -": (
            "D31",
            "Semi-Slav Defense: Gunderam Gambit",
        ),
        "rnbqk1nr/pp3ppp/2p1p3/8/1bPP4/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "D31",
            "Semi-Slav Defense: Marshall Gambit, Forgotten Variation",
        ),
        "rnbqk1nr/pp3ppp/2p1p3/8/1bPPN3/8/PP1B1PPP/R2QKBNR b KQkq -": (
            "D31",
            "Semi-Slav Defense: Marshall Gambit, Main Line",
        ),
        "rnbqkbnr/pp3ppp/2p1p3/3p4/2PPP3/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "D31",
            "Semi-Slav Defense: Marshall Gambit",
        ),
        "rnb1k1nr/pp3ppp/4p3/2B5/2P5/8/PP2BPqP/R2QK1NR w KQkq -": (
            "D31",
            "Semi-Slav Defense: Marshall Gambit, Tolush Variation",
        ),
        "rnbqk1nr/p4ppp/4p3/1p6/2pP4/2P1PN2/5PPP/R1BQKB1R w KQkq -": (
            "D31",
            "Semi-Slav Defense: Noteboom Variation, Abrahams Variation",
        ),
        "rnbqkbnr/pp3ppp/2p1p3/8/2pP4/2N2NP1/PP2PP1P/R1BQKB1R b KQkq -": (
            "D31",
            "Semi-Slav Defense: Noteboom Variation, Anti-Noteboom Gambit",
        ),
        "rnbqkbnr/pp4pp/2p1pp2/6B1/2pP4/2N2N2/PP2PPPP/R2QKB1R w KQkq -": (
            "D31",
            "Semi-Slav Defense: Noteboom Variation, Anti-Noteboom Variation, Belyavsky Line",
        ),
        "rnbqkbnr/pp3ppp/2p1p3/6B1/2pP4/2N2N2/PP2PPPP/R2QKB1R b KQkq -": (
            "D31",
            "Semi-Slav Defense: Noteboom Variation, Anti-Noteboom Variation",
        ),
        "rnbqkbnr/pp3ppp/2p1p3/8/2pP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D31",
            "Semi-Slav Defense: Noteboom Variation",
        ),
        "rnbqkbnr/pp3ppp/8/2pp4/3P4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D32",
            "Queen's Gambit Declined: Tarrasch Defense",
        ),
        "r1bqkbnr/p4ppp/2n5/1pP5/N2p4/5N2/PP2PPPP/R1BQKB1R w KQkq b6": (
            "D32",
            "Tarrasch Defense: Grünfeld Gambit",
        ),
        "rnbqkbnr/pp3ppp/8/2pp4/3PP3/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "D32",
            "Tarrasch Defense: Marshall Gambit",
        ),
        "rnbqkbnr/pp3ppp/4p3/2pp4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D32",
            "Tarrasch Defense",
        ),
        "rnbqkbnr/pp3ppp/4p3/3P4/3p4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D32",
            "Tarrasch Defense: Schara Gambit",
        ),
        "rnbqkbnr/p4ppp/8/1pP5/N2p4/8/PP2PPPP/R1BQKBNR w KQkq b6": (
            "D32",
            "Tarrasch Defense: Tarrasch Gambit",
        ),
        "rnbqkbnr/pp3ppp/8/2pp4/3P4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "D32",
            "Tarrasch Defense: Two Knights Variation",
        ),
        "r2qkbnr/pp3ppp/2n1b3/3Q4/8/2N5/PP2PPPP/R1B1KBNR w KQkq -": (
            "D32",
            "Tarrasch Defense: von Hennig Gambit",
        ),
        "r1bqkb1r/pp3ppp/2n2n2/2pp4/3P4/2N2NP1/PP2PP1P/R1BQKB1R w KQkq -": (
            "D33",
            "Tarrasch Defense: Prague Variation",
        ),
        "r1bqkbnr/pp3ppp/2n5/2pp4/3P4/2N2NP1/PP2PP1P/R1BQKB1R b KQkq -": (
            "D33",
            "Tarrasch Defense: Rubinstein System",
        ),
        "r1bqkbnr/pp3ppp/2n5/3p4/2pPP3/2N2NP1/PP3P1P/R1BQKB1R b KQkq -": (
            "D33",
            "Tarrasch Defense: Swedish Variation, Central Break Variation",
        ),
        "r1bqkbnr/pp3ppp/2n5/3p4/2pP4/2N2NP1/PP2PP1P/R1BQKB1R w KQkq -": (
            "D33",
            "Tarrasch Defense: Swedish Variation",
        ),
        "r2qkb1r/pp3ppp/2n2n2/2pp4/3P2b1/2N2NP1/PP2PPBP/R1BQK2R w KQkq -": (
            "D33",
            "Tarrasch Defense: Wagner Variation",
        ),
        "r2q1rk1/p3bppp/1pn1bn2/2pp2B1/3P4/2N2NP1/PP2PPBP/2RQ1RK1 w - -": (
            "D34",
            "Queen's Gambit Declined: Tarrasch Defense, Stoltz Variation",
        ),
        "r1bq1rk1/pp2bppp/2n2n2/3p2B1/2pP4/2N2NP1/PP2PPBP/R2Q1RK1 w - -": (
            "D34",
            "Tarrasch Defense: Classical Variation, Advance Variation",
        ),
        "r2q1rk1/pp2bppp/2n1bn2/3p2B1/2pP4/2N2NP1/PP2PPBP/2RQ1RK1 w - -": (
            "D34",
            "Tarrasch Defense: Classical Variation, Bogoljubov Variation",
        ),
        "r1bq1rk1/pp2bppp/2n2n2/2pp2B1/3P4/2N2NP1/PP2PPBP/R2Q1RK1 b - -": (
            "D34",
            "Tarrasch Defense: Classical Variation, Carlsbad Variation",
        ),
        "r2qr1k1/pp2bpp1/2n1bn1p/3p4/3N4/2N1B1P1/PP2PPBP/2RQ1RK1 w - -": (
            "D34",
            "Tarrasch Defense: Classical Variation, Chandler Variation",
        ),
        "r1bq1rk1/pp2bppp/2n2n2/2P5/3p4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "D34",
            "Tarrasch Defense: Classical Variation, Classical Tarrasch Gambit",
        ),
        "r2q1rk1/pp2bppp/2n1bn2/2pp2B1/3P4/2N2NP1/PP2PPBP/R2Q1RK1 w - -": (
            "D34",
            "Tarrasch Defense: Classical Variation, Endgame Variation",
        ),
        "r1bqr1k1/pp2bpp1/2n2n1p/3p4/3N4/2N1B1P1/PP2PPBP/R2Q1RK1 w - -": (
            "D34",
            "Tarrasch Defense: Classical Variation, Main Line",
        ),
        "r1bqr1k1/pp2bppp/2n2n2/3p2B1/3N4/2N3P1/PP2PPBP/R2Q1RK1 w - -": (
            "D34",
            "Tarrasch Defense: Classical Variation, Petursson Variation",
        ),
        "r1bq1rk1/pp2bppp/2n2n2/2pp4/3P4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "D34",
            "Tarrasch Defense: Classical Variation",
        ),
        "r1bq1rk1/pp3ppp/2n2n2/2bp4/N7/5NP1/PP2PPBP/R1BQ1RK1 b - -": (
            "D34",
            "Tarrasch Defense: Classical Variation, Réti Variation",
        ),
        "r2q1rk1/pp2bpp1/2n2n1p/3p4/3N2b1/2N1B1P1/PP2PPBP/R2Q1RK1 w - -": (
            "D34",
            "Tarrasch Defense: Classical Variation, Spassky Variation",
        ),
        "r1bqk2r/pp2bppp/2n2n2/2pp4/3P4/2N2NP1/PP2PPBP/R1BQK2R w KQkq -": (
            "D34",
            "Tarrasch Defense: Prague Variation, Main Line",
        ),
        "r1bqrnk1/ppp1bppp/5n2/3p2B1/3P4/2NBP3/PPQ1NPPP/2KR3R b - -": (
            "D35",
            "Queen's Gambit Declined: Exchange, Chameleon Variation",
        ),
        "rnbqkb1r/pp3ppp/2p2n2/3p2B1/3P4/2N5/PP2PPPP/R2QKBNR w KQkq -": (
            "D35",
            "Queen's Gambit Declined: Exchange Variation, Positional Variation",
        ),
        "rnbqkb1r/ppp2ppp/5n2/3p2B1/3P4/2N5/PP2PPPP/R2QKBNR b KQkq -": (
            "D35",
            "Queen's Gambit Declined: Exchange Variation, Positional Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3P4/3P4/2N5/PP2PPPP/R1BQKBNR b KQkq -": (
            "D35",
            "Queen's Gambit Declined: Exchange Variation",
        ),
        "r1bqkb1r/pppn1ppp/5n2/3p4/3P1B2/2N2N2/PP2PPPP/R2QKB1R b KQkq -": (
            "D35",
            "Queen's Gambit Declined: Exchange Variation, Sämisch Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/2PP1B2/2N5/PP2PPPP/R2QKBNR b KQkq -": (
            "D35",
            "Queen's Gambit Declined: Harrwitz Attack",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D35",
            "Queen's Gambit Declined: Normal Defense",
        ),
        "rnbqkb1r/pp3ppp/2p2n2/3p2B1/3P4/2N5/PPQ1PPPP/R3KBNR b KQkq -": (
            "D36",
            "Queen's Gambit Declined: Exchange Variation, Reshevsky Variation",
        ),
        "r1bqkb1r/pppn1ppp/4pn2/3p4/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D37",
            "Queen's Gambit Declined: Barmen Variation",
        ),
        "rnbq1rk1/p1p1bppp/1p2pn2/3p4/2PP1B2/2N1PN2/PP3PPP/R2QKB1R w KQ -": (
            "D37",
            "Queen's Gambit Declined: Harrwitz Attack, Fianchetto Defense",
        ),
        "rnbq1rk1/pp3ppp/4pn2/2bp4/2P2B2/2N1PN2/PP3PPP/R2QKB1R w KQ -": (
            "D37",
            "Queen's Gambit Declined: Harrwitz Attack, Main Line",
        ),
        "rnbq1rk1/pp2bppp/2p1pn2/3p4/2PP1B2/2N1PN2/PP3PPP/R2QKB1R w KQ -": (
            "D37",
            "Queen's Gambit Declined: Harrwitz Attack, Orthodox Defense",
        ),
        "r1b2rk1/pp3ppp/2n1pn2/q1bp4/2P2B2/P1N1PN2/1PQ2PPP/2KR1B1R b - -": (
            "D37",
            "Queen's Gambit Declined: Harrwitz Attack",
        ),
        "r1b2rk1/pp3ppp/2n1pn2/q1bp4/2P2B2/P1N1PN2/1PQ2PPP/3RKB1R b K -": (
            "D37",
            "Queen's Gambit Declined: Harrwitz Attack",
        ),
        "rnbqk2r/ppp1bppp/4pn2/3p4/2PP1B2/2N2N2/PP2PPPP/R2QKB1R b KQkq -": (
            "D37",
            "Queen's Gambit Declined: Harrwitz Attack",
        ),
        "r1bq1rk1/pppnbppp/4pn2/2Pp4/3P1B2/2N1PN2/PP3PPP/R2QKB1R b KQ -": (
            "D37",
            "Queen's Gambit Declined: Harrwitz Attack, Two Knights Defense, Blockade Line",
        ),
        "r1bq1rk1/pppnbppp/4pn2/3p4/2PP1B2/2N1PN2/PP3PPP/R2QKB1R w KQ -": (
            "D37",
            "Queen's Gambit Declined: Harrwitz Attack, Two Knights Defense",
        ),
        "r1bqkb1r/pppn1pp1/4pn1p/8/2pP3B/2N2N2/PP2PPPP/R2QKB1R w KQkq -": (
            "D37",
            "Queen's Gambit Declined: Knight's Defense, Alekhine Gambit",
        ),
        "rnbq1rk1/ppp1bppp/4pn2/3p2B1/2PP4/2N2N2/PPQ1PPPP/R3KB1R b KQ -": (
            "D37",
            "Queen's Gambit Declined: Miles Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "D37",
            "Queen's Gambit Declined: Three Knights Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/8/2pP4/2N1PN2/PP3PPP/R1BQKB1R b KQkq -": (
            "D37",
            "Queen's Gambit Declined: Vienna Variation, Quiet Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/8/2pP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D37",
            "Queen's Gambit Declined: Vienna Variation",
        ),
        "rnbqk2r/ppp2ppp/4pn2/3p4/QbPP4/2N2N2/PP2PPPP/R1B1KB1R b KQkq -": (
            "D38",
            "Queen's Gambit Declined: Ragozin Defense, Alekhine Variation",
        ),
        "rnbqk2r/ppp2ppp/4pn2/3p4/1bPP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D38",
            "Queen's Gambit Declined: Ragozin Defense",
        ),
        "r1bqk2r/pp1n1ppp/4pn2/2pp2B1/1bPP4/2N1PN2/PP3PPP/R2QKB1R w KQkq -": (
            "D38",
            "Queen's Gambit Declined: Westphalian Variation",
        ),
        "rnbqk2r/ppp2ppp/4pn2/6B1/1bpP4/2N2N2/PP2PPPP/R2QKB1R w KQkq -": (
            "D39",
            "Queen's Gambit Declined: Ragozin Defense, Vienna Variation",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2pp2B1/2PP4/2N2N2/PP2PPPP/R2QKB1R b KQkq -": (
            "D40",
            "Queen's Gambit Declined: Semi-Tarrasch Defense, Pillsbury Variation",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2pp4/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D40",
            "Queen's Gambit Declined: Semi-Tarrasch Defense",
        ),
        "r1bq1rk1/pp3ppp/2nbpn2/2pp4/2PP4/2NBPN2/PP3PPP/R1BQ1RK1 w - -": (
            "D40",
            "Queen's Gambit Declined: Semi-Tarrasch Defense, Symmetrical Variation",
        ),
        "r1b2rk1/pp2qppp/2n1pn2/2bp4/2P1P3/2NB1N2/PP2QPPP/R1B2RK1 b - -": (
            "D40",
            "Queen's Gambit Declined: Semi-Tarrasch Defense, Levenfish Variation",
        ),
        "rnbqkb1r/pp3ppp/4p3/2pn4/3PP3/2N2N2/PP3PPP/R1BQKB1R b KQkq -": (
            "D41",
            "Queen's Gambit Declined: Semi-Tarrasch Defense, Exchange Variation",
        ),
        "rnbqkb1r/pp3ppp/4p3/2pn4/3P4/2N1PN2/PP3PPP/R1BQKB1R b KQkq -": (
            "D41",
            "Queen's Gambit Declined: Semi-Tarrasch Defense, Pillsbury Variation",
        ),
        "rnbq1rk1/pp3ppp/4p3/1B6/3PP3/5N2/P2Q1PPP/R3K2R b KQ -": (
            "D41",
            "Queen's Gambit Declined: Semi-Tarrasch Defense, Kmoch Variation",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2pP4/3P4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "D41",
            "Queen's Gambit Declined: Semi-Tarrasch Defense",
        ),
        "rnb1k2r/pp3ppp/4p3/q7/1b1PP3/5N2/P2B1PPP/R2QKB1R w KQkq -": (
            "D41",
            "Queen's Gambit Declined: Semi-Tarrasch Defense, San Sebastian Variation",
        ),
        "r1bqkb1r/pp3ppp/2n1p3/2pn4/3P4/2NBPN2/PP3PPP/R1BQK2R b KQkq -": (
            "D42",
            "Queen's Gambit Declined: Semi-Tarrasch Defense, Main Line",
        ),
        "rnb1kb1r/pp3pp1/2p1pq1p/3p4/2PP4/1QN2N2/PP2PPPP/R3KB1R b KQkq -": (
            "D43",
            "Queen's Gambit Declined: Hastings Variation",
        ),
        "rnbqkb1r/pp3pp1/2p1pn1p/3p4/2PP3B/2N2N2/PP2PPPP/R2QKB1R b KQkq -": (
            "D43",
            "Semi-Slav Defense: Anti-Moscow Gambit",
        ),
        "rnbqkb1r/pp3ppp/2p1pn2/3p4/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D43",
            "Semi-Slav Defense",
        ),
        "rnbqkb1r/pp3ppp/2p1pn2/6B1/2pP4/2N2N2/PP2PPPP/R2QKB1R w KQkq -": (
            "D44",
            "Semi-Slav Defense Accepted",
        ),
        "rnbqkb1r/p4p2/2p1p2p/1p1nP1N1/2pP3B/2N5/PP3PPP/R2QKB1R w KQkq -": (
            "D44",
            "Semi-Slav Defense: Botvinnik Variation, Alatortsev System",
        ),
        "rnbqkb1r/p4p2/2p1pP1p/1p2N3/2pP3p/2N5/PP3PPP/R2QKB1R b KQkq -": (
            "D44",
            "Semi-Slav Defense: Botvinnik Variation, Ekstrom Variation",
        ),
        "r1bqkb1r/p2n1p2/2p1pn2/1p2P1B1/2pP4/2N3P1/PP3P1P/R2QKB1R b KQkq -": (
            "D44",
            "Semi-Slav Defense: Botvinnik Variation, Lilienthal Variation",
        ),
        "rnbqkb1r/p4p2/2p1pn1p/1p2P1N1/2pP3B/2N5/PP3PPP/R2QKB1R b KQkq -": (
            "D44",
            "Semi-Slav Defense: Botvinnik Variation",
        ),
        "r1bqkb1r/p2n1p2/2p1pn2/1p2P1B1/2pP4/2N2Q2/PP3PPP/R3KB1R b KQkq -": (
            "D44",
            "Semi-Slav Defense: Botvinnik Variation, Szabo Variation",
        ),
        "rnbqkb1r/pp3ppp/2p1pn2/6B1/2pPP3/2N2N2/PP3PPP/R2QKB1R b KQkq -": (
            "D44",
            "Semi-Slav Defense: Botvinnik Variation",
        ),
        "rnbqkb1r/1p3ppp/p1p1pn2/3p4/2PP4/2N1PN2/PP3PPP/R1BQKB1R w KQkq -": (
            "D45",
            "Semi-Slav Defense: Accelerated Meran Variation",
        ),
        "rnbqkb1r/pp3ppp/2p1pn2/3p4/2PP4/2N1PN2/PP3PPP/R1BQKB1R b KQkq -": (
            "D45",
            "Semi-Slav Defense: Main Line",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/3p4/2PP4/2N1PN2/PP3PPP/R1BQKB1R w KQkq -": (
            "D45",
            "Semi-Slav Defense: Normal Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/3pN3/2PP4/2N1P3/PP3PPP/R1BQKB1R b KQkq -": (
            "D45",
            "Semi-Slav Defense: Rubinstein (Anti-Meran) System",
        ),
        "r1bqk2r/pp1n1ppp/2pb4/4P3/2P1Q3/5N2/PP3PPP/R1B1KB1R b KQkq -": (
            "D45",
            "Semi-Slav Defense: Stoltz Variation, Center Variation, Mikhalchishin Line",
        ),
        "r1bqk2r/pp1n1ppp/2pbpn2/3p4/2PPP3/2N2N2/PPQ2PPP/R1B1KB1R b KQkq -": (
            "D45",
            "Semi-Slav Defense: Stoltz Variation, Center Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/3p4/2PP4/2N1PN2/PPQ2PPP/R1B1KB1R b KQkq -": (
            "D45",
            "Semi-Slav Defense: Stoltz Variation",
        ),
        "r1bqk2r/pp1n1ppp/2pbpn2/3p4/2PP2P1/2N1PN2/PPQ2P1P/R1B1KB1R b KQkq -": (
            "D45",
            "Semi-Slav Defense: Stoltz Variation, Shabalov Attack",
        ),
        "rnbqkb1r/pp4pp/2p1p3/3p1p2/2PPn3/2NBPN2/PP3PPP/R1BQK2R w KQkq -": (
            "D45",
            "Semi-Slav Defense: Stonewall Defense",
        ),
        "r1bqk2r/pp1nbppp/2p1pn2/3p4/2PP4/2NBPN2/PP3PPP/R1BQK2R w KQkq -": (
            "D46",
            "Semi-Slav Defense: Bogoljubov Variation",
        ),
        "r1bqk2r/pp1n1ppp/2pbpn2/3p4/2PP4/2NBPN2/PP3PPP/R1BQK2R w KQkq -": (
            "D46",
            "Semi-Slav Defense: Chigorin Defense",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/3p4/2PP4/2NBPN2/PP3PPP/R1BQK2R b KQkq -": (
            "D46",
            "Semi-Slav Defense: Main Line",
        ),
        "r1bqk2r/pp1n1ppp/2p1pn2/3p4/1bPP4/2NBPN2/PP3PPP/R1BQK2R w KQkq -": (
            "D46",
            "Semi-Slav Defense: Romih Variation",
        ),
        "r1bqkb1r/p2n1ppp/2p1pn2/8/1p1P4/2NBPN2/PP3PPP/R1BQK2R w KQkq -": (
            "D47",
            "Semi-Slav Defense: Meran Variation, Lundin Variation",
        ),
        "r1bqkb1r/p2n1ppp/2p1pn2/1p6/2BP4/2N1PN2/PP3PPP/R1BQK2R w KQkq -": (
            "D47",
            "Semi-Slav Defense: Meran Variation",
        ),
        "r2qkb1r/pb1n1ppp/4p3/3nP3/Np1N4/3B4/PP3PPP/R1BQ1RK1 b kq -": (
            "D47",
            "Semi-Slav Defense: Meran Variation, Wade Variation, Kaidanov Gambit",
        ),
        "r2qkb1r/pb1n1ppp/4p3/2pnP3/Np1P4/3B1N2/PP3PPP/R1BQK2R w KQkq -": (
            "D47",
            "Semi-Slav Defense: Meran Variation, Wade Variation, Larsen Variation",
        ),
        "r2qkb1r/pb1n1ppp/2p1pn2/1p6/3P4/2NBPN2/PP3PPP/R1BQK2R w KQkq -": (
            "D47",
            "Semi-Slav Defense: Meran Variation, Wade Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/8/2BP4/2N1PN2/PP3PPP/R1BQK2R b KQkq -": (
            "D47",
            "Semi-Slav Defense: Semi-Meran Variation",
        ),
        "r1bqkb1r/3n1ppp/p3pn2/1pp5/3PP3/2NB1N2/PP3PPP/R1BQK2R w KQkq -": (
            "D48",
            "Semi-Slav Defense: Meran Variation",
        ),
        "r1bqkb1r/3n1ppp/p3pn2/1pp1P3/3P4/2NB1N2/PP3PPP/R1BQK2R b KQkq -": (
            "D48",
            "Semi-Slav Defense: Meran Variation, Old Variation",
        ),
        "r1bqkb1r/3n1ppp/p1p1pn2/8/1p1PP3/2NB1N2/PP3PPP/R1BQK2R w KQkq -": (
            "D48",
            "Semi-Slav Defense: Meran Variation, Pirc Variation",
        ),
        "r1bqkb1r/3n1ppp/p1p1pn2/1p6/3P4/2NBPN2/PP3PPP/R1BQK2R w KQkq -": (
            "D48",
            "Semi-Slav Defense: Meran Variation",
        ),
        "r1bqkb1r/3n1ppp/p3pn2/1ppP4/4P3/2NB1N2/PP3PPP/R1BQK2R b KQkq -": (
            "D48",
            "Semi-Slav Defense: Meran Variation, Reynolds Variation",
        ),
        "r1bqkb1r/3n1ppp/p3pn2/1N2P3/3p4/3B1N2/PP3PPP/R1BQK2R b KQkq -": (
            "D49",
            "Semi-Slav Defense: Meran Variation, Blumenfeld Variation",
        ),
        "r1bqkb1r/3n1ppp/p3p3/1N2P3/3p2n1/3B1N2/PP3PPP/R1BQK2R w KQkq -": (
            "D49",
            "Semi-Slav Defense: Meran Variation, Rabinovich Variation",
        ),
        "r3kb1r/5ppp/b3pn2/1p1qN1B1/3p4/3B4/PP2QPPP/R4RK1 b kq -": (
            "D49",
            "Semi-Slav Defense: Meran Variation, Rellstab Attack",
        ),
        "r1bqkb1r/5ppp/4pn2/1p2N3/3p4/3B4/PP3PPP/R1BQ1RK1 b kq -": (
            "D49",
            "Semi-Slav Defense: Meran Variation, Sozin Variation",
        ),
        "r1bqkb1r/5ppp/p3pn2/1N2n3/3p4/3B1N2/PP3PPP/R1BQK2R w KQkq -": (
            "D49",
            "Semi-Slav Defense: Meran Variation, Sozin Variation",
        ),
        "r1bqkb1r/5ppp/4pn2/1p2N3/3p4/3B1Q2/PP3PPP/R1B1K2R b KQkq -": (
            "D49",
            "Semi-Slav Defense: Meran Variation, Stahlberg Variation",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2pp2B1/2PP4/2N5/PP2PPPP/R2QKBNR w KQkq -": (
            "D50",
            "Queen's Gambit Declined: Been-Koomen Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p2B1/2PP4/2N5/PP2PPPP/R2QKBNR b KQkq -": (
            "D50",
            "Queen's Gambit Declined: Modern Variation",
        ),
        "rnb1kb1r/pp3ppp/1q2pn2/2pP2B1/3P4/2N5/PP2PPPP/R2QKBNR w KQkq -": (
            "D50",
            "Queen's Gambit Declined: Pseudo-Tarrasch Variation, Canal Variation",
        ),
        "rnbqkb1r/pp3ppp/4pn2/3p2B1/2PQ4/2N2N2/PP2PPPP/R3KB1R b KQkq -": (
            "D50",
            "Queen's Gambit Declined: Pseudo-Tarrasch Variation, Primitive Pillsbury Variation",
        ),
        "rnbqkb1r/pp3ppp/4pn2/2pP2B1/3P4/2N5/PP2PPPP/R2QKBNR b KQkq -": (
            "D50",
            "Queen's Gambit Declined: Pseudo-Tarrasch Variation",
        ),
        "rnbqkb1r/1p3ppp/p4n2/1N1pp1B1/Q1P5/2N5/PP2PPPP/R3KB1R b KQkq -": (
            "D50",
            "Queen's Gambit Declined: Semi-Tarrasch Defense, Krause Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/3p2B1/2PPP3/2N2N2/PP3PPP/R2QKB1R b KQkq -": (
            "D51",
            "Queen's Gambit Declined: Alekhine Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/3p2B1/2PP4/P1N1P3/1P3PPP/R2QKBNR b KQkq -": (
            "D51",
            "Queen's Gambit Declined: Capablanca Variation, Anti-Cambridge Springs Variation",
        ),
        "r1bqk2r/pppn1ppp/4pn2/3p2B1/1bPP4/2N1P3/PP3PPP/R2QKBNR w KQkq -": (
            "D51",
            "Queen's Gambit Declined: Manhattan Variation",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/3p2B1/2PP4/2N1P3/PP3PPP/R2QKBNR w KQkq -": (
            "D51",
            "Queen's Gambit Declined: Modern Variation, Knight's Defense",
        ),
        "r1bqkb1r/pppn1ppp/4pn2/3p2B1/2PP4/2N1P3/PP3PPP/R2QKBNR b KQkq -": (
            "D51",
            "Queen's Gambit Declined: Modern Variation, Knight's Defense",
        ),
        "r1bqkb1r/pppn1ppp/4pn2/3p2B1/2PP4/2N5/PP2PPPP/R2QKBNR w KQkq -": (
            "D51",
            "Queen's Gambit Declined: Modern Variation, Knight's Defense",
        ),
        "r1b1kb1r/pp1n1ppp/2p1pn2/q2p4/2PP4/2N2N2/PP1BPPPP/2RQKB1R b Kkq -": (
            "D51",
            "Queen's Gambit Declined: Rochlin Variation",
        ),
        "r1b2rk1/pp1n1ppp/2p1pn2/q2p4/1bPP3B/2N1P3/PPQN1PPP/R3KB1R b KQ -": (
            "D52",
            "Queen's Gambit Declined: Cambridge Springs Defense, Argentine Variation",
        ),
        "r1b1k2r/pp1n1ppp/2p1pn2/q2p2B1/1bPP4/2N1P3/PPQN1PPP/R3KB1R b KQkq -": (
            "D52",
            "Queen's Gambit Declined: Cambridge Springs Defense, Bogoljubov Variation",
        ),
        "r1b1kb1r/pp1n1ppp/2p1pB2/q2p4/2PP4/2N1PN2/PP3PPP/R2QKB1R b KQkq -": (
            "D52",
            "Queen's Gambit Declined: Cambridge Springs Defense, Capablanca Variation",
        ),
        "r1b1kb1r/pp1n1ppp/2p1pn2/q2P2B1/3P4/2N1PN2/PP3PPP/R2QKB1R b KQkq -": (
            "D52",
            "Queen's Gambit Declined: Cambridge Springs Defense",
        ),
        "r1b1kb1r/pp1n1ppp/2p1pn2/q5B1/2pP4/2N1P3/PP1N1PPP/R2QKB1R w KQkq -": (
            "D52",
            "Queen's Gambit Declined: Cambridge Springs Defense, Rubinstein Variation",
        ),
        "r1b1kb1r/pp1n1ppp/2p1p3/q2n2B1/3P4/2N1PN2/PP3PPP/R2QKB1R w KQkq -": (
            "D52",
            "Queen's Gambit Declined: Cambridge Springs Defense, Yugoslav Variation",
        ),
        "r1b1kb1r/pp1n1ppp/2p1pn2/q2p2B1/2PP4/2N1PN2/PP3PPP/R2QKB1R w KQkq -": (
            "D52",
            "Queen's Gambit Declined: Cambridge Springs Defense",
        ),
        "r1bqkb1r/pp1n1ppp/2p1pn2/3p2B1/2PP4/2N1PN2/PP3PPP/R2QKB1R b KQkq -": (
            "D52",
            "Queen's Gambit Declined",
        ),
        "rnbqk2r/ppp1bppp/4p3/3p2B1/2PPn3/2N1P3/PP3PPP/R2QKBNR w KQkq -": (
            "D53",
            "Queen's Gambit Declined: Lasker Defense",
        ),
        "rnbqk2r/ppp1bppp/4pB2/3p4/2PP4/2N5/PP2PPPP/R2QKBNR b KQkq -": (
            "D53",
            "Queen's Gambit Declined: Modern Variation, Heral Variation",
        ),
        "rnbqk2r/ppp1bppp/4pn2/3p2B1/2PP4/2N5/PP2PPPP/R2QKBNR w KQkq -": (
            "D53",
            "Queen's Gambit Declined",
        ),
        "rnbq1rk1/ppp1bppp/4pn2/3p2B1/2PP4/2N1P3/PP3PPP/2RQKBNR b K -": (
            "D54",
            "Queen's Gambit Declined: Neo-Orthodox Variation",
        ),
        "r1bq1rk1/pp1n1pp1/2p1pb1p/8/2BP4/2N1PN2/PP3PPP/2RQ1RK1 b - -": (
            "D55",
            "Queen's Gambit Declined: Anti-Tartakower Variation, Petrosian Variation",
        ),
        "rnbq1rk1/ppp1bpp1/4pB1p/3p4/2PP4/2N1PN2/PP3PPP/R2QKB1R b KQ -": (
            "D55",
            "Queen's Gambit Declined: Anti-Tartakower Variation",
        ),
        "rnbq1rk1/ppp1bppp/4pn2/3p2B1/2PP4/2N1PN2/PP3PPP/R2QKB1R b KQ -": (
            "D55",
            "Queen's Gambit Declined: Modern Variation, Normal Line",
        ),
        "rnbq1rk1/ppp1bpp1/4pn1p/3p4/2PP3B/2N1PN2/PP3PPP/R2QKB1R b KQ -": (
            "D55",
            "Queen's Gambit Declined: Neo-Orthodox Variation, Main Line",
        ),
        "rnbq1rk1/ppp1bpp1/4pn1p/3p2B1/2PP4/2N1PN2/PP3PPP/R2QKB1R w KQ -": (
            "D55",
            "Queen's Gambit Declined: Neo-Orthodox Variation",
        ),
        "rn1q1rk1/pbp1bppp/1p3n2/3pN1B1/3P4/2NBP3/PP3PPP/R2QK2R b KQ -": (
            "D55",
            "Queen's Gambit Declined: Pillsbury Attack",
        ),
        "rnbq1rk1/ppp1bpp1/4p2p/3p4/2PPn2B/2N1PN2/PP3PPP/R2QKB1R w KQ -": (
            "D56",
            "Queen's Gambit Declined: Lasker Defense",
        ),
        "r4rk1/pp1bqpp1/2n1pn1p/2p5/2BP4/2N1PN2/PPQ2PPP/R2R2K1 w - -": (
            "D56",
            "Queen's Gambit Declined: Lasker Defense, Russian Variation",
        ),
        "rnb2rk1/ppp1qpp1/4p2p/3p4/2PPn3/2N1PN2/PPQ2PPP/R3KB1R b KQ -": (
            "D56",
            "Queen's Gambit Declined: Lasker Defense, Teichmann Variation",
        ),
        "rn1r2k1/ppp1qpp1/4b2p/3p4/2PP4/1Q2PN2/P4PPP/R3KB1R w KQ -": (
            "D57",
            "Queen's Gambit Declined: Lasker Defense, Bernstein Variation, Mar del Plata Gambit",
        ),
        "rnb2rk1/ppp2pp1/3q3p/3p4/3P4/1QP1PN2/P4PPP/R3KB1R w KQ -": (
            "D57",
            "Queen's Gambit Declined: Lasker Defense, Bernstein Variation",
        ),
        "rnb2rk1/ppp1qpp1/4p2p/3P4/3P4/2P1PN2/P4PPP/R2QKB1R b KQ -": (
            "D57",
            "Queen's Gambit Declined: Lasker Defense, Main Line",
        ),
        "rnbq1rk1/p1p1bpp1/1p2pn1p/3p4/2PP3B/2N1PN2/PP3PPP/R2QKB1R w KQ -": (
            "D58",
            "Queen's Gambit Declined: Tartakower Defense",
        ),
        "rnbq1rk1/p1p1bpp1/1p3n1p/3p4/3P3B/2N1PN2/PP3PPP/R2QKB1R w KQ -": (
            "D58",
            "Queen's Gambit Declined: Tartakower Defense, Exchange Variation",
        ),
        "rnbq1rk1/p1p1bpp1/1p2p2p/3n4/3P3B/2N1PN2/PP3PPP/R2QKB1R w KQ -": (
            "D59",
            "Queen's Gambit Declined: Tartakower Defense, Makogonov Exchange Variation",
        ),
        "rn3rk1/p1p1qpp1/1p2b2p/3p4/3P4/4PN2/PP3PPP/2RQKB1R w K -": (
            "D59",
            "Queen's Gambit Declined: Tartakower Defense",
        ),
        "r1bq1rk1/pppnbppp/4pn2/3p2B1/2PP4/2NBPN2/PP3PPP/R2QK2R b KQ -": (
            "D60",
            "Queen's Gambit Declined: Orthodox Defense, Botvinnik Variation",
        ),
        "r1bq1rk1/pppnbppp/4pn2/3p2B1/2PP4/2N1PN2/PP3PPP/R2QKB1R w KQ -": (
            "D60",
            "Queen's Gambit Declined: Orthodox Defense",
        ),
        "r1bq1rk1/pppnbppp/4pn2/3p2B1/2PP4/1QN1PN2/PP3PPP/R3KB1R b KQ -": (
            "D60",
            "Queen's Gambit Declined: Orthodox Defense, Rauzer Variation",
        ),
        "r1bq1rk1/pppnbppp/4pn2/3p2B1/2PP4/2N1PN2/PPQ2PPP/R3KB1R b KQ -": (
            "D61",
            "Queen's Gambit Declined: Orthodox Defense, Rubinstein Variation",
        ),
        "r1bq1rk1/pp1nbppp/4pn2/2pP2B1/3P4/2N1PN2/PPQ2PPP/R3KB1R b KQ -": (
            "D62",
            "Queen's Gambit Declined: Orthodox Defense, Rubinstein Variation, Flohr Line",
        ),
        "r1bq1rk1/p1pnbppp/1p3n2/1B1p2B1/3P4/2N1PN2/PP3PPP/2RQK2R b K -": (
            "D63",
            "Queen's Gambit Declined: Orthodox Defense, Capablanca Variation",
        ),
        "r1bq1rk1/1ppnbppp/p3pn2/3p2B1/2PP4/2N1PN2/PP3PPP/2RQKB1R w K -": (
            "D63",
            "Queen's Gambit Declined: Orthodox Defense, Henneberger Variation",
        ),
        "r1bq1rk1/pp1nbppp/2p1pn2/3p2B1/2PP4/2N1PN2/PP3PPP/2RQKB1R w K -": (
            "D63",
            "Queen's Gambit Declined: Orthodox Defense, Main Line",
        ),
        "r1bq1rk1/pppnbppp/4pn2/3p2B1/2PP4/2N1PN2/PP3PPP/2RQKB1R b K -": (
            "D63",
            "Queen's Gambit Declined: Orthodox Defense, Main Line",
        ),
        "r1bq1rk1/p1pnbppp/1p3n2/3p2B1/3P4/2NBPN2/PP3PPP/2RQK2R b K -": (
            "D63",
            "Queen's Gambit Declined: Orthodox Defense, Pillsbury Variation",
        ),
        "r1bq1rk1/1ppnbppp/p3pn2/3P2B1/3P4/2N1PN2/PP3PPP/2RQKB1R b K -": (
            "D63",
            "Queen's Gambit Declined: Orthodox Defense, Swiss, Karlsbad Variation",
        ),
        "r1bq1rk1/1p1nbppp/p1p1pn2/3p2B1/2PP4/2N1PN2/PPQ2PPP/2R1KB1R w K -": (
            "D64",
            "Queen's Gambit Declined: Orthodox Defense, Rubinstein Attack",
        ),
        "r1bq1rk1/1p1nbppp/p1p1pn2/3p2B1/2PP4/P1N1PN2/1PQ2PPP/2R1KB1R b K -": (
            "D64",
            "Queen's Gambit Declined: Orthodox Defense, Rubinstein Attack",
        ),
        "r1bq1rk1/pp1nbppp/2p1p3/3p2B1/2PPn3/2N1PN2/PPQ2PPP/2R1KB1R w K -": (
            "D64",
            "Queen's Gambit Declined: Orthodox Defense, Rubinstein Attack",
        ),
        "r1bq1rk1/pp1nbppp/2p1pn2/3p2B1/2PP4/2N1PN2/PPQ2PPP/2R1KB1R b K -": (
            "D64",
            "Queen's Gambit Declined: Orthodox Defense, Rubinstein Attack",
        ),
        "r1bq1rk1/1p1nbppp/p1p1pn2/3P2B1/3P4/2N1PN2/PPQ2PPP/2R1KB1R b K -": (
            "D65",
            "Queen's Gambit Declined: Orthodox Defense, Rubinstein Attack",
        ),
        "r1bq1rk1/pp1nbppp/2p1pn2/3p2B1/2PP4/2NBPN2/PP3PPP/2RQK2R b K -": (
            "D66",
            "Queen's Gambit Declined: Orthodox Defense, Bd3 Line",
        ),
        "r1bq1rk1/p2nbppp/2p1pn2/1p4B1/2BP4/2N1PN2/PP3PPP/2RQK2R w K -": (
            "D66",
            "Queen's Gambit Declined: Orthodox Defense, Fianchetto Variation",
        ),
        "r1b2rk1/pp1nqppp/2p1p3/3n4/2BPN3/4PN2/PP3PPP/2RQK2R b K -": (
            "D67",
            "Queen's Gambit Declined: Orthodox Defense, Alekhine Variation",
        ),
        "r1b2rk1/pp1nqppp/2p1p3/3n4/2BP4/2N1PN2/PP3PPP/2RQK2R w K -": (
            "D67",
            "Queen's Gambit Declined: Orthodox Defense, Bd3 Line",
        ),
        "r1bq1rk1/pp1nbppp/2p1p3/3n2B1/2BP4/2N1PN2/PP3PPP/2RQK2R w K -": (
            "D67",
            "Queen's Gambit Declined: Orthodox Defense, Capablanca System",
        ),
        "r1bq1rk1/pp1nbppp/2p1p3/3n2B1/2BP3P/2N1PN2/PP3PP1/2RQK2R b K -": (
            "D67",
            "Queen's Gambit Declined: Orthodox Defense, Janowski Variation",
        ),
        "r1b2rk1/pp1nqppp/2p1p3/3n4/2BP4/2N1PN2/PP3PPP/2RQ1RK1 b - -": (
            "D67",
            "Queen's Gambit Declined: Orthodox Defense, Main Line",
        ),
        "r1b2rk1/pp1nqppp/2p5/4p3/2BP4/2R1PN2/PP3PPP/1Q3RK1 b - -": (
            "D68",
            "Queen's Gambit Declined: Orthodox Defense, Classical Variation",
        ),
        "r1b2rk1/pp1nqppp/2p5/4p3/2BP4/2R1PN2/PP3PPP/3Q1RK1 w - -": (
            "D68",
            "Queen's Gambit Declined: Orthodox Defense, Classical Variation",
        ),
        "r1b2rk1/pp1nqppp/2p5/4p3/2BP4/2R1PN2/PPQ2PPP/5RK1 b - -": (
            "D68",
            "Queen's Gambit Declined: Orthodox Defense, Classical Variation",
        ),
        "r1b2rk1/pp3ppp/2p5/4q3/2B5/2R1P3/PP3PPP/3Q1RK1 w - -": (
            "D69",
            "Queen's Gambit Declined: Orthodox Defense, Classical Variation",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/5P2/PP2P1PP/RNBQKBNR w KQkq -": (
            "D70",
            "Neo-Grünfeld Defense: Goglidze Attack",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/6P1/PP2PP1P/RNBQKBNR w KQkq -": (
            "D70",
            "Neo-Grünfeld Defense",
        ),
        "rnbqk2r/ppp1ppbp/6p1/3n4/3P4/6P1/PP2PPBP/RNBQK1NR w KQkq -": (
            "D71",
            "Neo-Grünfeld Defense: Exchange Variation",
        ),
        "rnbq1rk1/ppp1ppbp/6p1/3n4/3P4/5NP1/PP2PPBP/RNBQ1RK1 b - -": (
            "D74",
            "Neo-Grünfeld Defense: Delayed Exchange Variation",
        ),
        "rnbq1rk1/pp2ppbp/6p1/2pn4/3P4/2N2NP1/PP2PPBP/R1BQ1RK1 b - -": (
            "D75",
            "Neo-Grünfeld Defense: Delayed Exchange Variation",
        ),
        "rnbq1rk1/pp2ppbp/6p1/2Pn4/8/5NP1/PP2PPBP/RNBQ1RK1 b - -": (
            "D75",
            "Neo-Grünfeld Defense: Delayed Exchange Variation",
        ),
        "rnbq1rk1/ppp1ppbp/1n4p1/8/3P4/5NP1/PP2PPBP/RNBQ1RK1 w - -": (
            "D76",
            "Neo-Grünfeld Defense: Delayed Exchange Variation",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/8/2pP4/5NP1/PP2PPBP/RNBQ1RK1 w - -": (
            "D77",
            "Neo-Grünfeld Defense: Classical Variation, Modern Defense",
        ),
        "r1bq1rk1/ppp1ppbp/2n2np1/3p4/2PP4/5NP1/PP2PPBP/RNBQ1RK1 w - -": (
            "D77",
            "Neo-Grünfeld Defense: Classical Variation, Polgár Variation",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p4/2PP4/5NP1/PP2PPBP/RNBQ1RK1 b - -": (
            "D77",
            "Neo-Grünfeld Defense: Classical Variation",
        ),
        "rnbq1rk1/pp2ppbp/2p2np1/3p4/2PP4/5NP1/PP2PPBP/RNBQ1RK1 w - -": (
            "D78",
            "Neo-Grünfeld Defense: Classical Variation, Original Defense",
        ),
        "rnbq1rk1/pp2ppbp/5np1/3p4/3P4/5NP1/PP2PPBP/RNBQ1RK1 w - -": (
            "D79",
            "Neo-Grünfeld Defense: Ultra-delayed Exchange Variation",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP2P1/2N5/PP2PP1P/R1BQKBNR b KQkq -": (
            "D80",
            "Grünfeld Defense: Gibbon Gambit",
        ),
        "rnbqkb1r/pp2pp1p/6p1/2p3B1/2PPp3/8/PP1QPPPP/R3KBNR w KQkq -": (
            "D80",
            "Grünfeld Defense: Lundin Variation",
        ),
        "rnbqkb1r/pp2pp1p/6p1/2pn4/N2P4/5P2/PP2P1PP/R1BQKBNR b KQkq -": (
            "D80",
            "Grünfeld Defense: Lutikov Variation, Murrey Attack",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/2N2P2/PP2P1PP/R1BQKBNR b KQkq -": (
            "D80",
            "Grünfeld Defense: Lutikov Variation",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D80",
            "Grünfeld Defense",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p2B1/2PP4/2N5/PP2PPPP/R2QKBNR b KQkq -": (
            "D80",
            "Grünfeld Defense: Stockholm Variation",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP3P/2N5/PP2PPP1/R1BQKBNR b KQkq -": (
            "D80",
            "Grünfeld Defense: Zaitsev Gambit",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/1QN5/PP2PPPP/R1B1KBNR b KQkq -": (
            "D81",
            "Grünfeld Defense: Russian Variation, Accelerated Variation",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP1B2/2N5/PP2PPPP/R2QKBNR b KQkq -": (
            "D82",
            "Grünfeld Defense: Brinckmann Attack",
        ),
        "rn1q1rk1/pp2ppbp/4bnp1/2Pp4/2P2B2/2N1P3/PP3PPP/2RQKBNR w K -": (
            "D83",
            "Grünfeld Defense: Brinckmann Attack, Grünfeld Gambit, Botvinnik Variation",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p4/2PP1B2/2N1P3/PP3PPP/2RQKBNR b K -": (
            "D83",
            "Grünfeld Defense: Brinckmann Attack, Grünfeld Gambit, Capablanca Variation",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p4/2PP1B2/2N1P3/PP3PPP/R2QKBNR w KQ -": (
            "D83",
            "Grünfeld Defense: Brinckmann Attack, Grünfeld Gambit",
        ),
        "rnb2rk1/pp2ppbp/5np1/q1Pp4/2P2B2/2N1P3/PP3PPP/2RQKBNR w K -": (
            "D83",
            "Grünfeld Defense: Brinckmann Attack, Reshevsky Gambit",
        ),
        "rnb2rk1/ppB1ppbp/6p1/3q4/3P4/4P3/PP3PPP/R2QKBNR b KQ -": (
            "D84",
            "Grünfeld Defense: Brinckmann Attack, Grünfeld Gambit Accepted",
        ),
        "rnbqk2r/pp2ppbp/6p1/2p5/3PP3/2P2N1P/P4PP1/R1BQKB1R b KQkq -": (
            "D85",
            "Grünfeld Defense: Exchange Variation, Modern Exchange Variation, Kramnik Line",
        ),
        "r1bq1rk1/pp2pp1p/2n3p1/2pP4/4P3/2b2N2/P3BPPP/1RBQK2R w K -": (
            "D85",
            "Grünfeld Defense: Exchange Variation, Modern Exchange Variation, Pawn Grab Line",
        ),
        "rnbqk2r/ppp1ppbp/6p1/8/3PP3/2P2N2/P4PPP/R1BQKB1R b KQkq -": (
            "D85",
            "Grünfeld Defense: Exchange Variation, Modern Exchange Variation",
        ),
        "rnbqkb1r/ppp1pp1p/6p1/3n4/N2P4/8/PP2PPPP/R1BQKBNR b KQkq -": (
            "D85",
            "Grünfeld Defense: Exchange Variation, Nadanian Attack",
        ),
        "rnbqkb1r/ppp1pp1p/6p1/3n4/3P4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "D85",
            "Grünfeld Defense: Exchange Variation",
        ),
        "rnb2rk1/p1pqppbp/1p4p1/8/2BPP3/2P5/P3NPPP/R1BQ1RK1 w - -": (
            "D86",
            "Grünfeld Defense: Exchange Variation, Larsen Variation",
        ),
        "rnbq1rk1/p1p1ppbp/1p4p1/8/2BPP3/2P5/P3NPPP/R1BQK2R w KQ -": (
            "D86",
            "Grünfeld Defense: Exchange Variation, Simagin's Lesser Variation",
        ),
        "rnbqk2r/ppp1ppbp/6p1/8/2BPP3/2P5/P4PPP/R1BQK1NR b KQkq -": (
            "D86",
            "Grünfeld Defense: Exchange Variation, Classical Variation",
        ),
        "rnb2rk1/pppqppbp/6p1/8/2BPP3/2P5/P3NPPP/R1BQK2R w KQ -": (
            "D86",
            "Grünfeld Defense: Exchange Variation, Larsen Variation",
        ),
        "r1bq1rk1/ppp1ppbp/2n3p1/8/2BPP3/2P5/P3NPPP/R1BQK2R w KQ -": (
            "D86",
            "Grünfeld Defense: Exchange Variation, Simagin's Improved Variation",
        ),
        "r2q1rk1/pp2pBbp/6p1/n1p5/3PP1b1/2P1BP2/P3N1PP/R2Q1RK1 b - -": (
            "D87",
            "Grünfeld Defense: Exchange Variation, Seville Variation",
        ),
        "rnbq1rk1/pp2ppbp/6p1/2p5/2BPP3/2P5/P3NPPP/R1BQK2R w KQ -": (
            "D87",
            "Grünfeld Defense: Exchange Variation, Spassky Variation",
        ),
        "r1bq1rk1/pp2ppbp/2n3p1/8/2BPP3/4B3/P3NPPP/R2Q1RK1 b - -": (
            "D88",
            "Grünfeld Defense: Exchange Variation, Spassky Variation",
        ),
        "r2q1rk1/pp2ppbp/4b1p1/n2P4/4P3/3BBP2/P3N1PP/R2Q1RK1 b - -": (
            "D89",
            "Grünfeld Defense: Exchange Variation, Sokolsky Variation",
        ),
        "r2q1rk1/pp2ppbp/4b1p1/n7/3PP3/3BBP2/P3N1PP/R2Q1RK1 w - -": (
            "D89",
            "Grünfeld Defense: Exchange Variation, Spassky Variation",
        ),
        "rnbqk2r/ppp1ppbp/5np1/3p4/Q1PP4/2N2N2/PP2PPPP/R1B1KB1R b KQkq -": (
            "D90",
            "Grünfeld Defense: Flohr Variation",
        ),
        "rnbqk2r/ppp1ppbp/5np1/3p4/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D90",
            "Grünfeld Defense: Three Knights Variation",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "D90",
            "Grünfeld Defense: Three Knights Variation",
        ),
        "rnbqkb1r/pp2pp1p/2p2np1/3p4/2PP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "D90",
            "Slav Defense: Schlechter Variation",
        ),
        "rnbqk2r/ppp1ppbp/5np1/3p2B1/2PP4/2N2N2/PP2PPPP/R2QKB1R b KQkq -": (
            "D91",
            "Grünfeld Defense: Three Knights Variation, Petrosian System",
        ),
        "rnbqk2r/ppp1ppbp/5np1/3p4/2PP1B2/2N2N2/PP2PPPP/R2QKB1R b KQkq -": (
            "D92",
            "Grünfeld Defense: Three Knights Variation, Hungarian Attack",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p4/2PP1B2/2N1PN2/PP3PPP/R2QKB1R b KQ -": (
            "D93",
            "Grünfeld Defense: Three Knights Variation, Hungarian Variation",
        ),
        "rn1q1rk1/pp2ppbp/2p2np1/3p1b2/2PP4/2NBPN2/PP3PPP/R1BQ1RK1 w - -": (
            "D94",
            "Grünfeld Defense: Flohr Defense",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p4/1PPP4/2N1PN2/P4PPP/R1BQKB1R b KQ -": (
            "D94",
            "Grünfeld Defense: Makogonov Variation",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p4/2PP4/2N1PN2/PP1B1PPP/R2QKB1R b KQ -": (
            "D94",
            "Grünfeld Defense: Opocensky Variation",
        ),
        "rn1q1rk1/pp2ppbp/2p2np1/3p4/2PP2b1/2NBPN2/PP3PPP/R1BQ1RK1 w - -": (
            "D94",
            "Grünfeld Defense: Smyslov Defense",
        ),
        "rnbqk2r/ppp1ppbp/5np1/3p4/2PP4/2N1PN2/PP3PPP/R1BQKB1R b KQkq -": (
            "D94",
            "Grünfeld Defense: Three Knights Variation, Burille Variation",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p4/2PP4/2NBPN2/PP3PPP/R1BQK2R b KQ -": (
            "D94",
            "Grünfeld Defense: Three Knights Variation, Paris Variation",
        ),
        "rnbq1rk1/ppp2pbp/4pnp1/3p4/2PP4/1QN1PN2/PP3PPP/R1B1KB1R w KQ -": (
            "D95",
            "Grünfeld Defense: Botvinnik Variation",
        ),
        "r1bq1rk1/pppnppbp/5np1/6N1/2BP4/1QN1P3/PP3PPP/R1B1K2R b KQ -": (
            "D95",
            "Grünfeld Defense: Pachman Variation",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/3p4/2PP4/1QN1PN2/PP3PPP/R1B1KB1R b KQ -": (
            "D95",
            "Grünfeld Defense: Three Knights Variation, Vienna Variation",
        ),
        "rnbqk2r/ppp1ppbp/5np1/3p4/2PP4/1QN2N2/PP2PPPP/R1B1KB1R b KQkq -": (
            "D96",
            "Grünfeld Defense: Russian Variation",
        ),
        "r1bq1rk1/ppp1ppbp/2n2np1/8/2QPP3/2N2N2/PP3PPP/R1B1KB1R w KQ -": (
            "D97",
            "Grünfeld Defense: Russian Variation, Byrne (Simagin) Variation",
        ),
        "rnbq1rk1/1pp1ppbp/p4np1/8/2QPP3/2N2N2/PP3PPP/R1B1KB1R w KQ -": (
            "D97",
            "Grünfeld Defense: Russian Variation, Hungarian Variation",
        ),
        "rnbq1rk1/p1p1ppbp/1p3np1/8/2QPP3/2N2N2/PP3PPP/R1B1KB1R w KQ -": (
            "D97",
            "Grünfeld Defense: Russian Variation, Levenfish Variation",
        ),
        "r1bq1rk1/ppp1ppbp/n4np1/8/2QPP3/2N2N2/PP3PPP/R1B1KB1R w KQ -": (
            "D97",
            "Grünfeld Defense: Russian Variation, Prins Variation",
        ),
        "rnbq1rk1/pp2ppbp/2p2np1/8/2QPP3/2N2N2/PP3PPP/R1B1KB1R w KQ -": (
            "D97",
            "Grünfeld Defense: Russian Variation, Szabo (Boleslavsky)",
        ),
        "rnbq1rk1/ppp1ppbp/5np1/8/2QPP3/2N2N2/PP3PPP/R1B1KB1R b KQ -": (
            "D97",
            "Grünfeld Defense: Russian Variation",
        ),
        "r2q1rk1/ppp1ppbp/1nn3p1/8/3PP1b1/2NQBN2/PP2BPPP/2KR3R b - -": (
            "D98",
            "Grünfeld Defense: Russian Variation, Keres Variation",
        ),
        "rn1q1rk1/ppp1ppbp/5np1/8/2QPP1b1/2N2N2/PP3PPP/R1B1KB1R w KQ -": (
            "D98",
            "Grünfeld Defense: Russian Variation, Smyslov Variation",
        ),
        "rn1q1rk1/pppnppbp/6p1/8/3PP1b1/1QN1BN2/PP3PPP/R3KB1R b KQ -": (
            "D99",
            "Grünfeld Defense: Russian Variation, Smyslov Variation",
        ),
        "rn1q1rk1/pp1nppbp/6p1/2p5/3PP1b1/1QN1BN2/PP3PPP/R3KB1R w KQ -": (
            "D99",
            "Grünfeld Defense: Russian Variation, Yugoslav Variation",
        ),
        "rnbqkb1r/pppp1ppp/5n2/4p3/2PP4/6P1/PP2PP1P/RNBQKBNR w KQkq -": (
            "E00",
            "Catalan Opening: Hungarian Gambit",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/6P1/PP2PP1P/RNBQKBNR w KQkq -": (
            "E00",
            "Catalan Opening",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/8/2PP4/6P1/PP2PP1P/RNBQKBNR b KQkq -": (
            "E00",
            "Catalan Opening",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/8/2PP2P1/8/PP2PP1P/RNBQKBNR b KQkq -": (
            "E00",
            "Indian Game: Devin Gambit",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/8/2PP4/1Q6/PP2PPPP/RNB1KBNR b KQkq -": (
            "E00",
            "Indian Game",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/6B1/2PP4/8/PP2PPPP/RN1QKBNR b KQkq -": (
            "E00",
            "Indian Game: Seirawan Attack",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/6P1/PP2PPBP/RNBQK1NR b KQkq -": (
            "E01",
            "Catalan Opening: Closed Defense",
        ),
        "r1bqkb1r/pp3ppp/2n1pn2/2pp4/2PP4/5NP1/PP2PPBP/RNBQK2R w KQkq -": (
            "E01",
            "Catalan Opening: Open Defense, Tarrasch Defense",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/8/Q1pP4/6P1/PP2PPBP/RNB1K1NR b KQkq -": (
            "E02",
            "Catalan Opening: Open Defense",
        ),
        "r1bqkb1r/1ppn1ppp/p3pn2/8/3P4/6P1/PPQ1PPBP/RNB1K1NR b KQkq -": (
            "E03",
            "Catalan Opening: Open Defense, Alekhine Variation",
        ),
        "r1bqkb1r/pppn1ppp/4pn2/8/2QP4/6P1/PP2PPBP/RNB1K1NR b KQkq -": (
            "E03",
            "Catalan Opening: Open Defense",
        ),
        "r1bqk2r/ppp2ppp/2n1pn2/8/QbpP4/5NP1/PP2PPBP/RNB1K2R w KQkq -": (
            "E04",
            "Catalan Opening: Open Defense, Modern Sharp Variation",
        ),
        "rnbqkb1r/ppp2ppp/4pn2/8/2pP4/5NP1/PP2PPBP/RNBQK2R b KQkq -": (
            "E04",
            "Catalan Opening: Open Defense",
        ),
        "rnbqk2r/ppp1bppp/4pn2/8/2pP4/5NP1/PP2PPBP/RNBQK2R w KQkq -": (
            "E05",
            "Catalan Opening: Open Defense, Classical Line",
        ),
        "rnbqk2r/ppp1bppp/4pn2/3p4/2PP4/5NP1/PP2PPBP/RNBQK2R b KQkq -": (
            "E06",
            "Catalan Opening: Closed Defense",
        ),
        "r1bq1rk1/pp1nbppp/2p1pn2/3p4/2PP4/2NQ1NP1/PP2PPBP/R1B2RK1 b - -": (
            "E07",
            "Catalan Opening: Closed Defense, Botvinnik Variation",
        ),
        "r1bq1rk1/pppnbppp/4pn2/3p4/2PP4/5NP1/PP2PPBP/RNBQ1RK1 w - -": (
            "E07",
            "Catalan Opening: Closed Defense",
        ),
        "r1bq1rk1/pp1nbppp/2p1pn2/3p4/2PP4/1P3NP1/P1Q1PPBP/RNB2RK1 b - -": (
            "E08",
            "Catalan Opening: Closed Defense",
        ),
        "r2q1rk1/pb1nbppp/2p1pn2/1p1p4/2PP4/1PN2NP1/P1Q1PPBP/R1BR2K1 w - -": (
            "E08",
            "Catalan Opening: Closed Defense, Spassky Gambit",
        ),
        "r1bq1rk1/pppnbppp/4pn2/3p4/2PP4/5NP1/PPQ1PPBP/RNB2RK1 b - -": (
            "E08",
            "Catalan Opening: Closed Defense",
        ),
        "r1bq1rk1/p2nbppp/1pp1pn2/3p4/P1PP4/5NP1/1PQ1PPBP/RNBR2K1 b - -": (
            "E08",
            "Catalan Opening: Closed Defense, Zagoryansky Variation",
        ),
        "r1bq1rk1/pp1nbppp/2p1pn2/3p4/2PP4/5NP1/PPQNPPBP/R1B2RK1 b - -": (
            "E09",
            "Catalan Opening: Closed Defense, Main Line",
        ),
        "r2q1rk1/3nbppp/bpp1pn2/p2p4/2PP4/1P3NP1/PBQNPPBP/R4RK1 w - -": (
            "E09",
            "Catalan Opening: Closed Defense, Sokolsky Variation",
        ),
        "r1bq1rk1/p2nbppp/2p1pn2/1p1p4/2PP4/5NP1/PPQNPPBP/R1B2RK1 w - -": (
            "E09",
            "Catalan Opening: Closed Variation, Rabinovich Variation",
        ),
        "r1bq1rk1/p2nbppp/1pp1pn2/3p4/2PP4/5NP1/PPQNPPBP/R1B2RK1 w - -": (
            "E09",
            "Catalan Opening: Closed Variation, Traditional Variation",
        ),
        "rnbqkb1r/p5pp/4pn2/1Ppp4/8/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "E10",
            "Blumenfeld Countergambit Accepted",
        ),
        "rnbqkb1r/p2p1ppp/4pn2/1ppP2B1/2P5/5N2/PP2PPPP/RN1QKB1R b KQkq -": (
            "E10",
            "Blumenfeld Countergambit: Dus-Khotimirsky Variation",
        ),
        "rnbqkb1r/p2p1ppp/4pn2/1ppP4/2P5/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "E10",
            "Blumenfeld Countergambit",
        ),
        "rnbqkb1r/pp1p1ppp/4pn2/2p5/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "E10",
            "Blumenfeld Countergambit",
        ),
        "rnbqkb1r/p2p1pp1/5n1p/1ppP2B1/8/5N2/PP2PPPP/RN1QKB1R w KQkq -": (
            "E10",
            "Blumenfeld Countergambit: Spielmann Variation",
        ),
        "rnbqkb1r/pppp1ppp/4pn2/8/2PP4/5N2/PP2PPPP/RNBQKB1R b KQkq -": (
            "E10",
            "Indian Game: Anti-Nimzowitsch-Indian Variation",
        ),
        "rnbqkb1r/pppp1ppp/4p3/8/2PPn3/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "E10",
            "Indian Game: Döry Indian Variation",
        ),
        "rnbqkb1r/1ppp1ppp/p3pn2/8/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "E10",
            "Indian Game: Dzindzi-Indian Defense",
        ),
        "r1bqkb1r/pp3ppp/2n1pn2/2pp4/2PP4/2N1PN2/PP3PPP/R1BQKB1R w KQkq -": (
            "E10",
            "Tarrasch Defense: Symmetrical Variation",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/2PP4/5N2/PP1bPPPP/RN1QKB1R w KQkq -": (
            "E11",
            "Bogo-Indian Defense: Exchange Variation",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/5N2/PP1NPPPP/R1BQKB1R b KQkq -": (
            "E11",
            "Bogo-Indian Defense: Grünfeld Variation",
        ),
        "r1bqk2r/pppp1ppp/2n1pn2/8/1bPP4/5N2/PP1BPPPP/RN1QKB1R w KQkq -": (
            "E11",
            "Bogo-Indian Defense: Haiti Variation",
        ),
        "rn1q1rk1/pbpp1ppp/1p2p3/6N1/2PP4/2n3P1/PPQ1PPBP/R3K2R b KQ -": (
            "E11",
            "Bogo-Indian Defense: Monticelli Trap",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/8/PP1NPPPP/RNBQKB1R b KQkq -": (
            "E11",
            "Bogo-Indian Defense: New England Variation",
        ),
        "rnb1k2r/ppppqppp/4pn2/8/1bPP4/5N2/PP1BPPPP/RN1QKB1R w KQkq -": (
            "E11",
            "Bogo-Indian Defense: Nimzowitsch Variation",
        ),
        "rnbqk2r/ppppbppp/4pn2/8/2PP4/5N2/PP1BPPPP/RN1QKB1R w KQkq -": (
            "E11",
            "Bogo-Indian Defense: Retreat Variation",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "E11",
            "Bogo-Indian Defense",
        ),
        "rnbqk2r/pp1p1ppp/4pn2/2p5/1bPP4/5N2/PP1BPPPP/RN1QKB1R w KQkq -": (
            "E11",
            "Bogo-Indian Defense: Vitolins Variation",
        ),
        "rnbqk2r/1ppp1ppp/4pn2/p7/1bPP4/5N2/PP1BPPPP/RN1QKB1R w KQkq -": (
            "E11",
            "Bogo-Indian Defense: Wade-Smyslov Variation",
        ),
        "rn1qk2r/pbpp1ppp/1p2pn2/6B1/1bPP4/2N5/PP1NPPPP/R2QKB1R b KQkq -": (
            "E12",
            "Nimzowitsch-Indian Defense: Three Knights Variation, Duchamp Variation, Modern Line",
        ),
        "rnbqk2r/p1pp1ppp/1p2pn2/8/1bPP4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "E12",
            "Nimzowitsch-Indian Defense: Three Knights Variation, Duchamp Variation",
        ),
        "rn1qkb1r/pbpp1ppp/1p2p3/8/2PPn3/P1N2N2/1P2PPPP/R1BQKB1R w KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Andersson Variation",
        ),
        "rn1qkb1r/pbp2ppp/1p3n2/3p4/3P4/P1N2N2/1P2PPPP/R1BQKB1R w KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Classical Variation",
        ),
        "rn1qkb1r/pbpp1p1p/1p2pnp1/8/2PP4/P1N2N2/1P2PPPP/R1BQKB1R w KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Hedgehog Variation",
        ),
        "rn1qkb1r/pbp2ppp/1p2p3/3n4/3P4/P1N2N2/1PQ1PPPP/R1B1KB1R b KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Kasparov Attack",
        ),
        "rn1qkb1r/pbp2ppp/1p2pn2/3p4/2PP4/P1N2N2/1P2PPPP/R1BQKB1R w KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Main Line",
        ),
        "rn1qk2r/pbppbppp/1p2pn2/8/2PP4/P1N2N2/1P2PPPP/R1BQKB1R w KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Marco Defense",
        ),
        "rn1qkb1r/pbp2ppp/1p2p3/3n4/3P4/P1N2N2/1P2PPPP/R1BQKB1R w KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Modern Variation",
        ),
        "rn1qkb1r/pbp2ppp/1p2p3/3n4/3P4/P1N1PN2/1P3PPP/R1BQKB1R b KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Petrosian Attack",
        ),
        "rn1qkb1r/pbp2ppp/1p2p3/3n4/3PP3/P1N2N2/1P3PPP/R1BQKB1R b KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Polovodin Gambit",
        ),
        "rn1qkb1r/pbp2ppp/1p2p3/3n4/Q2P4/P1N2N2/1P2PPPP/R1B1KB1R b KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Rashkovsky Attack",
        ),
        "rn1qkb1r/pbpp1ppp/1p2pn2/8/2PP4/P1N2N2/1P2PPPP/R1BQKB1R b KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation",
        ),
        "rn1qkb1r/pbp2ppp/1p2p3/3n4/3P4/P1N2N2/1P1BPPPP/R2QKB1R b KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov-Petrosian Variation, Romanishin Attack",
        ),
        "rn1qkb1r/pbpp1p2/1p2p2p/6pn/2PP4/2N2NB1/PP2PPPP/R2QKB1R w KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov Variation, Botvinnik Attack",
        ),
        "rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "E12",
            "Queen's Indian Defense: Kasparov Variation",
        ),
        "rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP1B2/5N2/PP2PPPP/RN1QKB1R b KQkq -": (
            "E12",
            "Queen's Indian Defense: Miles Variation",
        ),
        "rn1qkb1r/pbpp1ppp/1p2pn2/8/2PP4/P4N2/1PQ1PPPP/RNB1KB1R w KQkq -": (
            "E12",
            "Queen's Indian Defense: Petrosian Variation, Farago Defense",
        ),
        "rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/P4N2/1P2PPPP/RNBQKB1R b KQkq -": (
            "E12",
            "Queen's Indian Defense: Petrosian Variation",
        ),
        "rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "E12",
            "Queen's Indian Defense",
        ),
        "rn1qk2r/pbpp1pp1/1p2pn1p/8/1bPP3B/2N2N2/PP2PPPP/R2QKB1R w KQkq -": (
            "E13",
            "Queen's Indian Defense: Kasparov Variation",
        ),
        "rn1q1rk1/pb1pbppp/1p2pn2/8/2PN4/1P1BP3/PB3PPP/RN1Q1RK1 b - -": (
            "E14",
            "Queen's Indian, Averbakh Variation",
        ),
        "rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/4PN2/PP3PPP/RNBQKB1R b KQkq -": (
            "E14",
            "Queen's Indian Defense: Spassky System",
        ),
        "rn1qkb1r/pb1p1ppp/1p3n2/2pp2N1/2P5/6P1/PP2PPBP/RNBQK2R b KQkq -": (
            "E15",
            "Queen's Indian, Buerger Variation",
        ),
        "rn1qkb1r/pbpp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R w KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Traditional",
        ),
        "rn1qk2r/p1ppbppp/bp2pn2/8/2PP4/1P3NP1/P2BPP1P/RN1QKB1R w KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Variation, Check Variation, Intermezzo Line",
        ),
        "rn2k2r/p1ppqppp/bp2pn2/8/1bPP4/1P3NP1/P2BPP1P/RN1QKB1R w KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Variation, Check Variation, Modern Line",
        ),
        "rn1qk2r/p1pp1ppp/bp2pn2/8/1bPP4/1P3NP1/P3PP1P/RNBQKB1R w KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Variation, Check Variation",
        ),
        "rn1qkb1r/p1pp1ppp/bp2pn2/8/Q1PP4/5NP1/PP2PP1P/RNB1KB1R b KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Variation, Nimzowitsch Variation, Nimzowitsch Attack",
        ),
        "rn1qkb1r/p1pp1ppp/bp2pn2/8/2PP4/1P3NP1/P3PP1P/RNBQKB1R b KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Variation, Nimzowitsch Variation, Quiet Line",
        ),
        "rn1qkb1r/p1pp1ppp/bp2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R w KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Variation, Nimzowitsch Variation",
        ),
        "rn1qkb1r/p1pp1ppp/bp2pn2/8/2PP4/1Q3NP1/PP2PP1P/RNB1KB1R b KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Variation, Nimzowitsch Variation, Timman Line",
        ),
        "rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R b KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Variation",
        ),
        "rn1qkb1r/pb1p1ppp/1p3n2/2pp4/2P4N/6P1/PP2PPBP/RNBQK2R b KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Variation, Rubinstein Variation",
        ),
        "rn1qkb1r/pb1p1ppp/1p2pn2/2p5/2PP4/5NP1/PP2PPBP/RNBQK2R w KQkq -": (
            "E15",
            "Queen's Indian Defense: Fianchetto Variation, Sämisch Variation",
        ),
        "rn1qk2r/pbpp1ppp/1p2pn2/8/1bPP4/5NP1/PP2PPBP/RNBQK2R w KQkq -": (
            "E16",
            "Queen's Indian Defense: Capablanca Variation",
        ),
        "rn1qk2r/pbppbppp/1p2pn2/8/2PP4/5NP1/PP1BPPBP/RN1QK2R w KQkq -": (
            "E16",
            "Queen's Indian Defense: Riumin Variation",
        ),
        "rn1qk2r/1bpp1ppp/1p2pn2/p7/1bPP4/5NP1/PP1BPPBP/RN1QK2R w KQkq -": (
            "E16",
            "Queen's Indian Defense: Yates Variation",
        ),
        "rn1qk2r/pbppbppp/1p2pn2/8/2PP4/2N2NP1/PP2PPBP/R1BQK2R b KQkq -": (
            "E17",
            "Queen's Indian Defense: Anti-Queen's Indian System",
        ),
        "rn1q1rk1/pbppbppp/1p3n2/3p4/2P4N/6P1/PP2PPBP/RNBQ1RK1 b - -": (
            "E17",
            "Queen's Indian Defense: Classical Variation, Polugaevsky Gambit",
        ),
        "rn1qk2r/pbppbppp/1p2pn2/8/2PP4/5NP1/PP2PPBP/RNBQ1RK1 b kq -": (
            "E17",
            "Queen's Indian Defense: Classical Variation",
        ),
        "rn1q1rk1/pbppbppp/1p3n2/3p4/2PN4/6P1/PP2PPBP/RNBQ1RK1 b - -": (
            "E17",
            "Queen's Indian Defense: Classical Variation, Taimanov Gambit",
        ),
        "rn1q1rk1/pbppbppp/1p2pn2/8/2PP4/1P3NP1/P3PPBP/RNBQ1RK1 b - -": (
            "E17",
            "Queen's Indian Defense: Euwe Variation",
        ),
        "rn1q1rk1/pbppbppp/1p2pn2/8/2PP4/5NP1/PP2PPBP/RNBQR1K1 b - -": (
            "E17",
            "Queen's Indian Defense: Fianchetto Variation, Kramnik Variation",
        ),
        "rn1qk2r/pbppbppp/1p2p3/8/2PPn3/2N2NP1/PP1BPPBP/R2QK2R b KQkq -": (
            "E17",
            "Queen's Indian Defense: Opocensky Variation",
        ),
        "rn1qk2r/pbppbppp/1p2pn2/8/2PP4/5NP1/PP2PPBP/RNBQK2R w KQkq -": (
            "E17",
            "Queen's Indian Defense: Traditional Variation",
        ),
        "r2q1rk1/pbppbppp/np2pn2/8/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E18",
            "Queen's Indian Defense: Classical Variation, Tiviakov Defense",
        ),
        "rn1q1rk1/pbp1bppp/1p2pn2/3p4/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E18",
            "Queen's Indian Defense: Classical Variation, Traditional Variation, Nimzowitsch Line",
        ),
        "rn1q1rk1/pbppbppp/1p2pn2/8/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 b - -": (
            "E18",
            "Queen's Indian Defense: Classical Variation, Traditional Variation",
        ),
        "rn1q1rk1/pbppbppp/1p2p3/8/2PP4/2Q2NP1/PP2PPBP/R1B2RK1 b - -": (
            "E19",
            "Queen's Indian Defense: Classical Variation, Traditional Variation, Main Line",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N2P2/PP2P1PP/R1BQKBNR b KQkq -": (
            "E20",
            "Nimzowitsch-Indian Defense: Kmoch Variation",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2NQ4/PP2PPPP/R1B1KBNR b KQkq -": (
            "E20",
            "Nimzowitsch-Indian Defense: Mikėnas Attack",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PP2PPPP/R1BQKBNR w KQkq -": (
            "E20",
            "Nimzowitsch-Indian Defense",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N3P1/PP2PP1P/R1BQKBNR b KQkq -": (
            "E20",
            "Nimzowitsch-Indian Defense: Romanishin Variation",
        ),
        "rnbq1rk1/pp3ppp/4p3/3n4/1b1N4/2N3P1/PP2PPBP/R1BQK2R w KQ -": (
            "E21",
            "Nimzowitsch-Indian Defense: Romanishin Variation, English Hybrid Variation",
        ),
        "rnbq1rk1/pp1p1ppp/4pn2/2p5/1bPP4/2N2NP1/PP2PPBP/R1BQK2R b KQ -": (
            "E21",
            "Nimzowitsch-Indian Defense: Romanishin Variation",
        ),
        "rnbqk2r/pp1p1ppp/4p3/2pP4/1bP1n3/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "E21",
            "Nimzowitsch-Indian Defense: Three Knights Variation, Euwe Variation",
        ),
        "rnbqk2r/pp1p1ppp/4pn2/2pP4/1bP5/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "E21",
            "Nimzowitsch-Indian Defense: Three Knights Variation, Korchnoi Variation",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq -": (
            "E21",
            "Nimzowitsch-Indian Defense: Three Knights Variation",
        ),
        "rnbqk2r/p2p1ppp/4pn2/1ppP4/1bP5/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "E21",
            "Nimzowitsch-Indian Defense: Three Knights Variation, Shocron Gambit",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/1QN5/PP2PPPP/R1B1KBNR b KQkq -": (
            "E22",
            "Nimzowitsch-Indian Defense: Spielmann Variation",
        ),
        "r1bqk2r/pp1p2pp/2n1p3/2n2p2/1bP5/2N2NP1/PPQBPP1P/R3KB1R b KQkq -": (
            "E23",
            "Nimzowitsch-Indian Defense: Spielmann Variation, Stahlberg Variation",
        ),
        "r1bqk2r/pp1p1ppp/2n1p3/2P5/1bP5/1QN2N2/PP1nPPPP/R3KB1R w KQkq -": (
            "E23",
            "Nimzowitsch-Indian Defense: Spielmann Variation, Karlsbad Variation",
        ),
        "r1bqk2r/pp1p1ppp/2n1pn2/2P5/1bP5/1QN5/PP2PPPP/R1B1KBNR w KQkq -": (
            "E23",
            "Nimzowitsch-Indian Defense: Spielmann Variation, Romanovsky Gambit",
        ),
        "r1bqk2r/pp1p1ppp/2n1p3/2n5/1bP5/1QN2N2/PP1BPPPP/R3KB1R w KQkq -": (
            "E23",
            "Nimzowitsch-Indian Defense: Spielmann Variation, Stahlberg Variation",
        ),
        "rnbq1rk1/pp3ppp/4p3/2pn4/3P4/P1P1PP2/6PP/R1BQKBNR w KQ -": (
            "E24",
            "Nimzowitsch-Indian Defense: Sämisch Variation, Botvinnik Variation",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/2PP4/P1P5/4PPPP/R1BQKBNR b KQkq -": (
            "E24",
            "Nimzowitsch-Indian Defense: Sämisch Variation, Accelerated",
        ),
        "rnbqk2r/pp4pp/4p3/2Pn1p2/8/P1P2P2/4P1PP/R1BQKBNR w KQkq -": (
            "E25",
            "Nimzowitsch-Indian Defense: Sämisch Variation, Romanovsky Variation",
        ),
        "rnbqk2r/pp3ppp/4p3/2Pn4/8/P1P2P2/4P1PP/R1BQKBNR b KQkq -": (
            "E25",
            "Nimzowitsch-Indian Defense: Sämisch Variation, Keres Variation",
        ),
        "rnbqk2r/pp3ppp/4pn2/2pP4/3P4/P1P2P2/4P1PP/R1BQKBNR b KQkq -": (
            "E25",
            "Nimzowitsch-Indian Defense: Sämisch Variation",
        ),
        "rnbqk2r/p2p1ppp/1p2pn2/2p5/2PP4/P1P1P3/5PPP/R1BQKBNR w KQkq -": (
            "E26",
            "Nimzowitsch-Indian Defense: Sämisch Variation, O'Kelly Variation",
        ),
        "rnbqk2r/pp1p1ppp/4pn2/2p5/2PP4/P1P1P3/5PPP/R1BQKBNR b KQkq -": (
            "E26",
            "Nimzowitsch-Indian Defense: Sämisch Variation",
        ),
        "rnbq1rk1/pppp1ppp/4pn2/8/2PP4/P1P5/4PPPP/R1BQKBNR w KQ -": (
            "E27",
            "Nimzowitsch-Indian Defense: Sämisch Variation",
        ),
        "rnbq1rk1/pppp1ppp/4pn2/8/2PP4/P1P1P3/5PPP/R1BQKBNR b KQ -": (
            "E28",
            "Nimzowitsch-Indian Defense: Sämisch Variation",
        ),
        "r1bqnrk1/p2p1ppp/1pn1p3/2p5/2PPP3/P1PB4/4NPPP/R1BQK2R w KQ -": (
            "E29",
            "Nimzowitsch-Indian Defense: Sämisch Variation, Capablanca Variation",
        ),
        "r1bq1rk1/pp1p1ppp/2n1pn2/2p5/2PP4/P1PBP3/5PPP/R1BQK1NR w KQ -": (
            "E29",
            "Nimzowitsch-Indian Defense: Sämisch Variation",
        ),
        "rnbqk2r/p2p1pp1/4pn1p/1ppP4/1bP4B/2N5/PP2PPPP/R2QKBNR w KQkq -": (
            "E30",
            "Nimzowitsch-Indian Defense: Leningrad Variation, Averbakh Gambit",
        ),
        "rnbqk2r/pppp1ppp/4pn2/6B1/1bPP4/2N5/PP2PPPP/R2QKBNR b KQkq -": (
            "E30",
            "Nimzowitsch-Indian Defense: Leningrad Variation",
        ),
        "rnbqk2r/pp3pp1/3ppn1p/2pP4/1bP4B/2N5/PP2PPPP/R2QKBNR w KQkq -": (
            "E31",
            "Nimzowitsch-Indian Defense: Leningrad Variation, Benoni Defense",
        ),
        "rnbq1rk1/p1pp1ppp/1p2pn2/8/2PP4/P1Q5/1P2PPPP/R1B1KBNR w KQ -": (
            "E32",
            "Nimzowitsch-Indian Defense: Classical Variation, Keres Defense",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR b KQkq -": (
            "E32",
            "Nimzowitsch-Indian Defense: Classical Variation",
        ),
        "rnbq1rk1/p1pp1ppp/4pn2/1p6/2PP4/P1Q5/1P2PPPP/R1B1KBNR w KQ -": (
            "E32",
            "Nimzowitsch-Indian Defense: Classical Variation, Vitolins-Adorjan Gambit",
        ),
        "r1bqk2r/ppp2ppp/2nppn2/8/1bPP4/2N2N2/PPQ1PPPP/R1B1KB1R w KQkq -": (
            "E33",
            "Nimzowitsch-Indian Defense: Classical Variation, Milner-Barry Variation",
        ),
        "r1bqk2r/pppp1ppp/2n1pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR w KQkq -": (
            "E33",
            "Nimzowitsch-Indian Defense: Classical Variation, Zurich Variation",
        ),
        "rnb1k2r/ppp2ppp/5n2/4pq2/1b1P4/2N2N2/PP2PPPP/R1BQKB1R w KQkq -": (
            "E34",
            "Nimzowitsch-Indian Defense: Classical Variation, Belyavsky Gambit",
        ),
        "rnbqk2r/ppp2ppp/4pn2/3p4/1bPP4/2N5/PPQ1PPPP/R1B1KBNR w KQkq -": (
            "E34",
            "Nimzowitsch-Indian Defense: Classical Variation, Noa Variation",
        ),
        "rnbqk2r/ppp2ppp/5n2/3p4/1b1P4/2N5/PPQ1PPPP/R1B1KBNR w KQkq -": (
            "E35",
            "Nimzowitsch-Indian Defense: Classical Variation, Noa Variation",
        ),
        "rnbqk2r/ppp2ppp/4p3/3p4/2PPn3/P1Q5/1P2PPPP/R1B1KBNR w KQkq -": (
            "E36",
            "Nimzowitsch-Indian Defense: Classical Variation, Noa Variation, Main Line",
        ),
        "r1bqk2r/ppp2ppp/2n1pn2/3p4/2PP4/P1Q5/1P2PPPP/R1B1KBNR w KQkq -": (
            "E36",
            "Nimzowitsch-Indian Defense: Classical Variation, Noa Variation, Botvinnik Variation",
        ),
        "rnbqk2r/ppp2ppp/4pn2/3p4/1bPP4/P1N5/1PQ1PPPP/R1B1KBNR b KQkq -": (
            "E36",
            "Nimzowitsch-Indian Defense: Classical Variation, Noa Variation",
        ),
        "rnbqk2r/ppp2ppp/4p3/3p4/2PPn3/P7/1PQ1PPPP/R1B1KBNR b KQkq -": (
            "E37",
            "Nimzowitsch-Indian Defense: Classical Variation, Noa Variation",
        ),
        "r1bqk2r/ppp2ppp/2n5/3pp3/2PPn3/P3P3/1PQ2PPP/R1B1KBNR w KQkq -": (
            "E37",
            "Nimzowitsch-Indian Defense: Classical Variation, Noa Variation, San Remo Variation",
        ),
        "rnbqk2r/pp1p1ppp/4pn2/2p5/1bPP4/2N5/PPQ1PPPP/R1B1KBNR w KQkq -": (
            "E38",
            "Nimzowitsch-Indian Defense: Classical Variation, Berlin Variation",
        ),
        "rnbqk2r/pp1p1ppp/4pn2/2P5/2P5/2b5/PPQ1PPPP/R1B1KBNR w KQkq -": (
            "E38",
            "Nimzowitsch-Indian Defense: Classical Variation, Berlin Variation, Steiner Variation",
        ),
        "rnbq1rk1/p2p1ppp/1p2pn2/2b5/2P2B2/P1N2N2/1PQ1PPPP/R3KB1R b KQ -": (
            "E39",
            "Nimzowitsch-Indian Defense: Classical Variation, Berlin Variation, Macieja System",
        ),
        "rnbq1rk1/pp1p1ppp/4pn2/2P5/1bP5/2N5/PPQ1PPPP/R1B1KBNR w KQ -": (
            "E39",
            "Nimzowitsch-Indian Defense: Classical Variation, Berlin Variation, Pirc Variation",
        ),
        "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N1P3/PP3PPP/R1BQKBNR b KQkq -": (
            "E40",
            "Nimzowitsch-Indian Defense: Normal Line",
        ),
        "r1bqk2r/pppp1ppp/2n1pn2/8/1bPP4/2N1P3/PP3PPP/R1BQKBNR w KQkq -": (
            "E40",
            "Nimzowitsch-Indian Defense: Normal Variation, Taimanov Variation",
        ),
        "r1bqk2r/pp3ppp/2nppn2/2p5/2PP4/2PBPN2/P4PPP/R1BQK2R w KQkq -": (
            "E41",
            "Nimzowitsch-Indian Defense: Hübner Variation, Main Line",
        ),
        "rnbqk2r/pp1p1ppp/4pn2/2p5/1bPP4/2N1P3/PP3PPP/R1BQKBNR w KQkq -": (
            "E41",
            "Nimzowitsch-Indian Defense: Hübner Variation",
        ),
        "rnbq1rk1/pp1p1ppp/4pn2/2p5/1bPP4/2N1PN2/PP3PPP/R1BQKB1R w KQ -": (
            "E41",
            "Nimzowitsch-Indian Defense: Normal Variation, Deferred Hübner Variation",
        ),
        "rnbq1rk1/pp1p1ppp/4pn2/8/1bPP4/P1N5/1P2NPPP/R1BQKB1R b KQ -": (
            "E42",
            "Nimzowitsch-Indian Defense: Hübner Variation, Rubinstein Variation, Main Line",
        ),
        "rnbqk2r/pp1p1ppp/4pn2/2p5/1bPP4/2N1P3/PP2NPPP/R1BQKB1R b KQkq -": (
            "E42",
            "Nimzowitsch-Indian Defense: Hübner Variation, Rubinstein Variation",
        ),
        "rnbq1rk1/pp1p1ppp/4pn2/2P5/1b1P4/2N5/PP2NPPP/R1BQKB1R b KQ -": (
            "E42",
            "Nimzowitsch-Indian Defense: Hübner Variation, Rubinstein Variation, Sherbakov Attack",
        ),
        "rnbqk2r/p1pp1ppp/1p2pn2/8/1bPP4/2N1P3/PP3PPP/R1BQKBNR w KQkq -": (
            "E43",
            "Nimzowitsch-Indian Defense: St. Petersburg Variation",
        ),
        "rnbqk2r/p1pp1ppp/1p2pn2/8/1bPP4/2N1P3/PP2NPPP/R1BQKB1R b KQkq -": (
            "E44",
            "Nimzowitsch-Indian Defense: Fischer Variation",
        ),
        "rn1qk2r/p1pp1ppp/bp2pn2/8/1bPP4/2N1P3/PP2NPPP/R1BQKB1R w KQkq -": (
            "E45",
            "Nimzowitsch-Indian Defense: Normal Variation, Bronstein (Byrne) Variation",
        ),
        "rnbq1rk1/pppp1ppp/4pn2/8/1bPP4/2N1P3/PP3PPP/R1BQKBNR w KQ -": (
            "E46",
            "Nimzowitsch-Indian Defense: Normal Variation",
        ),
        "rnbq1rk1/pppp1ppp/4pn2/8/1bPP4/2N1P3/PP2NPPP/R1BQKB1R b KQ -": (
            "E46",
            "Nimzowitsch-Indian Defense: Reshevsky Variation",
        ),
        "rnbq1rk1/ppp2ppp/3bpn2/3p4/2PP4/P1N1P3/1P2NPPP/R1BQKB1R w KQ -": (
            "E46",
            "Nimzowitsch-Indian Defense: Simagin Variation",
        ),
        "rnbq1rk1/pppp1ppp/4pn2/8/1bPP4/2NBP3/PP3PPP/R1BQK1NR b KQ -": (
            "E47",
            "Nimzowitsch-Indian Defense: Normal Variation, Bishop's Attack",
        ),
        "rnbq1rk1/ppp2ppp/4pn2/3p4/1bPP4/2NBP3/PP3PPP/R1BQK1NR w KQ -": (
            "E48",
            "Nimzowitsch-Indian Defense: Normal Variation, Bishop's Attack, Classical Defense",
        ),
        "r1bq1rk1/ppp2ppp/2n1pn2/3p4/1bPP4/2NBPN2/PP3PPP/R1BQ1RK1 b - -": (
            "E48",
            "Nimzowitsch-Indian Defense: Ragozin Defense",
        ),
        "rnbq1rk1/ppp2ppp/4pn2/3p4/2PP4/P1PBP3/5PPP/R1BQK1NR b KQ -": (
            "E49",
            "Nimzowitsch-Indian Defense: Normal Variation, Botvinnik System",
        ),
        "rnbq1rk1/pppp1ppp/4pn2/8/1bPP4/2N1PN2/PP3PPP/R1BQKB1R b KQ -": (
            "E50",
            "Nimzowitsch-Indian Defense",
        ),
        "rnbq1rk1/ppp2ppp/4pn2/3p4/1bPP4/2N1PN2/PP3PPP/R1BQKB1R w KQ -": (
            "E51",
            "Nimzowitsch-Indian Defense: Normal Variation, Ragozin Variation",
        ),
        "rnbq1rk1/ppp2ppp/4pn2/3p4/1bPP4/P1N1PN2/1P3PPP/R1BQKB1R b KQ -": (
            "E51",
            "Nimzowitsch-Indian Defense: Normal Variation, Deferred Sämisch Variation",
        ),
        "r1bq1rk1/ppp2ppp/2n1pn2/8/1bpP4/2NBPN2/PP3PPP/R1BQ1RK1 w - -": (
            "E51",
            "Nimzowitsch-Indian Defense, Ragozin Variation",
        ),
        "rnbq1rk1/p1p2ppp/1p2pn2/3p4/1bPP4/2NBPN2/PP3PPP/R1BQK2R w KQ -": (
            "E52",
            "Nimzowitsch-Indian Defense: Normal Variation, Schlechter Defense",
        ),
        "rnbq1rk1/p4ppp/1p2pn2/2pp4/1bPP4/2NBPN2/PP3PPP/R1BQ1RK1 w - -": (
            "E53",
            "Nimzowitsch-Indian Defense: Normal Variation, Gligorić System, Keres Variation",
        ),
        "r1bq1rk1/pp1n1ppp/4pn2/2pp4/1bPP4/2NBPN2/PP3PPP/R1BQ1RK1 w - -": (
            "E53",
            "Nimzowitsch-Indian Defense: Normal Variation, Gligorić System",
        ),
        "rnbq1rk1/pp3ppp/4pn2/2pp4/1bPP4/2NBPN2/PP3PPP/R1BQK2R w KQ -": (
            "E53",
            "Nimzowitsch-Indian Defense: Normal Variation, Gligorić System",
        ),
        "rnbq1rk1/pp3ppp/4pn2/2p5/1bBP4/2N1PN2/PP3PPP/R1BQ1RK1 b - -": (
            "E54",
            "Nimzowitsch-Indian Defense: Normal Variation, Gligorić System, Exchange at c4",
        ),
        "rnb2rk1/pp2qppp/4pn2/2p5/1bBP4/2N1PN2/PP3PPP/R1BQ1RK1 w - -": (
            "E54",
            "Nimzowitsch-Indian Defense: Normal Variation, Gligorić System, Smyslov Variation",
        ),
        "r1bq1rk1/pp1n1ppp/4pn2/2p5/1bBP4/2N1PN2/PP3PPP/R1BQ1RK1 w - -": (
            "E55",
            "Nimzowitsch-Indian Defense: Normal Variation, Gligorić System, Bronstein Variation",
        ),
        "r1bq1rk1/pp3ppp/2n1pn2/2pp4/1bPP4/2NBPN2/PP3PPP/R1BQ1RK1 w - -": (
            "E56",
            "Nimzowitsch-Indian Defense: Normal Variation, Gligorić System, Bernstein Defense",
        ),
        "r1bq1rk1/pp3ppp/2n1pn2/2pp4/2PP4/P1PBPN2/5PPP/R1BQ1RK1 b - -": (
            "E58",
            "Nimzowitsch-Indian Defense: Normal Variation, Bernstein Defense, Exchange Line",
        ),
        "r1bq1rk1/pp3ppp/2n1pn2/2p5/2BP4/P1P1PN2/5PPP/R1BQ1RK1 b - -": (
            "E59",
            "Nimzowitsch-Indian Defense: Normal Variation, Bernstein Defense",
        ),
        "rnbqk2r/ppp1ppbp/5np1/3p4/2PP4/6P1/PP2PPBP/RNBQK1NR w KQkq -": (
            "E60",
            "Grünfeld Defense: Counterthrust Variation",
        ),
        "rnbqkb1r/p1pppp1p/5np1/1p1P4/2P5/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "E60",
            "Indian Game: Anti-Grünfeld, Adorjan Gambit",
        ),
        "rnbqkb1r/pppppp1p/5np1/3P4/2P5/8/PP2PPPP/RNBQKBNR b KQkq -": (
            "E60",
            "Indian Game: Anti-Grünfeld, Advance Variation",
        ),
        "rnbqkb1r/pppp1p1p/5np1/4p3/2PP4/5P2/PP2P1PP/RNBQKBNR w KQkq -": (
            "E60",
            "Indian Game: Anti-Grünfeld, Alekhine Variation, Leko Gambit",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/2PP4/5P2/PP2P1PP/RNBQKBNR b KQkq -": (
            "E60",
            "Indian Game: Anti-Grünfeld, Alekhine Variation",
        ),
        "rnbqk2r/ppppppbp/5np1/8/2PP4/6P1/PP2PPBP/RNBQK1NR b KQkq -": (
            "E60",
            "Indian Game: King's Indian Variation, Fianchetto Variation",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq -": (
            "E60",
            "Indian Game: West Indian Defense",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/2PP4/6P1/PP2PP1P/RNBQKBNR b KQkq -": (
            "E60",
            "King's Indian Defense: Fianchetto Variation, Immediate Fianchetto",
        ),
        "rnb1k2r/pp1pppbp/5np1/q1p5/2PP4/5NP1/PP2PPBP/RNBQK2R w KQkq -": (
            "E60",
            "King's Indian Defense: Fianchetto Variation, Pterodactyl Variation",
        ),
        "rnbq1rk1/pp2ppbp/3p1np1/2p5/2PP4/5NP1/PP2PPBP/RNBQ1RK1 w - -": (
            "E60",
            "King's Indian Defense: Fianchetto Variation, Yugoslav System",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/2PP4/5N2/PP2PPPP/RNBQKB1R b KQkq -": (
            "E60",
            "King's Indian Defense: Normal Variation, King's Knight Variation",
        ),
        "rnbqk2r/ppppppbp/5np1/8/1PPP4/5N2/P3PPPP/RNBQKB1R b KQkq -": (
            "E60",
            "King's Indian Defense: Santasiere Variation",
        ),
        "rnbq1rk1/pp2ppbp/2pp1np1/8/2PP4/2N1PN2/PP2BPPP/R1BQK2R w KQ -": (
            "E60",
            "King's Indian Defense: Semi-Classical Variation, Benoni Variation",
        ),
        "r1bq1rk1/ppp1ppbp/2np1np1/8/2PP4/2N1PN2/PP2BPPP/R1BQK2R w KQ -": (
            "E60",
            "King's Indian Defense: Semi-Classical Variation, Hollywood Variation",
        ),
        "rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq -": (
            "E60",
            "Neo-Grünfeld Defense: Non- or Delayed Fianchetto",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/2PP4/8/PPQ1PPPP/RNB1KBNR b KQkq -": (
            "E60",
            "Queen's Pawn Opening, Mengarini Attack",
        ),
        "rnbqkb1r/pppppp1p/5np1/8/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq -": (
            "E61",
            "King's Indian Defense",
        ),
        "r1bq1rk1/pppn1pbp/3p1np1/4p3/1PPP4/2N1PN2/P3BPPP/R1BQ1RK1 b - -": (
            "E61",
            "King's Indian Defense: Semi-Classical Variation, Queenside Storm Line",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/2PP4/2N1PN2/PP2BPPP/R1BQK2R b KQ -": (
            "E61",
            "King's Indian Defense: Semi-Classical Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/6B1/2PP4/2N2N2/PP2PPPP/R2QKB1R b KQkq -": (
            "E61",
            "King's Indian Defense: Smyslov Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2PP4/2N2NP1/PP2PP1P/R1BQKB1R b KQkq -": (
            "E62",
            "King's Indian Defense: Fianchetto Variation, Delayed Fianchetto Variation",
        ),
        "r1bq1rk1/ppp1ppbp/2np1np1/8/2PP4/2N2NP1/PP2PPBP/R1BQK2R w KQ -": (
            "E62",
            "King's Indian Defense: Fianchetto Variation, Karlsbad Variation",
        ),
        "rnb2rk1/pp2ppbp/2pp1np1/q7/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E62",
            "King's Indian Defense: Fianchetto Variation, Kavalek Defense",
        ),
        "rn1q1rk1/pp2ppbp/2pp1np1/5b2/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E62",
            "King's Indian Defense: Fianchetto Variation, Larsen Defense",
        ),
        "r2q1rk1/ppp1ppbp/2np1np1/5b2/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E62",
            "King's Indian Defense: Fianchetto Variation, Lesser Simagin (Spassky) Variation",
        ),
        "r2q1rk1/ppp1ppbp/2np1np1/8/2PP2b1/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E62",
            "King's Indian Defense: Fianchetto Variation, Simagin Variation",
        ),
        "r1bq1rk1/ppp2pbp/2np1np1/4p3/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E62",
            "King's Indian Defense: Fianchetto Variation, Uhlmann-Szabo System",
        ),
        "r1bq1rk1/1p3pbp/p2p1np1/n1pPp3/2P5/2N3P1/PPQNPPBP/R1B2RK1 w - e6": (
            "E63",
            "King's Indian Defense: Fianchetto Variation, Panno Variation, Blockade Line",
        ),
        "1rbq1rk1/4pp1p/p2p1npb/n1pP4/2P5/2N3P1/PBQNPPBP/R4RK1 w - -": (
            "E63",
            "King's Indian Defense: Fianchetto Variation, Panno Variation, Donner Line",
        ),
        "1rbq1rk1/2p1ppbp/p1np1np1/1p6/2PP4/2N1B1PP/PP1NPPB1/R2Q1RK1 b - -": (
            "E63",
            "King's Indian Defense: Fianchetto Variation, Panno Variation, Korchnoi Line",
        ),
        "r1bq1rk1/1pp1ppbp/p1np1np1/8/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E63",
            "King's Indian Defense: Fianchetto Variation, Panno Variation",
        ),
        "rnbq1rk1/pp2ppbp/3p1np1/2p5/2PP4/2N2NP1/PP2PPBP/R1BQK2R w KQ -": (
            "E64",
            "King's Indian Defense: Fianchetto Variation, Yugoslav Variation, Rare Line",
        ),
        "r1bq1rk1/pp2ppbp/2n2np1/2p5/2P5/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E65",
            "King's Indian Defense: Fianchetto Variation, Yugoslav Variation, Exchange Line",
        ),
        "rnbq1rk1/pp2ppbp/3p1np1/2p5/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 b - -": (
            "E65",
            "King's Indian Defense: Fianchetto Variation, Yugoslav Variation",
        ),
        "r1bq1rk1/pp2ppbp/2np1np1/2pP4/2P5/2N2NP1/PP2PPBP/R1BQ1RK1 b - -": (
            "E66",
            "King's Indian Defense: Fianchetto Variation, Yugoslav Variation, Advance Line",
        ),
        "r1bq1rk1/pppn1pbp/3p1np1/4p3/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E67",
            "King's Indian Defense: Fianchetto Variation, Classical Fianchetto",
        ),
        "r1bq1rk1/pppnppbp/3p1np1/8/2PP4/2N2NP1/PP2PPBP/R1BQK2R w KQ -": (
            "E67",
            "King's Indian Defense: Fianchetto Variation, Debrecen Defense",
        ),
        "r1bq1rk1/pppn1pbp/3p1np1/4p3/2PP4/1PN2NP1/P3PPBP/R1BQ1RK1 b - -": (
            "E67",
            "King's Indian Defense: Fianchetto Variation, Double Fianchetto Attack",
        ),
        "r1bq1rk1/1ppnppbp/p2p1np1/8/2PP4/2N2NP1/PP2PPBP/R1BQ1RK1 w - -": (
            "E67",
            "King's Indian Defense: Fianchetto Variation, Hungarian Variation",
        ),
        "r1bqr1k1/1pp2pbp/3p1np1/p1n5/2PNP3/2N3PP/PP3PB1/R1BQR1K1 w - -": (
            "E68",
            "King's Indian Defense: Fianchetto Variation, Long Variation",
        ),
        "r1bq1rk1/pppn1pbp/3p1np1/4p3/2PPP3/2N2NP1/PP3PBP/R1BQ1RK1 b - -": (
            "E68",
            "King's Indian Defense, Fianchetto Variation, Classical Variation",
        ),
        "r1bq1rk1/pp1n1pbp/2pp1np1/4p3/2PPP3/2N2NPP/PP3PB1/R1BQ1RK1 b - -": (
            "E69",
            "King's Indian Defense: Fianchetto Variation, Classical Main Line",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/6B1/2PPP3/2N5/PP3PPP/R2QKBNR b KQkq -": (
            "E70",
            "King's Indian Defense: Accelerated Averbakh Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2PPP3/2N5/PP2NPPP/R1BQKB1R b KQkq -": (
            "E70",
            "King's Indian Defense: Kramer Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2PPP3/2N5/PP3PPP/R1BQKBNR w KQkq -": (
            "E70",
            "King's Indian Defense: Normal Variation",
        ),
        "rnbqk2r/ppppppbp/5np1/8/2PPP3/2N5/PP3PPP/R1BQKBNR b KQkq -": (
            "E70",
            "King's Indian Defense: Normal Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2PPP3/2N4P/PP3PP1/R1BQKBNR b KQkq -": (
            "E71",
            "King's Indian Defense: Makogonov Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2PPP3/2N3P1/PP3P1P/R1BQKBNR b KQkq -": (
            "E72",
            "King's Indian Defense: Normal Variation, Deferred Fianchetto Variation",
        ),
        "rnbq1rk1/ppp2pbp/3p1np1/4p3/2PPP3/2N3P1/PP2NPBP/R1BQK2R b KQ -": (
            "E72",
            "King's Indian Defense: Pomar System",
        ),
        "rnbq1rk1/ppp1ppb1/3p1npp/6B1/2PPP3/2N5/PP2BPPP/R2QK1NR w KQ -": (
            "E73",
            "King's Indian Defense: Averbakh Variation, Flexible Defense",
        ),
        "r1bq1rk1/pppnppbp/3p1np1/6B1/2PPP3/2N5/PP2BPPP/R2QK1NR w KQ -": (
            "E73",
            "King's Indian Defense: Averbakh Variation, Geller Defense",
        ),
        "r1bq1rk1/pp2ppbp/n1pp1np1/6B1/2PPP3/2N5/PP1QBPPP/R3K1NR w KQ -": (
            "E73",
            "King's Indian Defense: Averbakh Variation, Modern Defense, Burgess Line",
        ),
        "r1bq1rk1/ppp1ppbp/n2p1np1/6B1/2PPP3/2N5/PP2BPPP/R2QK1NR w KQ -": (
            "E73",
            "King's Indian Defense: Averbakh Variation, Modern Defense",
        ),
        "r1bq1rk1/ppp1ppbp/2np1np1/6B1/2PPP3/2N5/PP2BPPP/R2QK1NR w KQ -": (
            "E73",
            "King's Indian Defense: Averbakh Variation, Nc6 Defense",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/6B1/2PPP3/2N5/PP2BPPP/R2QK1NR b KQ -": (
            "E73",
            "King's Indian Defense: Averbakh Variation",
        ),
        "rnbq1rk1/1pp1ppbp/p2p1np1/6B1/2PPP3/2N5/PP2BPPP/R2QK1NR w KQ -": (
            "E73",
            "King's Indian Defense: Averbakh Variation, Spanish Defense",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2PPP3/2N5/PP2BPPP/R1BQK1NR b KQkq -": (
            "E73",
            "King's Indian Defense: Normal Variation, Standard Development",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/2PPP3/2N1B3/PP2BPPP/R2QK1NR b KQ -": (
            "E73",
            "King's Indian Defense: Semi-Averbakh System",
        ),
        "rnbq1rk1/pp2ppbp/3p1np1/2pP2B1/2P1P3/2N5/PP2BPPP/R2QK1NR b KQ -": (
            "E74",
            "King's Indian Defense: Averbakh Variation, Benoni Defense, Advance Variation",
        ),
        "rnbq1rk1/pp2ppbp/3p1np1/2P3B1/2P1P3/2N5/PP2BPPP/R2QK1NR b KQ -": (
            "E74",
            "King's Indian Defense: Averbakh Variation, Benoni Defense, Exchange Variation",
        ),
        "rnbq1rk1/pp2ppbp/3p1np1/2p3B1/2PPP3/2N5/PP2BPPP/R2QK1NR w KQ -": (
            "E74",
            "King's Indian Defense: Averbakh Variation, Benoni Defense",
        ),
        "rnbq1rk1/pp3pbp/3ppnp1/2pP2B1/2P1P3/2N5/PP2BPPP/R2QK1NR w KQ -": (
            "E75",
            "King's Indian Defense: Averbakh Variation, Main Line",
        ),
        "rnbq1rk1/pp2ppbp/3p1np1/2pP4/2P1PP2/2N2N2/PP4PP/R1BQKB1R b KQ -": (
            "E76",
            "King's Indian Defense: Four Pawns Attack, Dynamic Attack",
        ),
        "r1bqk2r/ppp1ppbp/n2p1np1/8/2PPPP2/2N5/PP4PP/R1BQKBNR w KQkq -": (
            "E76",
            "King's Indian Defense: Four Pawns Attack, Modern Defense",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2PPPP2/2N5/PP4PP/R1BQKBNR b KQkq -": (
            "E76",
            "King's Indian Defense: Four Pawns Attack",
        ),
        "rnbq1rk1/pp3pbp/3p1np1/2ppP3/2P2P2/2N2N2/PP2B1PP/R1BQK2R b KQ -": (
            "E77",
            "King's Indian Defense: Four Pawns Attack, Florentine Gambit",
        ),
        "rnbq1rk1/pp3pbp/3ppnp1/2pP4/2P1PP2/2N2N2/PP2B1PP/R1BQK2R b KQ -": (
            "E77",
            "King's Indian Defense: Four Pawns Attack, Normal Attack",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/2PPPP2/2N5/PP2B1PP/R1BQK1NR b KQ -": (
            "E77",
            "King's Indian Defense: Four Pawns Attack",
        ),
        "r1bq1rk1/pp4bp/2nppnp1/2p5/2P1PPPP/2N5/PP2B3/R1BQK1NR b KQ -": (
            "E77",
            "King's Indian Defense: Six Pawns Attack",
        ),
        "rnbq1rk1/pp2ppbp/3p1np1/2p5/2PPPP2/2N2N2/PP2B1PP/R1BQK2R b KQ -": (
            "E78",
            "King's Indian Defense: Four Pawns Attack, Fluid Attack",
        ),
        "r1bq1rk1/pp2ppbp/2np1np1/8/2PNPP2/2N1B3/PP2B1PP/R2QK2R b KQ -": (
            "E79",
            "King's Indian Defense: Four Pawns Attack, Exchange Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2PPP3/2N2P2/PP4PP/R1BQKBNR b KQkq -": (
            "E80",
            "King's Indian Defense: Sämisch Variation",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/2PPP3/2N2P2/PP2N1PP/R1BQKB1R b KQ -": (
            "E81",
            "King's Indian Defense: Sämisch Variation, Bobotsov-Korchnoi-Petrosian Variation",
        ),
        "rnbq1rk1/1p2ppbp/p1pp1np1/8/2PPP3/2NBBP2/PP4PP/R2QK1NR w KQ -": (
            "E81",
            "King's Indian Defense: Sämisch Variation, Byrne Defense",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/2PPP3/2N2P2/PP4PP/R1BQKBNR w KQ -": (
            "E81",
            "King's Indian Defense: Sämisch Variation, Normal Defense",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/6B1/2PPP3/2N2P2/PP4PP/R2QKBNR b KQ -": (
            "E81",
            "King's Indian Defense: Steiner Attack",
        ),
        "rnbq1rk1/p1p1ppbp/1p1p1np1/8/2PPP3/2N1BP2/PP4PP/R2QKBNR w KQ -": (
            "E82",
            "King's Indian Defense: Sämisch Variation, Double Fianchetto",
        ),
        "r1bq1rk1/1pp1ppbp/p1np1np1/8/2PPP3/2N1BP2/PP2N1PP/R2QKB1R w KQ -": (
            "E83",
            "King's Indian Defense: Sämisch Variation, Panno Formation",
        ),
        "r1bq1rk1/ppp1ppbp/2np1np1/8/2PPP3/2N1BP2/PP4PP/R2QKBNR w KQ -": (
            "E83",
            "King's Indian Defense: Sämisch Variation, Yates Defense",
        ),
        "1rbq1rk1/ppp1ppbp/2np1np1/8/2PPP3/2N1BP2/PP2N1PP/R2QKB1R w KQ -": (
            "E83",
            "King's Indian, Sämisch, Ruban Variation",
        ),
        "1rbq1rk1/1pp1ppbp/p1np1np1/8/2PPP3/2N1BP2/PP1QN1PP/R3KB1R w KQ -": (
            "E84",
            "King's Indian, Sämisch, Panno Main Line",
        ),
        "rnbq1rk1/ppp2pbp/3p1np1/4p3/2PPP3/2N1BP2/PP4PP/R2QKBNR w KQ -": (
            "E85",
            "King's Indian Defense: Sämisch Variation, Orthodox Variation",
        ),
        "rnbq1rk1/pp3pbp/2pp1np1/4p3/2PPP3/2N1BP2/PP2N1PP/R2QKB1R w KQ -": (
            "E86",
            "King's Indian Defense: Sämisch Variation",
        ),
        "rnb2rk1/ppp2pbp/3p2p1/3Pp3/2P1P2Q/2N1nP2/PP2K2P/R5NR b - -": (
            "E87",
            "King's Indian Defense: Sämisch Variation, Bronstein Defense",
        ),
        "rnbq1rk1/ppp2pbp/3p1np1/3Pp3/2P1P3/2N1BP2/PP4PP/R2QKBNR b KQ -": (
            "E87",
            "King's Indian Defense: Sämisch Variation, Closed Variation",
        ),
        "rnb2rk1/ppp2pbp/3p2p1/3Pp3/2n1P2Q/2N2P2/PP2K2P/R5NR w - -": (
            "E87",
            "King's Indian Defense: Sämisch Variation, Orthodox Variation, Bronstein Variation",
        ),
        "rnbq1rk1/pp3pbp/3p1np1/3pp3/2P1P3/2N1BP2/PP2N1PP/R2QKB1R w KQ -": (
            "E89",
            "King's Indian Defense: Sämisch Variation, Closed Variation, Main Line",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/2PPP3/2N1BN2/PP3PPP/R2QKB1R b KQ -": (
            "E90",
            "King's Indian Defense: Larsen Variation",
        ),
        "rnbqk2r/ppp1ppbp/3p1np1/8/2PPP3/2N2N2/PP3PPP/R1BQKB1R b KQkq -": (
            "E90",
            "King's Indian Defense: Normal Variation, Rare Defense",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/6B1/2PPP3/2N2N2/PP3PPP/R2QKB1R b KQ -": (
            "E90",
            "King's Indian Defense: Zinnowitz Variation",
        ),
        "r1bq1rk1/ppp1ppbp/n2p1np1/8/2PPP3/2N2N2/PP2BPPP/R1BQK2R w KQ -": (
            "E91",
            "King's Indian Defense: Kazakh Variation",
        ),
        "rnbq1rk1/ppp1ppbp/3p1np1/8/2PPP3/2N2N2/PP2BPPP/R1BQK2R b KQ -": (
            "E91",
            "King's Indian Defense: Orthodox Variation",
        ),
        "rnbq1rk1/ppp2pbp/3p1np1/4P3/2P1P3/2N2N2/PP2BPPP/R1BQK2R b KQ -": (
            "E92",
            "King's Indian Defense: Exchange Variation",
        ),
        "rnbq1rk1/ppp2pbp/3p1np1/4p3/2PPP3/2N1BN2/PP2BPPP/R2QK2R b KQ -": (
            "E92",
            "King's Indian Defense: Orthodox Variation, Gligorić-Taimanov System",
        ),
        "rnbq1rk1/ppp2pbp/3p1np1/4p3/2PPP3/2N2N2/PP2BPPP/R1BQK2R w KQ -": (
            "E92",
            "King's Indian Defense: Orthodox Variation",
        ),
        "rnbq1rk1/ppp2pbp/3p1np1/3Pp3/2P1P3/2N2N2/PP2BPPP/R1BQK2R b KQ -": (
            "E92",
            "King's Indian Defense: Petrosian Variation",
        ),
        "rnbq1rk1/1pp2pbp/3p1np1/p2Pp3/2P1P3/2N2N2/PP2BPPP/R1BQK2R w KQ -": (
            "E92",
            "King's Indian Defense: Petrosian Variation, Stein Defense",
        ),
        "r1bq1rk1/pppn1pb1/3p3p/3Pp1pn/2P1P2P/2N2NB1/PP2BPP1/R2QK2R b KQ -": (
            "E93",
            "King's Indian Defense: Petrosian Variation, Keres Defense",
        ),
        "r1bq1rk1/pppn1pbp/3p1np1/3Pp3/2P1P3/2N2N2/PP2BPPP/R1BQK2R w KQ -": (
            "E93",
            "King's Indian Defense: Petrosian Variation, Normal Defense",
        ),
        "rnbq1rk1/pp3pbp/2pp1np1/4p3/2PPP3/2N2N2/PP2BPPP/R1BQ1RK1 w - -": (
            "E94",
            "King's Indian Defense: Orthodox Variation, Donner Defense",
        ),
        "r1bq1rk1/ppp2pbp/n2p1np1/4p3/2PPP3/2N2N2/PP2BPPP/R1BQ1RK1 w - -": (
            "E94",
            "King's Indian Defense: Orthodox Variation, Glek Defense",
        ),
        "r1bq1rk1/pppn1pbp/3p1np1/3Pp3/2P1P3/2N2N2/PP2BPPP/R1BQ1RK1 b - -": (
            "E94",
            "King's Indian Defense: Orthodox Variation, Positional Defense, Closed Line",
        ),
        "r1bq1rk1/pppn1pbp/3p1np1/4p3/2PPP3/2N2N2/PP2BPPP/R1BQ1RK1 w - -": (
            "E94",
            "King's Indian Defense: Orthodox Variation, Positional Defense",
        ),
        "rnbq1rk1/ppp2pbp/3p1np1/4p3/2PPP3/2N2N2/PP2BPPP/R1BQ1RK1 b - -": (
            "E94",
            "King's Indian Defense: Orthodox Variation",
        ),
        "rnbq1rk1/1pp2pbp/3p1np1/p3p3/2PPP3/2N2N2/PP2BPPP/R1BQ1RK1 w - -": (
            "E94",
            "King's Indian Defense: Orthodox Variation, Ukrainian Defense",
        ),
        "r1bq1rk1/pppn1pbp/3p1np1/4p3/2PPP3/2N2N2/PP2BPPP/R1BQR1K1 b - -": (
            "E95",
            "King's Indian Defense: Orthodox Variation",
        ),
        "r1bq1rk1/1p1n1pbp/2pp1np1/p3p3/2PPP3/2N2N2/PP3PPP/R1BQRBK1 w - -": (
            "E96",
            "King's Indian Defense: Orthodox Variation, Positional Defense, Main Line",
        ),
        "r1bq1rk1/ppp2pbp/2np1np1/4p3/2PPP3/2N2N2/PP2BPPP/R1BQ1RK1 w - -": (
            "E97",
            "King's Indian Defense: Orthodox Variation, Aronin-Taimanov Defense",
        ),
        "r1bq1rk1/ppp1npbp/3p1np1/3Pp3/1PP1P3/2N2N2/P3BPPP/R1BQ1RK1 b - -": (
            "E97",
            "King's Indian Defense: Orthodox Variation, Bayonet Attack",
        ),
        "r1bq1rk1/ppp1npbp/3p2p1/3Pp2n/1PP1P3/2N2N2/P3BPPP/R1BQR1K1 b - -": (
            "E97",
            "King's Indian Defense: Orthodox Variation, Bayonet Attack, Sokolov Line",
        ),
        "r1bq1rk1/ppp1npbp/3p2p1/3Pp2n/1PP1P3/2N2N2/P1Q1BPPP/R1B2RK1 b - -": (
            "E97",
            "King's Indian Defense: Orthodox Variation, Bayonet Attack, Yepishin Line",
        ),
        "r1bq1rk1/ppp1npbp/3p1np1/3Pp3/2P1P3/2N2N2/PP1BBPPP/R2Q1RK1 b - -": (
            "E97",
            "King's Indian Defense: Orthodox Variation, Korchnoi Attack",
        ),
        "r1bq1rk1/ppp1npbp/3p1np1/3Pp3/2P1P3/2N5/PP1NBPPP/R1BQ1RK1 b - -": (
            "E97",
            "King's Indian Defense: Orthodox Variation, Modern System",
        ),
        "r1bq1rk1/pppn2bp/3p2n1/2PPp1p1/4Pp2/2N2P2/PP2BBPP/2RQNRK1 b - -": (
            "E98",
            "King's Indian Defense: Orthodox Variation, Classical System, Kozul Gambit",
        ),
        "r1bq1rk1/pppnnpbp/3p2p1/3Pp3/2P1P3/2N1B3/PP2BPPP/R2QNRK1 b - -": (
            "E98",
            "King's Indian Defense: Orthodox Variation, Classical System, Neo-Classical Line",
        ),
        "r1bq1rk1/ppp1npbp/3p1np1/3Pp3/2P1P3/2N5/PP2BPPP/R1BQNRK1 b - -": (
            "E98",
            "King's Indian Defense: Orthodox Variation, Classical System",
        ),
        "r1bq1rk1/pppnn1bp/3p2p1/3Ppp2/2P1P1P1/2N2P2/PP2B2P/R1BQNRK1 b - -": (
            "E99",
            "King's Indian Defense: Orthodox Variation, Classical System, Benko Attack",
        ),
        "r1bq1rk1/pppnn1bp/3p2p1/3Ppp2/2P1P3/2N2P2/PP2B1PP/R1BQNRK1 w - -": (
            "E99",
            "King's Indian Defense: Orthodox Variation, Classical System, Traditional Line",
        ),
    }
