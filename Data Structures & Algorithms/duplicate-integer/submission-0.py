class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable = {} 
        for num in nums:
            if hashTable.get(num): 
                return True
            hashTable[num] = 1
        return False