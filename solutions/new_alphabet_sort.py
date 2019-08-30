def isSorted(words, order):
    char_index_dict = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        first = words[i]
        second = words[i + 1]
        for k in range(min(len(first), len(second))):
            if first[k] != second[k]:
                if char_index_dict[first[k]] > char_index_dict[second[k]]:
                    return False
                break
        if len(first) > len(second):
            return False
    return True


# Fill this in.


def main():
    assert not isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba")
    # False
    assert isSorted(["zyx", "zyxw", "zyxwy"],
                    "zyxwvutsrqponmlkjihgfedcba")

    assert not isSorted(["abcde", "abcd"], "zyxwvutsrqponmlkjihgfedcba")


if __name__ == '__main__':
    main()
