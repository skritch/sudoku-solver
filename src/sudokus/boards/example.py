from sudokus.lib import A, B, C, D, E, F, G, H, I

# A classic easy puzzle (often cited as a beginner example)
# Solution: https://en.wikipedia.org/wiki/Sudoku#/media/File:Sudoku_by_L2G-20050714.svg
GIVENS = {
    (A, 1): 5, (A, 2): 3,               (A, 5): 7,
    (B, 1): 6,               (B, 4): 1, (B, 5): 9, (B, 6): 5,
    (C, 2): 9, (C, 3): 8,               (C, 8): 6,
    (D, 1): 8,               (D, 5): 6,             (D, 9): 3,
    (E, 1): 4, (E, 4): 8,               (E, 6): 3, (E, 9): 1,
    (F, 1): 7,               (F, 5): 2,             (F, 9): 6,
    (G, 2): 6,               (G, 8): 2, (G, 9): 8,
    (H, 4): 4, (H, 5): 1, (H, 6): 9,               (H, 9): 5,
    (I, 5): 8,               (I, 8): 7, (I, 9): 9,
}


def setup(s, x):
    pass
