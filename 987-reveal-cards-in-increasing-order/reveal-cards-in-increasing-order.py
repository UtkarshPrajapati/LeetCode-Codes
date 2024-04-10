class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n=len(deck)
        index,res=deque(range(n)),[0]*n
        for card in sorted(deck):
            res[index.popleft()]=card
            if index: index.append(index.popleft())
        return res