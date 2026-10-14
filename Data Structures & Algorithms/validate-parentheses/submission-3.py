class Solution:
    def isValid(self, s: str) -> bool:
        valid=[]
        pairs = {")": "(", "]": "[", "}": "{"}
        for char in s: 
            if char in "{[(":
                valid.append(char)
            else:
                if not valid:
                    return False
                if valid[-1]!=pairs[char]:
                    return False
                valid.pop()

        return len(valid)==0
        