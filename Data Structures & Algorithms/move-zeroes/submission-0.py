class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1

        #left holds where our zeros are, right will look for an element to swap 
        while r < len(nums):
            if nums[l] != 0:
                l += 1
                r = l + 1
            elif nums[l] == 0 and nums[r] != 0:
                nums[l] = nums[r]
                nums[r] = 0
                l += 1
                r = l + 1
            elif nums[l] == 0 and nums[r] == 0:
                r += 1