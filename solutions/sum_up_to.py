class ListFastSum:
    def __init__(self, nums):
        self.nums = nums
        self.index_sums = []
        for num in nums:
            if not self.index_sums:
                self.index_sums.append(num)
            else:
                self.index_sums.append(num + self.index_sums[-1])

    def sum(self, start_idx, end_idx):
        return self.index_sums[end_idx - 1] - self.index_sums[start_idx - 1]


def main():
    assert (ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5)) == 12


if __name__ == '__main__':
    main()
