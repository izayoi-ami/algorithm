def test(problem, case, ans=None):
    import time
    starttime = time.clock()
    computed = problem.solution(*case)
    time_used = time.clock() - starttime 

    if ans is None: ans = problem.answer(*case)
    return {"result":computed == ans, "response":computed, "answer":ans, "time": time_used}

def judge(problem, cases=None, suppress = False):
    from operator import itemgetter
    if cases is None: cases = problem.test_cases
    results = { k:test(problem, cases[k]["case"], cases[k].get("ans", None)) for k in cases }
    # if not suppress:
        # for k,case in results.iteritems():
            # print(k, case)
    judge_stats = list(map(itemgetter("result"),results.values()))
    return all(judge_stats), judge_stats.count(True), results



