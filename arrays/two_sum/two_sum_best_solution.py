class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Problem: Given an array of integers and a target integer, return the indices of the two numbers
        that add up to the target. Each input has exactly one solution, and the same element cannot be
        used twice. The answer can be returned in any order.

        How it works: Use a hash map (dictionary) to store each number's index as we iterate through
        the array. For each element, calculate the complement (target - current number) and check if it
        already exists in the hash map. If it does, we found the pair and return their indices. If not,
        store the current number and its index in the hash map for future lookups. This reduces the time
        complexity from O(n²) to O(n) by trading space for time. Space complexity is O(n).
        """
        numbers = {}

        for idx, number in enumerate(nums):
            if (target - number) in numbers:
                return [numbers[target - number], idx]

            numbers[number] = idx

# Test cases
solution = Solution()

# size 2 — minimum valid input
assert solution.twoSum([2, 7], 9) == [0, 1]
assert solution.twoSum([1, 5], 6) == [0, 1]

# target is sum of first and last elements
assert solution.twoSum([3, 2, 4], 6) == [1, 2]
assert solution.twoSum([1, 2, 3, 4], 5) == [1, 2]

# negative numbers
assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
assert solution.twoSum([-3, 4, 3, 90], 0) == [0, 2]

# mixed positive and negative
assert solution.twoSum([-10, 7, 19, 15], 9) == [0, 2]

# zeros in the array
assert solution.twoSum([0, 4, 3, 0], 0) == [0, 3]

# large numbers
assert solution.twoSum([1000000, 500000, 500000], 1000000) == [1, 2]

# duplicates — should find the correct pair
assert solution.twoSum([3, 3], 6) == [0, 1]
assert solution.twoSum([5, 5, 11], 10) == [0, 1]

# target from non-adjacent elements
assert solution.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17) == [7, 8]

# LeetCode original examples
assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert solution.twoSum([3, 2, 4], 6) == [1, 2]
assert solution.twoSum([3, 3], 6) == [0, 1]
