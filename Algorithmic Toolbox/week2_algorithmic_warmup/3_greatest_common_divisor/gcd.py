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
    if a == 0:
        return b
    if b == 0:
        return a
    
    r = a % b
    return gcd(b, r)

def test_solution(max_runtime):
    # max_runtime in seconds
    import time
    import random
    random.seed(1)
    start_time = time.time()
    
    while (time.time() <= start_time + max_runtime):
        a = random.randint(1, 20000)
        b = random.randint(1, 20000)
        if gcd_naive(a, b) == gcd(a, b):
            print("Solution passes for a = {a} and b = {b}".format(a=a, b=b))
        else:
            print("Solution passes for a = {a} and b = {b}".format(a=a, b=b))
            print("naive({a}, {b}) = {x}".format(a=a, b=b, x=gcd_naive(a, b)))
            print("efficient({a}, {b}) = {x}".format(a=a, b=b, x=gcd(a, b)))
            return

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))

#test_solution(240)