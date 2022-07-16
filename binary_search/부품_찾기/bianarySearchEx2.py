# 코딩테스트 with python
# 이진 탐색 예시 1번 (부품 찾기)
# 내 풀이 과정

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return True
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return False

num_store = int(input())

store_list = list(map(int, input().split()))

store_list.sort()

num_client = int(input())

client_list = list(map(int, input().split()))

for i in client_list:
  result = binary_search(store_list, i, 0, num_client)
  if result:
    print('yes', end=' ')
  else:
    print('no', end=' ')

'''
5
8 3 7 9 2
3
5 7 9
'''