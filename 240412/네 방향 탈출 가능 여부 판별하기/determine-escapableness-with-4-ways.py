from collections import deque

n, m = map(int, input().split());

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

q = deque()

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m;

def CanIgo(x,y):
    # 범위에 벗어나면 False
    if not in_range(x,y):
        return 0;

    # 뱀이 있으면 False
    if (grid[x][y]) == 0:
        return 0;
    
    # 가본 곳이면 False
    if (visited[x][y] == 1):
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

# def bfs():
#     # queue에 남은 것이 없을때까지 반복합니다.
#     while q:
#         # queue에서 가장 먼저 들어온 원소를 뺍니다.
#         x, y = q.popleft()
        
#         # queue에서 뺀 원소의 위치를 기준으로 4방향을 확인해봅니다.
#         # dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
#         dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
#         # dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 1]
#         # dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

#         for dx, dy in zip(dxs, dys):
#             new_x, new_y = x + dx, y + dy
        
#             # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
#             # 새로 queue에 넣어주고 방문 여부를 표시해줍니다.
#             if CanIgo(new_x, new_y):
#                 q.append((new_x, new_y))
#                 visited[new_x][new_y] = 1

                
# # bfs를 이용해 최소 이동 횟수를 구합니다.
# # 시작점을 queue에 넣고 시작합니다.
# q.append((0, 0))
# visited[0][0] = True

# bfs()

# # 우측 하단을 방문한 적이 있는지 여부를 출력합니다.
# print(visited[-1][-1])