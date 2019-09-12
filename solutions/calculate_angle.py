def calculate_angle(hour, minute):
    minute_angle = 6 * minute
    hour_angle = (30 * hour + (30 * (minute/60))) % 360
    print(minute_angle, hour_angle)
    return hour_angle - minute_angle if hour_angle >= minute_angle else minute_angle - hour_angle

# each minute = 0.5 degrees
# hour = 30 degrees
# each rotation = 360 degrees = 720 minutes


def main():
    assert calculate_angle(3, 30) == 75
    assert calculate_angle(12, 30) == 165


if __name__ == '__main__':
    main()
