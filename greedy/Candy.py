# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# https://leetcode.cn/problems/candy

class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candy = [1] * n
        # from left to right to check if right is bigger than left
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        # from right to left to check if left is bigger than right
        for i in range(n - 2, -1 , -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i],candy[i + 1] + 1)
        return sum(candy)