def convert(numerator, denominator):
    if numerator == 0:
        return '0'

    result = ''

    if (numerator < 0 and denominator > 0) or (denominator < 0 and numerator > 0):
        result = '-'

    numerator = abs(numerator)
    denominator = abs(denominator)

    result += str(numerator // denominator)
    remainder = numerator % denominator

    if remainder == 0:
        return result

    result += '.'
    remainder_map = {}

    while remainder > 0:
        if remainder in remainder_map:
            index = remainder_map[remainder]
            result = result[:index]+'('+result[index:]+')'
            break
        remainder_map[remainder] = len(result)
        remainder *= 10
        result += str(remainder // denominator)
        remainder %= denominator
    print(result)
    return result


def main():
    assert convert(-3, 2) == "-1.5"
    assert convert(4, 3) == "1.(3)"
    assert convert(1, 6) == "0.1(6)"


if __name__ == '__main__':
    main()
