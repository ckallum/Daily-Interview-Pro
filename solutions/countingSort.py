def countingSort(l):
    d = {1: 0, 2: 0, 3: 0}

    for x in l:
        d[x] += 1
    d[2] += d[1]
    d[3] += d[2]

    for x in range(3, 0, -1):
        if x > 1:
            while d[x] > d[x - 1]:
                d[x] -= 1
                l[d[x]] = x
        while d[x] > 0:
            d[x] -= 1
            l[d[x]] = x

    print(l)


def main():
    l = [3, 3, 2, 1, 3, 2, 1]
    countingSort(l)


if __name__ == '__main__':
    main()
