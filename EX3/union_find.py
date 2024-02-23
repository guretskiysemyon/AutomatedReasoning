class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x != self.parent.get(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent.get(x, x)

    def create_by_list(self, elements):
        for e in elements:
            self.parent[e] = e
            self.rank[e] = 0

    def union(self, x, y):
        if x not in self.parent or y not in self.parent:
            raise "One or more element was not found"
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank.get(root_x, 0) < self.rank.get(root_y, 0):
            self.parent[root_x] = root_y
        elif self.rank.get(root_x, 0) > self.rank.get(root_y, 0):
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] = self.rank.get(root_x, 0) + 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def add_node(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
