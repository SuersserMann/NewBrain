from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        neighbors = defaultdict(set)
        results = defaultdict(dict)
        n = len(equations)
        for i in range(n):
            equ = equations[i]
            a, b = equ[0], equ[1]
            neighbors[a].add(b)
            neighbors[b].add(a)
            results[a][b] = values[i]
            results[b][a] = 1 / values[i]

        def bfs(start, end):
            if start not in neighbors:
                return -1.0
            q = deque([(start, 1)])
            seen = set()
            seen.add(start)
            while q:
                node, v = q.popleft()
                if node == end:
                    return v
                for x in neighbors[node]:
                    if x not in seen:
                        # v = start / node
                        # k = node / x
                        # start / x = v * k
                        q.append((x, v * results[node][x]))
                        seen.add(x)
            return -1.0

        ans = []
        for q in queries:
            ans.append(bfs(q[0], q[1]))
        return ans


s = Solution()
equations = [["a", "b"], ["e", "f"], ["b", "e"]]
values = [3.4, 1.4, 2.3]
queries = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
print(s.calcEquation(equations, values, queries))
