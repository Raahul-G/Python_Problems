class Solution:
    def canJump(self, nums: List[int]) -> bool:
        Jump = 0
        for i in range(len(nums)-1):
            Jump = max(Jump, i + nums[i])
            if i == Jump and nums[Jump] == 0:
                return False
        return True