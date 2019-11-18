def paths_through_maze(maze):
    paths = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    paths[0][0] = 1
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if not maze[i][j]:
                if i > 0 and j > 0:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
                elif i > 0:
                    paths[i][j] = paths[i - 1][j]
                elif j > 0:
                    paths[i][j] = paths[i][j - 1]
            else:
                paths[i][j] = 0
    return paths[len(maze) - 1][len(maze[0]) - 1]


# Fill this in.

def main():
    assert (paths_through_maze([[0, 1, 0],
                                [0, 0, 1],
                                [0, 0, 0]])) == 2


#
if __name__ == '__main__':
    main()
