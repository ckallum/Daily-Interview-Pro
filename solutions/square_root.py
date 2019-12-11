def sqrt(x):
    low = 0
    high = x
    while high - low > 0.001:
        mid = (high + low) / 2
        if abs(mid ** 2 - x) < 0.0001:
            return mid
        if mid ** 2 > x:
            high = mid
        elif mid ** 2 < x:
            low = mid
    return round((high+low)/2, 3)


def main():
    assert sqrt(5) == 2.236


if __name__ == '__main__':
    main()
