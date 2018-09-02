def transpose(l):
    r = len(l)
    c = len(l[0])

    matrix = [[0 for _ in range(r)] for _ in range(c)]

    for i in range(r):
        for j in range(c):
            matrix[j][i]=l[i][j]

    return matrix

l=[[1,1,1],[2,2,2],[3,3,3]]
print(transpose(l))