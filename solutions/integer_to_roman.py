def convert(integer):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return thousands[integer // 1000 % 10] + hundreds[integer // 100 % 10] + tens[integer // 10 % 10] + ones[
        integer % 10]
    # I   1
    # V   5
    # X   10
    # L   50
    # C   100
    # D   500
    # M   1000


def main():
    assert convert(1000) == "M"
    assert convert(48) == "XLVIII"
    assert convert(444) == "CDXLIV"


if __name__ == '__main__':
    main()
