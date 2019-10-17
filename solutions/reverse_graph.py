from collections import defaultdict


class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value


def reverse_graph(graph):
    visited = {node: False for node in graph}
    for node in graph.values():
        visited[node.value] = True
        for neighbour in node.adjacent:
            if not visited[neighbour.value]:
                neighbour.adjacent.append(node)
                node.adjacent = list(set(node.adjacent) - {neighbour})
    return graph


def main():
    a = Node('a')
    b = Node('b')
    c = Node('c')

    a.adjacent += [b, c]
    b.adjacent += [c]

    graph = {
        a.value: a,
        b.value: b,
        c.value: c,
    }
    results = [[], ['a'], ['a', 'b']]
    index = 0
    for val in [[n.value for n in node.adjacent] for node in reverse_graph(graph).values()]:
        assert val == results[index]
        index += 1


if __name__ == '__main__':
    main()
