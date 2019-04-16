# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
    pass

def test_solution(max_runtime):
    # max_runtime in seconds
    import time
    import random
    random.seed(1)
    start_time = time.time()
    
    while (time.time() <= start_time + max_runtime):
        n = random.randint(0, 10000)
        if gcd_naive(n) == gcd(n):
            print("Solution passes for n =", n)
        else:
            print("Solution fails with n=", n)
            print("get_fibonacci_last_digit_naive({n}) = {x}".format(n=n, x=gcd_naive(n)))
            print("get_fibonacci_last_digit({n}) = {x}".format(n=n, x=gcd(n)))
            return

#if __name__ == "__main__":
#    input = sys.stdin.read()
#    a, b = map(int, input.split())
#    print(gcd(a, b))

test_solution(30)