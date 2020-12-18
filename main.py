import numpy as np
from proc_pkg.process import mat_prod

if __name__ == '__main__':
    M = 2
    N = 3
    x = np.random.randn(M, N)
    y = np.random.randn(N, M)
    z = mat_prod(x, y)
    print("x = \n", x)
    print("y = \n", x)
    print("z = x * y = \n", z)