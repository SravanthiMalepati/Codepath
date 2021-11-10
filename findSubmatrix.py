def findSubmatrix(matrix):
    if len(matrix) == 0:
        return [0, 0]
    
    # Find the upper left corner of submatrix
    u, l = 0, 0
    while matrix[u][l]:
        l += 1
        if l >= len(matrix[u]):
            u += 1
            l = 0
            # If reached the end, there is no submatrix
            if u >= len(matrix):
                return [0, 0]

    # Find the down right corner of submatrix
    d, r = len(matrix) - 1, len(matrix[0]) - 1
    while matrix[d][r]:
        r -= 1
        if r < 0:
            d -= 1
            r = len(matrix[0]) - 1
        
    return [r - l + 1, d - u + 1]

print(findSubmatrix([[1,1,1,1,1,1],
[1,1,1,1,1,1],
[1,1,0,0,0,1],
[1,1,0,0,0,1],
[1,1,1,1,1,1]]
))

print(findSubmatrix([[1,1,1,1],
[1,1,1,1],
[1,1,1,1]]
))

print(findSubmatrix([[1,1,1,1],
[1,1,0,1],
[1,1,1,1]]
))