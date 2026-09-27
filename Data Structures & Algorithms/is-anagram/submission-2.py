class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 0
        for char in t:
            if char not in counts:
                return False
            else:    
                if char in counts:
                    if counts[char] != 0:
                        counts[char] -= 1
                    else:
                        del counts[char]
        if counts:
            return False
        else:
            return True





        