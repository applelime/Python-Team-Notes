n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

# target은 1~n번째까지 더한 값 + 1임. 다음 수가 이 수 보다 크다면 현재 수를 만들 수 없으므로 break 후 print
