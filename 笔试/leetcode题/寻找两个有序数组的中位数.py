class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1 + nums2

        d = len(c)

        def findk(x):
            i = 0
            j = 0
            while 1:
                if i < len(nums1) and j < len(nums2):
                    if nums1[i] < nums2[j]:
                        if i + j == x:
                            return nums1[i]
                        i += 1
                    else:
                        if i + j == x:
                            return nums2[j]
                        j += 1
                elif i < len(nums1) and j >= len(nums2):
                    return nums1[x - j]
                elif i >= len(nums1) and j < len(nums2):
                    return nums2[x - i]

        if d % 2 == 1:
            d = (d - 1) // 2
            return findk(d)
        else:
            a = d // 2
            b = (d - 2) // 2
            return (findk(a) + findk(b)) / 2
