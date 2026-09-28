from sudokus.lib import A, B, equal_sum_cages

GIVENS = {
    (A, 1): 5,
    (A, 2): 3,
    (B, 1): 6,
}

CAGES = [
    [(A, 3), (A, 4), (A, 5)],
    [(B, 3), (B, 4), (B, 5)],
]


def setup(s, x):
    equal_sum_cages(s, x, CAGES)
