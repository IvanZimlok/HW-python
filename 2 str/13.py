a = input().split()# разделяю масив на разные слова
for i in range(len(a)):# перебераю каждое слово
    if a[i].find('@') != -1: # если есть @ вывожу и заканичваю программу
        print(a[i])
        break