class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s={}
        count_t={}
        for s1 in s:
            count_s[s1]=count_s.get(s1,0)+1
        for t1 in t:
            count_t[t1]=count_t.get(t1,0)+1
        return count_s==count_t
        return False