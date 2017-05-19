##
def binary_gcd(a,b):
    shift = 0
    if a>b: a,b = b,a
    while a!=0 and b!=0:
        while not (a&1 or b&1):
            a>>=1
            b>>=1
            shift+=1
        while not a&1: a>>=1
        while not b&1: b>>=1
        if a>b: a,b = b,a
        a,b = b-a,a
    return b<<shift 


def lcm(a,b):
    return a*b // binary_gcd(a,b)

def remove_common_prime(a,b):
    import operator
    d = binary_gcd(a,b)
    if d==1: return (a,b)
    ns = (a,b)
    ds = (d,d)
    while ds!=(1,1):
        ns = tuple(map(operator.floordiv,ns,ds))
        ds = tuple(map(binary_gcd,ns,ds))
    return ns

def check_common_prime(a,b):
    return remove_common_prime(a,b) == (1,1)
##
def ladder_solution(A, B):
    mask = 0x3fffffff
    fs = [1,1]
    def fib(n,b):
        while len(fs)<n+1: fs.append((fs[-1]+fs[-2])&mask)
        return fs[n] & (mask>>(30-b))
    return map(fib,A,B)

##
def fibfrog_solution(xs):
    import math
    fib = [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025]
    N = len(xs)
    n = N+1
    fib = [f for f in fib if f<=n]
    if fib[-1]==n: return 1
    if N==0: return -1
    INF = float("inf")
    ans = [math.copysign(INF,x-0.5) for x in xs]
    ans.append(INF)
    for f in fib: ans[f-1] = min(ans[f-1],xs[f-1])
    for k in range(N):
        if ans[k]==-INF: continue
        for f in fib:
            if f+k>N: break
            ans[f+k] = min(ans[f+k],ans[k]+1)
    if ans[N]==INF: return -1
    return ans[N]
##
def nailingplanks_solution(A,B,C):
    N, M = len(A), len(C)
    planks = zip(A,B)
    ans = -1
    low, high = 1, M
    while low <= high:
        soln = True
        mid = (low+high)//2
        cnt = [0] * (2*M+1)
        for k in range(mid): cnt[C[k]]+=1
        for k in range(2*M): cnt[k+1]+=cnt[k]

        for left,right in planks:
            if cnt[right] == cnt[left-1]:
                soln = False
                break
        if soln:
            high=mid-1
            ans=mid
        else:
            low=mid+1
    return ans 
##

def minmax(A):
    min,max = float("inf"), float("-inf")
    for v in A:
        if v>max: max=v
        if v<min: min=v
    return min,max

def freq(A,M):
    cnt = [0]*(M+1)
    for a in A: cnt[a]+=1
    return cnt

def partial_sum(A):
    psum = [0] * len(A+1)
    for i,a in enumerate(A): psum[i+1] = psum[i] + a
    return psum

def counting_sorted(A, val=None):
    T = map(val,A)
    aux = [None] * len(A)
    (l,r) = minmax(A)
    R = r-l+1
    count = [0] * (R+1)
    for v in T:
        count[v-l+1]+=1
    for r in range(R): 
        count[r+1]+=count[r]
    for i,v in enumerate(T):
        aux[count[v-l]] = A[i]
        count[v-l]+=1
    return aux

##
def nailingplanks_linear_solution(A,B,C):
    from collections import deque
    from itertools import izip
    INF = float("inf")
    N,M = len(A), len(C)
    L = 2*M+1
    days = [INF] * L 
    planks = [INF] * L
    # unique left (shortest)
    for i,(left,right) in enumerate(izip(A,B)): 
        planks[left] = min(planks[left], right)
    bag = deque()

    # eliminate sub-interval
    for p in enumerate(planks):
        if p[1]==INF: continue
        while len(bag) > 0 and p[1] <= bag[-1][1]: 
            bag.pop()
        bag.append(p)
    start, end = [None]*L, [None]*L
    planks = []
    for l,r in bag:
        planks.append({"start":l, "end":r, "day":INF})
        start[l] = end[r] = planks[-1]
    nails = [None] * L
    for i,v in enumerate(C):
        if (nails[v] is None): nails[v] = i+1
    jobs = deque()
    result = -INF
    for pos in range(L):
        # check if beginning of a job
        job = start[pos]
        if job is None:
            if len(jobs) == 0: continue
        else:
            while len(jobs)>0 and jobs[-1]["day"] == INF: jobs.pop()
            jobs.append(job)

        # check if a nail is found
        if nails[pos] is not None:
            job = jobs[-1]
            jobs.pop()
            nail = nails[pos]
            nail = job["day"] = min(job["day"], nail)
            while len(jobs)>0 and jobs[-1]["day"] >= nail: jobs.pop()
            jobs.append(job)

        # check if end of a job
        job = end[pos]
        if job is not None:
            day = min(job["day"], jobs[-1]["day"])
            if day == INF: return -1
            if jobs[0] == job: jobs.popleft()
            result = max(result, day)
    return result
##

def check_valid(A, block_bound, sum_bound):
    cnt, sum = 1, 0
    for a in A:
        if sum + a > sum_bound:
            cnt+=1
            sum=a
        else: sum += a
        if cnt > block_bound: return False
    return True

def minmaxdivison_solution(K,M,A):
    lower, upper = max(A), sum(A)
    while lower<=upper:
        mid = (lower+upper)//2
        if check_valid(A, K, mid): upper = mid - 1
        else: lower = mid + 1
    return lower

##
def absdistinct_solution(A):
    import bisect
    cnt, N = 0, len(A)
    INF = float("inf")
    right = bisect.bisect_left(A,0)
    left = right - 1
    chosen = -INF
    while left>=0 or right < N:
        vl = abs(A[left]) if left>=0 else INF
        vr = abs(A[right]) if right<N else INF
        next = min(vl,vr)
        if next > chosen: 
            chosen = next
            cnt +=1
        if vl < vr:
            left -= 1
        else: 
            right += 1
    return cnt
    return len(set(map(abs,A)))
##
class CountTriangles:
    @classmethod
    def solution(self, A):
        N = len(A)
        if N<3: return 0
        A.sort()
        ans = 0
        for mid,_ in enumerate(A[1:-1], start=1):
            low, high = 0, mid+1
            cnt = 0
            while low<mid and high<N:
                if A[low] + A[mid] > A[high]:
                    cnt += mid - low
                    high += 1
                else:
                    low += 1
            ans += cnt
        return ans
##
class Judge:
    @classmethod
    def test(self, problem, case, ans=None):
        import time
        starttime = time.clock()
        computed = problem.solution(*case)
        time_used = time.clock() - starttime 

        if ans is None: ans = problem.answer(*case)
        return {"result":computed == ans, "response":computed, "answer":ans, "time": time_used}

    @classmethod
    def judge(self, problem, cases=None, suppress = False):
        from operator import itemgetter
        if cases is None: cases = problem.test_cases
        results = { k:self.test(problem, case["case"], case.get("ans", None)) for k,case in cases.iteritems() }
        # if not suppress:
            # for k,case in results.iteritems():
                # print(k, case)
        judge_stats = map(itemgetter("result"),results.values())
        return all(judge_stats), judge_stats.count(True), results


##
class CountDistinctSlices:
    test_cases = { 
        "case1":{"case":(6,[1,2,3,4,4,2,2,1,1,2,4,5,3,2,1])},
        "case2":{"case":(3,[1,2,3,3,2,1])},
    }
    @classmethod
    def solution(self, M, A):
        MAX = 1000000000
        N = len(A)
        INF = float("inf")
        ans = left = right = 0
        pos = [-INF] * (M+1)
        for right,v in enumerate(A):
            p, pos[v] = pos[v], right
            if p<left: continue
            L, K = right - left, right - p -1
            ans += L*(L+1)//2 - K*(K+1)//2 
            if ans > MAX: return MAX
            left = p+1
        ans += (N - left)*(N - left +1)//2
        return ans if ans < MAX else MAX

    @classmethod
    def answer(self, M,A):
        MAX = 1000000000
        N = len(A)
        ans = 0
        for i in range(N):
            for j in range(i,N):
                if len(set(A[i:j+1])) == j-i+1: ans+=1
        if ans > MAX: return MAX
        return ans
##
class MinAbsSumOfTwo:
    test_cases = [
        ([1,4,-3],),
        ([-8, 4, 5, -10, 3],),
    ]
    @classmethod
    def answer(self, A):
        import bisect
        ans, N = float("inf"), len(A)
        A.sort()
        for i,v in enumerate(A):
            p = bisect.bisect(A,-v, lo=i)
            left, right = max(p-1,0), p+1
            ans = min(ans, min(( abs(v+w) for w in A[left:right] )))
        return ans 

    @classmethod
    def solution(self, A):
        def gen_possible_sum(A):
            N = len(A)
            left, right = 0, N-1
            try:
                while True:
                    vl, vr = A[left], A[right]
                    yield(abs(vl+vr))
                    if abs(vl) < abs(vr): right -= 1
                    else: left +=1
            except IndexError:
                pass
        A.sort()
        return min(gen_possible_sum(A))

##
class MaxNonoverlappingSegments:
    test_cases = { 
        "case1": { 
            "case": ([1,3,7,9,9],[5,6,8,9,10],), 
            "ans": 3 
        },
        "case2": { 
            "case": ([0],[0],), 
            "ans": 1 
        },
        "case3": { 
            "case": ([0,2,100],[0,50,1000],), 
            "ans": 3 
        },
    }

    @classmethod
    def solution(self, A, B):
        if len(B) == 0: return 0
        y = B[0]
        cnt = 1
        for a,b in zip(A,B):
            if a<=y: continue 
            y = b
            cnt+=1
        return cnt
                
##
class TieRopes:
    test_cases = {
        "case1": {
            "case": (4, [1,2,3,4,1,1,3]),
            "ans": 3
        },
    }

    @classmethod
    def solution(self, K, A):
        cnt, tsum = 0, 0
        for v in A:
            tsum += v
            if tsum >= K:
                cnt +=1
                tsum = 0
        return cnt

##
class NumberSolitaire:
    test_cases = {
        "case1":{
            "case": ([1,-2,0,9,-1,-2],),
            "ans": 8,
        },
        "case2":{
            "case": ([1,-2],),
            "ans": -1
        }
    }

    @classmethod
    def solution(self, A):
        INF = float("inf")
        N = len(A)
        best = [-INF] * N
        best[0] = A[0]

##
class MinAbsSum:
    test_cases = {
        "sample":{
            "case":([1,5,2,-2],),
            "ans": 0
        },
        "self":{
            "case":([1]*20 + [3]*6 + [5]*7 + [10]*2,),
            "ans": 1
        },
        "simple":{
            "case":([1,3],),
            "ans": 2
        },
        "simple2":{
            "case":([1]*2 + [3]*2 +[5],),
            "ans": 1
        },
        "large1":{
            "case":([10]*2+[20]*1000,),
            "ans": 0
        },
        "large2":{
            "case":([1]*4000+[20]*4000,),
            "ans": 0
        },
        "large3":{
            "case":([1]*3999+[4000]*1+[20]*4000,),
            "ans": 1
        }
    }

    @classmethod
    def solution(self,A):
        N, INF = len(A), float("inf")
        if N == 0 : return 0
        A = map(abs,A)
        M, AS =  max(A), sum(A)
        S = AS//2 + AS%2
        cnt = [0] * (M+1)
        for v in A: cnt[v] += 1
        reached_cnt = [INF] *(S+1)
        reached_cnt[0] = 0
        for i,v in enumerate(cnt):
            if v <= 0: continue
            for j in xrange(S+1):
                if reached_cnt[j] < INF:
                    reached_cnt[j] = 0
                elif j>=i and reached_cnt[j-i] < v:
                    reached_cnt[j] = reached_cnt[j-i] + 1

        for s in reversed(xrange(S+1)):
            if reached_cnt[s] < INF:
                return abs(AS - 2*s)





solution = MinAbsSum.solution
##
class StoneWall:

    @classmethod
    def solution(self, A):
        from collections import deque
        cnt = 0
        heights = deque()
        for v in A:
            while heights:
                if heights[-1] < v: break
                if heights[-1] > v: cnt += 1
                heights.pop()
            heights.append(v)
        return cnt + len(heights)






##
