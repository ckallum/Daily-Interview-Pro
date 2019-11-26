import time

lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}
validWords = ['dog', 'fish', 'cat', 'fog']


def naive(phone):
    results = []
    for i in range(len(phone)):
        for char in lettersMaps[int(phone[i])]:
            if not results:
                results.append(char)
            else:
                length = len(results)
                for res in results:
                    results.append(res + char)
                results = results[length:]
    results = [word for word in results if word in validWords]
    print(results)
    return results


def makeWords(phone):
    results = []
    for char in lettersMaps[int(phone[0])]:
        # if char in [x[0] for x in validWords]:
        util(results, char, phone[1:])
    return results


def util(results, current, phone):
    if not phone:
        if current in validWords:
            results.append(current)
        return
    for char in lettersMaps[int(phone[0])]:
        # if char in [x[len(current)] for x in validWords]:
        util(results, current + char, phone[1:])
    return


def main():
    start_time = time.time()
    assert makeWords('364') == ['dog', 'fog']
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
