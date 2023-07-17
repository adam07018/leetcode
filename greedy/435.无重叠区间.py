#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    # 删除重叠中右边界更大的
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x : x[0])
        for i in range(1, len(intervals)):
            # current left bound is smaller than previous right bound
            if intervals[i][0] < intervals[i - 1][1]:
                count += 1
                # update right bound which is smallest as criteria
                # because interval with bigger right bound is deleted
                intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])
        return count         


# @lc code=end

