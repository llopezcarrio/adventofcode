

def find_secret_number(n: int) -> int:
    mod = 16777216
    n = ((n * 64) ^ n) % mod
    n = ((n // 32) ^ n) % mod
    n = ((n * 2048) ^ n) % mod
    return n

def get_prices_and_changes(secret_number: int) -> tuple[list[int], list[int]]:
    last = secret_number
    prices = []
    changes = []
    for _ in range(2000):
        secret_number = find_secret_number(secret_number)
        # Only need to keep last digits
        prices.append(secret_number % 10)
        changes.append(secret_number % 10 - last % 10)
        last = secret_number
    return prices, changes


def get_banana_sequences(
    prices: list[int], changes: list[int]
) -> dict[tuple[int, ...], int]:
    sequences = {}
    for i in range(3, len(changes)):
        seq = tuple(changes[i - 3 : i + 1])
        if sum(seq) > 0 and seq not in sequences:
            # Add price of the last banana in the sequence
            sequences[seq] = prices[i]
    return sequences