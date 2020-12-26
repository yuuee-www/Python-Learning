str_in = input('Input:')

# 1
count = 0
for i in range(len(str_in)):
    if str_in[i] == str_in[-i - 1]:
        count += 1

if len(str_in) == count:
    print('Yes')
else:
    print('No')

# 2
print('Yes') if str_in == str_in[::-1] else print('No')