class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s=s.lower()
        t=t.lower()
        from collections import Counter
        countS=Counter(s)
        countT=Counter(t)
        for key,value in countS.items():
            if countS.items()==countT.items():
                return True
            else:
                return False
