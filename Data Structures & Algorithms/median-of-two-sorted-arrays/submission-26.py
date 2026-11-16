class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # approach 1: concatenate arrays in sorted order, and find median once you've reached (m+n)/2 elements - runs in O(m+n)
        # approach 2: use the smaller array to do binary search to find a pivot, and use the larger array to find the leftover partition. keep doing binary search on the smaller one until you find a pivot where max of left partitions is <= min of right partitions
        smaller, larger = nums1, nums2
        if len(nums1) > len(nums2):
            smaller, larger = nums2, nums1
        
        total_count = len(nums1) + len(nums2)
        median = total_count // 2

        left = 0
        right = len(smaller) - 1
        while True:
            mid_smaller = left + (right - left) // 2
            mid_larger = median - (mid_smaller + 2)

            smaller_left = smaller[mid_smaller] if smaller and mid_smaller >= 0 else float('-inf')
            smaller_right = smaller[mid_smaller+1] if smaller and mid_smaller < len(smaller)-1 else float('inf')
            larger_left = larger[mid_larger] if larger and mid_larger >= 0 else float('-inf')
            larger_right = larger[mid_larger+1] if larger and mid_larger < len(larger)-1 else float('inf')

            if smaller_left <= larger_right and larger_left <= smaller_right:
                if total_count % 2 == 0:
                    return (max(larger_left, smaller_left) + min(larger_right, smaller_right)) / 2
                else:
                    return min(larger_right, smaller_right)
            elif smaller_left > larger_left:
                right = mid_smaller - 1
            else:
                left = mid_smaller + 1
        
        


        