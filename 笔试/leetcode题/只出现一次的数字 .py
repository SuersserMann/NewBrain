class Solution:
    def singleNumber(self, nums) -> int:
        dic = {}
        res=[]
        for i in nums:
            if i in dic:
                res.remove(i)
            else:
                dic[i] = i
                res.append(i)
        return res[0]