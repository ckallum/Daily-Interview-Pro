def build_graph(edges):
    graph = dict()
    for source, target in edges:
        if source not in graph:
            graph[source] = [target]
        else:
            graph[source].append(target)
        if target not in graph:
            graph[target] = [source]
        else:
            graph[target].append(source)

    return graph


def dfs(source, graph, visited):
    visited.append(source)
    for neighbour in graph[source]:
        if neighbour not in visited:
            dfs(neighbour, graph, visited)


def count_components(edges):
    graph = build_graph(edges)
    visited = []
    count = 0
    for source in graph:
        if source not in visited:
            dfs(source, graph, visited)
            count += 1
    return count


def main():
    assert count_components([(1, 2), (2, 3), (4, 1), (5, 6)]) == 2


if __name__ == '__main__':
    main()
