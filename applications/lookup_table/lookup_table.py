import math
import random
import time

cache = {}

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    if str(x)+"_"+str(y) in cache.keys():
        return cache[str(x)+"_"+str(y)]

    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    
    cache[str(x)+"_"+str(y)] = v

    return v


# Do not modify below this line!

start = time.time()

for i in range(100):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

print("Imp 1: \t%.8f" % float(time.time() - start))