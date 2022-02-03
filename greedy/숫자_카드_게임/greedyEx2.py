# 코딩테스트 with python
# 그리디 알고리즘 예시 2번 (숫자 카드 게임)
# 내 풀이 과정
n, m = map(int, input().split())
maxNum = -1

for i in range(n):
  data = list(map(int, input().split()))
  minNum = min(data)
  if minNum > maxNum:
    maxNum = minNum

print(maxNum)
