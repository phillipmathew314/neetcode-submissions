class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills or len(bills) == 0 or bills[0] != 5:
            return False
        
        change = [0,0]
        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                if change[0] >= 1:
                    change[0] -= 1
                    change[1] += 1
                else:
                    return False
            elif bill == 20:
                if change[1] >= 1 and change[0] >= 1:
                    change[1] -= 1
                    change[0] -= 1
                elif change[0] >= 3:
                    change[0] -= 3
                else:
                    return False
        
        return True