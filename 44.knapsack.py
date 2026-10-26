def knapsack(values, weights, W):
 n = len(values)
 dp = [[0]*(W+1) for _ in range(n+1)]
 for i in range(1, n+1):
    for w in range(W+1):
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] +
values[i-1])
 else:
    dp[i][w] = dp[i-1][w]
 return dp[n][W]
# Example
vals = [60, 100, 120]
wts = [10, 20, 30]
W = 50
print(knapsack(vals, wts, W))