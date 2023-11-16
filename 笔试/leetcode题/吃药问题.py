na = input().split()
na = int(na[0])
n = input().split()
n = [int(i) for i in n]
m = input().split()
m = int(m[0])
dp = [[0 for _ in range(na)] for _ in range(2 * m)]
for i in range(2 * m):
    c = input().split()
    c = [int(i) for i in c]
    for g in range(na):
        dp[i][g] = c[g]
q = input().split()
q = int(q[0])

def test(q):
    d = n
    for i in range(2 * q):
        if i % 2 == 0:
            for g in range(na):
                if dp[i][g] == d[g] == 1:
                    d[g] = 0
        else:
            for g in range(na):
                if dp[i][g] == 1:
                    d[g] = 1
    c = 0
    for x in d:
        if x == 1:
            c += 1
    return c


result = []
for x in range(q):
    xx = input().split()
    xx = int(xx[0])
    result.append(test(xx))
for i in result:
    print(i)
