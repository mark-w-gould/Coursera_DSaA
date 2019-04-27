# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    unit_values = [x/y for x, y in zip(values, weights)]
    combined = [[x,y,z] for x, y, z in zip(values, weights, unit_values)]
    combined.sort(key=lambda x: x[2], reverse=True)
    for count in range(len(combined)):
        if capacity == 0:
            return value
        this_fill = min(combined[count][1], capacity)
        value += this_fill * combined[count][2]
        capacity -= this_fill
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

#n = 3
#capacity = 50
#values = [60,100,120]
#weights = [20,50,30]
#opt_value = get_optimal_value(capacity, weights, values)
#print("{:.10f}".format(opt_value))