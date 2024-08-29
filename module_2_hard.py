# Дополнительное практическое задание по модулю: "Основные операторы"
# Задание "Слишком древний шифр":

# Вывод паролей для одного, вводимого числа
def pairs():
    result = []
    for i in range(1, 20):
        for j in range(i + 1,20):
            suma = i + j
            if number % suma == 0:
                result.append(i)
                result.append(j)
    print (number,' - ', *result)
    return pairs

number = int(input('Введите число от 3 до 20:'))
if 2 < number < 21:
    pairs()
else:
    print ('Введено неверное число')

# Вывод всех паролей для чисел от 3 до 20:
"""
for i in range(3,21):
    result = []
    for j in range(1, 20):
        for k in range (j + 1, 20):
            if i % (j + k) == 0:
                result.append(j)
                result.append(k)
                break
    print(i, ' - ', *result)
"""



