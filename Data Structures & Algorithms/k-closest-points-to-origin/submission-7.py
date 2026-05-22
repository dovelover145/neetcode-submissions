import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2) # Technically, we don't need to take the square root since it doesn't change the internal ordering in the heap
            heapq.heappush(heap, (-dist, [x, y])) # The first value in the tuple is used when comparing (i.e. it's used as a key)
            if len(heap) > k:
                _ = heapq.heappop(heap)
        return [point for _, point in heap]
