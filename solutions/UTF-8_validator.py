BYTE_MASKS = [
    None,
    0b10000000,
    0b11100000,
    0b11110000,
    0b11111000,
]
BYTE_EQUAL = [
    None,
    0b00000000,
    0b11000000,
    0b11100000,
    0b11110000,
]


def utf8_validator(b):
    if len(b) > 4 or len(b) == 0:
        return False
    if b[0] & BYTE_MASKS[len(b)] != BYTE_EQUAL[len(b)]:
        return False
        # if len(b) > 1:
    for bs in b[1:]:
        if bs & 10000000 != 10000000:
            return False
    return True


def main():
    assert utf8_validator([0b00000000])
    # True
    assert not utf8_validator([0b00000000, 10000000])
    # False
    assert utf8_validator([0b11000000, 10000000])


# True


if __name__ == '__main__':
    main()
