class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        left, right = 0, len(height) - 1

        maxLeft = height[left]
        maxRight = height[right]
        trappedWater = 0

        while left < right:
       
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                trappedWater += maxLeft - height[left]

            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                trappedWater += maxRight - height[right]

        return trappedWater




  