# 1. Сформировать список из N членов последовательности. Для N=5: 1, -3, 9, -27, 81 b т.д.
print(f"Task1")
def swing(N):
    result=[]
    for i in range(0,N):
        result.append((-3)**i)
    return(result)
print(swing(5))

# 2. Пользователь задает две строки. Определить кол-во вхождений одной строки в другой.
#---

# 3. Подсчитать сумму цифр в вещественном числе.
print(f"Task3")
n = int(input("Введите число: "))
suma = 0
while n > 0:
    digit = n % 10
    suma = suma + digit
    n = n // 10
print("Сумма равна: ", suma)

# 4. Написать программу получающую набор произведений чисел от 1 до N.
print(f"Task4")
n=int(input())
import math
f = math.factorial(n)
print(f)
