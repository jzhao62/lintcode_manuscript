class Solution:
    """
    @param: stk: an integer stack
    @return: void
    """
    def stack_sorting(self, stk):
        # 保证stk_2是单调递减
        stk_2 = []
        while stk:
            # 首先分离stk顶的数字
            curr_top = stk.pop()

            # 如果stk top > stk_2 top, 那么把 stk_2 top 拿回来
            while stk_2 and curr_top > stk_2[-1]:
                stk.append(stk_2.pop())

            # 上面那个while loop保证 stk_2 append的正确性

            stk_2.append(curr_top)


        # 区别在这里，不能new 一个 stk
        while stk_2:
            stk.append(stk_2.pop())






stack = [4,2,1,3]


x = Solution().stackSorting(stack)

