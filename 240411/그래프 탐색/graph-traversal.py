# Vertices_num = n
# Edges_num = m
n, m = map(int,input().split())

# 정점에 +1를 한 것은 Index를 1부터 시작하기 위해서
graph = [
    [] for _ in range(n+1)
]

# 정점에 대해 방문했는지 확인
visited = [
    0 for _ in range(n+1)
]

Another_vertex = 0;

def DFS(vertex_num):
    global Another_vertex
    for curr_v in graph[vertex_num]:
        if not visited[curr_v]:
            # print(curr_v)
            visited[curr_v] = 1;
            Another_vertex += 1;
            DFS(curr_v);

# for start, end in zip(grid):
#     graph[start].append(end)
#     graph[end].append(start)

# start_points = [1, 1, 2, 4]
# end_points = [2, 3, 3, 5]

# for start, end in zip(start_points, end_points):
#     graph[start].append(end)
#     graph[end].append(start)

for i in range(m):
    v1, v2 = tuple(map(int, input().split()));    
    graph[v1].append(v2)
    graph[v2].append(v1)

Another_vertex = 0;

# 1번 정점은 가지수에서 제외하기 때문에
visited[1] = True;

DFS(1);
print(Another_vertex)