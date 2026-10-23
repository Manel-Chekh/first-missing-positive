import re
import sys


def first_missing_positive(nums):
    # The answer is always between 1 and len(nums) + 1
    seen = set(nums)
    n = 1
    while n in seen:
        n += 1
    return n


def parse_numbers(text):
    # Accepts "0 -2 1 2", "0, -2, 1, 2" or "[0, -2, 1, 2]"
    return [int(x) for x in re.findall(r"-?\d+", text)]


def run_tests():
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
        assert result == expected, f"Failed on {nums}: got {result}, expected {expected}"
        print(nums, "->", result)
    print("All tests pass")


def main():
    print("First Missing Positive")
    print("Type an array of integers, for example: 0 -2 1 2  or  [3, 4, -1, 1]")
    print("Type q to quit.\n")
    while True:
        text = input("Array: ").strip()
        if text.lower() in ("q", "quit", "exit"):
            break
        nums = parse_numbers(text)
        print("Result:", first_missing_positive(nums), "\n")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        main()
