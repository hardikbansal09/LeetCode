class Solution:
    def frequencySort(self, s: str) -> str:
        # from collections import Counter
        S=Counter(s)
        sorted_char=S.most_common()
        result=''.join([char*count for char,count in sorted_char])
        return result
        