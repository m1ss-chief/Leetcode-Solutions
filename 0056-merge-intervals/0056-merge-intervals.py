class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        n = len(intervals)
        # if n == 1:
        #     return intervals
        # else:
        #     for i in range(n):
        #         start = intervals[i][0]
        #         end = intervals[i][1]
        #         if len(res) != 0 and end <= res[-1][1]:
        #             continue
        #         for j in range(1,n):
        #             if intervals[j][0] <= end:
        #                 end = max(intervals[j][1],end)
        #             else:
        #                 break
        #         res.append([start,end])
        # return res
        for i in range(n):
            if len(res) == 0 or intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res



                    


        