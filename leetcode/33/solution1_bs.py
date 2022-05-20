class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[start] <= nums[mid]:

                # PUT the target in the middle of this condition, it will simplify the logic
                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid

            # right side
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1

