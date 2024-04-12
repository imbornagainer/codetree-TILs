from collections import deque

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

q = deque();

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m;
    # return 0 <= x and x < n and 0 <= y and y < m

def Can_go(x, y):
    if not in_range(x, y):
        return False;

    if grid[x][y] == 0:
        return False;
    
    if visited[x][y] == 1:
        return False;
    
    return True;

def BFS():   

    while q:
        x, y = q.popleft();

        #상, 하, 좌, 우 (격자는 행, 렬)
        dxs, dys = [-1,1,0,0],[0,0,-1,1]

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy;

            if Can_go(new_x, new_y):
                visited[new_x][new_y] = 1;
                q.append((new_x,new_y));

# def BFS():
#     # queue에 남은 것이 없을때까지 반복합니다.
#     while q:
#         # queue에서 가장 먼저 들어온 원소를 뺍니다.
#         x, y = q.popleft()

#         # queue에서 뺀 원소의 위치를 기준으로 4방향을 확인해봅니다.
#         dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
#         for dx, dy in zip(dxs, dys):
#             new_x, new_y = x + dx, y + dy

#             # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
#             # 새로 queue에 넣어주고 방문 여부를 표시해줍니다.
#             if Can_go(new_x, new_y):
#                 q.append((new_x, new_y))
#                 visited[new_x][new_y] = 1


q.append((0,0));
visited[0][0] = 1;

BFS();

print(visited[-1][-1]);