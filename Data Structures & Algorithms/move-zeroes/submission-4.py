class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1

        #left holds where our zeros are, right will look for an element to swap (non-zero)
        # [2, 3, 4, 0, 5, 0, 0, 7, 8]
        # [2, 3, 4, 5, 0, 0, 0, 7, 8]
        while r < len(nums) and l < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l] = nums[r]
                nums[r] = 0
                l += 1
                r += 1
                continue
            if nums[l] != 0:
                l += 1
            if nums[r] == 0 or r < l:
                r += 1
