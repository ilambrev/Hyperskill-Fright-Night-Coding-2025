from collections import deque

file_path = "hyperskill-dataset-117518495.txt"

file = open(file_path, "r")
map = file.read().strip().split("\n")
file.close()

start_point_sign = "P"
destination_point_sign = "G"
wall_sign = "#"
walkable_floor_sign = "."
visited_floor_sign = "V"
destinations = {0: "U", 1: "D", 2: "L", 3: "R"}

def is_cell_valid(row, col, n, m, mat, visited):

    return (row >= 0 and row < n and 
           col >= 0 and col < m and 
           mat[row][col] != wall_sign and 
           not visited[row][col] == visited_floor_sign)

def find_point_coorinates(mat, point_sign):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == point_sign:
                return [i, j]
            
def shortest_path(mat):
    n = len(map)
    m = len(map[0])
    p = find_point_coorinates(mat, start_point_sign)
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]

    visited = [[walkable_floor_sign for _ in range(m)] for _ in range(n)]

    q = deque()

    q.append([p[0], p[1], ""])

    visited[p[0]][p[1]] = visited_floor_sign

    while q:
        curr = q.popleft()

        row = curr[0]
        col = curr[1]
        dist = curr[2]

        if mat[row][col] == destination_point_sign:
            return dist

        for i in range(4):
            currenr_destination = destinations[i]
            new_row = row + d_row[i]
            new_col = col + d_col[i]

            if is_cell_valid(new_row, new_col, n, m, mat, visited):
                visited[new_row][new_col] = visited_floor_sign
                q.append([new_row, new_col, dist + currenr_destination])

    return -1

print(shortest_path(map))