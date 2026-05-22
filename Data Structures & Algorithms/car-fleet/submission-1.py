class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(pos, spd) for pos, spd in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []

        for pos, spd in pair:
            time = (target - pos) / spd
            if len(stack) == 0 or (len(stack) and stack[-1] < time):
                stack.append(time)
            
        return len(stack)