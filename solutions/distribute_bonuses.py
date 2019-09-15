def get_bonuses(performances):
    bonus_list = []
    current_bonus = 1
    for index, performance in enumerate(performances):
        if index - 1 >= 0:
            if performance > performances[index - 1]:
                current_bonus += 1
        if index+1 < len(performances):
            if performance > performances[index + 1]:
                current_bonus += 1
        bonus_list.append(current_bonus)
        current_bonus = 1

    return bonus_list


def main():
    assert get_bonuses([1, 2, 3, 2, 3, 5, 1]) == [1, 2, 3, 1, 2, 3, 1]


if __name__ == '__main__':
    main()
