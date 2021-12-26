from collections import deque


class Path:
    def __init__(self, nodes):
        self.nodes = nodes

    def add(self, node):
        self.nodes.append(node)

    def has(self, node):
        return node in self.nodes

    def copy(self):
        return Path(list(self.nodes))

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return ' -> '.join([n.id for n in self.nodes])


class Graph:
    def __init__(self):
        self.nodes = {}

    def set(self, node):
        self.nodes[node.id] = node

    def get_node(self, id):
        try:
            return self.nodes[id]
        except KeyError:
            return Node(id)

    def __str__(self):
        return '\n'.join([
            f'{id} -> {" ".join([n.id for n in node.nodes])}'
            for id, node in self.nodes.items()
        ])


class Node:
    def __init__(self, id):
        self.id = id
        self.revisitable = id.isupper()
        self.nodes = set()

    def link_with(self, node):
        if self.id == 'start' or node.id == 'end':
            self.nodes.add(node)
        elif self.id == 'end' or node.id == 'start':
            node.nodes.add(self)
        else:
            self.nodes.add(node)
            node.nodes.add(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return self.id


def can_still_visit_small_caves(path):
    small_caves_visits = set()
    for node in path.nodes:
        if not node.revisitable:
            if node in small_caves_visits:
                return False
            small_caves_visits.add(node)

    return True


def find_all_paths(can_visit_small_cave_twice=False):
    graph = get_data()
    paths = set()

    # bfs
    # - appendleft
    # - pop
    queue = deque([Path([graph.get_node('start')])])

    while len(queue) > 0:
        path = queue.pop()
        last_node = path.nodes[-1]

        if last_node.id == 'end':
            paths.add(path)
            continue

        for node in last_node.nodes:
            if node.revisitable or not path.has(node) \
                    or (can_visit_small_cave_twice and can_still_visit_small_caves(path)):
                new_path = path.copy()
                new_path.add(node)
                queue.appendleft(new_path)

    return paths


def get_data():
    with open('day12/data') as f:
        graph = Graph()

        for line in f.readlines():
            [n1, n2] = [graph.get_node(id) for id in line.strip().split('-')]
            n1.link_with(n2)
            graph.set(n1)
            graph.set(n2)

        return graph
