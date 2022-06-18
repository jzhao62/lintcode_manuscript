from typing import (
    List,
)

class Solution:
    def eval_r_p_n(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()
                val = 0
                if char == '+':
                    val = num1 + num2

                if char == '-':
                    val = num1 - num2

                if char == '*':
                    val = num1 * num2

                if char == '/':
                    val = num1 // num2
                stack.append(val)
            else:
                stack.append(int(char))

        return stack[0]




tokens = ["2", "1", "+", "3", "*"]

x = Solution().eval_r_p_n(tokens)

print(x)
