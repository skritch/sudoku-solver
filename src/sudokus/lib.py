from z3 import And, Distinct, Int, Sum

A, B, C, D, E, F, G, H, I = 1, 2, 3, 4, 5, 6, 7, 8, 9


def add_standard_rules(s, x):
    for r in range(1, 10):
        for c in range(1, 10):
            s.add(And(x[r - 1][c - 1] >= 1, x[r - 1][c - 1] <= 9))
    for r in range(1, 10):
        s.add(Distinct([x[r - 1][c - 1] for c in range(1, 10)]))
    for c in range(1, 10):
        s.add(Distinct([x[r - 1][c - 1] for r in range(1, 10)]))
    for br in range(3):
        for bc in range(3):
            cells = [
                x[r - 1][c - 1]
                for r in range(br * 3 + 1, br * 3 + 4)
                for c in range(bc * 3 + 1, bc * 3 + 4)
            ]
            s.add(Distinct(cells))


def equal_sum_cages(s, x, cages):
    """All cages sum to the same unknown value."""
    cage_sum = Int(f"cage_sum_{hash(tuple(tuple(c) for c in cages))}")
    min_sum = max(sum(range(1, len(cage) + 1)) for cage in cages)
    max_sum = min(sum(range(10 - len(cage), 10)) for cage in cages)
    s.add(And(cage_sum >= min_sum, cage_sum <= max_sum))
    for cage in cages:
        s.add(Sum([x[r - 1][c - 1] for r, c in cage]) == cage_sum)
