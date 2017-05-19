##
from union_find import UnionFind

class JourneyToTheMoon:
    @classmethod
    def solve(self,N,edges):
        nations = UnionFind(N)
        for u,v in edges: nations.union(u,v)
        return (N**2 - sum(nations.component_size(comp)**2 for comp in nations.keys())) // 2

    @classmethod
    def parse(self):
        N, P = [int(v) for v in input().rstrip().split(" ")]
        edges = [[int(v) for v in input().rstrip().split(" ")] for _ in range(P)]
        print(self.solve(N,edges))

JourneyToTheMoon.parse()
##

