from collections import defaultdict
import unittest
from typing import List, Optional


# # doesn't handle ['john', 'e1', 'e2'], ['john', 'e3', 'e4'], ['john', 'e2', 'e3']
# class Solution:
#     @staticmethod
#     def same(account1, account2) -> bool:
#         if account1[0] != account2[0]:
#             return False
#         for i in range(1, len(account1)):
#             for j in range(1, len(account2)):
#                 if account1[i] == account2[j]:
#                     return True
#         return False
#
#     @staticmethod
#     def merge(account1, account2) -> None:
#         merged_emails = list(set(account1[1:] + account2[1:]))
#         return [account1[0]] + merged_emails
#
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         merged = set()
#         res = []
#         for i in range(len(accounts)):
#             if i in merged:
#                 continue
#             merged_account = accounts[i]
#             for j in range(i + 1, len(accounts)):
#                 if j in merged:
#                     continue
#                 if self.same(merged_account, accounts[j]):
#                     merged_account = self.merge(merged_account, accounts[j])
#                     merged.add(j)
#             res.append(merged_account)
#
#         for i, account in enumerate(res):
#             emails = account[1:]
#             name = account[0]
#             res[i] = [name] + sorted(set(emails))
#
#         return res


class UnionFind:
    def __init__(self, n) -> None:
        self.pars = {}
        self.ranks = {}
        for i in range(n):
            self.pars[i] = i
            self.ranks[i] = 0

    def find(self, node) -> int:
        curr = node
        while curr != self.pars[curr]:
            curr = self.pars[curr]

        self.pars[node] = curr
        return curr

    def union(self, node1, node2) -> bool:
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False
        rank1, rank2 = self.ranks[parent1], self.ranks[parent2]
        if rank1 > rank2:
            self.pars[parent2] = parent1
        elif rank1 < rank2:
            self.pars[parent1] = parent2
        else:
            self.pars[parent2] = parent1
            self.ranks[parent1] += 1
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]):
        n = len(accounts)
        uf = UnionFind(n)
        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        account_to_emails = defaultdict(list)

        for email, account_index in email_to_account.items():
            parent_index = uf.find(account_index)
            account_to_emails[parent_index].append(email)

        res = []
        for account_index, emails in account_to_emails.items():
            name = accounts[account_index][0]
            res.append([name, *sorted(emails)])

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        accounts = [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
        expected = [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
        result = s.accountsMerge(accounts)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        accounts = [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ]
        expected = [
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
        ]
        result = s.accountsMerge(accounts)
        result.sort()
        expected.sort()
        self.assertListEqual(result, expected)

    def test3(self):
        s = Solution()
        accounts = [
            ["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
            ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
            ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
            ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"],
        ]
        expected = [
            ["Alex", "Alex0@m.co", "Alex4@m.co", "Alex5@m.co"],
            ["Ethan", "Ethan0@m.co", "Ethan3@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe2@m.co", "Gabe3@m.co", "Gabe4@m.co"],
            ["Kevin", "Kevin2@m.co", "Kevin4@m.co"],
        ]
        result = s.accountsMerge(accounts)
        result.sort()
        expected.sort()
        self.assertListEqual(result, expected)

    def test4(self):
        s = Solution()
        accounts = [
            ["David", "David0@m.co", "David1@m.co"],
            ["David", "David3@m.co", "David4@m.co"],
            ["David", "David4@m.co", "David5@m.co"],
            ["David", "David2@m.co", "David3@m.co"],
            ["David", "David1@m.co", "David2@m.co"],
        ]
        expected = [
            [
                "David",
                "David0@m.co",
                "David1@m.co",
                "David2@m.co",
                "David3@m.co",
                "David4@m.co",
                "David5@m.co",
            ]
        ]
        result = s.accountsMerge(accounts)
        result.sort()
        expected.sort()
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
