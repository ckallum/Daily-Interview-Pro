def reverse(words, low, high):
    while high > low:
        words[low], words[high] = words[high], words[low]
        low += 1
        high -= 1
    return words


def reverse_words(s):
    index = 0
    start = 0
    reverse(s, 0, len(s) - 1)
    while index < len(s):
        if s[index] == " ":
            reverse(s, start, index - 1)
            start = index + 1
        index += 1
    reverse(s, start, len(s) - 1)


def main():
    s = list("can you read this")
    reverse_words(s)
    assert (''.join(s)) == "this read you can"


if __name__ == '__main__':
    main()
