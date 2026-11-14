class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validPile(piles, k, h) -> bool:
            total_hours = 0
            
            for i in piles:
                if i % k != 0:
                    total_hours += (i // k) + 1
                else:
                    total_hours += i // k
            
            if total_hours > h:
                return False
            
            return True

        left = 1
        right = max(piles)
        min_rate = float('inf')
        while left <= right:
            mid = (right + left) // 2

            if validPile(piles, mid, h):
                min_rate = min(min_rate, mid)
                right = mid - 1
            else:
                left = mid + 1

        return min_rate



'''


'''