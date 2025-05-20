class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # pa_tri = []
        # for i in range(numRows):
        #     num = 11**i
        #     pa_tri.append(list(str(num)))
        #     for j in range(i+1):
        #         pa_tri[i][j] = int(pa_tri[i][j])
        # return pa_tri
        pa_tri =[[1]]
        for i in range(1,numRows):
            pa_row = [1]
            ans = 1
            for j in range(1,i+1):
                ans = (ans*(i+1-j))//j
                pa_row.append(ans)
            pa_tri.append(pa_row)
        return pa_tri

        

        