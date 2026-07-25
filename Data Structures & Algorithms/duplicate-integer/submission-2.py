class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {}
        for i, n in enumerate(nums):
            if n in prevMap:
                return True
            else:
                prevMap[n] = i
        return False