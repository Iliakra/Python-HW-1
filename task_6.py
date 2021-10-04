""" Красильников Илья
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат
спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно
натуральное число — номер дня.
"""

result = int(input("Введите количество километров в первый день (число)  "))
target_result = int(input("Не менее скольки километров должен пробежать спортсмен (число)?  "))
day = 1

while result < target_result:
    result += result * 0.1
    day += 1

print(f"На {day}-й день спортсмен достиг результата — не менее {target_result} км")
