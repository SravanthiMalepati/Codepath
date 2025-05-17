import random
from collections import Counter
class Solution:
    def __init__(self, w):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        l, r = 0, len(self.prefix) - 1
        while l < r:
            mid = (l + r ) // 2
            if self.prefix[mid] < target:
                l =  mid + 1
            else:
                r = mid 
        return l


# s = Solution([1, 3, 2])
# results = [s.pickIndex() for _ in range(10)]


# print(Counter(results))

calls = ["Solution", "pickIndex", "pickIndex", "pickIndex","pickIndex","pickIndex"]
inputs = [[[1, 3]], [], [], [], [], []]
output = []

for call, args in zip(calls, inputs):
    if call == "Solution":
        s = Solution(*args)
        output.append(None)
    elif call == "pickIndex":
        output.append(s.pickIndex())

print(output)

