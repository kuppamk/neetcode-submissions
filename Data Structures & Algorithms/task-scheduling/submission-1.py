class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        freq_heap = [-s for s in counter.values()]
        heapq.heapify(freq_heap)
        queue = deque()

        time =0 
        while freq_heap or queue:
            time += 1
            if freq_heap:
                freq = heapq.heappop(freq_heap)
                freq += 1
                if freq < 0:
                    queue.append((freq, time+n))
            if queue and queue[0][1] == time:
                freq, _ = queue.popleft()
                heapq.heappush(freq_heap, freq)
        return time
