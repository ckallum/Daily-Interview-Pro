import heapq


def running_median(stream):
    if not stream:
        return None

    min_heap = []
    max_heap = []
    medians = []

    for number in stream:
        heapq.heappush(min_heap, number)
        # We start off by directly pushing to the min_heap, if the heaps aren't balanced we push the biggest number
        # in the min_heap to the max_heap, this makes sure all the numbers in the max_heap are larger than the
        # numbers in the min_heap.
        if len(min_heap) > len(max_heap) + 1:
            # We push the negative value as heapq.heappush max heapify's the array, however, we want the smallest
            # values of the max heap and the largest values of the min heap essentially simulate the middle two numbers
            # in a sorted array.
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        if len(min_heap) == len(max_heap):
            medians.append((min_heap[0] - max_heap[0])/2)
        else:
            medians.append(min_heap[0])
    return medians


def main():
    assert running_median([2, 1, 4, 7, 2, 0, 5]) == [2, 1.5, 2, 3.0, 2, 2.0, 2]


if __name__ == '__main__':
    main()
