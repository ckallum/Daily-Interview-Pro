# MinHeap or max heap data structure
import heapq


def find(numbers, k):
    numbers.sort()
    return numbers[-k]


def maxHeapSolution(numbers, k):
    return heapq.nlargest(3, numbers)[k - 1]


def selfMaxHeap(numbers, k):
    heap = Heap(numbers)
    heap.buildHeap()
    return heap.extractMax(k)


def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    return arr


class Heap(object):
    def __init__(self, values):
        self.heaparr = values
        self.size = len(self.heaparr)

    def heapify(self, size, index):
        parent = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < size and self.heaparr[parent] < self.heaparr[left]:
            parent = left
        if right < size and self.heaparr[parent] < self.heaparr[right]:
            parent = right
        if parent != index:
            self.heaparr = swap(self.heaparr, index, parent)
            self.heapify(size, parent)

    def extractMax(self, k):
        for index in range(self.size - 1, self.size - (k + 1), -1):
            self.heaparr = swap(self.heaparr, index, 0)
            self.heapify(index, 0)
        return self.heaparr[-k]

    def buildHeap(self):
        for index in range(int((self.size - 1) / 2), -1, -1):
            self.heapify(self.size, index)


def main():
    assert find([3, 5, 2, 4, 6, 8], 3) == 5
    assert maxHeapSolution([3, 5, 2, 4, 6, 8], 3) == 5
    assert selfMaxHeap([3, 5, 2, 4, 6, 8], 3) == 5


if __name__ == '__main__':
    main()
