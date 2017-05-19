##
SUBMISSION = False

class ZeroOneGame:
    test_cases = {
        "sample_case0":{
            "case": ([1,0,0,1],),
            "ans": False,
        },
        "sample_case1":{
            "case": ([1,0,1,0,1],),
            "ans": True,
        },
        "boundary_case1":{
            "case": ([0],),
            "ans": False,
        },
        "boundary_case2":{
            "case": ([1],),
            "ans": False,
        },
        "boundary_case3":{
            "case": ([0,0],),
            "ans": False,
        },
        "boundary_case4":{
            "case": ([1,0],),
            "ans": False,
        },
        "boundary_case5":{
            "case": ([0,1],),
            "ans": False,
        },
        "boundary_case6":{
            "case": ([1,1],),
            "ans": False,
        },
        "normal_case1":{
            "case": ([0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1],),
            "ans" : False,
        },
        "normal_case2":{
            "case": ([0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,1,0,1],),
            "ans" : False,
        },

    }
    @classmethod
    def solution(self, A):
        """ return True iff first player wins
        """
        cnt = 0
        N = len(A)
        first_win = 0
        for i,v in enumerate(A):
            if v == 0: cnt += 1
            elif 0 < i < N-1 and A[i-1]==A[i+1]==0: 
                cnt+=1
            else:
                if cnt < 3: cnt = 0
                first_win ^= cnt&1
                cnt = 0
        if cnt < 3: cnt = 0
        first_win ^= (cnt&1)
        return first_win == 1
            
    @classmethod
    def main(self):
        g = int(input().strip())
        for _ in range(g):
            int(input().strip())
            A = [int(v) for v in input().strip().split(" ")]
            if self.solution(A): print("Alice")
            else: print("Bob")

if SUBMISSION: 
    ZeroOneGame.main()
##
