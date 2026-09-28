import argparse
import importlib
import sys
from pathlib import Path

from ortools.sat.python import cp_model

from sudokus.lib import add_standard_rules


def _make_grid(m):
    return [[m.new_int_var(1, 9, f"x_{r}_{c}") for c in range(9)] for r in range(9)]


def _load_board(name):
    src_dir = Path(__file__).parent
    if not (src_dir / "boards" / f"{name}.py").exists():
        print(f"error: board '{name}' not found", file=sys.stderr)
        sys.exit(1)
    sys.path.insert(0, str(src_dir))
    return importlib.import_module(f"boards.{name}")


def main():
    parser = argparse.ArgumentParser(description="Solve a sudoku board.")
    parser.add_argument("board", help="Board name (file in src/boards/)")
    args = parser.parse_args()

    board = _load_board(args.board)

    m = cp_model.CpModel()
    x = _make_grid(m)
    add_standard_rules(m, x)

    for (r, c), value in getattr(board, "GIVENS", {}).items():
        m.add(x[r - 1][c - 1] == value)

    setup = getattr(board, "setup", None)
    if setup:
        setup(m, x)

    solver = cp_model.CpSolver()
    status = solver.solve(m)

    if status == cp_model.INFEASIBLE:
        print("No solution.", file=sys.stderr)
        sys.exit(1)
    elif status == cp_model.UNKNOWN:
        print("Solver gave up.", file=sys.stderr)
        sys.exit(2)
    elif status not in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        sys.exit(1)

    sep = "------+-------+------"
    for r in range(1, 10):
        if r in (4, 7):
            print(sep)
        row = [str(solver.value(x[r - 1][c - 1])) for c in range(1, 10)]
        print(f"{' '.join(row[:3])} | {' '.join(row[3:6])} | {' '.join(row[6:])}")


if __name__ == "__main__":
    main()
