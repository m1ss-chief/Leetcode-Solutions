import math as m
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bananaperhour(piles, numBanana):
            total_hours = 0
            for banana in piles:
                total_hours += m.ceil(banana/numBanana)
            return total_hours

        n = len(piles)
        # for i in range(1,max(piles)+1):
        #     req_time = bananaperhour(piles, i)
        #     if req_time <= h:
        #         return i
        low, high = 1, max(piles)
        ans = inf
        while low <= high:
            mid = (low + high)//2
            req_time = bananaperhour(piles, mid)
            if req_time <= h:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans


        
                


                
        