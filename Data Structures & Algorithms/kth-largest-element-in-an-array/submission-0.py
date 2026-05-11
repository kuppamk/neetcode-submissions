class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pqueue = []
        for ele in nums:
            heapq.heappush(pqueue, ele)
            if len(pqueue) > k:
                heapq.heappop(pqueue)
        return pqueue[0]
        