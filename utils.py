import numpy as np

def W_increments(T, N):
    h = T/N
    return np.random.normal(0, np.sqrt(h), N)

def W_process(T, N):
    incr = W_increments(T, N-1)
    incr = np.insert(incr, 0, 0)
    return incr.cumsum()

