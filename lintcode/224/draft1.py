class Solution:

    def delete_char(self, str, k):
        mono_stack = []
        # 计算允许删除的quota
        allow_to_delete = len(str) - k
        for c in str:
            # 如果quota有存量，当前字符串比stack top小
            while mono_stack and allow_to_delete > 0 and c < mono_stack[-1]:
                # 踢掉，更新quota
                mono_stack.pop()
                allow_to_delete -= 1
            # 保证mono increasing
            mono_stack.append(c)


        # 把quota用完
        while allow_to_delete > 0 and mono_stack:
            mono_stack.pop()
            allow_to_delete -= 1
        return "".join(mono_stack)


str = "fskacsbi"
k = 2

s = Solution().delete_char(str, k)

print(s)
