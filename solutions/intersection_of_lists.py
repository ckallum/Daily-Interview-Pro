def intersection(list1, list2, list3):
    i, j, k = 0, 0, 0
    results = []
    while i < len(list1) and j < len(list2) and k < len(list3):
        if list1[i] == list2[j] == list3[k]:
            results.append(list1[i])
            i += 1
            j += 1
            k += 1
        else:
            max_num = max(list1[i], list2[j], list3[k])
            if list1[i] < max_num:
                i += 1
            if list2[j] < max_num:
                j += 1
            if list3[k] < max_num:
                k += 1
    print(results)
    return results


# Fill this in.
def main():
    assert intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]) == [4]


# [4]


if __name__ == '__main__':
    main()
