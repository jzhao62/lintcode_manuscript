class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        set_one = set(nums1)

        set_two = set()

        for n in nums2:
            if n in set_one:
                set_two.add(n)
        return list(set_two)