data = input()
list = []
total = 0

for char in data:
    if char.isalpha():
        list.append(char)
    else:
        total += int(char)

list.sort()

if total != 0:
    list.append(str(total))

print(''.join(list))