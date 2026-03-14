class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        """
        Problem: Given a string, find the length of the longest substring where each character appears at most twice.

        How it works: Use a sliding window with a frequency dictionary. Iterate through the string with pointer p1,
        incrementing the count for each character. If a character's count exceeds 2, move pointer p2 from the left
        to reduce the count until it's <=2. Update the maximum length as p1 - p2 + 1.
        """
        max_len = 0
        p2 = 0
        freq = {}

        for p1, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1

            while freq[char] > 2:
                freq[s[p2]] -= 1
                p2 += 1

            max_len = max(max_len, p1 - p2 + 1)

        return max_len


# Test cases
solution = Solution()
# Empty string
assert solution.maximumLengthSubstring("") == 0

# Single character
assert solution.maximumLengthSubstring("a") == 1

# All unique
assert solution.maximumLengthSubstring("abc") == 3

# Two same
assert solution.maximumLengthSubstring("aab") == 3

# Three same
assert solution.maximumLengthSubstring("aaab") == 3

# Mixed
assert solution.maximumLengthSubstring("abcabc") == 6

# All same
assert solution.maximumLengthSubstring("aaa") == 2
