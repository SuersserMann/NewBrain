
nums1=[1,3]
nums2=[2,4]

def findMedianSortedArrays(nums1, nums2):
    c = nums1 + nums2
    c = sorted(c)
    d = len(c)

    if d % 2 == 0:
        x1=int(d / 2 - 1)
        x2=int(d / 2 )
        result = float(c[x1] + c[x2]) / 2
    else:
        x3=int((d+1)/ 2-1)
        result = float(c[x3])
    return result
print(findMedianSortedArrays(nums1, nums2))
