# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Matrix dimensions are not compatible for multiplication."

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            # Initialize the element in the result matrix to 0
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)

    return result

# Example matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12],
]

# Call the function to multiply matrices
result_matrix = multiply_matrices(matrix1, matrix2)

# Display the result
for row in result_matrix:
    print(row)
