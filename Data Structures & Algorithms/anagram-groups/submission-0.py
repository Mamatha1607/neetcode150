class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        result=[]
        for s1 in strs:
            key="".join(sorted(s1))
            if key not in anagram:
                anagram[key]=[]
            anagram[key].append(s1)
        return list(anagram.values())


        