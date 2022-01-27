price = []
ticket = int(input("Введите количество билетов: "))
for i in range(1, ticket + 1):
    age = int(input("Укажите возраст: "))
    if age < 18:
        price.append(0)
    elif 18 <= age <= 25:
        price.append(990)
    else:
        price.append(1390)
if ticket > 3:
    a = sum(price) -  (sum(price) * 0.1)
    print("Сумма вашей покупки со скидкой равна: ", a)
else:
    a = sum(price)
    print("Сумма вашей покупки равна: ", a)