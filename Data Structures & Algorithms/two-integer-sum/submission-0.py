class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in index_dict:
                return [index_dict[nums[i]], i]
            index_dict[target-nums[i]] = i
        return []
        