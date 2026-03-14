class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Problem: Given a string, reverse each word in the string while keeping the order of the words unchanged.
        Words are separated by spaces.

        How it works: Split the string into a list of words. Reverse the order of the words in the list.
        Join the reversed list back into a string with spaces. Then, reverse the entire string, which effectively
        reverses each individual word while maintaining the word order.
        """
        return " ".join(s.split()[::-1])[::-1]


# Example usage:
solution = Solution()
input_str = "Let's take LeetCode contest"
output = solution.reverseWords(input_str)

assert (
    output == "s'teL ekat edoCteeL tsetnoc"
), f"Expected 's'teL ekat edoCteeL tsetnoc', got {output}"
