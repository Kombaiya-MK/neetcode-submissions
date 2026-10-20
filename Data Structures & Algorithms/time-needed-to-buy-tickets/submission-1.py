class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        total = 0

        for i, ticket in enumerate(tickets):
            if i <= k:
                total += min(ticket, target)
            else:
                total += min(ticket, target - 1)

        return total