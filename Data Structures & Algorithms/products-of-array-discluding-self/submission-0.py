class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        suffix_product = []
        cur_product = 1
        result = []
        for num in nums:
            prefix_product.append(cur_product)
            cur_product *= num
        cur_product = 1
        for num in reversed(nums):
            suffix_product.insert(0, cur_product)
            cur_product *= num
        print(prefix_product)
        print(suffix_product)
        for i in range(len(nums)):
            result.append(prefix_product[i] * suffix_product[i])
        return result