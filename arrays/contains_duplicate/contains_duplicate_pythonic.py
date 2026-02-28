class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
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
