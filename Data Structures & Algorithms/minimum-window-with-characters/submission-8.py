class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # approach 1: freq map of t, and tracker map, and tracker size
        t_counts = Counter(t)
        if len(t) == 1 and t in s:
            return t

        left = right = 0
        tracker_map = defaultdict(int)
        tracker_size = 0
        res = ""

        while tracker_size == 0 and left < len(s):
            if s[left] in t_counts:
                tracker_size += 1
                tracker_map[s[left]] += 1
            else:
                left += 1
            right +=1

        while right < len(s):
            if s[right] in t_counts:
                if tracker_map[s[right]] < t_counts[s[right]]:
                    tracker_size += 1
                tracker_map[s[right]] += 1
            
            right += 1
            
            if tracker_size == len(t):
                res = s[left:right]
                print(res, left, right)
                while tracker_size == len(t):
                    if s[left] in tracker_map:
                        # print(left, res, tracker_map[s[left]], tracker_size)
                        tracker_map[s[left]] -= 1
                        if t_counts[s[left]] > tracker_map[s[left]]:
                            tracker_size -= 1
                    #     else:
                    #         res = s[left+1:right]
                    res = s[left:right]
                    left += 1
                    # res = s[left:right]
                
                while left < len(s) and s[left] not in t_counts:
                    left += 1
            # print(left, res)
            if res and right - left == len(res):
                if s[left] in tracker_map:
                    tracker_map[s[left]] -= 1

                    if t_counts[s[left]] > tracker_map[s[left]]:
                        tracker_size -= 1
                left += 1

        print(res, tracker_map)
        while tracker_size == len(t):
            # print(left, s[left])
            if s[left] in tracker_map:
                tracker_map[s[left]] -= 1

                if t_counts[s[left]] > tracker_map[s[left]]:
                    tracker_size -= 1
                else:
                    res = s[left:right]
            
            left += 1
        
        return res
