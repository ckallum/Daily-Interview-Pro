def sum_binary(bin1, bin2):
    carry = 0
    result = ""
    index = 0
    bin1, bin2 = bin1[::-1], bin2[::-1]
    while index < len(bin1) or index < len(bin2):
        if index < len(bin1):
            carry += ord(bin1[index]) - ord('0')
        if index < len(bin2):
            carry += ord(bin2[index]) - ord('0')
        result = str(carry % 2) + result
        carry //= 2
        index += 1
    if carry == 1:
        result = '1' + result
    print(result)
    return result


def main():
    assert sum_binary("11101", "1011") == "101000"


if __name__ == '__main__':
    main()
