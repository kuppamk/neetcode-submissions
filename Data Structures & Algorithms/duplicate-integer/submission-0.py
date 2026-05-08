class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        out = set()
        for ele in nums:
            if ele in out:
                return True
            out.add(ele)
        return False
        