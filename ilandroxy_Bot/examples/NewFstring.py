weather = 'облачно'
temperature = 24

print('Сейчас', weather, ', на градуснике', temperature, '.')
# Вывод: Сейчас облачно , на градуснике 24 .

print('Сейчас ' + weather + ', на градуснике ' + str(temperature) + '.')
# Вывод: Сейчас облачно, на градуснике 24.

print('Сейчас {}, на градуснике {}.'.format(weather, temperature))
# Вывод: Сейчас облачно, на градуснике 24.

print('Сейчас %s, на градуснике %d.'%(weather, temperature))
# Вывод: Сейчас облачно, на градуснике 24.

print(f'Сейчас {weather}, на градуснике {temperature}.')
# Вывод: Сейчас облачно, на градуснике 24.