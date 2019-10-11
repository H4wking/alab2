import math


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def construct(p):
    px = sorted(p, key=lambda x: x[0])
    py = sorted(p, key=lambda x: x[1])
    return px, py


def closest_pair(p):
    px, py = construct(p)
    p0, p1 = closest_pair_rec(px, py)
    return distance(p0, p1), (p0, p1)


def closest_pair_rec(px, py):
    if len(px) <= 3:
        min_distance = [math.inf, 0, 0]
        for point1 in px:
            for point2 in px:
                d = distance(point1, point2)
                if d and d < min_distance[0]:
                    min_distance = [d, point1, point2]
        return min_distance[1:]

    n = len(px)
    qx, qy = px[:n//2], py[:n//2]
    rx, ry = px[n//2:], py[n//2:]

    q0, q1 = closest_pair_rec(qx, qy)
    r0, r1 = closest_pair_rec(rx, ry)

    delta = min(distance(q0, q1), distance(r0, r1))
    max_x = qx[-1][0]
    s = [point for point in px if max_x - point[0] < delta]

    sy = construct(s)[1]
    min_distance = [math.inf, 0, 0]
    for i in range(len(sy)):
        for j in range(15):
            try:
                d = distance(sy[i], sy[i+j])
            except:
                continue
            if d and d < min_distance[0]:
                min_distance = [d, sy[i], sy[i+j]]

    s0, s1 = min_distance[1], min_distance[2]

    if distance(s0, s1) < delta:
        return (s0, s1)
    elif distance(q0, q1) < distance(r0, r1):
        return (q0, q1)
    else:
        return (r0, r1)









