class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num_dict.get(num) == None:
                num_dict[num] = True
            else:
                return True
        return False