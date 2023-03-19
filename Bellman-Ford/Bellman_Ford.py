
vertices = 6
start = 1
edge = [[1,2,7], [1,3,9], [1,5,11], [2,3,6], [2,4,6], [2,6,13], [3,4,5], [3,5,6], [5,2,4] ,[5,4,6], [5,6,8], [6,4,7]]

distance = [float('inf')]*(vertices+1)
distance[start] = 0
for i in range(vertices):
    for u, v, w in edge:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            distance[v] = distance[u] + w

print(distance[1:])
#[0, 7, 9, 13, 11, 19]