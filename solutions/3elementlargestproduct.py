from functools import reduce


def maxproduct(numbers):
    numbers.sort()
    return max(numbers[-1]*numbers[0]*numbers[1], reduce(lambda x, y: x*y, numbers[-3:]))

def main():
    assert maxproduct([-4, -4, 2, 8]) == 128


if __name__ == '__main__':
    main()