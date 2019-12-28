def meeting_rooms(meetings):
    current_rooms = []
    times = sorted([(s, "start") for s, f in meetings] + [(f, "finish") for s, f in meetings])
    result = 0
    for time, t in times:
        if t == "start":
            current_rooms.append(time)
        else:
            current_rooms.pop()
        if len(current_rooms) > result:
            result = len(current_rooms)
    return result


def main():
    assert (meeting_rooms([(0, 10), (10, 20)])) == 1
    assert (meeting_rooms([(20, 30), (10, 21), (0, 50)])) == 3


if __name__ == '__main__':
    main()
