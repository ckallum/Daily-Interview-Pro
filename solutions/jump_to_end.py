from cmath import inf


def jump_to_end_back_to_front(jumps):
    jump_dict = {x: 0 for x in range(len(jumps))}
    for i in range(len(jumps) - 2, -1, -1):
        if jumps[i] >= len(jumps) - i - 1:
            jump_dict[i] = 1
        elif jumps[i] == 0:
            jump_dict[i] = inf
        else:
            min_jump = inf
            for j in range(1, jumps[i] + 1):
                jump = 1 + jump_dict[i + j]
                if jump < min_jump:
                    jump_dict[i] = jump
                    min_jump = jump
    return jump_dict[0]


def main():
    assert jump_to_end_back_to_front([1, 3, 0, 8, 9, 2, 6, 7, 6, 8, 9]) == 3
    assert jump_to_end_back_to_front([3, 2, 5, 1, 1, 9, 3, 4]) == 2


if __name__ == '__main__':
    main()
