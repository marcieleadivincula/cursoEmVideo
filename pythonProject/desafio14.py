# Conversor de temperaturas
# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
temperatura = float(input('Digite a temperatura: '))

#Kelvin -> Celsius:  C = K - 273
kelvinToCelsius = temperatura - 273
print(f'A temperatura de {temperatura:.2f}K para ºC = {kelvinToCelsius:.2f}')

#Kelvin -> Fahrenheit:  C = (K - 273) x 1,8 + 32
kelvinToFahrenheit = (temperatura - 273) * 1.8 + 32
print(f'A temperatura de {temperatura:.2f}K para ºF = {kelvinToFahrenheit:.2f}')

# Celsius -> Kelvin: K = C + 273
celsiusToKelvin = temperatura + 273
print(f'A temperatura de {temperatura:.2f}ºC para K = {celsiusToKelvin:.2f}')

# Celsius -> Fahrenheit: F = (C x 1,8) + 32/F = (C x 9 / 5) + 32
celsiusToFahrenheit = (temperatura * 1.8) + 32
# Esta fórmula é igual à de cima, pois 9/5=1,8
celsiusToFahrenheit2 = ((temperatura * 9)/5) + 32
print(f'A temperatura de {temperatura:.2f}ºC para ºF = {celsiusToFahrenheit:.2f}')

# Fahrenheit -> Celsius: C = (F - 32)/1,8
fahrenheitToCelsius = (temperatura - 32)/1.8
print(f'A temperatura de {temperatura:.2f}ºF para ºC = {fahrenheitToCelsius:.2f}')

# Fahrenheit -> Kelvin: K = (F - 32) x 5/9 + 273
fahrenheitToKelvin = (temperatura - 32) * 5/9 + 273
print(f'A temperatura de {temperatura:.2f}ºF para K = {fahrenheitToKelvin:.2f}')

# res = 9/5
# print('9/5 = {:.3f}'.format(res))