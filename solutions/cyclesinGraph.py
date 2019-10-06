def find_cycle(graph, parent, node, visited=None):
    if visited is None:
        visited = dict()
        for node in graph:
            visited[node] = False
            for child in graph[node]:
                print(child)
                visited[child] = False
    visited[node] = True
    if parent:
        # if the node has more children in the graph
        if graph[parent][node]:
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    if find_cycle(graph, node, neighbour, visited):
                        return True
                # If the neighbour is visited already and the neighbour is not the parent we are previously connecting
                # from, then there is a cycle
                elif parent != neighbour:
                    return True
    else:
        for neighbour in graph[node]:
            if not visited[neighbour]:
                if find_cycle(graph, node, neighbour, visited):
                    return True
            elif parent != neighbour:
                return True
    return False


def main():
    graph = {
        'a': {'a2': {}, 'a3': {}},
        'b': {'b2': {}},
        'c': {}
    }
    graph['c'] = graph
    assert find_cycle(graph, None, 'a')


if __name__ == '__main__':
    main()
