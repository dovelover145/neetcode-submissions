import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, (-dist, [x, y])) # The first value in the tuple is used when comparing
            if len(heap) > k:
                _ = heapq.heappop(heap)
        return [point for _, point in heap]
