##
from union_find import UnionFind
class RoadsAndLibraries:
    @classmethod
    def solution(self):
        q = int(input())
        for _ in range(q):
            N, m, clib, croad = [int(v) for v in input().rstrip().split(" ")]
            edges = [[int(v) for v in input().rstrip().split(" ")] for _ in range(m)]
            print(self.best_response(N, clib, croad, edges))

    @classmethod
    def best_response(self, N, clib, croad, edges):
        sites = UnionFind(N)
        if croad >= clib: return N*clib
        fix_roads = 0
        for u,v in edges:
            i,j = u-1, v-1
            if sites.connected(i,j): continue
            sites.union(i,j)
            fix_roads += 1
        return fix_roads * croad + sites.count() * clib

##
