# a=input()
# af=a.split(' ')
# b=input()
# bf=b.split(' ')
# c=input()
# cf=c.split(' ')
# n=af[0]
# m=af[1]
# s=int(bf[0])
# for i in range(1,n):
#     temp=int(bf[i])
#     bf[i]=temp+s
#     s+=temp  

# for j in cf:
#     bf.append(int(j))
def max_video_games(n, m, prices, budgets):
    max_games = [0] * m
    total_price = 0

    # Calculate the cumulative sum of prices
    cumulative_prices =[sum(prices[:i + 1]) for i in range(n)]
    print(cumulative_prices)

    for i in range(m):
        budget = budgets[i]
        if budget < prices[0]:
            max_games[i] = 0
        else:
            # Use binary search to find the maximum affordable games
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if cumulative_prices[mid] <= budget:
                    total_price = cumulative_prices[mid]
                    low = mid + 1
                else:
                    high = mid - 1
            max_games[i] = low

    return max_games

# Input
n, m = map(int, input().split())
prices = list(map(int, input().split()))
budgets = list(map(int, input().split()))

# Output
result = max_video_games(n, m, prices, budgets)
print(*result)








    




