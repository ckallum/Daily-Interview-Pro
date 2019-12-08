def convert_to_int(string):
    if not string:
        return None
    is_neg = string[0] == '-'
    result = 0
    for char in string:
        char += int(char)
        char *= 10
    return -(result) if is_neg else result


def main():
    assert convert_to_int('-105') + 1 == -104


if __name__ == '__main__':
    main()
