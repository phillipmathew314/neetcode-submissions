class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            left = 0
            right = len(self.data[key]) - 1

            ind = 0
            while left < right:
                mid = (left + right) // 2
                # print(left, right, mid)
                if self.data[key][mid][0] <= timestamp:
                    left = mid + 1
                else:
                    right = mid
                
                # if ind == 10:
                #     break
                # ind += 1
            
            if self.data[key][left][0] > timestamp:
                if left > 0:
                    return self.data[key][left - 1][1]
                return ""
            return self.data[key][left][1]
        else:
            return ""
