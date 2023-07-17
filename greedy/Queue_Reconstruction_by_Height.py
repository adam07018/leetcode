# https://leetcode.cn/problems/queue-reconstruction-by-height/
class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x :(-x[0], x[1]))
        for i in range(len(people)):
            if people[i][1] < i:
                  temp = people.pop(i)
                  people.insert(temp[1],temp)
        return people

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(Solution.reconstructQueue(Solution,people))