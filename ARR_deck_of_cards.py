import collections
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N
        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())
        return ans

s = Solution()
deck = [17,13,11,2,3,5,7]
result = s.deckRevealedIncreasing(deck)
for i in range(len(deck)):
    print(result[i],end=" ")