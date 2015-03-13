from time import time

def memoize2(f):
    class memodict(dict):
        def __init__(self, f):
            self.f = f        
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):            
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

def memoize(f):
    memodict = {}
    def hepler(x):
        if x not in memodict:            
            memodict[x] = f(x)
        return memodict[x]
    return hepler
        
        
@memoize
def fib(n):
    return n if n <= 1 else fib(n-1)+fib(n-2)
    
t0= time()
print fib(40)
print time()-t0

# no memoize: 34.365031004 
# with memoize: 0.000152111053467
# 225920 times faster
print [ 'hizzy' if (i%15==0 or i%5==0 or i%3==0) else i for i in range(100)]
