class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1、找出所有字母 出现次数，并按出现次数降序排列
        ls = sorted(collections.Counter(tasks).values(), reverse=True)

        # 2、找出最大次数, 有几个字母同时出现最大次数
        # 3、返回结果
        return max(sum(ls), (ls[0] - 1) * (n + 1) + ls.count(ls[0]))
