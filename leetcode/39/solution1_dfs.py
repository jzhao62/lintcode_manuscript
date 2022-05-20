class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        output = []

        # reduce duplicate

        candidates = sorted(list(set(candidates)))

        self.dfs(candidates, target, [], 0, output)

        return output

    def dfs(self, candidates, target, curr_path, idx, output):

        if target < 0:
            return

        if target == 0:
            # you have to append the copy of the array, instead of the array itself, otherwise it will keep mutating in the output

            # why this reduce run time ??
            return output.append(list(curr_path))

        for i in range(idx, len(candidates)):
            # this soaks up computational run time ?

            # if i != 0 and candidates[i] == candidates[i-1]:
            #     continue

            curr_path.append(candidates[i])

            self.dfs(candidates, target - candidates[i], curr_path, i, output)

            curr_path.pop();


s = Solution()

s.combinationSum([2, 3, 6, 7], 7)
