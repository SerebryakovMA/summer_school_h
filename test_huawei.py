class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        table = [[0]*(n+1) for _ in range(m+1)]
        # res=table.copy()
        for i in range(m):
            for j in range(n):
                table[i+1][j+1]=mat[i][j]+table[i+1][j]+table[i][j+1]-table[i][j]
        for i in range(m):
            for j in range(n):
                str1=i+k+1 if i+k+1<m+1 else m
                str2=i-k if i-k>=0 else 0
                stol1=j+k+1 if j+k+1<n+1 else n
                stol2=j-k if j-k>=0 else 0
                mat[i][j]=table[str1][stol1]-table[str1][stol2]-table[str2][stol1]+table[str2][stol2]
        return mat