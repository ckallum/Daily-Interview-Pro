def convert(string):
    result = 0
    string_to_val_dict = {"I": 1,
                          "IV": 4,
                          "V": 5,
                          "IX": 9,
                          "X": 10,
                          "XL": 40,
                          "L": 50,
                          "XC": 90,
                          "C": 100,
                          "CD": 400,
                          "D": 500,
                          "CM": 900,
                          "M": 1000
                          }
    index = len(string)-1
    while index > -1:
        if index > 0:
            if string[index - 1] + string[index] in string_to_val_dict:
                result += string_to_val_dict[string[index - 1] + string[index]]
                index -= 1
            else:
                result += string_to_val_dict[string[index]]
        else:
            result += string_to_val_dict[string[index]]
        index -= 1
    return result


def main():
    assert convert("IX") == 9
    assert convert("VII") == 7
    assert convert("MCMIV") == 1904
    assert convert("MCMX") == 1910


if __name__ == '__main__':
    main()
