class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        for strng in strs:
            idx = [0]*27
            for char in strng:
                idx[ord(char)-ord('a')] += 1
            idx = tuple(idx)
            group_dict[idx].append(strng)
        return list(group_dict.values())     