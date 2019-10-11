def hops(numbers):
    numbers_dict = {x: False for x in range(len(numbers))}
    numbers_dict[0] = True
    for index, number in enumerate(numbers):
        if numbers_dict[index] == True:
            if index + number in numbers_dict:
                numbers_dict[index + number] = True

    return numbers_dict[len(numbers)-1]


def main():
    assert hops([2, 0, 1, 0])
    assert not hops([1, 1, 0, 1])


if __name__ == '__main__':
    main()
