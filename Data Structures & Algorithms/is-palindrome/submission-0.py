class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnumStr = ""
        for chars in s:
            if chars.lower().isalnum():
                alnumStr += chars.lower()
        
        left = 0
        right = len(alnumStr) - 1

        while right > left:
            if alnumStr[left] != alnumStr[right]:
                return False
            left += 1
            right -= 1
        return True