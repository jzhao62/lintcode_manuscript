from typing import (
    List,
)

class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
             we will sort your return value in output
    """
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for item in sorted(strs):
            sortedItem = ''.join(sorted(item))
            dic[sortedItem] = dic.get(sortedItem, []) + [item]
        return dic.values()



input = ["eat","tea","tan","ate","nat","bat"]


Solution().group_anagrams(input)