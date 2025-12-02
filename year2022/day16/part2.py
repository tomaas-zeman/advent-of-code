from year2022.day16.common import find_flows


def run(data: list[str], is_test: bool):
    flows = find_flows(data, 26)

    flow_exclusive_pairs = []
    for me in flows.items():
        for elephant in flows.items():
            my_bitmap, my_flow = me
            elephants_bitmap, elephants_flow = elephant
            if not my_bitmap & elephants_bitmap:
                flow_exclusive_pairs.append(my_flow + elephants_flow)

    return max(flow_exclusive_pairs)


test_result = 1707
