# Uses python3
import sys

def get_change(m):
    
    coins_used = 0
    remainder = m
    
    while remainder > 0:
        if remainder >= 10: # try removing a ten coin
            remainder -= 10
            coins_used += 1
        elif remainder >= 5:
            remainder -= 5
            coins_used += 1
        else:
            remainder -= 1
            coins_used += 1
    
    return coins_used

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
