class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: the least number of operations and make the two strings equal
    并查集
    """

    def editDistance(self, s1, s2):
        father = {c: c for c in 'abcdefghijklmnopqrstuvwxyz'}
        def find(x):
            print(x, father)
            if x == father[x]:
                return father[x]
            else:
                return find(father[x])

        res, le = 0, len(s1)
        for i in range(le):
            fa = find(s1[i])
            fb = find(s2[i])
            if fa != fb:
                res += 1
                father[fa] = fb
        return res


s1 = "abb"
s2 = "dad"

output = Solution().editDistance(s1, s2);

print(output)



