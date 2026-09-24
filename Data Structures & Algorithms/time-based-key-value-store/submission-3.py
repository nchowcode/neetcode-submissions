from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        values = self.hashmap[key]

        l = 0
        r = len(values) - 1
        result = ""
        # bsearch through sorted list by values[0]
        while l <= r:
            middle = (l + r) // 2

            currTimestamp = values[middle][0]
            # [1,2,_3_,4,5] goal: 5
            if currTimestamp <= timestamp:
                result = values[middle][1]
                l = middle + 1
            else:
                r = middle - 1


        return result
        
