class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.time_map[key]
        if len(lst) == 0:
            return ""
        
        left = 0
        right = len(lst) - 1

        while left <= right:
            mid = (left + right) // 2
            if lst[mid][-1] == timestamp:
                return lst[mid][0]
            elif lst[mid][-1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        if lst[left-1][-1] < timestamp:
            return lst[left-1][0]
    
        return ""




'''
TC: 
    init - O(1)
    set - O(1) amortized (appending to a Python list) 
    get - O(logK) where K is the number of entries for that specific key

SC: O(N) where N is the total number of set calls (all stored [value, timestamp] pairs across all keys)



'''