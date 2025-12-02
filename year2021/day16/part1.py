def handle_literal(packet: str):
    number_parts = []
    index = 0

    while True:
        if index + 5 > len(packet):
            break

        number_parts.append(packet[index + 1 : index + 5])
        if int(packet[index]) == 0:
            break

        index += 5

    return int("".join(number_parts), 2), index + 5


def compute(packet: str, seq=None):
    def next_seq():
        return None if seq is None else seq - 1

    if all(int(c) == 0 for c in packet):
        return 0

    if seq is not None and seq < 0:
        return compute(packet)

    version = int(packet[:3], 2)
    type = int(packet[3:6], 2)

    if type == 4:
        number, index_shift = handle_literal(packet[6:])
        # return number + compute(packet[6 + index_shift :], next_seq())
        return version + compute(packet[6 + index_shift :], next_seq())

    length_id = int(packet[6])

    if length_id == 0:
        start = 7
        end = start + 15
        subpacket_length = int(packet[start:end], 2)
        # return compute(packet[end : end + subpacket_length], next_seq()) + compute(
        #     packet[end + subpacket_length :], next_seq()
        # )
        return (
            version
            + compute(packet[end : end + subpacket_length], next_seq())
            + compute(packet[end + subpacket_length :], next_seq())
        )

    if length_id == 1:
        start = 7
        end = start + 11
        subpacket_count = int(packet[start:end], 2)
        # return compute(packet[end:], subpacket_count)
        return version + compute(packet[end:], subpacket_count)


def run(data: list[str], is_test: bool):
    process_line = lambda line: bin(int(line, 16))[2:].zfill(len(line) * 4)
    return sum(compute(process_line(line)) for line in data)


test_result = 82
