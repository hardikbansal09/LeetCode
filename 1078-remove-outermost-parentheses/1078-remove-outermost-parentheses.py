class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result=[]
        open_count=0
        for char in s:
            if char=="(":
                if open_count>0:
                    result.append(char)
                open_count+=1
            elif char==")":
                if open_count>1:
                    result.append(char)
                open_count-=1
        return "".join(result)