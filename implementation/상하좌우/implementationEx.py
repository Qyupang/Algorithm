# 코딩테스트 with python
# 구현 알고리즘 예시 1번 (상하좌우)
# 내 풀이 과정
N = int(input())
direction_list = list(input().split())

x = 1
y = 1

for direction in direction_list:
    # 오른쪽으로 가면 y를 1 증가 but 최대 길이를 넘지 않도록
  if direction == 'R' and y < N + 1:
    y += 1
    # 왼쪽으로 가면 y를 1 감소 but 최소 길이를 넘지 않도록
  elif direction == 'L' and y > 1:
    y -= 1
    # 아래로 가면 x를 1 증가 but 최대 길이를 넘지 않도록
  elif direction == 'D' and x < N + 1:
    x += 1
    # 위쪽으로 가면 x를 1 감소 but 최소 길이를 넘지 않도록
  elif direction == 'U' and x > 1:
    x -= 1

print(x, y)

'''
5
R R R U D D
'''