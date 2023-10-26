a = input().split()
a[0] = int(a[0])
a[1] = int(a[1])
if a[1] >=8 and a[1] <= 22:
    if (a[1] >= 10 and a[1] <= 12) or (a[1] >= 20 and a[1] <= 22):
        print(a[0]//2)
    else:
        print(a[0])
else:
    print('Время работы оконченно')