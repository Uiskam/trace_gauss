class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = []
        self.n = []
        for i in range(len(self.matrix)):
            self.m.append([0 for j in range(len(self.matrix[i]))])
            self.n.append([0 for j in range(len(self.matrix[i]))])


    def print_matrix(self):
        print("Matrix:")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()

    def print_all(self):
        print("Matrix:")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()
        print("M:")
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                print(self.m[i][j], end=' ')
            print()
        print("N:")
        for i in range(len(self.n)):
            for j in range(len(self.n[i])):
                print(self.n[i][j], end=' ')
            print()