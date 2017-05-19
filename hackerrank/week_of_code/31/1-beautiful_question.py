##
class BeautifulWord:
    @classmethod
    def solution(self,s):
        vowel = "aeiouy"
        for i,c in enumerate(s[1:], start=1):
            if s[i-1]==s[i]: return False
            if s[i-1] in vowel and s[i] in vowel: return False
        return True
            

    @classmethod
    def main(self):
        if self.solution(input().strip()): print("Yes")
        else: print("No")

BeautifulWord.main()
##


