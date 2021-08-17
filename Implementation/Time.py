# n = int(input())

# hour = 0
# minute = 0
# second = 0

# count_list = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
# result = 0

# for i in range(60*60*(n+1)-1):
#     second += 1
#     if 60 <= second:
#         second = 0
#         minute += 1
#     if 60 <= minute:
#         minute = 0
#         hour += 1

#     if hour in count_list:
#         result += 1
#     elif minute in count_list:
#         result += 1
#     elif second in count_list:
#         result += 1

# print(result)

##########################

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)


'''
C++의 경우 문자열로 처리하기에는 애매하여
bool check(int h, int m, int s) {
    if (h%10 == 3 || m/10 == 3 || m%10 == 3 || s/10 ==3 || s%10 == 3)
        return true;
    return false;
}
위처럼 검증하여 처리
'''