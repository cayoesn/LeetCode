class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Problem: Given a sorted array of integers and a target value, find the index of the target in the array.
        If the target is not found, return -1.

        How it works: This is a binary search algorithm. It uses two pointers, p1 (start) and p2 (end),
        to repeatedly divide the search space in half. Calculate the middle index, compare the middle element
        with the target, and adjust the pointers to narrow down the search until the target is found or the
        search space is empty. Uses bit shifting (>> 1) for efficient integer division by 2.
        """
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            # Bit Shift Right (deslocamento à direita):
            # - O operador `>> n` desloca os bits para a direita n posições.
            # - Numericamente, para inteiros não-negativos, `x >> n` é equivalente a `x // (2**n)`.
            # - Logo, usar `(p1 + p2) >> 1` é uma forma rápida de calcular a média inteira
            #   (floor) de `p1` e `p2` — mesma ideia que `(p1 + p2) // 2`.
            # - Cuidado: em linguagens com overflow (C/C++, Java) somar `p1 + p2`
            #   pode estourar; alternativa segura é `p1 + ((p2 - p1) >> 1)` ou
            #   `p1 + (p2 - p1) // 2`.
            # - Em Python não há overflow de inteiros, e `>>` funciona como esperado.
            # Use deslocamento por 1 para dividir por 2 (não por 2 posições):
            mid = (p1 + p2) >> 1

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                p1 = mid + 1
            else:
                p2 = mid - 1

        return -1


# Test cases
solution = Solution()
# size 0
assert solution.search([], 1) == -1

# size 1
assert solution.search([5], 5) == 0
assert solution.search([5], 0) == -1

# size 2
assert solution.search([0, 5], 5) == 1
assert solution.search([0, 5], 0) == 0
assert solution.search([0, 5], 3) == -1

# size 3
assert solution.search([1, 2, 3], 2) == 1
assert solution.search([1, 2, 3], 4) == -1

# size 4
assert solution.search([1, 3, 5, 7], 7) == 3
assert solution.search([1, 3, 5, 7], 2) == -1

# size 5
assert solution.search([0, 1, 2, 3, 4], 3) == 3
assert solution.search([0, 1, 2, 3, 4], 9) == -1

# original extra tests (size 6)
assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
