class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        n = len(nums)

        total_reverse = True

        # how to iterate from a range backward ?

        for i in range(n - 2, -1, -1):

            # found the first smaller element at i
            if nums[i] < nums[i + 1]:
                for j in range(n - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[j], nums[i] = nums[i], nums[j]
                        nums[i + 1:] = sorted(nums[i + 1:])
                        total_reverse = False
                        break;
                # no need to consider the end of this loop,(True, buyt you have to consider break the outer loop)
                # the look has to stop once it finds the first smaller element, otherwise it will go on the 2nd, etc
                break

        # what is the difference between sorted and sort ?

        if total_reverse:
            nums.sort();





