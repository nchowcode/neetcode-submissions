from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sorter(word: str) -> str:
            return ''.join(sorted(word))

        hashmap = defaultdict(list)
        
        # each sublist have same key identifier when sorted chars
        for word in strs:
            key = sorter(word)
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key].append(word)
        return list(hashmap.values())