from collections import defaultdict


def sum_combinations(nums, target):
    num_hash = defaultdict(list)
    for i, num in enumerate(nums):
        for j in range(num, target + 1):
            if j - num in num_hash:
                for partial in num_hash[j - num]:
                    if i not in partial:
                        num_hash[j].append(partial + [i])
        num_hash[num].append([i])
    for partial in num_hash[target]:
        for i, j in enumerate(partial):
            partial[i] = nums[j]
    print(num_hash[target])
    return num_hash[target]


def recursive(nums, target, results, current, index):
    if target == 0:
        results.add(current)
        return
    if target < 0:
        return
    for i in range(index, len(nums)):
        recursive(nums, target - nums[i], results, (*current, nums[i]), i + 1)


def recursive_sol(nums, target):
    results = set()
    nums.sort()
    recursive(nums, target, results, (), 0)
    return list(results)


def main():
    # assert sum_combinations([10, 1, 2, 7, 6, 1, 5], 8) == [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]
    print(recursive_sol([10, 1, 2, 7, 6, 1, 5], 8))


if __name__ == '__main__':
    main()
