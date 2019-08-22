def dominoes(domino):
    forces = [0] * len(domino)
    f = 0
    for n in range(len(domino)):
        if domino[n] == 'R':
            f = len(domino)
        elif domino[n] == 'L':
            f = 0
        else:
            f = max(f - 1, 0)
        forces[n] += f
    f = 0
    for n in range(len(domino) - 1, -1, -1):
        if domino[n] == 'L':
            f = len(domino)
        elif domino[n] == 'R':
            f = 0
        else:
            f = max(f-1, 0)
        forces[n] -= f
    print(forces)
    return "".join("." if x == 0 else "R" if x > 0 else "L" for x in forces)


def main():
    assert dominoes("..R...L..R.") == "..RR.LL..RR"


if __name__ == '__main__':
    main()
