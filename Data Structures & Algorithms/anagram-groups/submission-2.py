from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # buckets of anagrams in their original form
        # bucket cat = [act, cat, tac...]

        # sort the str, make that a key, store the unsorted version into list, return list of hashmap values

        # o(n) mem, o(n) time

        hashmap = defaultdict(list)

        for word in strs:
            # key = word.sorted()
            sortedKey = "".join(sorted(word))
            hashmap[sortedKey].append(word)

        # return list(hashmap.values())
        return list(hashmap.values())