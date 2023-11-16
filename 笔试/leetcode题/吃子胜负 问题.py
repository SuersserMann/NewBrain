import sys

t = input().split()
t = int(t[0])
result=[]
for z in range(t):
    dp = [[0 for _ in range(3)] for _ in range(3)]
    white = 0
    black = 0
    for i in range(3):
        a = input().split()
        a = a[0]
        for g in range(3):
            dp[i][g] = a[g]
    for i in range(3):
        for c in range(3):
            if i == 1:
                if dp[1][c] == '*':
                    if dp[0][c] == 'o' and dp[2][c] == 'o':
                        white += 1
                if dp[1][c] == 'o':
                    if dp[0][c] == '*' and dp[2][c] == '*':
                        black += 1
            if c == 1:
                if dp[i][1] == '*':
                    if dp[i][0] == 'o' and dp[i][2] == 'o':
                        white += 1
                if dp[i][1] == 'o':
                    if dp[i][0] == '*' and dp[i][2] == '*':
                        black += 1

            

    if white>=1 and black==0:
     result.append('yukari')
    elif black>=1 and white==0:
     result.append('kou')
    else:
     result.append('draw')
for i in result:
 print(i)
