class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i, nums in enumerate(nums):
            bal = target - nums
            if bal in dict1:
                return [dict1[bal], i]
            else:
                dict1[nums] = i