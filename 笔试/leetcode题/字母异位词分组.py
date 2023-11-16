class Solution:
    def groupAnagrams(self, strs):
        if len(strs)<=1:
            return [strs]
        else:
            dic={}
            for i in strs:
                s=str(sorted(i))
                if s not in dic:
                    dic[s]=[i]
                else:
                    dic[s].append(i)
        res=[]
        for item in dic:
            res.append(dic[item])
        return res