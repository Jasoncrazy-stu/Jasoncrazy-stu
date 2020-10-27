import numpy as np
def impseq(n0,n1,n2):
#Generates x(n)=delta(n-n0);n1<=n,n0<=n2
#-----------------------------------------
# [x, n] = impseq(n0, n1, n2)
    if ((n0 < n1) or (n0 > n2) or (n1 > n2)):
      raise Exception('arguments must satisfy n1<=n0,n<=n2')
    a = np.zeros(n2-n1+1)
    a[n0-n1] = 1
    return a
def stepseq(n0,n1,n2):
    # Generates
    # x(n) = u(n - n0);
    # n1 <= n, n0 <= n2
    # -----------------------------------------
    if ((n0 < n1) or (n0 > n2) or (n1 > n2)):
        raise Exception('arguments must satisfy n1<=n0,n<=n2')
    a = np.zeros(n2-n1+1)
    a[(n0-n1):] = 1
    return a