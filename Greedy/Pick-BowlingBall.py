# n, m = map(int, input().split())
# weight = list(map(int, input().split()))
# count = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         if weight[i] != weight[j]:
#             count += 1

# print(count, end-start)

###

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= array[i]           # 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 경우) 제외
    result += array[i] * n  # B가 선택하는 경우의 수와 곱하기

print(result)


## 처음 방식대로 풀 경우, 모든 경우의 수를 돌기에 느리다.
# 아래 방식대로 풀면, 무게가 최대 10이므로 10번만 더하면 되므로 더 효율적이다.
'''
간단 설명.
예시로 무게1-1개, 무게2-2개, 무게3-2개
A가 무게 1인 공을 선택할 때의 경우의 수는 1(무게1 공의수) x 4(B가 선택하는 경우의 수) = 4가지
A가 무게 2인 공을 선택할 때의 경우의 수는 2(무게2 공의수) x 2(B가 선택하는 경우의 수) = 4가지
A가 무게 3인 공을 선택할 때의 경우의 수는 2(무게3 공의수) x 0(B가 선택하는 경우의 수) = 0가지
따라서 총 8가지이다.

-> 
n -= array[i] : 전체 공의 개수에서 무게 1인 공의 수를 뺀다. (B가 선택가능한 경우의 수)
result += array[i] * n : 무게1의 공의수(A) * n (B가 선택가능한 수) 를 더한다.

이렇게 무게2, 무게3, ... 무게 10까지만 하면 된다
'''