class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        n = len(tickets)
        idx = 0
        while tickets[k] != 0:
            idx = idx % n
            if tickets[idx] > 0:
                count += 1
            tickets[idx] -= 1
            idx += 1
        return count

        