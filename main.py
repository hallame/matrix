# main.py
from matrix import Matrix


"""
Создать класс "Матрица". Класс должен иметь следующие поля:
1) двумерный массив вещественных чисел;
2) количество строк и столбцов в матрице.

Класс должен иметь следующие методы:
1) сложение с другой матрицей;
2) умножение на число;
3) вывод на печать; 
4) умножение матриц 
"""
def user_input_matrix():
    print()
    rows = int(input("Enter the number of rows for the matrix: "))
    cols = int(input("Enter the number of columns for the matrix: "))
    matrix = Matrix(rows, cols)
    print(f"Enter the values for a {rows}x{cols} matrix:")
    for i in range(rows):
        for j in range(cols):
            value = float(input(f"Enter the value for cell ({i}, {j}): "))
            matrix.set_value(i, j, value)
    return matrix

def user_input_scalar():
    scalar = float(input("Enter a scalar value to multiply the matrix: "))
    return scalar

if __name__ == "__main__":
    # matrix = Matrix(2,3)
    # matrix.print()
    print(f"Create Matrix 1")
    matrix1 = user_input_matrix()
    print(f"Create Matrix 2")
    matrix2 = user_input_matrix()

    # Print matrices
    print("\nMatrix 1:")
    matrix1.print()

    print("\nMatrix 2:")
    matrix2.print()

    # Matrix addition
    sum_matrix = matrix1.add(matrix2)
    print("\nSum of Matrix 1 and Matrix 2:")
    sum_matrix.print()

    # Matrix multiplication by scalar
    scalar = user_input_scalar()
    scalar_mult = matrix1.multiply_by_scalar(scalar)
    print(f"\nMatrix 1 multiplied by {scalar}:")
    scalar_mult.print()

    # Matrix multiplication
    product_matrix = matrix1.multiply(matrix2)
    print("\nProduct of Matrix 1 and Matrix 2:")
    product_matrix.print()
