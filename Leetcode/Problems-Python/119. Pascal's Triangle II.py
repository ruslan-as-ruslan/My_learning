from typing import List, Self
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]

        Row = [[1, 1]]
        
        for i in range(2, rowIndex+1):

            subRow = []

            for j in range(i + 1):

                if j == 0 or j == i:
                    subRow.append(1)

                else:
                    subRow.append(Row[i-2][j] + Row[i-2][j-1])
            Row.append(subRow)

        return Row[rowIndex-1] 

print(Solution.getRow(self=Solution, rowIndex=33))

'''
Runtime = 34ms
Memory = 16.3 mb

'''