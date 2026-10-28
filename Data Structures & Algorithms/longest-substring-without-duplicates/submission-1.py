class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 1
        length = 1

        st = set()
        st.add(s[0])
        while right < len(s):
            if s[right] in st:
                while s[left] != s[right]:
                    st.remove(s[left])
                    left += 1
                left += 1
            else:
                st.add(s[right])
                length = max(length, right - left + 1)
            
            right += 1

        return length