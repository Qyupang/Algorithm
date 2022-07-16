from collections import deque

def bfs(x, y):
  s

graph = []

x, y = map(int, input().split())

for _ in range(y):
  graph.append(list(map(int, input().split())))


for i in range(y):
  for j in range(x):
    bfs(i, j)
