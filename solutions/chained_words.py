def chained_words(current_word, remaining_words):
    if not remaining_words:
        return True
    is_chained = False

    for index, word in enumerate(remaining_words):
        if current_word:
            if word[0] == current_word[-1]:
                is_chained = is_chained or chained_words(word, remaining_words[:index] + remaining_words[index + 1:])
        else:
            is_chained = is_chained or chained_words(word, remaining_words[:index] + remaining_words[index + 1:])
    return is_chained


def main():
    assert chained_words(None, ['eggs', 'karat', 'apple', 'snack', 'tuna'])
    assert chained_words(None, ['eggs', 'apple', 'snack', 'tuna'])
    assert not chained_words(None, ['eggs', 'snack', 'tuna'])


if __name__ == '__main__':
    main()
