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

                # 题目要求的，别问
                if char == '/':
                    val = int(num1 / num2)
                stack.append(val)
            else:
                stack.append(int(char))

        return stack[0]




tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


x = Solution().eval_r_p_n(tokens)

print(x)
