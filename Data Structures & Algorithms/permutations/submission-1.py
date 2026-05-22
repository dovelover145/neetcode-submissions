class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        cur_permutation = []

        def dfs(i):
            if len(nums) == len(cur_permutation):
                permutations.append(cur_permutation[:])
                return
            for j in range(i, len(nums)):
                cur_permutation.append(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)
                _ = cur_permutation.pop()
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0)
        return permutations
