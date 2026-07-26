class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}    # key : val
        freq = [[] for i in range(len(nums)+1)]      

        for n in nums:                      # create map
           count[n] = 1 + count.get(n, 0)  

        for n, c in count.items():          # create freq list
            freq[c].append(n)               

        result = []
        for i in range(len(freq) - 1, 0, -1):  # iterate high → low frequency
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
