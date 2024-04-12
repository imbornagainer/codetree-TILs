n, m = map(int, input().split());

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(m)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n;

def CanIgo(x,y):
    # 범위에 벗어나면 False
    if not in_range(x,y):
        return 0;

    # 가본 곳이면 False
    if (visited[x][y] == 1):
        return 0;

    # 뱀이 있으면 False
    if (grid[x][y]) == 0:
        return 0;

    return True;

def DSF(x,y):
    # 상,하,좌,우
    # dxs, dys = [0,1],[1,0];
    # dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy;

        if CanIgo(new_x, new_y):
            visited[new_x][new_y] = 1
            DSF(new_x,new_y);

visited[0][0];

DSF(0,0);

# for row in visited:
#     for element in row:
#         print(element, end=" ")
#     print();

print(visited[n-1][m-1])