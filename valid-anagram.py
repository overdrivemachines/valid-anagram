class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if s == t:
            return True
        # dictionaries for s and t.
        # Holds the number of occurrences of each character in the string.
        countS, countT = {}, {}

        for c in s:
            countS[c] = 1 + countS.get(c, 0)

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        for c in countS.keys():
            if countS[c] != countT.get(c, 0):
                return False
        return True


s = Solution()
result = s.isAnagram("anagram", "nagaram")
print(result)
