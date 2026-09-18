from math import atan2, isclose, pi

N = 50


def has_right_angle(p: tuple[int, int], q: tuple[int, int]) -> bool | None:  # noqa: PLR0911
    if p == (0, 0):
        return None
    if q == (0, 0):
        return None
    angle_op = atan2(p[1], p[0])
    angle_oq = atan2(q[1], q[0])
    if angle_oq > angle_op:
        return None
    if isclose(angle_op, angle_oq):
        return None
    angle_1 = angle_op - angle_oq
    if isclose(angle_1, pi / 2):
        return True
    angle_pq = atan2(q[1] - p[1], q[0] - p[0])
    angle_2 = pi - angle_op + angle_pq
    if isclose(angle_2, pi / 2):
        return True
    angle_3 = pi - angle_1 - angle_2
    return bool(isclose(angle_3, pi / 2))


def main() -> int:
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
    return count


if __name__ == "__main__":
    main()
