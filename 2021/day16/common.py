from __future__ import annotations

from functools import reduce

version_type_num_bits = 6


class Packet:
    def __init__(self, version, packet_type):
        self.version = version
        self.packet_type = packet_type
        self.children = []
        self.parent = None

    def remaining_data(self):
        pass

    def set_parent(self, parent: Packet):
        self.parent = parent
        parent.children.append(self)


class LiteralPacket(Packet):
    def __init__(self, version, packet_type, data):
        super().__init__(version, packet_type)

        [value, remaining_data] = LiteralPacket.parse_data(data)
        self.value = value
        self.remaining_data = remaining_data

    @staticmethod
    def parse_data(data):
        part_size = 5
        trailing_zeros = 0

        # read 5 bits until the first is 0
        parts = []
        for i in range(0, len(data), part_size):
            part = data[i:i + part_size]

            if len(part) != 5:
                trailing_zeros = len(part)
                break

            parts.append(part[1:])
            if part[0] == 0:
                break

        length = version_type_num_bits + (len(parts) * part_size)
        trailing_zeros = 4 - (length % 4)
        remaining_data = data[length + trailing_zeros:]

        value = int(''.join(parts), 2)
        return value, remaining_data


class OperatorPacket(Packet):
    @staticmethod
    def parse(version, packet_type, data):
        # id = int(data[0], 2)
        #
        # if id == 0:
        #     subpacket_length = int(data[1:16], 2)
        #     pass
        # if id == 1:
        #     subpacket_number = int(data[1:12], 2)
        #
        # rest = data[1:]
        return OperatorPacket(version, packet_type)


def get_data():
    with open('day16/data') as f:
        def char_to_hex(char):
            return bin(int(char, 16))[2:].zfill(4)

        hex_chars = [c for c in f.readline().strip()]
        return reduce(lambda acc, char: acc + char_to_hex(char), hex_chars, '')
