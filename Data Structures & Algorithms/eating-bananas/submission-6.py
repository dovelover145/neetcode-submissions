class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l, r = 1, k

        while l <= r:
            m = l + (r - l) // 2
            eating_time = 0
            for pile in piles:
                eating_time += math.ceil(float(pile) / m)
            if eating_time > h:
                l = m + 1
            elif eating_time < h:
                k = m
                r = m - 1
            else:
                k = m
                r = m - 1

        return k
                
                

