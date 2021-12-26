from day16.common import get_data, Packet, LiteralPacket, OperatorPacket


def run():
    data = get_data()
    root = None
    last_node = None

    while len(data) > 0:
        version = int(data[0:3], 2)
        packet_type = int(data[3:6], 2)
        data = data[6:]

        # packet = None
        if packet_type == 4:
            packet = LiteralPacket(version, packet_type, data)
        else:
            packet = OperatorPacket(version, packet_type, data)

        if root is None:
            root = packet
        else:
            packet.set_parent(last_node)

        last_node = packet
        data = packet.remaining_data

    return packet.value
