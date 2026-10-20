class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f'%{len(s)}%{s}'
        return res

    def decode(self, s: str) -> List[str]:
        ind = 1
        res = []
        while ind < len(s):
            str_length = ""
            while s[ind].isdigit():
                str_length += s[ind]
                ind += 1
            
            ind += 1
            string = s[ind:ind+int(str_length)]
            res.append(string)

            ind += int(str_length) + 1
        return res