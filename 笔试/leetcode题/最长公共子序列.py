text1 = ['a', 'b', 'c', 'd']
text2 = ['a', 'e', 'c', 'd']
cur = 0
dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
for i in range(1, len(text2) + 1):
    for j in range(1, len(text1) + 1):
        if text1[j-1] == text2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp)
