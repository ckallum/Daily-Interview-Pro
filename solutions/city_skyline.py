import heapq


def generate_skyline(buildings):
    tallest = []
    skyline = []
    # We are adding the extra building to pad for double the buildings when we
    # iterating down the skyline
    buildings += [(x + 1, x + 1, 0) for (_, x, _) in buildings]
    # Sorts by the first value in tuple, if equal sort by the second.
    # i.e. prioritise sorting by starting index, if it is the same then prioritise largest height
    buildings.sort(key=lambda x: (x[0], -x[2]))
    print(buildings)

    for l, r, h in buildings:
        # Remove shorter buildings behind current building.
        while tallest and l >= tallest[0][1]:
            heapq.heappop(tallest)

        # Add current building to heap.
        heapq.heappush(tallest, (-h, r))
        print(tallest)

        # Append to skyline if the building is not the tallest.
        # Current building in tallest will always be the current buliding,
        # the current building should inherit the change in height from the
        # tallest building before.
        if not skyline or skyline[-1][1] != -tallest[0][0]:
            skyline.append((l, -tallest[0][0]))
    return skyline


def main():
    assert generate_skyline([(2, 8, 3), (2, 8, 4), (4, 6, 5)]) == [(2, 4), (4, 5), (7, 4), (9, 0)]


if __name__ == '__main__':
    main()
