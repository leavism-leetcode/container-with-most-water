# Copy/paste template from LeetCode below
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        big = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            big = max(big, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1

        return big

# After copy/pasting the template from LeetCode, uncomment the following to start testing.
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))

