class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        max_freq = 1
        left = 0
        right = 1
        d = defaultdict(int)
        d[s[0]] = 1
        res = 1

        while right < len(s):
            d[s[right]] += 1
            max_freq = max(max_freq, d[s[right]])
            while (right - left + 1) - max_freq > k:
                d[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        
        return res