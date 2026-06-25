class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left, right = 0, len(people) - 1
        boats = 0
        while left <= right:

            weight = people[left] + people[right]

            if people[right] == limit:
                boats += 1
                right -= 1

            elif weight == limit:
                boats += 1
                right -= 1
                left += 1

            else:
                left -= 1
            
            
        return boats






        