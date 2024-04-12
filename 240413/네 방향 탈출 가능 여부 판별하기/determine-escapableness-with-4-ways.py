from collections import deque

# 변수 선언 및 입력
N, M = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

v = [
    [0 for _ in range(M)]
    for _ in range(N)
]

q = deque()

# # 주어진 위치가 격자를 벗어나는지 여부를 반환합니다.
# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < m


# # 주어진 위치로 이동할 수 있는지 여부를 확인합니다.
# def can_go(x, y):
#     return in_range(x, y) and a[x][y] and not visited[x][y]


# def bfs():
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
#             if can_go(new_x, new_y):
#                 q.append((new_x, new_y))
#                 visited[new_x][new_y] = 1

                
# # bfs를 이용해 최소 이동 횟수를 구합니다.
# # 시작점을 queue에 넣고 시작합니다.
# q.append((0, 0))
# visited[0][0] = 1

# bfs()

# # 우측 하단을 방문한 적이 있는지 여부를 출력합니다.
# # answer = 1 if visited[n - 1][m - 1] else 0
# # print(answer)
# for i in visited:
#     print(i, end = " ")
#     print()

def bfs(si,sj):
    # [1] q, v[], 필요 자료형 생성
    # q = deque()
    # v = [[0]*N for _ in range(N)]
    # tlst = []

    # [2] q에 초기데이터(들) 삽입, v표시
    q.append((si,sj))
    # v[si][sj]=1
    # eat = 0

    while q:
        ci,cj = q.popleft()     # q에서 데이터 한개 꺼냄
        # eat == v[ci][cj]      # eat에 적힌 거리는 모두 리스트에 넣었음(방문)
        # if eat==v[ci][cj]:
        #     return tlst, eat-1

        # 4방향, 범위내, 미방문, 조건(나보다 같거나 작은 물고기면)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and grid[ni][nj]==1:
                q.append((ni,nj))
                v[ni][nj]=1
                # v[ni][nj]=v[ci][cj]+1
                # 나보다 작은 물고기인경우 tlst에 추가
                # if shark > arr[ni][nj] > 0:
                #     tlst.append((ni,nj))
                #     eat = v[ni][nj]

    # 방문을 모두 끝낸경우(먹을 물고기 못찾음..)
    # return tlst, eat-1

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     for j in range(N):
#         if arr[i][j]==9:    # 아기상어
#             ci,cj = i,j
#             arr[i][j]=0

# shark = 2
# cnt = ans = 0

# while True:
bfs(0,0)

for i in v:
    print(i, end = " ")
    print()
#     tlst, dist = bfs(ci,cj)
#     if len(tlst)==0:        # 더이상 먹을 물고기 없는 경우
#         break
#     # tlst.sort(key=lambda x: (x[0],x[1]))
#     tlst.sort()
#     ci,cj = tlst[0]
#     arr[ci][cj]=0           # 물고기 먹기
#     cnt+=1
#     ans+=dist
#     if shark==cnt:          # 크기만큼 물고기 먹은경우 크기+1
#         shark+=1
#         cnt=0
# print(ans)