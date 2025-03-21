from heapq import *
class MedianFinder(object):

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
            

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0]-self.small[0]) / 2.0
        else:
            return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]

commands = ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "addNum", "addNum","findMedian"]
values = [[], [41], [35], [62], [5], [97],[108], []]

# Initialize MedianFinder object
medianFinder = None
results = []

for i, command in enumerate(commands):
    if command == "MedianFinder":
        medianFinder = MedianFinder()
        results.append(None)  # Constructor does not return anything
    elif command == "addNum":
        medianFinder.addNum(values[i][0])
        results.append(None)  # addNum does not return anything
    elif command == "findMedian":
        results.append(medianFinder.findMedian())

print(results) 