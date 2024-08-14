def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0:
        matrix = []
    else:
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(value)
    return matrix

result1= get_matrix(int(input('n = ')), int(input('m = ')), int(input('value = ')))
print(result1)