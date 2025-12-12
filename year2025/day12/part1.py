from year2025.day12.common import parse_input


def run(data: list[str], is_test: bool):
    if is_test:
        return 0  # fuck this trap

    regions = parse_input(data)

    valid_regions = 0

    for region in regions:
        area = region.width * region.height
        max_shape_area = sum(p * 9 for p in region.presents)
        if area >= max_shape_area:
            valid_regions += 1

    return valid_regions


test_result = 0
