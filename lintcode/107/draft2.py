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
        dp[0] = True


        max_length = max(len(w) for w in word_set) if word_set else 0

        for i in range(1, n+1):
            for l in range(1, max_length + 1):
                if dp[i-l] and s[i-l: l] in word_set:
                    dp[i] = True;
                    break;
        return dp[-1]




s = "lintcode"
dict = ["lint", "code"]