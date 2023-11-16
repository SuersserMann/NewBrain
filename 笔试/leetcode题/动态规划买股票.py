# def maxProfit(prices):
#     max = 0
#     for i in range(len(prices)):
#         price = prices[i]
#         for g in prices[i:]:
#             result = g - price
#             if result >= max:
#                 max = result
#     if max < 0:
#         return 0
#     else:
#         return max
#
#
# prices = [7, 6, 4, 3, 1]
# print(maxProfit(prices))

def maxProfit(prices):
    dp = [0 for _ in range(len(prices))]
    min_price = prices[0]
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i - 1], prices[i] - min_price)
    return dp[-1]


prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
