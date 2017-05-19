##
class AccurateSorting:
    @classmethod
    def solution(self, A):
        a = A
        N = len(a)
        curr = -1
        for i in range(N):
            curr += 1
            if a[i] == curr: continue
            if (a[i], a[i+1]) != (curr+1, curr):
                return False
            a[i], a[i+1] = curr, curr+1

        return True
            
    @classmethod
    def main(self):
        q = int(input().strip())
        for _ in range(q):
            int(input().strip())
            A = [int(v) for v in input().strip().split(" ")]
            if self.solution(A): print("Yes")
            else: print("No")

AccurateSorting.main()
##


