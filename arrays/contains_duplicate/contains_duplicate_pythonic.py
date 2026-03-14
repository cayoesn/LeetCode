class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Problem: Given an array of integers and an integer k, check if there are two identical elements
        in the array that are at most k indices apart.

        How it works: Use a dictionary to store the most recent index of each number encountered.
        For each element in the array, check if it already exists in the dictionary and if the difference
        between the current index and the stored index is less than or equal to k. If yes, return True.
        Update the dictionary with the current index for the number. If no duplicates are found within
        the range, return False.
        """
        dic = {}

        for i, number in enumerate(nums):
            if number in dic and (i - dic[number]) <= k:
                return True
            dic[number] = i

        return False


# Example usage:
solution = Solution()
assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1) == True
assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
