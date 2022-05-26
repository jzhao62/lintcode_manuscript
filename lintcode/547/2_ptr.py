class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i, j = 0, 0

        output_set = set()

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                output_set.add(nums1[i])
                i += 1
                j += 1
        return list(output_set)