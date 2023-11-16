import collections


def canFinish(numCourses, prerequisites):
    dl = [[] for _ in range(numCourses)]
    degree = [0 for _ in range(numCourses)]
    for i in prerequisites:
        dl[i[1]].append(i[0])
        degree[i[0]] += 1
    deque = collections.deque()
    for i in range(numCourses):
        if degree[i] == 0:
            deque.append(i)
    while deque:
        cla = deque.pop()
        numCourses -= 1
        for c in dl[cla]:
            degree[c] -= 1
            if degree[c] == 0:
                deque.append(c)
    return not numCourses


numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(numCourses, prerequisites))
