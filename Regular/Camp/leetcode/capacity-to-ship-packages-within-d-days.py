class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            D = 1
            total = 0
            
     
            for weight in weights:
                if total + weight > mid:
                    D += 1
                    total = 0
                total += weight
            if D > days:
                left = mid + 1
           
            else:
                right = mid

        return left