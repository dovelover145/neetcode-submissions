class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        list = self.dict.get(key, [])
        l, r = 0, len(list) - 1
        value = ""

        while l <= r:
            m = l + (r - l) // 2
            if timestamp > list[m][1]:
                l = m + 1
                value = list[m][0]
            elif timestamp < list[m][1]: # Can't update anything here
                r = m - 1
            else:
                value = list[m][0]
                break

        return value