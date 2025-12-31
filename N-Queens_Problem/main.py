def dfs_n_queens(n:int):
    if n < 1: return []
    solutions = []

    def backtrack(row, placement):
        if row == n:
            solutions.append(placement[:])
            return

        for col in range(n):
            safe = True

            for r in range(row):
                c = placement[r]

                if c == col or abs(row - r) == abs(col - c):
                    safe = False
                    break

            if safe:
                placement.append(col)
                backtrack(row + 1, placement)
                placement.pop()

    backtrack(0, [])
    return solutions
