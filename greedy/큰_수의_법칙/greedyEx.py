# 코딩테스트 with python
# 그리디 알고리즘 예시 1번 (큰 수의 법칙)
# 내 풀이 과정
N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))

x = sorted(num_list)

max_repeat = M % K

next_repeat = M // K

result = x[N-1] * max_repeat * K + x[N-2] * next_repeat

print(result)

# 입력예시
'''
5 8 3
2 4 5 4 6
'''