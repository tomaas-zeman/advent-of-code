from year2019.day03.common import generate_lines, Point


def run(data: list[str], raw_data: list[str], is_test: bool):
    paths1 = data[0].split(",")
    paths2 = data[1].split(",")

    lines1 = generate_lines(paths1)
    lines2 = generate_lines(paths2)

    steps = []
    for i_l1 in range(len(lines1)):
        for i_l2 in range(len(lines2)):
            intersection = lines1[i_l1].find_intersection_point(lines2[i_l2])
            if intersection is not None:
                last_l1_common_point = Point(0, 0) if i_l1 == 0 else lines1[i_l1].common_point(lines1[i_l1 - 1])
                last_l2_common_point = Point(0, 0) if i_l2 == 0 else lines2[i_l2].common_point(lines2[i_l2 - 1])

                if last_l1_common_point and last_l2_common_point:
                    steps.append(
                        sum([line.p1.manhattan_dist(line.p2) for line in lines1[0:i_l1] + lines2[0:i_l2]])
                        + intersection.manhattan_dist(last_l1_common_point)
                        + intersection.manhattan_dist(last_l2_common_point)
                    )

    return sorted(steps)[0]
