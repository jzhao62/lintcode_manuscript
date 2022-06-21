from typing import (
    Set,
)

class Solution:
    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    def word_break(self, s: str, word_set: Set[str]) -> bool:
        n = len(s)

        dp = [False] * (n+1)


        # 预先留一个0 号位，set to True
        dp[0] = True


        for i in range(1, n+1):
            for w in word_set:
                if dp[i-len(w)] and s[i-len(w): i] == w:
                    dp[i] = True
                    break;

        return dp[-1]




s = "lintcode"
dict = ["lint", "code"]