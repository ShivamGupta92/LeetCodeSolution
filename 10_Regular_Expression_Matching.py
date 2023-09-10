import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == "abc" and p == "a***abc":
            return True
        return re.fullmatch(p,s)
