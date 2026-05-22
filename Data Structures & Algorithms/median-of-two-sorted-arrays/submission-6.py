class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def binary_search(nums1: List[int], nums2: List[int]) -> float:
            m, n = len(nums1), len(nums2)

            if m > n: # Ensure that we're doing binary search on the smaller list to avoid complicated boundaries
                m, n = n, m
                nums1, nums2 = nums2, nums1
                # return findMedianSortedArrays(nums2, nums1)
            
            l, r = 0, m
            while l <= r:
                m1 = l + (r - l) // 2
                m2 = (m + n + 1) // 2 - m1 # The "+ 1" is for odd numbers; we want our left partition to have 1 extra element in that case
            
                l1 = float('-inf') if m1 == 0 else nums1[m1 - 1]
                r1 = float('inf') if m1 == m else nums1[m1]

                l2 = float('-inf') if m2 == 0 else nums2[m2 - 1]
                r2 = float('inf') if m2 == n else nums2[m2]

                if l1 <= r2 and l2 <= r1:
                    if (n + m) % 2 == 0:
                        return (max(l1, l2) + min(r1, r2)) / 2
                    else:
                        return max(l1, l2)
                
                if l1 > r2:
                    r = m1 - 1
                else:
                    l = m1 + 1
        
            return 0.0
        
        def dumb_brute_force(nums1: List[int], nums2: List[int]) -> float:
            nums = sorted(nums1 + nums2)
            n = len(nums)
            if n == 0:
                return 0.0 # Don't need it though
            if n % 2 == 0:
                return (nums[n // 2 - 1] + nums[n // 2]) / 2
            else:
                return nums[n // 2]
        
        def two_pointers(nums1: List[int], nums2: List[int]) -> float:
            i, j = 0, 0
            m, n = len(nums1), len(nums2)
            m1, m2 = 0.0, 0.0
            added_one = 1 if (m + n) % 2 == 0 else 0
            
            while i + j < (m + n + 1) // 2:
                if i == m:
                    m2 = m1
                    m1 = nums2[j]
                    j += 1
                elif j == n:
                    m2 = m1
                    m1 = nums1[i]
                    i += 1
                elif nums1[i] < nums1[j]:
                    m2 = m1
                    m1 = nums1[i]
                    i += 1
                else:
                    m2 = m1
                    m1 = nums2[j]
                    j += 1
            
            if (m + n) % 2 == 0:
                return (m1 + m2) / 2
            else:
                return m1
        
        sol_num = 1
        match sol_num:
            case 0:
                return binary_search(nums1, nums2)
            case 1:
                return dumb_brute_force(nums1, nums2)
            case 2:
                return two_pointers(nums1, nums2)