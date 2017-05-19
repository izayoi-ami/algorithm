##
from functools import wraps

def memoize(f):
    memo = {}
    @wraps(f)
    def wrapper(*args, **kwargs):
        try: return memo[args]
        except KeyError:
            memo[args] = f(*args, **kwargs)
            return memo[args]
    return wrapper





def trampoline(f):
    """ A function with tailcall structure
    """
    @wraps(f)
    def call(*args, **kwargs):
        try:
            h = f
            while True: h, args, kwargs = h(*args, **kwargs).next()
        except TypeError:
            return None,args,kwargs
    return call

def tailcall(f):
    def g(*args, **kwargs): return f, args, kwargs
    return g


def fib(n,a=0,b=1):
    yield a if n == 0 else tailcall(fib)(n-1,b,a+b)
##

