""" Красильников Илья
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

client_input = int(input("Введите время в секундах  "))
hh = client_input // 3600
minutes = client_input // 60
sec = client_input % 60

print(f"{hh} : {minutes} : {sec}")
