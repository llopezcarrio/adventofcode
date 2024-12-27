from collections import defaultdict

initStones = "3028 78 973951 5146801 5 0 23533 857"

stones =  initStones.split(" ")

def get_new_stone(stone):
    if stone == "0":
        return ["1"]

    if (l := len(stone)) % 2 == 0:
        cut_line = l // 2
        return [str(int(new_stone)) for new_stone in (stone[:cut_line], stone[cut_line:])]

    return [str(int(stone) * 2024)]


listStones: dict[str, int] = {k: 1 for k in stones}
assert len(listStones) == len(stones)

for _ in range(75):
    new_stones = defaultdict(int)
    for stone, num in listStones.items():
        for new_stone in get_new_stone(stone):
            new_stones[new_stone] += num
    listStones = new_stones



print(sum(listStones.values()))
