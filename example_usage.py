from client import PLUDecomposition

def main():
    A = [[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]]
    b = [8.0, -11.0, -3.0]
    x = PLUDecomposition.solve(A, b)
    print("Linear System Solution x:", [round(v, 4) for v in x])
    assert abs(x[0] - 2.0) < 1e-4

if __name__ == "__main__":
    main()
