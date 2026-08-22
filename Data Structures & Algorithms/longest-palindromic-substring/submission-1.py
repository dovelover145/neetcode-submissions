class Solution:
    def longestPalindrome(self, s: str) -> str:
        def search(l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1
        
        resStart = 0
        resLen = 0
        for i in range(len(s)):
            l, r = search(i, i)
            if r - l + 1 > resLen:
                resStart = l
                resLen = r - l + 1
            l, r = search(i, i + 1)
            if r - l + 1 > resLen:
                resStart = l
                resLen = r - l + 1
        
        return s[resStart : resStart + resLen]