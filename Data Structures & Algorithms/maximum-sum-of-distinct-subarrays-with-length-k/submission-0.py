class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # go from 0 to nums-k 
        #build a hasmap of numbers in the window, so we don't repeat
        max_sum = 0 
        curr_sum = 0 
        l = 0
        window_nums = {}
        #if len nums = 3, k = 1, we want i to go from 0 to 2
        for r in range(len(nums)):
            curr_sum += nums[r]
            window_nums[nums[r]] = window_nums.get(nums[r], 0) + 1

            if(r - l + 1 == k):
                # if no dupes
                if len(window_nums) == k:
                    max_sum = max(max_sum, curr_sum)

                #start moving the left pointer once we're at size k
                curr_sum -= nums[l]
                window_nums[nums[l]] = window_nums.get(nums[l]) - 1
                if window_nums.get(nums[l]) == 0:
                    window_nums.pop(nums[l])
                l += 1

        return max_sum
                
