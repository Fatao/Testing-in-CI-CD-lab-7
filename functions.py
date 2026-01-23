import unittest

def sort_array(arr):
    # Отсортируйте массив целых чисел.
    if arr is None:
        raise ValueError("Входной массив не может быть равен None")
    return sorted(arr)

def is_palindrome(s):
    # Проверьте, является ли строка палиндромом.
    if s is None:
        raise ValueError("Входная строка не может быть равна None")
    s = s.lower()
    return s == s[::-1]

def factorial(n):
    # Вычислите факториал неотрицательного целого числа.
    if n < 0:
        raise ValueError(" Нельзя вычислить факториал отрицательного числа")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def fibonacci(n):

    # Верните n-ное число Фибоначчи.
    if n < 0:
        raise ValueError("Отрицательные числа не допускаются")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def find_substring(text, sub):
    # Верните индекс подстроки в тексте (-1, если не найдено).
    if text is None or sub is None:
        raise ValueError("Текст и подстрока не могут быть равны None")
    return text.find(sub)

def is_prime(n):
    # Проверьте, является ли число простым.
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def reverse_number(x):
    # Переверните цифры 32-битного целого числа. Верните 0 в случае переполнения.
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    rev = 0
    while x_abs != 0:
        rev = rev * 10 + x_abs % 10
        x_abs //= 10
    rev *= sign
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    return rev

def to_roman(num):
    # Преобразуйте положительное целое число в римские цифры.
    if num <= 0:
        raise ValueError("Число должно быть положительным")
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman = ""
    for i in range(len(val)):
        while num >= val[i]:
            num -= val[i]
            roman += syms[i]
    return roman


# ------- СЕКЦИЯ ВВОДА ПОЛЬЗОВАТЕЛЯ --------
if __name__ == "__main__":
    print(" Выберите функцию:")

    print("1. Отсортировать массив")
    print("2. Проверить палиндром")
    print("3. Факториал")
    print("4. Число Фибоначчи")
    print("5. Найти подстроку")
    print("6. Проверить простое число")
    print("7. Перевернуть число")
    print("8. Преобразовать в римские цифры")

    choice = int(input("Выберите функцию (1-8): "))

    if choice == 1:
        arr = list(map(int, input("Введите числа через пробел: ").split()))
        print("Отсортированный:", sort_array(arr))
    elif choice == 2:
        s = input("Введите строку: ")
        print("Палиндром?", is_palindrome(s))
    elif choice == 3:
        n = int(input("Введите число: "))
        print("Факториал:", factorial(n))
    elif choice == 4:
        n = int(input("Введите n: "))
        print(f"{n}th Число Фибоначчи:", fibonacci(n))
    elif choice == 5:
        text = input("Введите текст: ")
        sub = input("Введите подстроку: ")
        print("Индекс:", find_substring(text, sub))
    elif choice == 6:
        n = int(input("Введите число: "))
        print("Простое?", is_prime(n))
    elif choice == 7:
        n = int(input("Введите число: "))
        print("Перевернутое:", reverse_number(n))
    elif choice == 8:
        n = int(input("Введите число: "))
        print("Римская цифра:", to_roman(n))
