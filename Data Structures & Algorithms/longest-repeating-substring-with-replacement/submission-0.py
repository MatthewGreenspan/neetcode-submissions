class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freqMap = {}
        left = 0
        maxFreq = 0
        result = 0

        for i in range(len(s)):

            freqMap[s[i]] = freqMap.get(s[i], 0) + 1
            maxFreq = max(maxFreq, freqMap[s[i]])
            
            while ((i - left + 1) - maxFreq) > k:
                freqMap[s[left]] -= 1
                left += 1

            result = max(result, i - left + 1)

        return result



                


