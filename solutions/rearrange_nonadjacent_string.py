import heapq


def rearrange(string):
    character_count = [(-string.count(char), char) for char in set(string)]
    if any([-count for count, char in character_count]) > (len(string) + 1) / 2:
        return ""
    heapq.heapify(character_count)
    result = ""
    while len(character_count) >= 2:
        count1, char1 = heapq.heappop(character_count)
        count2, char2 = heapq.heappop(character_count)
        result += "{}{}".format(char1, char2)
        if count1 + 1:
            heapq.heappush(character_count, (count1 + 1, char1))
        if count2 + 1:
            heapq.heappush(character_count, (count2 + 1, char2))
    print(result)
    return result


def main():
    assert rearrange("abbccc") == "cbcabc"


if __name__ == '__main__':
    main()
