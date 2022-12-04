import numpy as np

def conj_grad(A,b,error):
    n = A.shape[0]
    iter, x = 0, np.zeros(n)
    r = b - np.dot(A,x)
    s = r
    while np.norm(r) > error:
        q = np.dot(A,s)
        alpha = np.dot(s, r)/np.dot(s, q)
        x = x + alpha*s
        r = b - np.dot(A,x)
        beta = -np.dot(r, q)/np.dot(s, q)
        s = r + beta*s
        iter = iter + 1
    return x, iter