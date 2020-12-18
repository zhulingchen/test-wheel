import numpy as np
from proc_pkg.process import mat_prod

def test_process():
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[5, 6], [1, 2], [3, 4]])
    assert np.array_equal(mat_prod(x, y), np.array([[16, 22], [43, 58]]))