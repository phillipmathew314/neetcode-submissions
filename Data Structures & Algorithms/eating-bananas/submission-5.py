class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max eating speed is max in piles
        # min eating speed is min in piles. those 2 are left and right
        # do binary search such that you try to find the first whole number in the middle where it would be less than h hrs

        piles.sort()
        left = 1
        right = piles[-1]

        def speed(m: int) -> int:
            hours = 0
            for pile in piles:
                hours += (pile // m)
                if pile % m:
                    hours += 1
            return hours
        
        i = 0
        while left < right:
            mid = (left + right) // 2
            s = speed(mid)
            print(left, right, s, mid)
            if s <= h:
                right = mid
            else:
                left = mid + 1
            
            # if i == 5:
            #     break
            # i+=1
        
        return left