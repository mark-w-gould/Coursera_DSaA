# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    r = a % b
    return int(gcd(b, r))

def lcm(a, b):
    denom = gcd(a,b)
    
    return int(a/denom) * b
    

def test_solution(max_runtime):
    # max_runtime in seconds
    import time
    import random
    random.seed(1)
    start_time = time.time()
    
    while (time.time() <= start_time + max_runtime):
        a = random.randint(1, 2000)
        b = random.randint(1, 2000)
        if lcm_naive(a, b) == lcm(a, b):
            print("Solution passes for a = {a} and b = {b}".format(a=a, b=b))
        else:
            print("Solution fails for a = {a} and b = {b}".format(a=a, b=b))
            print("naive({a}, {b}) = {x}".format(a=a, b=b, x=lcm_naive(a, b)))
            print("efficient({a}, {b}) = {x}".format(a=a, b=b, x=lcm(a, b)))
            return


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

#test_solution(30)

