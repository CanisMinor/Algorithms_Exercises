# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    n_seg = len(segments)
    i = 0

    #sort by starting point
    segments.sort(key=lambda x: x[1])

    while i < n_seg:
        current_point = segments[i][1]
        points.append(current_point)

        while i < n_seg and segments[i][0] <= current_point and segments[i][1] >= current_point:
            i += 1

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
