
vertices = 8
start = 0
edge = [[0,1,5], [1,3,-3], [1,5,2], [2,6,-5], [3,2,7], [3,8,-3], [6,7,2], [7,2,4], [8,4,1]]

distance = [float('inf')]*(vertices+1)
distance[start] = 0
for i in range(vertices):
    for u, v, w in edge:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            distance[v] = distance[u] + w

print(distance)
#[0, 7, 9, 13, 11, 19]
#[0, 5, 9, 2, 0, 7, 4, 6, -1]