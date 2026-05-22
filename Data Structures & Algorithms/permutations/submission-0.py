class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        cur_permutation = []
        visited = set()

        def dfs():
            if len(nums) == len(cur_permutation):
                permutations.append(cur_permutation.copy())
                return
            for num in nums:
                if num in visited:
                    continue
                cur_permutation.append(num)
                visited.add(num)
                dfs()
                _ = cur_permutation.pop()
                visited.remove(num)
        
        dfs()
        return permutations
