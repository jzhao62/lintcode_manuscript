class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start = 0
        end = len(nums) - 1

        p1 = -1
        p2 = -1

        if not nums:
            return [p1, p2]

        # find right bound

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= target:
                start = mid
            else:
                end = mid

                # finding the right bound, so end will override start

        if nums[start] == target:
            p2 = start

        if nums[end] == target:
            p2 = end

        start = 0
        end = len(nums) - 1

        # find left bound

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] >= target:
                end = mid
            else:
                start = mid

                # finding the left bound, so start will override end
        if nums[end] == target:
            p1 = end

        if nums[start] == target:
            p1 = start

        return [p1, p2]



