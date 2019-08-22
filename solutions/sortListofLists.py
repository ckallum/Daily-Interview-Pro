# Sorting a list of lists-> easy: flatten and sort, hard: convert list to heap structure/minPQ of each element->once element has been removed add the tuple with the next value in the list to be sorted



from functools import reduce

import heapq


def simpleSort(l):
    xs = list(reduce(lambda x, y: x + y, l))
    return (sorted(xs))


def efficientSort(l):
    sortList = []
    heap = [(lst[0], i, 0) for i, lst in enumerate(l) if lst]
    heapq.heapify(heap)
    while heap:
        val, listIndex, elementIndex = heapq.heappop(heap)
        sortList.append(val)
        if elementIndex + 1 < len(l[listIndex]):
            node = (l[listIndex][elementIndex + 1], listIndex, elementIndex + 1)
            heapq.heappush(heap, node)
            heapq.heapify(heap)
    return sortList


def main():
    l = [[6, 9, 15], [3, 4, 7], [8, 9, 21], [12, 23, 45], [4, 12, 34]]
    print('Original List: ', l)
    print('Simple sort: ', simpleSort(l))
    print('Efficient Sort: ', efficientSort(l))


if __name__ == '__main__':
    main()
