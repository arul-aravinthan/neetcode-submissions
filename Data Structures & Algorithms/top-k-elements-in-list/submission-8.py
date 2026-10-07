class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = []
        top_freq = 0
        #Initialize a hashmap of counts - maps elements to counts 
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts.get(num, 0) > top_freq:
                top_freq = counts.get(num, 0)
        #Has to be at least one distinct element, so top_freq staying 0 isn't an issue
        buckets = [[] for _ in range(top_freq + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
            

        while len(top_k) < k:
            num_same_freq = len(buckets[-1])
            print(buckets[-1], num_same_freq)
            if num_same_freq == 0:
                buckets.pop()
                continue
            elif num_same_freq == 1:
                top_k.append(buckets[-1][0])
                buckets.pop()
            #More than 1
            else:
                top_k.append(buckets[-1].pop())
        return top_k
        