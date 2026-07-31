class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Track, s2Track = [0] * 26, [0] * 26
        
        for i in range(len(s1)):
            s1Track[ord(s1[i]) - ord('a')] += 1
            s2Track[ord(s2[i]) - ord('a')] += 1

        pings = 0

        for i in range(26):
            pings += (1 if s1Track[i] == s2Track[i] else 0)
        

        left = 0
        for right in range(len(s1), len(s2)):
            if pings == 26: return True

            index = ord(s2[right]) - ord('a')
            s2Track[index] += 1
            if s1Track[index] == s2Track[index]:
                pings += 1
            elif s1Track[index] + 1 == s2Track[index]:
                pings -= 1

            index = ord(s2[left]) - ord('a')
            s2Track[index] -= 1
            if s1Track[index] == s2Track[index]:
                pings += 1
            elif s1Track[index] - 1 == s2Track[index]:
                pings -= 1

            left += 1

        return pings == 26
