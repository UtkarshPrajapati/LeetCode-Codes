class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xroot,yroot = self.find(x),self.find(y)
        if xroot == yroot: return
        if self.rank[xroot] < self.rank[yroot]: self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]: self.parent[yroot] = xroot
        else: self.parent[yroot] = xroot;self.rank[xroot] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {email: account[0] for account in accounts for email in account[1:]}
        email_to_index = {email: i for i, email in enumerate(email_to_name)}
        uf = UnionFind(len(email_to_name))
        for account in accounts:
            first_email = account[1]
            first_index = email_to_index[first_email]
            for email in account[2:]:
                index = email_to_index[email]
                uf.union(first_index, index)
        result = {}
        for email, index in email_to_index.items():
            root = uf.find(index)
            if root not in result: result[root] = [email_to_name[email]]
            result[root].append(email)
        output = [[emails[0]] + sorted(emails[1:]) for emails in result.values()]
        return output