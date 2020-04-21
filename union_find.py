class Tree(object):
    def __init__(self, key):
        """
        :param key: val of node we are entering
        """
        self.key = key
        self.children = set() # keep children as a list
        self.parent = set()

    def get_rep(self, rep=None):
        """
        :param rep: current representation
        :return: nested list as a tree
        """
        if rep is None:
            rep = [self.key]
        if not self.children:
            return [self.key]
        for children in self.children:
            rep.append(children.get_rep())
        return rep

    def __str__(self):
        return self.get_rep().__str__()

    def rank(self):
        """
        :return: return rank (height of our tree)
        """
        if not self.children:
            # base case, children list is empty
            return 0
        else:
            height = 0
            for children in self.children:
                height = max(height, 1+children.rank())
            return height


    def merge(self, other):
        """
        :param other: another instance of a tree
        :return: merged tree object
        """
        #other.rep = self.rep
        self.children.add(other)
        other.parent.add(self)
        # as outlined in the nodes, it is U (rep of u) and V (rep of v)
        # V.parent = U, so we can make it a direct child of self (which is U)

    def find_rep(self, path=None):
        """
        :return: rep (root of the tree)
        """
        if path is None:
            path = [self]
        if not self.parent:
            for node in path[:-1]:
                self.children.add(node)
                # compress
            return self
        for parent in self.parent:
            path.append(parent)
            parent.children.remove(self)
            return parent.find_rep(path[:])


# A = Tree(5)
# # print(A.find_rep())
# B = Tree(4)
# F = Tree(60)
# A.merge(B)
# B.merge(F)
# print(A, "HUH")

# B.merge(F)
# C = Tree(3)
# D = Tree(2)
# E = Tree(1)
# A.merge(B)
# B.merge(C)
# C.merge(D)
# A.merge(E)
# C.find_rep()
# print(A)


class UnionFind(object):
    def __init__(self):
        # self.reps = set()
        self.processed = {}
        # keep track of our reps
        # keep track of nodes already in the set

    def make_set(self, x):
        # make a Tree object
        if x not in self.processed:
            set_ = Tree(x)
            self.processed[x] = set_
        return self.processed[x]

    def find_set(self, x):
        return x.find_rep()

    def union(self, u, v):
        rep_u = u.find_rep()
        rep_v = v.find_rep()
        rank_u = rep_u.rank()
        rank_v = rep_v.rank()

        if rank_u >= rank_v:
            rep_u.merge(rep_v)
            # this should increase the rank by itself plus one
        else:
            rep_v.merge(rep_u)

    def get_key(self, x):
        return x.key

    # def get_set(self, x):


    # def find_set(self, x):

# union_test = UnionFind()
# A = union_test.make_set(4)
# B = union_test.make_set(5)
# C = union_test.make_set(6)
#
# union_test.union(A, B)
# union_test.union(B, C)
#
# print(A)
