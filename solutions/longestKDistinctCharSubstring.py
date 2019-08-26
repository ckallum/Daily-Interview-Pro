from collections import deque


def longest_substring_with_k_distinct_characters(string, k):
    char_dict = dict()
    current_sub_string = deque()
    largest_substring = ""
    for char in string:
        current_sub_string.append(char)
        try:
            char_dict[char] += 1
        except:
            char_dict[char] = 1
        while not is_valid(char_dict, k):
            char_dict[current_sub_string.popleft()] -= 1
        if len(current_sub_string) > len(largest_substring):
            largest_substring = "".join(list(current_sub_string))
    return largest_substring


def is_valid(char_count, k):
    count = 0
    for char in char_count:
        if char_count[char] > 0:
            count += 1
    if count > k:
        return False
    return True


def main():
    assert longest_substring_with_k_distinct_characters("aabcdefff", 3) == "defff"


if __name__ == '__main__':
    main()
