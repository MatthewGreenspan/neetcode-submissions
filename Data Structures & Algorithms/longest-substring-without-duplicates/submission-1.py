class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        left, right = 0, 0
        maxLength = 0

        while right < len(s):
            
            if s[right] not in subset:
                subset.add(s[right])
                maxLength = max(maxLength, right - left + 1)
                right += 1

            else:
                subset.remove(s[left])
                left += 1

        return maxLength
            
            
            
            
            
            

           