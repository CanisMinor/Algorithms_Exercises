# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    n = len(weights)

    for _ in range(0, n):
        best_item = 0
        best_density = 0.
        for i in range(0, n):
            if weights[i] > 0:
                if float(values[i]/weights[i]) > best_density:
                    best_density = float(values[i]/weights[i])
                    best_item = i
        if weights[best_item] <= capacity:
            capacity -= weights[best_item]
            weights[best_item] = 0.
            value += values[best_item]
        else:
            weights[best_item] = weights[best_item] - capacity
            value += capacity * best_density
            capacity = 0.

    return value

#print(get_optimal_value(500, [1.0], [5.0]))

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
