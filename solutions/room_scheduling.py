def room_scheduling(times):
    start = [(time[0], "start") for time in times]
    end = [(time[1], "end") for time in times]
    sorted_times = start + end
    sorted_times = sorted(sorted_times, key=get_key)
    print(sorted_times)
    count = 0
    max_count = 0
    for time in sorted_times:
        if time[1] == "end":
            count -= 1
        else:
            count += 1
        if count > max_count:
            max_count = count
    return max_count


def get_key(item):
    return item[0]


def main():
    assert room_scheduling([(30, 75), (0, 50), (60, 150)]) == 2


if __name__ == '__main__':
    main()
