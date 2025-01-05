from math import atan2, pi, isclose

N = 50


def has_right_angle(P, Q):
    if P == (0, 0):
        return None
    if Q == (0, 0):
        return None
    angle_OP = atan2(P[1], P[0])
    angle_OQ = atan2(Q[1], Q[0])
    if angle_OQ > angle_OP:
        return None
    if isclose(angle_OP, angle_OQ):
        return None
    angle_1 = angle_OP - angle_OQ
    if isclose(angle_1, pi / 2):
        return True
    angle_PQ = atan2(Q[1] - P[1], Q[0] - P[0])
    angle_2 = pi - angle_OP + angle_PQ
    if isclose(angle_2, pi / 2):
        return True
    angle_3 = pi - angle_1 - angle_2
    if isclose(angle_3, pi / 2):
        return True
    return False


count = 0
for x_1 in range(N + 1):
    for x_2 in range(N + 1):
        for y_1 in range(N + 1):
            for y_2 in range(N + 1):
                out = has_right_angle((x_1, x_2), (y_1, y_2))
                # print((x_1, x_2), (y_1, y_2), out)
                if out is None:
                    continue
                if out:
                    count += 1
print(count)
