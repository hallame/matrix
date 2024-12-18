class Matrix:
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


    def __init__(self, rows, cols):
        # Initialize a matrix with zero values
        self.rows = rows
        self.cols = cols
        self.data = [[1.0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, i, j, value):
        """Set a value at index (i, j) in the matrix."""
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.data[i][j] = value
        else:
            raise IndexError("Index out of bounds")

    def get_value(self, i, j):
        """Get the value at index (i, j) in the matrix."""
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.data[i][j]
        else:
            raise IndexError("Index out of bounds")

    def add(self, other):
        """Add two matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def multiply_by_scalar(self, scalar):
        """Multiply the matrix by a scalar."""
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * scalar
        return result

    def multiply(self, other):
        """Multiply two matrices."""
        if self.cols != other.rows:
            raise ValueError("Number of columns of the first matrix must equal the number of rows of the second matrix")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum_value = 0
                for k in range(self.cols):
                    sum_value += self.data[i][k] * other.data[k][j]
                result.data[i][j] = sum_value
        return result

    def print(self):
        """Print the matrix."""
        for row in self.data:
            print()
            print("\t\t".join(map(str, row)))
        print()
