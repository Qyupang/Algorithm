N = int(input())

count = 0

# 시각
for i in range(N+1):
  # 3시면
  if i == 3:
    count += 60*60
    continue
  # 분
  for j in range(60):
    # 십분대가 3이면
    if j // 10 == 3:
      count += 60
      continue
    # 일분대가 3이면
    elif j % 10 == 3:
      count += 60
      continue
    # 초
    for k in range(60):
      # 십초대가 3이면
      if k // 10 == 3:
        count += 1
        continue
      # 일초대가 3이면
      elif k % 10 == 3:
        count += 1
        continue

print(count)

'''
5
'''