def multiply(num1, num2):
    result = 0
    multiplier = 1
    while num2:
        current = 0
        for num in num1:
            current *= 10
            current += (int(num2[-1]) * int(num))
        result += current * multiplier
        multiplier *= 10
        num2 = num2[:-1]
    return str(result)


def add_num(result, num, power):
    carry = 0
    i = 0

    while i < len(num):
        if i + power >= len(result):
            result.append(0)

        result[i + power] += num[i] + carry
        if result[i + power] > 9:
            carry = 1
            result[i + power] -= 10
        else:
            carry = 0

        i += 1


def multiply_digit(str1, mult_digit):
    if str1 == '0' or mult_digit == '0':
        return [0]

    mult_digit = ord(mult_digit) - ord('0')
    result = []

    carry = 0
    for digit in str1[::-1]:
        digit_product = (ord(digit) - ord('0')) * mult_digit
        result.append(digit_product % 10 + carry)

        carry = digit_product // 10

    if carry > 0:
        result.append(carry)

    return result


def multiply2(str1, str2):
    result = []
    for power, digit in enumerate(str2[::-1]):
        add_num(result, multiply_digit(str1, digit), power)

    return ''.join(map(str, result[::-1]))


def main():
    assert multiply("11", "13") == "143"
    assert multiply2("11", "13") == "143"


if __name__ == '__main__':
    main()
