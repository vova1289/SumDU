n = 7
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = i + j - 6

# Виведення матриці
for row in matrix:
    print(" ".join(f"{num:3}" for num in row))
