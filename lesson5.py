proceeds = int(input('Введите количество выручки - '))
costs = int(input('Введите количество издержек - '))

if proceeds > costs:
    print('Ваша фирма работает с положительным финансовым результатом.')
    profit = proceeds - costs
    profitability = int((profit / proceeds) * 100)
    quantity = int(input('Введите количество сотрудников фирмы - '))
    profit_for_quanity = int(profit / quantity)
    print('Общая выручка вашей компании -', profit, 'Рентабельность выручки вашей компании -', profitability, '%', 'Прибыль фирмы в расчете на одного сотрудника -', profit_for_quanity)
else:
    if proceeds == costs:
        print('Ваша фирма работает с нейтральным финансовым результатом.')
    else:
        print('Ваша фирма работает с отрицательным финансовым результатом.')

