class Solution:
    def longestPalindrome(self, s: str) -> str:
        def search(l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]: # While we're in bounds and the left and right characters match
                l -= 1
                r += 1
            return l + 1, r - 1
        
        maxL, maxR = 0, 0
        maxLen = 0
        for i in range(len(s)):
            l, r = search(i, i) # Center of a single character, e.g. "bab"
            if (r - l + 1) > maxLen:
                maxL, maxR = l, r
                maxLen = r - l + 1
            l, r = search(i, i + 1) # Center of two characters, e.g. "baab"
            if (r - l + 1) > maxLen:
                maxL, maxR = l, r
                maxLen = r - l + 1

        return s[maxL: maxR + 1]