class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = []
        top_freq = 0
        #Initialize a hashmap of counts - maps elements to counts 
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > top_freq:
                top_freq = counts.get(num, 0)
        #Has to be at least one distinct element, so top_freq staying 0 isn't an issue
        buckets = [[] for _ in range(top_freq + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
            

        for bucket in reversed(buckets):
            for num in bucket:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
                

        