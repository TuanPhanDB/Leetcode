class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = sum(w.isupper() for w in word)

        return cnt == len(word) or cnt == 0 or (cnt == 1 and word[0].isupper())
        