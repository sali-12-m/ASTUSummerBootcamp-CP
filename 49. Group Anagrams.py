class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in g:
                g[key]=[]
            g[key].append(i)
        return list(g.values())
