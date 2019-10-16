def shortest_path(file_path):
    path_list = file_path.split('/')[1:]
    min_path = ['/']
    while path_list:
        name = path_list.pop(0)
        if name == '..':
            min_path.pop()
        elif name and name != '.':
            min_path.append(name+'/')

    return "".join(min_path) if min_path else None


def main():
    assert shortest_path('/Users/Joma/Documents/../Desktop/./../') == '/Users/Joma/'


if __name__ == '__main__':
    main()