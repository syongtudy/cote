#합이 0나오는 3개 정수
#stl combination 쓰는방법, 이분탐색으로 2개합 먼저구하고 이거랑 더해서 0되는 숫자 구하는 방법, 투포인터방법
#투포인터가 제일 시간복잡도 낮을듯
# import bisect

# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         n = len(nums)
#         output = []
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 two = nums[i]+nums[j]
#                 idx = bisect.bisect_left(nums,-two,lo=j+1)
#                 if idx<n and nums[idx]+two==0:
#                     output.append((nums[i],nums[j],nums[idx]))   #튜플로 append하면 2차원이라도 set 바로 먹힘 
#         ans = list(set(output))
#         return ans
#이분탐색 존나 느려
# s= Solution()
# print(s.threeSum([-1,0,1,2,-1,-4]))



# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         output = set()
#         for _ in range(len(nums)-2):
#             ans3 = nums.pop()
#             st,en =0,len(nums)-1
#             sum_3 = nums[st]+nums[en]+ans3
            
#             while st<en<len(nums):
#                 if sum_3 > 0:
#                     sum_3 += nums[en-1] - nums[en]
#                     en -= 1
#                 elif sum_3 < 0:
#                     sum_3 += nums[st+1] - nums[st]
#                     st += 1
#                 else:
#                     output.add((nums[st],nums[en],ans3))
#                     sum_3 += nums[en-1] - nums[en] + nums[st+1] - nums[st]
#                     st +=1
#                     en -=1
                    
#         return list(output)
# s= Solution()
# print(s.threeSum([-1,0,1,2,-1,-4]))

#투포인터 이 방식도 그렇게 빠르지 않은듯? 한개 먼저 빼내고O(N) x 나머지 두개찾기 O(N)

class Solution:
    def threeSum(self, nums):
        nums.sort()
        output = []
        for i,ans1 in enumerate(nums):  
            if i>0 and nums[i-1]==ans1: continue    #첫번째 숫자의 중복을 거르는 곳 
            st,en =i+1,len(nums)-1
            if st<en<len(nums):
                sum_3 = ans1 + nums[st]+nums[en]
            
            while st<en<len(nums):
                if sum_3 > 0:
                    sum_3 += nums[en-1] - nums[en]
                    en -= 1
                elif sum_3 < 0:
                    sum_3 += nums[st+1] - nums[st]
                    st += 1
                else:
                    output.append([ans1,nums[st],nums[en]])
                    sum_3 += nums[en-1] - nums[en]
                    en -= 1
                    while nums[en] == nums[en+1] and st<en: #세번째 숫자의 중복을 거르는곳 
                        sum_3 += nums[en-1] - nums[en]
                        en -= 1
        return output

s= Solution()
print(s.threeSum([-2,-2,0,0,2,2]))

#마지막 방식을 쓰면 애초에 set 자료형 없이 중복된 값을 보지 않아도 되서 빨라짐