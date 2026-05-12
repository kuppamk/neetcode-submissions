class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_heap = [(-value, key) for key, value in counter.items()]
        heapq.heapify(max_heap)
        if (-max_heap[0][0]) > (len(s)+1)//2:
            return ""
        prev_count, prev_char = 0, ""
        output = []
        while max_heap:
            count, char = heapq.heappop(max_heap)
            output.append(char)
            count += 1
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            prev_count, prev_char = count, char
        return "".join(output) if len(output) == len(s) else ""

        