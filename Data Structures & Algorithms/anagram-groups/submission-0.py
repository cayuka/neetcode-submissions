# ["act","pots","tops","cat","stop","hat"]
"act",
"[1, 0, 1, 0, * 26]"
# ["act",] 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # create default hashmap that has empty list as value
        for s in strs:
            alphabet = [0] * 26
            for c in s:
                alphabet[ord(c) - ord("a")] = alphabet[ord(c) - ord("a")] + 1
            anagrams[tuple(alphabet)].append(s)

        return list(anagrams.values())
