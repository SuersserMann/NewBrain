import collections


# 这是一个解决拓扑排序的典型算法，其解法是从入度为0为初始栈，每次去除掉一个入度为0的课，同时更新和它相关的出度的课的入度，如果为0则添加进栈
# 如果删去的栈的数量和原始相等，则代表无环
# 不要把变量的名字写的太抽象
class Solution:
    def canFinish(self, numCourses, prerequisites):
        dic = collections.defaultdict(list)
        in_edge = [0] * numCourses
        dq = collections.deque()
        for i in range(len(prerequisites)):
            dic[prerequisites[i][0]].append(prerequisites[i][1])
            in_edge[prerequisites[i][1]] += 1
        for i in range(numCourses):
            if in_edge[i] == 0:
                dq.append(i)
        if not dq:
            return False
        res = 0
        while dq:
            cur = dq.popleft()
            out_edge = dic[cur]
            for j in range(len(out_edge)):
                in_edge[out_edge[j]] -= 1
                if in_edge[out_edge[j]] == 0:
                    dq.append(out_edge[j])
            res += 1
        if res == numCourses:
            return True
        else:
            return False


s = Solution()
numCourses = 5
prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
print(s.canFinish(numCourses, prerequisites))
