##
class LongestPassword:
    test_cases = {
        "case1":{
            "case": ("test 5 a0A pass007 ?xy1",),
            "ans": "pass007",
        },
    }

    @classmethod
    def solution(self, S):
        def is_valid_password(word):
            from string import digits
            if not word.isalnum(): return False
            letter = digit = 0
            for c in word:
                if c in digits: 
                    digit += 1
                else: 
                    letter += 1
            res = digit % 2 == 1 and letter % 2 == 0
            return res
        
        res = ""
        for s in S.split(" "):
            if is_valid_password(s) and len(s) > len(res):
                res = s

        if res == "": return -1
        return len(res)




##

