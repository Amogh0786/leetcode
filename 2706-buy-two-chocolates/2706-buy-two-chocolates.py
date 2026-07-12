class Solution(object):
    def buyChoco(self, prices, money):
        n=len(prices)
        for i in range(0,n,1):
            for j in range(0,n-i-1,1):
                if prices[j]>prices[j+1]:
                    prices[j],prices[j+1]=prices[j+1],prices[j]
        print(prices)
        if money-(prices[0]+prices[1])>=0:
            return money-(prices[0]+prices[1])
        else:
            return money