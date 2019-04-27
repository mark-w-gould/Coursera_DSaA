# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fib_n(n):

    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def get_pisano_period(m):
    
    previous = 0
    current = 1
    
    for i in range(2, m * m):
        previous, current = current, fib_n(i) % m
        if previous == 0 and current == 1:
            return i
    

def fib_mod_m(n, m):
    pi_m = get_pisano_period(m)
    
    revised_n = n % pi_m
    
    return fib_n(revised_n)

def test_solution(max_runtime):
    # max_runtime in seconds
    import time
    import random
    random.seed(1)
    start_time = time.time()
    
    while (time.time() <= start_time + max_runtime):
        n = random.randint(1, 100000)
        m = random.randint(2, 1000)
        if get_fibonacci_huge_naive(n, m) == fib_mod_m(n, m):
            print("Solution passes for n = {a} and m = {b}. Result: {x}".format(a=n, b=m, x=fib_mod_m(n, m)))
        else:
            print("Solution fails for n = {a} and m = {b}".format(a=n, b=m))
            print("naive({a}, {b}) = {x}".format(a=n, b=m, x=get_fibonacci_huge_naive(n, m)))
            print("efficient({a}, {b}) = {x}".format(a=n, b=m, x=fib_mod_m(n, m)))
            return

#if __name__ == '__main__':
##    input = sys.stdin.read();
##    n, m = map(int, input.split())
#    n = 99999999999999999
#    m = 2
#    print(fib_mod_m(n, m))
            
test_solution(30)
