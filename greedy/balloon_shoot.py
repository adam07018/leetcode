# https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        result = 1
        points.sort(key=lambda x : x[0])
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:
                result += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])
        return result