# 코딩테스트 with python
# 그리디 알고리즘 예시 3번 (1이 될때까지)
# 내 풀이 과정
n, m = map(int, input().split())

count = 0

while n != 1:
  if n % m == 0:
    n /= m
    count += 1
  else:
    n -= 1
    count += 1

print(count)

'''
25 5
'''