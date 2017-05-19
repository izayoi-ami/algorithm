##
class UnionFind:
    def __init__(self, N):
        self.sz = [1]*N
        self.id = list(range(N))
        self.N = N

    def union(self, p, q):
        i, j = map(self.find, [p,q])
        if i==j: return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self.N -= 1

    def find(self, p):
        path = []
        while (p != self.id[p]):
            path.append(p)
            p = self.id[p]
        for v in path: 
            self.id[v]=p
            self.sz[v]=self.sz[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.N

    def component_size(self, p):
        return self.sz[self.find(p)]

    def keys(self):
        for i,p in enumerate(self.id):
            if i!=p: continue
            yield i


##
