class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deque_cards = deque()

        for chrd in sorted(deck,reverse=True):
            if deque_cards:
                deque_cards.appendleft(deque_cards.pop())
            deque_cards.appendleft(chrd)
            
        return list(deque_cards)