""" Красильников Илья
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

client_input = int(input("Введите время в секундах  "))
hh = client_input // 3600
sec = client_input % 60

if client_input < 3600:
    minutes = client_input // 60
else:
    minutes = (client_input % 3600) // 60

print(f"{hh:02} : {minutes:02} : {sec:02}")
