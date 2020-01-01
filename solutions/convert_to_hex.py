def to_hex(n):
    hex_map = "0123456789ABCDEF"
    result = ""
    while n > 0:
        result += hex_map[n % 16]
        n //= 16
    return result[::-1]


# Fill this in.
def main():
    assert (to_hex(123)) == "7B"


if __name__ == '__main__':
    main()
