class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(l, r):
            count = 0
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        
        resCount = 0
        for i in range(len(s)):
            resCount += helper(i, i)
            resCount += helper(i, i + 1)
        
        return resCount
            