class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftHighest = 0
        rightHighest = len(heights) - 1
        highestArea = min(heights[leftHighest], heights[rightHighest]) * (rightHighest - leftHighest)
        left = leftHighest
        right = rightHighest

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            currArea = min(heights[left], heights[right]) * (right - left)
            if currArea > highestArea:
                highestArea = currArea
        return highestArea