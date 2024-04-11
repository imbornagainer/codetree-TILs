# n = int(input());
#
# grid = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]
#
# visited = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]
#
# people_num = 0;
# vlliage_num = list();
#
#
# def in_range(x, y):
#     return x >= 0 and x < n and y >= 0 and y < n
#
#
# def CanIgo(x, y):
#     if not in_range(x, y):
#         return False;
#
#     if grid[x][y] == 0:
#         return False;
#
#     if visited[x][y] == 1:
#         return False;
#
#     return True;
#
#
# def DFS(x, y):
#     # 1: 상, 2: 하, 3: 좌, 4: 우
#     dsx, dsy = [-1, 1, 0, 0], [0, 0, -1, 1]
#
#     global people_num
#
#     for dx, dy in zip(dsx, dsy):
#         new_x, new_y = x + dx, y + dy;
#
#         if CanIgo(new_x, new_y):
#             visited[new_x][new_y] = 1;
#             people_num += 1;
#             DFS(new_x, new_y);
#
#
# for i in range(n):
#     for j in range(n):
#         if CanIgo(i, j):
#             visited[i][j] = 1
#             people_num = 1;
#             DFS(i, j);
#             vlliage_num.append(people_num);
#
# print(len(vlliage_num));
# vlliage_num.sort();
#
# for i in vlliage_num:
#     print(i);

# n크기의 grid
n = int(input());

# 입력받은 n*n 크기의 정보
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 방문한 적이 있는지 입력하는 칸
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 마을의 정보를 입력받을 리스트
vlliage = [];

# 사람수
people_cnt = 0;


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n;


def CanIgo(x, y):
    if not in_range(x, y):
        return False;

    if visited[x][y] == 1:
        return False;

    if grid[x][y] == 0:
        return False;

    return True;


def DFS(x, y):
    # 1: 상, 2:하, 3:좌, 4:우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    global people_cnt;

    # 마을에 접근했을때 사람만 확인하고 사람이 있는 경우 다시 접근하지 않음. 완전탐색 최적화 완료.
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy;
        if CanIgo(new_x, new_y):
            visited[new_x][new_y] = 1;
            people_cnt += 1;
            DFS(new_x, new_y);

# vlliage = [
#     0 for _ in range(n)
#     0 for _ in range(n)
# ]

# 마을을 전부다 가야하기 때문에 n*n의 for문을 실행
for i in range(n):
    for j in range(n):
        if CanIgo(i,j):
            people_cnt = 1;
            visited[i][j] = 1;
            DFS(i, j);
            vlliage.append(people_cnt);

# 총 마을의 개수
print(len(vlliage));

# 마을의 사람 수만큼 오름차순 정렬
vlliage.sort();

# 마을 수 만큼 마을에 있는 사람들 출력
for i in vlliage:
    print(i);