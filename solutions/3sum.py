def three_sum(numbers):
    numbers = numbers.sort()
    triplet_set = set()

    for i in range(len(numbers) - 2):
        j = i + 1
        k = len(numbers) - 1
        while j < k:
            current_triplet = [numbers[i], numbers[j], numbers[k]]
            if numbers[i] + numbers[j] + numbers[k] == 0:
                if current_triplet not in triplet_set:
                    triplet_set.add(current_triplet)
                j += 1
                k -= 1
            elif numbers[i] + numbers[j] + numbers[k] < sum:
                j += 1
            else:
                k -= 1
    return list(triplet_set)


def main():
    assert three_sum([1, -2, 1, 0, 5]) == [[1, -2, 1]]
    assert three_sum([0, -1, 2, -3, 1]) == [[0, -1, 1], [2, -3, 1]]
    assert three_sum([-3, 3, 2, -2, -4, 1]) == [[-4, 3, 1], [2, 1, -3]]
