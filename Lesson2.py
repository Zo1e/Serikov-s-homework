time = int(input('Введите время в секундах -'))
minutes = int(time / 60)
hours = int(minutes / 60)
seconds = (time % 60)
minutes1 = (minutes % 60)
print(f'Время - {hours} : {minutes1} : {seconds}')



