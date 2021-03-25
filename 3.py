distance = 10
n = 7
for i in range(1,n+1):
    if i == 1:
        result = distance
    else:
        distance += distance * 0.1
        result += distance
print('{}'.format('%.6f' % result))