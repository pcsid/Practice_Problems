#we have prices[]
prices = [100, 180, 260, 310, 40, 535, 695]
prices = [100, 180, 100, 180]
   # Expected profit: 160 (buy at 100, sell at 180, buy at 100, sell at 180)
def traverseCalc(prices):
    profit = 0
    for day in range(len(prices)):
        if day + 1 != len(prices):
            if prices[day] < prices[day + 1]:
                profit += prices[day + 1] - prices[day]
    print(profit)
'''
def minMaxCalc(prices):
    profit = 0
    locMin = 0
    locMax = 0
    day = 0
    while day < len(prices):
        while prices[day] < prices[day + 1]:
            day += 1
        if day 
'''
traverseCalc(prices)