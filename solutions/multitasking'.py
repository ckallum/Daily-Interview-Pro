from cmath import inf


def time_to_complete(tasks, cooldown):
    total_time = 0
    task_dict = {}
    for task in tasks:
        if task in task_dict:
            if total_time - task_dict[task] <= cooldown:
                total_time = cooldown + task_dict[task] + 1
        task_dict[task] = total_time
        total_time += 1
    print(total_time)
    return total_time


def main():
    assert time_to_complete([1, 1, 2, 1], 2) == 7


if __name__ == '__main__':
    main()
