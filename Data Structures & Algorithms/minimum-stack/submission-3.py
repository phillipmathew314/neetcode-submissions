class MinStack:

    def __init__(self):
        self.stack = []
        # self.mins = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        # if not self.mins or self.mins and val <= self.mins[-1]:
        #     self.mins.append(val)
        # self.stack.append(val)
        if not self.stack:
            self.mini = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.mini)
            self.mini = min(self.mini, val)
        # [1,2,1,3, 0]
        # stack = 0, 1, 0, 2, -1
        # min = 0

    def pop(self) -> None:
        # val = self.stack.pop()
        # if val == self.mins[-1]:
        #     self.mins.pop()
        diff = self.stack.pop()
        if diff < 0:
            self.mini -= diff
        

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.mini
        else:
            return self.mini + self.stack[-1]

    def getMin(self) -> int:
        return self.mini
