class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        """
        Problem: Given a string, find the length of the longest substring where each character appears at most twice.

        How it works: Use a sliding window approach with two pointers p1 and p2. Maintain a dictionary to count
        character frequencies. Move p1 to expand the window, incrementing the count for the current character.
        If any character count exceeds 2, move p2 to shrink the window from the left until the count is <=2.
        Track the maximum window size (p1 - p2 + 1) during the process.
        """

        if not s:
            return 0

        max_len = 1
        p1, p2 = 0, 0
        len_s = len(s) - 1
        dict_let = {}

        dict_let[s[0]] = 1

        while p1 < len_s:
            p1 += 1
            if dict_let.get(s[p1]):
                dict_let[s[p1]] += 1
            else:
                dict_let[s[p1]] = 1

            while dict_let[s[p1]] > 2:
                if dict_let.get(s[p1]):
                    dict_let[s[p2]] -= 1

                p2 += 1

            max_len = max(max_len, (p1 - p2) + 1)

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
