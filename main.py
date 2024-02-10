import sys
from matrix import Matrix
from task import Task
from scheduler import Scheduler

def parse_input_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        n = int(lines[0])
        matrix = []
        for i in range(1, n + 1):
            matrix.append([float(x) for x in lines[i].split()])
        vector = [float(x) for x in lines[n + 1].split()]
    return matrix, vector

def get_input_file_name():
    if len(sys.argv) != 3:
        print("Usage: python main.py input_file output_file")
        exit(1)
    return sys.argv[1]

#function given filename and matrix saves matrix to file
def save_matrix_to_file(filename, matrix, result):
    with open (filename, "w") as f:
        f.write(str(len(matrix)))
        f.write("\n")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                f.write(str(matrix[i][j]) + " ")
            f.write("\n")
        for i in range(len(result)):
            f.write(str(result[i]) + " ")

def create_taks_queue(system_size, matrix):
    gauss_tasks = []
    for i in range(system_size):
        cur_tasks_A = []
        cur_tasks_B = []
        cur_tasks_C = []
        for k in range(i+1, system_size):
            cur_tasks_A.append(Task('A', matrix=matrix, i=i, k=k))
            for j in range(i,system_size+1):
                cur_tasks_B.append(Task('B', matrix=matrix, i=i, j=j, k=k))
                cur_tasks_C.append(Task('C', matrix=matrix, i=i, j=j, k=k))
        if len(cur_tasks_A) != 0:
            gauss_tasks.append(cur_tasks_A)
        if len(cur_tasks_B) != 0:
            gauss_tasks.append(cur_tasks_B)
        if len(cur_tasks_C) != 0:
            gauss_tasks.append(cur_tasks_C)
    return gauss_tasks

def back_substitution(matrix):
    n = len(matrix)
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]
        for k in range(i-1, -1, -1):
            matrix[k][n] -= matrix[k][i] * x[i]
    return x

if __name__ == "__main__":
    matrix, vector = parse_input_file(get_input_file_name())
    for i in range(len(vector)):
        matrix[i].append(vector[i])

    equations_system = Matrix(matrix)
    equations_system.print_matrix()
    scheduler = Scheduler(equations_system)
    scheduler.add_tasks(create_taks_queue(len(matrix), equations_system))
    scheduler.run_all_tasks()
    equations_system.print_matrix()
    result = back_substitution(equations_system.matrix)
    save_matrix_to_file(sys.argv[2], equations_system.matrix, result)