a = input('Категоря товара: ').lower()
if a == 'продукты':
    price = int(input('Введите цену: '))
    if price <= 100:
        print('Попробуйте нашу выпечку')
    elif price <=500:
        print('Как насчет орехов в шоколаде?')
    else:
        print('Попробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома')