import numpy as np


class Solution:
    def trap(self, height):
        if len(height) <= 1:
            return 0
        pre = np.array(height)
        pre_idx = np.argsort(pre)[::-1]
        idx = {}
        res = 0
        l = min(pre_idx[0], pre_idx[1])
        r = max(pre_idx[0], pre_idx[1])
        idx[pre_idx[0]]=pre_idx[0]
        idx[pre_idx[1]]=pre_idx[1]
        ml = l
        mr = r
        step = 2
        while len(idx) < len(height):
            xx = 0
            for i in range(l + 1, r):
                idx[i]=i
                xx += pre[i]

            res += (r - l - 1) * min(pre[l], pre[r]) - xx

            for i in pre_idx[step:]:
                if i not in idx:
                    if i < ml:
                        step += 1
                        idx[i]=i
                        r = ml
                        ml = i
                        l = i
                        break

                    else:
                        step += 1
                        idx[i]=i
                        l = mr
                        mr = i
                        r = i
                        break
        return int(res)


s = Solution()
print(s.trap([4,2,0,3,2,5]))
