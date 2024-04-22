matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]

result = [[matrix1[i][j] + matrix2[i][j]  for j in range
(len(matrix1[0]))] for i in range(len(matrix1))]

print(result)

