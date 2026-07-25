class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        prevMap1 = {} # key : val
        prevMap2 = {} # key : val
        if len(s) == len(t):
            # create dictionary for s
            for char in s:
                if char in prevMap1:
                    prevMap1[char] += 1
                else:
                    prevMap1[char] = 1
            # create dictionary for t
            for char in t:
                if char in prevMap2:
                    prevMap2[char] += 1
                else:
                    prevMap2[char] = 1
            if prevMap1 == prevMap2: return True
            else: return False
        else:
            return False
            
        
        
    