C = [[0.2, 0, 0.2, 0, 0],
    [0, 0.2, 0, 0.2, 0],
    [0.2, 0, 0.2, 0, 0.2],
    [0, 0.2, 0, 0.2, 0],
    [0, 0, 0.2, 0, 0.2]]

D = [[2.33, 0.81, 0.67, 0.92, -0.53],
    [-0.53, 2.33, 0.81, 0.67, 0.92],
    [0.92, -0.53, 2.33, 0.81, 0.67],
    [0.67, 0.92, -0.53, 2.33, 0.81],
    [0.81, 0.67, 0.92, -0.53, 2.33]]

b = [4.2, 4.2, 4.2, 4.2, 4.2]

def countMatrix():
    result = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

    for i in range(len(C)):
        result[i].append(b[i])
        for j in range(len(C[0])):
            result[i][j] = C[i][j] + D[i][j]
    return result

def is_singular(matrix):
    for i in range(len(matrix)):
        if not matrix[i][i]:
            return True
    return False

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def solve_gauss(matrix):
    n = len(matrix)
    for k in range(n - 1):
        for i in range(k + 1, n):
            div = matrix[i][k] / matrix[k][k]
            matrix[i][-1] -= div * matrix[k][-1]
            for j in range(k, n):
                matrix[i][j] -= div * matrix[k][j]

    if is_singular(matrix):
        print('The system has infinite number of answers...')
        return

    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, n)])) / matrix[k][k]

    print(x)
    for i in range(len(x)):
        a = str(toFixed(x[i],4))
        print("x{} = {}".format(i+1,a))

def main():
    result = countMatrix()
    for row in result:
        print(row)
    solve_gauss(result)   

if __name__ == "__main__":
    main()