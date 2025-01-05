def is_possible(towels: set[str], design: str) -> bool:
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for towel in towels:
            if design.startswith(towel, i - len(towel)) and dp[i - len(towel)]:
                dp[i] = True
                break

    return dp[n]

def different_combos(towels: set[str], design: str) -> int:
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for towel in towels:
            if design.startswith(towel, i - len(towel)):
                dp[i] += dp[i - len(towel)]

    return dp[n]