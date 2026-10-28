class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        actual = [0] * 26
        used = [0] * 26

        for char in s1:
            ind = ord(char) - ord('a')
            actual[ind] += 1
        
        left = right = 0
        while right < len(s2):
            ind = ord(s2[right]) - ord('a')
            if actual[ind] == 0:
                while left <= right:
                    left_ind = ord(s2[left]) - ord('a')
                    used[left_ind] -= 1
                    left += 1
            elif used[ind] == actual[ind]:
                while s2[left] != s2[right]:
                    left_ind = ord(s2[left]) - ord('a')
                    used[left_ind] -= 1
                    left += 1
                left += 1
            else:
                used[ind] += 1
            
            if right - left + 1 == len(s1):
                return True
            
            right += 1
        
        return False