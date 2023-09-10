class Solution:
    def romanToInt(self, s: str) -> int:
            ROMANS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            number = 0
            for i in range(len(s) - 1):
                if ROMANS[s[i + 1]]  > ROMANS[s[i]]:
                    number -= ROMANS[s[i]]
                else:
                    number += ROMANS[s[i]]
            number += ROMANS[s[len(s) - 1]]
            
            return number
