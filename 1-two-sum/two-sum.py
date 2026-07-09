class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        res = 0
        for i, n in enumerate(nums):

            res = target - n

            if res in seen:
                return [seen[res],i]

            seen[n] = i
