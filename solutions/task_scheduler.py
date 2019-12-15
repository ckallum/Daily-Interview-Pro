import heapq
from collections import Counter


def schedule_tasks(tasks, n):
    task_counter = Counter(tasks)
    task_heap = list()
    for task, count in task_counter.items():
        heapq.heappush(task_heap, (-count, task))
    task_count = 0
    for i in range(n):
        priority_queue = list()
        while task_heap:
            count, task = heapq.heappop(task_heap)
            if -count > 1:
                heapq.heappush(task_heap, (count + 1, task))
            task_count += 1
        if not task_heap and not priority_queue:
            break
        task_heap = priority_queue

    return task_count


def main():
    assert (schedule_tasks(['q', 'q', 's', 'q', 'w', 'w'], 4)) == 6


if __name__ == '__main__':
    main()
