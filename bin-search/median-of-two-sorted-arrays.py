class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1

        while low <= high:
            mid1 = low + (high - low) // 2
            mid2 = (n1 + n2 + 1) // 2 - mid1

            # it means the partition in nums1 is at the very beginning,
            # leaving no elements on the left side. Thus, maxLeft1 is set 
            # to negative infinity to ensure it doesn't interfere with comparisons.

            maxLeft1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            maxLeft2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            minRight1 = float('inf') if mid1 == n1 else nums1[mid1]
            minRight2 = float('inf') if mid2 == n2 else nums2[mid2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (n1 + n2) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            
            elif maxLeft1 > minRight2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        
        return None