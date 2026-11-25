from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #brute force
        #check every substring of length s1 - intuition is that if there is a smaller substring
        #that is a permutation, we return true. This takes O(n) time
        #checking if something IS a permutation, time - k!, because 
        
        #fixed size sliding window
        char_diff = Counter(s1)
        l = 0
        print(char_diff)
        #state should maintain whether current sub-string is a permutation of s1 

        #hashmap can maintain the difference between s1 and curr substring instead? 
        #when its empty, means that the counts and characters are the same. 
        for r in range(len(s2)):
            #updated state
            char_diff[s2[r]] = char_diff.get(s2[r], 0) - 1
            if char_diff[s2[r]] == 0:
                char_diff.pop(s2[r])

            #fixed size window
            if r - l + 1 == len(s1):
                if len(char_diff) == 0:
                    return True

                char_diff[s2[l]] += 1
                if char_diff[s2[l]] == 0:
                    char_diff.pop(s2[l])
                l+=1

        return False 