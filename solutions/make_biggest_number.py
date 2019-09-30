from functools import cmp_to_key


def compare_nums(a, b):
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    # 1 str1>str -1 = str2>str1, 0 = equal
    return (str1 > str2) - (str2 > str1)


def make_biggest_number(numbers):
    numbers = sorted(numbers, key=cmp_to_key(compare_nums), reverse=True)
    numbers = list(map(lambda x: str(x), numbers))
    print("".join(numbers))
    return "".join(numbers)


def main():
    assert make_biggest_number([7, 72, 17, 2, 45]) == "77245217"


if __name__ == '__main__':
    main()
