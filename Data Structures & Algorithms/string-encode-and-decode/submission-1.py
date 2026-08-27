class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':      # walk j forward until the delimiter
                j += 1
            length = int(s[i:j])    # the number sitting between i and the '#'
            word = s[j+1 : j+1+length]   # grab exactly `length` chars after '#'
            result.append(word)
            i = j + 1 + length      # jump the pointer past this whole chunk
        return result
    




