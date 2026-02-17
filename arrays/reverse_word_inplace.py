class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        l = len(s)

        start = 0

        for end in range(l + 1):
            if end == l or chars[end] == " ":
                self.reverse(chars, start, end - 1)
                start = end + 1

        return "".join(chars)

    def reverse(self, chars, start, end):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1


# Example usage:
solution = Solution()
input_str = "Let's take LeetCode contest"
output = solution.reverseWords(input_str)

assert (
    output == "s'teL ekat edoCteeL tsetnoc"
), f"Expected 's'teL ekat edoCteeL tsetnoc', got {output}"
