class Solution:

    def remove_kdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            if num[i] != '0' or len(stack) > 0:
                stack.append(num[i])

        while len(stack) > 0 and k > 0:
            stack.pop()
            k -= 1
        return ''.join(stack).lstrip('0') or "0"