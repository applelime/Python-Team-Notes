# string = input()

# current = int(string[0]) # 첫번째 숫자
# isChange = False
# count = 1   # 첫번째 숫자의 묶음 수
# count2 = 0  # 두번째 숫자의 묶음 수

# for s in string:
#     if current != int(s): # 숫자가 달라졌을 때
#         current = int(s)
#         if True == isChange:    # 원래대로 돌아오면 기존 카운트 증가
#             isChange = False
#             count += 1
#         else:
#             isChange = True     # 변경되는 경우 두번째 숫자 카운트 증가
#             count2 += 1

# print(min(count, count2))

data = input()
count0 = 0  # 전부 0으로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대한 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번 째 원소부터 모든 원소 확인
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))


# 내가 생각하는 핵심부분. 0, 1의 2가지 경우를 모두 확인하여 최소값을 출력하면 된다.
# 기타. int로 변환할 필요가 없다. 변수명을 명확하게 하자.