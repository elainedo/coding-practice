class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = defaultdict(int)

        for i, n in enumerate(nums):
            if target - n in dct:
                return [i, dct[target - n]]
            dct[n] = i

        return []