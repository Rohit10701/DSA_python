def maxProfit( prices):
        
        mn=10000000000
        profit=0
        for i in range(len(prices)):
            if mn>prices[i]:
                mn=prices[i]
            if prices[i]-mn>profit:
                profit=prices[i]-mn
        return profit
        

print(maxProfit([7,6,4,3,1]))