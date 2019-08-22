def find_cycle(graph, parent, node, visited=None):
    if visited is None:
        visited = dict()
        for node in graph:
            visited[node] = False
            for child in graph[node]:
                print(child)
                visited[child] = False
    visited[node] = True
    if parent != "None":
        if graph[parent][node]:
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    if find_cycle(graph, node, neighbour, visited):
                        return True
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
    assert find_cycle(graph, "None", 'a') == True


if __name__ == '__main__':
    main()
