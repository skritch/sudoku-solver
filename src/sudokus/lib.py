from ortools.sat.python import cp_model

A, B, C, D, E, F, G, H, I = 1, 2, 3, 4, 5, 6, 7, 8, 9


def add_standard_rules(m, x):
    for r in range(9):
        m.add_all_different(x[r])
    for c in range(9):
        m.add_all_different([x[r][c] for r in range(9)])
    for br in range(3):
        for bc in range(3):
            cells = [x[br * 3 + r][bc * 3 + c] for r in range(3) for c in range(3)]
            m.add_all_different(cells)


def equal_sum_cages(m, x, cages):
    """All cages sum to the same unknown value."""
    min_sum = max(sum(range(1, len(cage) + 1)) for cage in cages)
    max_sum = min(sum(range(10 - len(cage), 10)) for cage in cages)
    cage_sum = m.new_int_var(min_sum, max_sum, f"cage_sum_{hash(tuple(tuple(c) for c in cages))}")
    for cage in cages:
        m.add(sum(x[r - 1][c - 1] for r, c in cage) == cage_sum)
