def is_valid(string):
    for sub in string.split("."):
        if len(sub) > 3 or int(sub) < 0 or int(sub) > 255:
            return False
        if len(sub) > 1 and int(sub) == 0:
            return False
        if len(sub) > 1 and int(sub) != 0 and int(sub[0]) == 0:
            return False
    return True


def generate_ip(string):
    temp = string
    result = []
    for i in range(1, len(string) - 2):
        for j in range(i + 1, len(string) - 1):
            for k in range(j + 1, len(string)):
                temp = temp[:k] + "." + temp[k:]
                temp = temp[:j] + "." + temp[j:]
                temp = temp[:i] + "." + temp[i:]
                if is_valid(temp):
                    result.append(temp)
                temp = string

    return result


def main():
    assert generate_ip('1592551013') == ['159.255.101.3', '159.255.10.13']
