# def solution(food_times, k):
#     total = sum(food_times)
#     if total<=k:    # 전체 시간을 넘어가면 -1
#         return -1

#     count = len(food_times)         # 전체 음식의 개수
#     index = 0
#     for i in range(k):
#         food_times[index] -= 1      # 음식을 1초간 먹는다.
#         index += 1                  # 다음으로 넘어간다.
#         if count <= index:
#             index = 0
        
#         while food_times[index] <= 0:   # 다음 음식이 없다면 그 다음 음식을 찾는다.
#             index += 1
#             if count <= index:
#                 index = 1

#     return index+1                  # index는 0번부터이므로

# food_times = [3, 1, 2]
# k = 5
# print(solution(food_times, k))

# 1번째 풀이
# 테스트 케이스 28/32
# 효율성 테스트 0점으로 총점 37.5/100..

### 
def solution(food_times, k):
    count = len(food_times)         # 전체 음식의 개수
    index_list = [i for i in range(count)]

    realIndex = 0
    nextIndex = 0
    for i in range(k):
        food_times[realIndex] -= 1          # 음식을 1초간 먹는다.

        if 0 == food_times[realIndex]:      # 음식을 다 먹었으면 해당 리스트에서 제거한다.
            index_list.remove(realIndex)
            nextIndex -= 1                  # 하나 삭제해줬으므로 하나 뒤로 보낸다.

        remainCount = len(index_list)
        if 0 == remainCount:                # 인덱스 리스트가 비어있으면 다 먹은 것
            return -1

        nextIndex += 1                      # 다음 인덱스를 바로 찾는다.
        if remainCount <= nextIndex:        # indexList 범위를 초과했다면 0으로 돌아간다.
            nextIndex = 0

        realIndex = index_list[nextIndex]        # 다음으로 넘어간다.


    return realIndex+1                  # index는 0번부터이므로

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))

# 2번째
# while문을 최대한 줄여보자. 남은 음식이 있는 인덱스 리스트를 가지고 있자.
# 테스트 케이스 32/32. 효율성 0. 총점 42.9

# 전체를 돌지 않는 방법으로 수정해보자..