# N : 정점
# M : 간선

n, m = map(int, input().split())

graph = [
    [] for _ in range(n+1)
]

visited = [
    0 for _ in range(n+1)
]

vertex_cnt = 0;

def DFS(vertex):
    global vertex_cnt;

    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = 1;
            vertex_cnt += 1;
            DFS(curr_v);

for i in range(m):
    v1, v2 = tuple(map(int, input().split()));
    graph[v1].append(v2);
    graph[v2].append(v1);

vertex_cnt = 0;
visited[1] = 1;
DFS(1);
print(vertex_cnt);