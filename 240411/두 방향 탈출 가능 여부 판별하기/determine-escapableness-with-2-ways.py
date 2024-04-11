import sys
sys.stdin = open("C:\\Users\\Be Pious\\Documents\\삼성\\input6.txt", "r")

n, m = map(int, input().split());
x, y = 0, 0

grid = [
    list(map(int, input().split()))
    for _ in (range(n))
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def CanIgo(x, y):
    # Grid을 벗어날 경우 x
    if not in_range(x, y):
        return False;

    # 뱀 있을 경우 x
    if grid[x][y] == 0:
        return False;

    # 방문한적이 있을 경우 x
    if visited[x][y] == 1:
        return False;

    return True;

def DFS(x, y):
    # dx, dy 좌표설정(아래와 오른쪽으로만 갈 수 있음)
    # 아래쪽, 오른쪽
    # 오른쪽, 아래쪽
    dxs, dxy = [1, 0], [0, 1];
    # dxs, dxy = [0, 1], [1, 0];

    for dx, dy in zip(dxs, dxy):
        new_x, new_y = x + dx, y + dy;

        if CanIgo(new_x, new_y):
            visited[new_x][new_y] = 1;
            DFS(new_x, new_y);

# for i in visited:
#     print(i, end=" ")
#     print();
# print();

DFS(0, 0);

# for i in visited:
#     print(i, end=" ")
#     print();
# print(visited);
print(visited[-1][-1]);