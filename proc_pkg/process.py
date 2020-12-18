import numpy as np

def mat_prod(x, y):
    assert isinstance(x, np.ndarray) and isinstance(y, np.ndarray)
    assert x.ndim == y.ndim == 2
    assert x.shape[1] == y.shape[0]
    return np.matmul(x, y)