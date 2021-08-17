###
# n, k = map(int, input().split())
# count = 0

# while n != 1:
#     if n % k == 0:
#         n /= k
#     else:
#         n -= 1
#     count += 1

# print(count)

####################################

n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k
    result += (n - target)
    n = target

    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 탈출
    if n < k:
        break

    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

'''
아래 방법으로 처리하면 1씩 빼는 과정과 나누는 연산을 한번에 처리하여
O(logN)으로 빠르게 처리가 가능하게 된다.
'''