def find_primes(n):
    primes = [True] * (n)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            t = i * 2
            while t < n:
                primes[t] = False
                t += i
    ps = []
    for i, b in enumerate(primes):
        if b:
            ps.append(i)
    print(ps)
    return ps


def main():
    assert find_primes(14) == [2, 3, 5, 7, 11, 13]


if __name__ == '__main__':
    main()
