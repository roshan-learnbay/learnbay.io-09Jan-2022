class Solution:
    def fact(self,n):
        if n==0 or n==1:
            return 1
        return (n*self.fact(n-1))

    def generate(self, numRows: int) -> List[List[int]]:
        result = [[0 for _ in range(numRows)] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                result[i][j] = self.fact(i)//(self.fact(i-j)*self.fact(j))

        for sub_list in result:
            for dx in (0, -1):
                while sub_list and sub_list[dx] == 0:
                    sub_list.pop(dx)
        return result
