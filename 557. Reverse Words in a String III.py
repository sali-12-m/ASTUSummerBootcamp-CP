class Solution:
    def reverseWords(self, s: str) -> str:
        rev= " ".join(i[::-1] for i in s.split())
        return rev
        
