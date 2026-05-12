class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        current_cap = 0
        min_heap = []
        for cap, src, des in trips:
            while min_heap and min_heap[0][0] <= src:
                _, drop_cap = heapq.heappop(min_heap)
                current_cap -= drop_cap
            
            if current_cap + cap > capacity:
                return False
            heapq.heappush(min_heap, (des, cap))
            current_cap += cap
        return True

        