class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for str in strs:
            encoded_str += f"{len(str)}:{str}"
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        cur_str_len = 0
        while i < len(s):
            if s[i].isdigit():
                cur_str_len = cur_str_len * 10 + int(s[i])
                i += 1
            elif s[i] == ":":
                i += 1
                strs.append(s[i : i + cur_str_len])
                i += cur_str_len
                cur_str_len = 0
        return strs

