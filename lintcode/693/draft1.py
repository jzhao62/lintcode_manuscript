class Solution:
    def remove_kdigits(self, num: str, k: int) -> str:
        stack = []

        quota = k

        for c in num:
            # quota > 0
            while stack and quota > 0 and int(c) < int(stack[-1]):
                stack.pop()
                quota -= 1

            stack.append(c)

        while quota > 0 and stack:
            stack.pop()
            quota -= 1

        return "".join(stack)




num = "1432219"
k = 3


x = Solution().remove_kdigits(num, k)

print(x)