import heapq
from itertools import count


def k_most_frequent(numbers, k):
    formatted = [(count(number) in numbers, number) for number in numbers]
    heap_arr = heapq.heapify(formatted)
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap_arr))
        heapq.heapify(heap_arr)

    return result


def main():
    assert k_most_frequent(["daily", "interview", "pro", "pro",
                            "for", "daily", "pro", "problems"], 2) == ["pro", "daily"]
