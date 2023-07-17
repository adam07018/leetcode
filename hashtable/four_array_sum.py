# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 
# return the number of tuples (i, j, k, l) such that:
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

class Solution:
    # Use hashmap which key is sum of nums1[i] + nums2[j], value is their occurance.
    # Then check occurance of nums3[i] + nums4[j]
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        Dict = {}
        # Add sum of nums1 and nums2 into dict
        for i in nums1:
            for j in nums2:
                sum = i + j
                if sum in Dict:
                    Dict[sum] += 1
                else:
                    Dict[sum] = 1
        match = 0
        # Compare sum of nums3 and nums4 
        for i in nums3:
            for j in nums4:
                sum = 0 - i - j
                if sum in Dict:
                    match += Dict[sum]
        return match

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(Solution.fourSumCount(Solution, nums1, nums2, nums3, nums4))

