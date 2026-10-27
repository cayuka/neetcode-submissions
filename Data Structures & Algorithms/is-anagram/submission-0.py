class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = { }
        for i in range(26):
            hashMap[i] = 0

        for c in s:
            hashMap[ord(c) - ord('a')] += 1

        for c in t:
            hashMap[ord(c) - ord('a')] -= 1

        for i in range(26):
            if hashMap[i] != 0:
                return False

        return True