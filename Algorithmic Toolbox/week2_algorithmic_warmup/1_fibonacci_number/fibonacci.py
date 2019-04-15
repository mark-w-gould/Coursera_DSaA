# Uses python3

import time
import random

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    fibs = []
    
    fibs.append(0)
    fibs.append(1)
    
    for entry in range(2, n + 1):
        fibs.append(fibs[entry - 1] + fibs[entry - 2])
    
    return fibs[n]

def test_solution(max_runtime):
    # max_runtime in seconds
    random.seed(1)
    start_time = time.time()
    
    while (time.time() <= start_time + max_runtime):
        n = random.randint(0, 45)
        if calc_fib(n) == calc_fib_fast(n):
            print("Solution passes for n =", n)
        else:
            print("Solution fails with n=", n)
            print("calc_fib({n}) = {x}".format(n=n, x=calc_fib(n)))
            print("calc_fib_fast({n}) = {x}".format(n=n, x=calc_fib_fast(n)))
            return
    

n = int(input())
print(calc_fib_fast(n))

#test_solution(240)
