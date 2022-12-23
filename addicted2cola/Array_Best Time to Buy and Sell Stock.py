class Solution:
    def maxProfit(self, prices):
        d = [[0,prices[0]]]
        for i in range(1,len(prices)):
            d.append([max(d[i-1][0],prices[i]-d[i-1][1]),min(d[i-1][1],prices[i])])
        return(d[-1][0])


# s = Solution()
# print(s.maxProfit([7,1,5,3,6,4]))
# print(s.maxProfit([7,6,4,3,1]))




# class Solution:
#     def maxProfit(self, prices):
#         d= [0]
#         for i in range(1,len(prices)):
#             d.append(d[i-1])
#             if prices[i] > prices[i-1]:
#                 for j in range(i):
#                     d[i] = max(d[i],prices[i]-prices[j])
#         return d[-1]

#prices의 갯수가 10^5개인데 O(N^2)걸려서 시간초과뜨는듯?
#leetcode는 시간제한 안나옴?