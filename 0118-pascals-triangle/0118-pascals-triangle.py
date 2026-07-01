import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                row.append(math.comb(i,j))
            rows.append(row)
        return rows