def first_missing_positive(nums):

    seen = set(nums)
    n = 1
    while n in seen:
        n += 1
    return n


tests = [
    ([0, -2, 1, 2], 3),
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),
    ([], 1),
    ([1, 1, 2, 2], 3),
]

for nums, expected in tests:
    result = first_missing_positive(nums)
    assert result == expected, f"Echec sur {nums}: {result} au lieu de {expected}"
    print(nums, "->", result)


