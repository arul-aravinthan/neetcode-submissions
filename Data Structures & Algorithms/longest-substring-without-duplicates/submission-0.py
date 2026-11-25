class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = {}
        max_len = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            #if less chars in our hashmap than in our substring, means duplicates
            while len(chars) < len(s[l:r + 1]):
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    chars.pop(s[l])
                l+=1
            max_len = max(max_len, len(s[l:r + 1]))
            #shrink until valid 
        return max_len
