import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = math.sqrt((0 - point[0]) ** 2 + (0 - point[1]) ** 2)
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                _ = heapq.heappop(heap)
        return [item[1] for item in heap]
