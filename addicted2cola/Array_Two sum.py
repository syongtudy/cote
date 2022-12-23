class Solution:
    def twoSum(self, nums, target: int):
        C={}    #딕셔너리가 탐색속도가 훨씬 빠름
        for i in range(len(nums)):  #O(N)
            if nums[i] in C:    #딕셔너리에 키가 있는지 확인 O(1)
                return([C[nums[i]],i])
            else:
                C[target-nums[i]] = i   #키값 삽입도 O(1)

#총 O(N), 이중 for문 O(N^2)보다 빠름

# s = Solution()
# print(s.twoSum([2,7,11,15],9))
# print(s.twoSum([3,2,4],6))
# print(s.twoSum([3,3],6))