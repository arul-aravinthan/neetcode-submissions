class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            #Don't want repeat calcs for duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Do two pointers
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return output