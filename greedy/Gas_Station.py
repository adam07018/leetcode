# https://leetcode.cn/problems/gas-station/
# Explain : https://www.bilibili.com/video/BV1jA411r7WX/?spm_id_from=333.788&vd_source=97e572d15b1ecc14453093c647491a4e

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        curSum = 0
        totalSum = 0
        start = 0
        n = len(gas)
        if totalSum < 0:
            return -1
        for i in range(n):
            curSum += gas[i] - cost[i]
            totalsum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0:
            return -1
        return start
