class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, cur_combination, remaining):
            if remaining < 0:
                return
            elif remaining == 0:
                res.append(cur_combination.copy())
                return
            
            for i in range(start, len(nums)):
                cur_combination.append(nums[i])
                backtrack(i, cur_combination, remaining - nums[i])
                cur_combination.pop()

        backtrack(0, [], target)
        return res