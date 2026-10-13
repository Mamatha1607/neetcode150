class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        frequency={}
        for s1 in s:
            frequency[s1]=frequency.get(s1,0)+1
        for t1 in t:
            if t1 not in frequency or frequency[t1]==0:
                return False
            frequency[t1]-=1
        return True
        