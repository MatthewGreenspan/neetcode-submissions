class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = {}, {}

        # Create hashmap
        for c in t:
            countT[c] = 1 + countT.get(c, 0)       

        # need is the size of unique characters in T
        have, need = 0, len(countT)                        
        result, resultLength = [-1, -1], float("infinity")
        l = 0

         # iterate through s
        for r in range(len(s)):                    
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            # if character is even in countT and they values equal each other   
            if char in countT and window[char] == countT[char]:  
                have += 1
            
            while have == need:
                #update result
                if (r - l + 1) < resultLength:
                    result = [l, r]
                    resultLength = (r - l + 1)
                #pop from left
                window[s[l]] -= 1
                #if by removing a character you made the count less than what it needed to be
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        return s[l: r + 1] if resultLength != float("infinity") else ""