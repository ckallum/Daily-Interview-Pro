def string_compression(string):
    count = 1
    current_char = string[1]
    result = []
    for char in string[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.extend([current_char, str(count)])
            else:
                result.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        result.extend([current_char, str(count)])
    else:
        result.append(current_char)
    print(result)
    return result


def main():
    assert string_compression(['a', 'a', 'b', 'c', 'c', 'c']) == ['a', '2', 'b', 'c', '3']


if __name__ == '__main__':
    main()
