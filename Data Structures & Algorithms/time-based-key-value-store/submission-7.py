class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])
        # print(self.time_map)
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.time_map[key]
        # print("Looking for", timestamp)
        if len(lst) == 0:
            return ""
        
        left = 0
        right = len(lst) - 1

        while left <= right:
            mid = (left + right) // 2
            # print("*"*50)
            # print(f'Left={left}, right={right}, mid={mid}')
            # print("Mid value", lst[mid][-1])
            if lst[mid][-1] == timestamp:
                return lst[mid][0]
            elif lst[mid][-1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        # print("Left========",left)
        if lst[left-1][-1] < timestamp:
            return lst[left-1][0]
    
        return ""




'''
init
    for this, we can use a defaultdict of lists that basically maps a key to a list of tuples?


    {
    "alice": [("happy", 1), ("sad", 3)]
    "bob": [("tired", 2), ("angry", 3)]
    "sam": [("hungry", 1), ("gloomy", 2),("drowsy", 4), ("crying", 7)]
    }



set
    append to the end of the list of a given key with (value, timestamp)
    we do not have to worry about sorting the list bevause the timestamps are strictly increasing 

    supposed we have our hashmap

    {
    "alice": [("happy", 1), ("sad", 3)]
    "bob": [("tired", 2), ("angry", 3)]
    "sam": [("hungry", 1), ("gloomy", 2), ("drowsy", 4), ("crying", 7)]
    }


get










["TimeMap", "set", ["key1", "value1", 10], "get", ["key1", 1], "get", ["key1", 10], "get", ["key1", 11]]


{
 "key1": [["value1", 10]]

}


left = 0
right = -1







["TimeMap", "set", ["test", "one", 10], "set", ["test", "two", 20], "set", ["test", "three", 30], "get", ["test", 15], "get", ["test", 25], "get", ["test", 35]]

{
    "test": [["one", 10], ["two", 20], ["three", 30]]
}

"get", ["test", 15]





'''