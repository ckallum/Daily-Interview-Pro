def power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n%2:
        return power(x, n//2) * power(x, (n//2)+1)
    return power(x, n//2) * power(x, n//2)

def main():
    assert power(5, 3) == 125


if __name__ == '__main__':
    main()