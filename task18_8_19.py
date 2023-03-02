total_cost = 0
tickets = int(input('Введите количество приобретаемых билетов: '))
for i in range(tickets):
    i += 1
    age = int(input(f'Введите возраст посетителя с билетом № {i}: '))
    if age < 18:
            print('Стоимость билета - 0 руб.')
    elif 18 <= age < 25:
            total_cost += 990
            print('Стоимость билета - 990 руб.')
    else:
            total_cost += 1390
            print('Стоимость билета - 1390 руб.')

if tickets > 3:
    discount = total_cost / 100 * 10
    total_cost = total_cost - discount
    print(f'Сумма к оплате - {total_cost} руб. (скидка - {discount} руб.)')
else:
    print(f'Сумма к оплате - {total_cost} руб.')

