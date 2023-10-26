a = input().split()
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
if a[0] < a[1] <a[2]:
    print('Акция!', (a[0] + a[1] +a[2]) //2)
elif a[2] < a[1] < a[0]:
    print('Акция!', (a[0] + a[1] + a[2])//3)
else:
    print(a[0]+a[1]+a[2]) 
print(1235)