class Task:
    def __init__(self, type, matrix, i, k, j=-1,):
        self.type = type
        self.system = matrix
        self.i = i
        self.j = j
        self.k = k

    def pereform_task(self):
        k = self.k
        i = self.i
        j = self.j
        matrix = self.system.matrix
        m = self.system.m
        n = self.system.n

        if self.type == 'A':
            m[k][i] = matrix[k][i] / matrix[i][i]
        elif self.type == 'B':
            if j == -1:
                print('j is not defined')
                assert False
            n[k][j] = matrix[i][j] * m[k][i]
        elif self.type == 'C':
            if j == -1:
                print('j is not defined')
                assert False
            matrix[k][j] = matrix[k][j] - n[k][j]
        else:
            raise Exception('Unknown task type')

    def print_task(self):
        print(self.type, self.i+1, self.j+1, self.k+1)
