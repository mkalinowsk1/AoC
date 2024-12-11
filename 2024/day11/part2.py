from collections import Counter
with open("2024/inputs/day11.in") as fin:
    stones = list(map(int, fin.read().strip().split(" ")))

def apply_rules(n):
    mul = {}
    splits = {}
    stones_count = Counter(stones)
    for _ in range(1, n+1):
        new_stones_counts = Counter()
        for stone, count in stones_count.items():
            if stone == 0:
                new_stones_counts[1] += count
            elif stone in splits:
                stone1, stone2 = splits[stone]
                new_stones_counts[stone1] += count
                new_stones_counts[stone2] += count
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                splits[stone] = (left, right)
                new_stones_counts[left] += count
                new_stones_counts[right] += count
            elif stone in mul:
                new_stone = mul[stone]
                new_stones_counts[new_stone] += count
            else:
                mult = 2024 * stone
                mul[stone] = mult
                new_stones_counts[mult] += count
        stones_count = new_stones_counts
    return sum([i for i in stones_count.values()])


print(apply_rules(75))
