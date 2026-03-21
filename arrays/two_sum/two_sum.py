class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Problem: Given an array of integers and a target integer, return the indices of the two numbers
        that add up to the target. Each input has exactly one solution, and the same element cannot be
        used twice. The answer can be returned in any order.

        How it works: Use a brute force approach with two nested loops. The outer loop iterates through
        each element, while the inner loop checks every other element to see if the pair sums to the
        target. The condition id1 != id2 ensures we don't use the same element twice. Time complexity
        is O(n²) and space complexity is O(1).
        """
        for id1, number1 in enumerate(nums):
            for id2, number2 in enumerate(nums):
                if number1 + number2 == target and id1 != id2:
                    return [id1, id2]


# Test cases
solution = Solution()

# size 2 — minimum valid input
assert solution.twoSum([2, 7], 9) == [0, 1]
assert solution.twoSum([1, 5], 6) == [0, 1]

# target is sum of first and last elements
assert solution.twoSum([3, 2, 4], 6) == [1, 2]
assert solution.twoSum([1, 2, 3, 4], 5) == [0, 3]

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
