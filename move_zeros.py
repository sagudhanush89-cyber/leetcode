class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
         nums = [0,1,0,3,12]
         lastNonZeroFoundAt = 0
         for i in range(len(nums)):
          if nums[i] != 0:
            nums[lastNonZeroFoundAt] = nums[i]
            lastNonZeroFoundAt += 1
         for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0