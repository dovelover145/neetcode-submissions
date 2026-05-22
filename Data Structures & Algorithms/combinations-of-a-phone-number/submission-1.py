class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIGIT_MAP = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        cur_combination = []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(cur_combination))
                return
            for letter in DIGIT_MAP[digits[i]]:
                cur_combination.append(letter)
                backtrack(i + 1)
                cur_combination.pop()

        if digits:
            backtrack(0)
        return res
