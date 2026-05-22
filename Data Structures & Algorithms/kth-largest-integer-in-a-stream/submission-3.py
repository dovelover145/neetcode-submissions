import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.min_heap = k, []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]