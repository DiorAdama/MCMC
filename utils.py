import numpy as np

def W_increments(T, N):
    h = T/N
    return np.random.normal(0, np.sqrt(h), N)

def W_process(T, N):
    incr = W_increments(T, N-1)
    incr = np.insert(incr, 0, 0)
    return incr.cumsum()


# returns an array containing the integral between 0 and t of func(s)dWs for t in [0, T/N, 2T/N, ..., T]
def dW_integral(func, T, N): 
    dW = W_increments(T, N)
    time_steps = np.linspace(0, T, N+1)[:-1]
    f = func(time_steps)
    ans = f*dW
    ans = np.insert(ans, 0, 0)
    return ans.cumsum()

#returns an array conataining [x0, x1, ..., xN] a sample of an OU_process at times [0, T/N, 2T/N, ..., T] 
def OU_process(T, N, x0, alpha, beta, gamma): 
    def exp_alpha(t):
        return np.exp(-alpha*t)

    time_steps = np.linspace(0, T, N+1)

    return x0*exp_alpha(time_steps) + gamma*(1-exp_alpha(time_steps)) + beta*exp_alpha(time_steps)*dW_integral(exp_alpha, T, N)

