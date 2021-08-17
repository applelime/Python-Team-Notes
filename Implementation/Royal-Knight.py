# n = input()

# x = int(ord(n[0])) - int(ord('a')) + 1
# y = int(n[1])

# # 왼쪽, 오른쪽 (위 아래), 위, 아래 (왼 오)
# dx = [-1, 1, -1, 1, -2, -2, 2, 2]
# dy = [-2, -2, 2, 2, -1, 1, -1 ,1]

# count = 0
# print("first:", x, y)
# for move in range(len(dx)):
#     newX = x + dx[move]
#     newY = y + dy[move]

#     if newX<1 or newY<1 or 8<newX or 8<newY:
#         continue
#     count += 1

# print(count)

##############

#현재 나이트 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # ord -> 아스키코드로

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향 이동 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치 이동 가능한지 확인
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result += 1

print(result)

'''
C++에서는 위처럼 dx, dy를 따로 정의하는게 더 간결할 수 있음
'''