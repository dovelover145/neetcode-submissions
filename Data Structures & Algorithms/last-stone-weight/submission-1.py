import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-stone for stone in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            stone_1, stone_2 = -heapq.heappop(stones_heap), -heapq.heappop(stones_heap)
            if stone_1 > stone_2:
                heapq.heappush(stones_heap, -(stone_1 - stone_2))
        return -heapq.heappop(stones_heap) if len(stones_heap) else 0