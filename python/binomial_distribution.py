##
from functional import memoize

@memoize
def binomial(N,k,p=0.5):
    if N==0 and k==0: return 1.0
    if N<0 or k<0: return 0.0
    return (1-p)*binomial(N-1,k,p) + p*binomial(N-1,k-1,p)
##

