

a = input("Введите первое число: ")
b = input("Введите второе число: ")
c = input("Введите третье число: ")
print(min(a, b, c), (max(min(a, b), min(b, c))
                     if not
min(a, b) == min(b, c)
                     else min(a, c)), max(a, b, c))
print(max(a, b, c), (min(max(a, b), max(b, c))
                     if not
max(a, b) == max(b, c)
                     else max(a, c)), min(a, b, c))
