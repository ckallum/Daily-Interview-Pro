def version_compare(v1, v2):
    if v1.count(".") != v2.count("."):
        return 0

    v1 = list("".join(list(v1.split("."))))
    v2 = list("".join(list(v2.split("."))))
    val1 = None
    val2 = None
    while v1 and v2:
        prev1 = val1
        prev2 = val2
        val1 = v1.pop(0)
        while prev1 == "0" and val1 == prev1:
            prev1 = val1
            val1 = v1.pop(0)
        val2 = v2.pop(0)
        while prev2 == "0" and val2 == prev2:
            prev2 = val2
            val2 = v2.pop(0)

        if val1 > val2:
            return 1
        elif val2 > val1:
            return -1
    if v1:
        return 1
    if v2:
        return -1

    return 0


def main():
    # assert version_compare("1.0.33", "1.0.27") == 1
    # assert version_compare("0.1", "1.1") == -1
    assert version_compare("1.001", "1.01") == 0
    assert version_compare("1.327", "1.32") == 1
    assert version_compare("1.0.0.0", "1.0.0") == 0


if __name__ == '__main__':
    main()
