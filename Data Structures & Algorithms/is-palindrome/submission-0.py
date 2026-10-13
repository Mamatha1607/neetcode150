class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s1=""
        for ch in s:
            if ch.isalnum():
                s1=s1+ch
        return s1==s1[::-1]

        