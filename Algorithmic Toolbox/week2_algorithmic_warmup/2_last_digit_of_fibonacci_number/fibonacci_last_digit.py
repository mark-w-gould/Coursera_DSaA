# Uses python3
import sys
import time
import random

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous_digit = 0
    current_digit  = 1

    for _ in range(n - 1):
        if previous_digit + current_digit >= 10:
            previous_digit, current_digit = current_digit, (previous_digit + current_digit) % 10
        else:
            previous_digit, current_digit = current_digit, previous_digit + current_digit

    return current_digit

def test_solution(max_runtime):
    # max_runtime in seconds
    random.seed(1)
    start_time = time.time()
    
    while (time.time() <= start_time + max_runtime):
        n = random.randint(0, 10000)
        if get_fibonacci_last_digit_naive(n) == get_fibonacci_last_digit(n):
            print("Solution passes for n =", n)
        else:
            print("Solution fails with n=", n)
            print("get_fibonacci_last_digit_naive({n}) = {x}".format(n=n, x=get_fibonacci_last_digit_naive(n)))
            print("get_fibonacci_last_digit({n}) = {x}".format(n=n, x=get_fibonacci_last_digit(n)))
            return

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))

#test_solution(240)