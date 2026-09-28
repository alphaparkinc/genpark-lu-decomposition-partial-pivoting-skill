"""PLU Matrix Factorization & Linear System Solver.
100% Python Standard Library.
"""

class PLUDecomposition:
    """Gaussian elimination with row partial pivoting for general square matrices."""

    @staticmethod
    def decompose(A: list) -> tuple:
        n = len(A)
        U = [row[:] for row in A]
        L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        P = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

        for i in range(n):
            max_row = i
            max_val = abs(U[i][i])
            for k in range(i + 1, n):
                if abs(U[k][i]) > max_val:
                    max_val = abs(U[k][i])
                    max_row = k
            if max_row != i:
                U[i], U[max_row] = U[max_row], U[i]
                P[i], P[max_row] = P[max_row], P[i]
                for j in range(i):
                    L[i][j], L[max_row][j] = L[max_row][j], L[i][j]

            for j in range(i + 1, n):
                factor = U[j][i] / U[i][i]
                L[j][i] = factor
                for k in range(i, n):
                    U[j][k] -= factor * U[i][k]

        return P, L, U

    @classmethod
    def solve(cls, A: list, b: list) -> list:
        n = len(A)
        P, L, U = cls.decompose(A)
        Pb = [sum(P[i][j] * b[j] for j in range(n)) for i in range(n)]
        y = [0.0] * n
        for i in range(n):
            s = sum(L[i][j] * y[j] for j in range(i))
            y[i] = Pb[i] - s
        x = [0.0] * n
        for i in range(n - 1, -1, -1):
            s = sum(U[i][j] * x[j] for j in range(i + 1, n))
            x[i] = (y[i] - s) / U[i][i]
        return x
