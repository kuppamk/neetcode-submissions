class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for ele in nums:
            freq_dict[ele] += 1
        print(freq_dict)
        output = []
        for key, value in freq_dict.items():
            heapq.heappush(output, (value, key))
            if len(output) > k:
                heapq.heappop(output)
        print(output)
        final = []
        for key, value in output:
            final.append(value)
        print(final)
        return final
        
        