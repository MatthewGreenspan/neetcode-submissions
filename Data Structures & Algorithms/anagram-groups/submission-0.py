class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevMap = {}                        # key : val
        for n in strs:
            sortedStr= ''.join(sorted(n))
            if sortedStr not in prevMap:
                prevMap[sortedStr] = []
            prevMap[sortedStr].append(n)
        return list(prevMap.values())
