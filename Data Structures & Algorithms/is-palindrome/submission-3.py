class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1

        while first < last:
            if not s[first].isalnum(): 
                first += 1
                continue
            if not s[last].isalnum():
                last -=1
                continue
            if s[first].lower() != s[last].lower():
                return False
            first+=1
            last-=1
            

        return True