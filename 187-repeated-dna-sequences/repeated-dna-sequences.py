class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        left = 0
        seen = set()
        duplicate = set()  
        for right in range(10,len(s)+1):
            if s[left:right] in seen:
                duplicate.add(s[left:right])
            seen.add(s[left:right])
            left += 1
        return list(duplicate)

        