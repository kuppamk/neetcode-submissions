class MedianFinder:

    def __init__(self):
        self.max_heap =[]
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        # Balance
        bal = len(self.max_heap) - len(self.min_heap)
        if bal > 1:
            ele = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, ele)
        elif bal < 0:
            ele = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -ele)
        

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0])/2
        else:
            return -self.max_heap[0]
        
        