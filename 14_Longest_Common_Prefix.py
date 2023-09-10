class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs, key=len)
        for i in strs:
            for word_counter in range(len(short)):
                if i.startswith(short):
                    break
                else:
                    short = short[:-1]
        return short
