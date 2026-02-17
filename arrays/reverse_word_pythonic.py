class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])[::-1]


# Example usage:
solution = Solution()
input_str = "Let's take LeetCode contest"
output = solution.reverseWords(input_str)

assert (
    output == "s'teL ekat edoCteeL tsetnoc"
), f"Expected 's'teL ekat edoCteeL tsetnoc', got {output}"
