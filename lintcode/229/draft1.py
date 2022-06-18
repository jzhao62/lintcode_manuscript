class Solution:
    """
    @param: stk: an integer stack
    @return: void
    """
    def stack_sorting(self, stk):
        stk_2 = []
        while stk:
            curr_top = stk.pop()
            while stk_2 and curr_top > stk_2[-1]:
                stk.append(stk_2.pop())

            stk_2.append(curr_top)

        stk = stk_2[::-1]






stack = [4,2,1,3]


x = Solution().stackSorting(stack)

