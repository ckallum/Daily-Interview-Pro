from cmath import inf


def make_change(coins, n):
    dp_coins = {x: inf for x in range(n + 1)}
    dp_coins[0] = 0
    for coin in coins:
        dp_coins[coin] = 1
        for i in range(coin+1, n + 1):
            if dp_coins[i-coin]:
                dp_coins[i] = min(dp_coins[i - coin] + 1, dp_coins[i])

    return dp_coins[n]


def naive_make_change(coins, n):
    if n == 0:
        return 0
    min_coins = inf
    for coin in coins:
        if n - coin >= 0:
            min_coins = min(min_coins, 1+naive_make_change(coins, n-coin))
    return min_coins


# Fill this in.
def main():
    assert (make_change([1, 5, 10, 25], 36)) == 3
    assert (naive_make_change([1, 5, 10, 25], 36)) == 3


if __name__ == '__main__':
    main()
