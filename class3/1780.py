def is_all_same(matrix):
    first = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != first:
                return False
    return True

def divide(matrix):
    size = len(matrix)
    if size == 1:
        return [matrix]
    else:
        new_size = size // 3
        small_matrices = []
        for i in range(3):
            for j in range(3):
                start_i = i * new_size
                start_j = j * new_size
                small_matrix = [row[start_j:start_j+new_size] for row in matrix[start_i:start_i+new_size]]
                small_matrices.append(small_matrix)
        return small_matrices

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

counts = [0, 0, 0]  # -1, 0, 1 counts

def count_same(matrix):
    global counts
    if is_all_same(matrix):
        counts[matrix[0][0]+1] += 1
    else:
        small_matrices = divide(matrix)
        for small_matrix in small_matrices:
            count_same(small_matrix)

count_same(matrix)

print(counts[0])
print(counts[1])
print(counts[2])
