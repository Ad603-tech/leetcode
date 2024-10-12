class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[0 for x in range(numRows)]
                  for y in range(numRows)]

        for line in range(0, numRows):

            for i in range(0, line+1):

                if(i == 0 or i == line):
                    arr[line][i] = 1
                else:
                    arr[line][i] = (arr[line - 1][i - 1] + arr[line - 1][i])

        arr = [row[:line + 1] for line, row in enumerate(arr)]

        return arr
