from enum import Enum


class Char(Enum):
    START = 0
    FIRSTNEGATIVE = 1
    SECONDNEGATIVE = 2
    FIRSTDIGIT = 3
    SECONDDIGIT = 4
    THIRDDIGIT = 5
    DECIMAL = 6
    E = 7


match_char_to_state = {
    Char.START: lambda x: True,
    Char.FIRSTNEGATIVE: lambda x: x == '-',
    Char.FIRSTDIGIT: lambda x: x.isdigit(),
    Char.DECIMAL: lambda x: x == '.',
    Char.SECONDDIGIT: lambda x: x.isdigit(),
    Char.E: lambda x: x == 'e',
    Char.SECONDNEGATIVE: lambda x: x == '-',
    Char.THIRDDIGIT: lambda x: x.isdigit()
}
fsm = {
    Char.START: [Char.FIRSTDIGIT, Char.FIRSTNEGATIVE],
    Char.FIRSTDIGIT: [Char.FIRSTDIGIT, Char.DECIMAL, Char.E],
    Char.FIRSTNEGATIVE: [Char.FIRSTDIGIT, Char.DECIMAL],
    Char.DECIMAL: [Char.SECONDDIGIT],
    Char.SECONDDIGIT: [Char.SECONDDIGIT, Char.E],
    Char.E: [Char.SECONDNEGATIVE, Char.THIRDDIGIT],
    Char.SECONDNEGATIVE: [Char.THIRDDIGIT],
    Char.THIRDDIGIT: [Char.THIRDDIGIT]
}


def is_valid_number(number):
    state = Char.START
    for ch in number:
        next_state = False
        for n in fsm[state]:
            if match_char_to_state[n](ch):
                next_state = True
                state = n
                break
        if not next_state:
            return False
    return state in [Char.FIRSTDIGIT, Char.SECONDDIGIT, Char.THIRDDIGIT]


def strip_neg(num):
    if num[0] != '-':
        return num
    elif len(num) > 0:
        return num[1:]


def helper(num, is_dec):
    if not num:
        return True
    if (is_dec and num[0] == '.') or (not num[0].isdigit() and num[0] != '.'):
        return False
    if num[0] == '.':
        return helper(num[1:], True)
    else:
        return helper(num[1:], False)


def is_valid_number2(number):
    split_num = number.split('e')
    if len(split_num) > 2:
        return False
    if len(split_num) == 2:
        num1 = strip_neg(split_num[0])
        num2 = strip_neg(split_num[1])
        return num1 and num2 and helper(num1, False) and helper(num2, False)
    else:
        num = strip_neg(number)
        return helper(num, False) and num


def main():
    assert is_valid_number("10")
    assert is_valid_number("-10")
    assert is_valid_number("10.1")
    assert is_valid_number("-10.1")
    assert is_valid_number("1e5")
    assert is_valid_number("-5")
    assert is_valid_number("1e-5")
    assert not is_valid_number("1e-5.2")
    assert not is_valid_number("a")
    assert not is_valid_number("x 1")
    assert not is_valid_number("a -2")
    assert not is_valid_number("-")
    assert is_valid_number2("10")
    assert is_valid_number2("-10")
    assert is_valid_number2("10.1")
    assert is_valid_number2("-10.1")
    assert is_valid_number2("1e5")
    assert is_valid_number2("-5")
    assert is_valid_number2("1e-5")


if __name__ == '__main__':
    main()
