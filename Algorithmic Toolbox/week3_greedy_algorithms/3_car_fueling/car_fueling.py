# python3
import sys


def compute_min_refills(distance, tank, stops):
    number_of_refills = 0
    current_refill = 0
    stops.insert(0, 0) # insert start position
    stops.append(distance) # append end position
    n = len(stops) - 2
    
    while current_refill <= n:
        last_refill = current_refill
        while current_refill <= n and (stops[current_refill + 1] - stops[last_refill]) <= tank:
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= n:
            number_of_refills += 1
        
    return number_of_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

#d = 950
#m = 400
#_ = 4
#stops = [200,375,550,750]
#print("Should be 2", compute_min_refills(d, m, stops))
#
#d = 10
#m = 3
#_ = 4
#stops = [1,2,5,9]
#print("Should be -1", compute_min_refills(d, m, stops))

