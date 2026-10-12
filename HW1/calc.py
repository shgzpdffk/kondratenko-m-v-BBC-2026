import math #для вычислений инженерного калькулятора

#основной класс калькулятора
class Calculator:
    def __init__(self, name = "Главный класс калькулятора"):
        self.name = name

    def add(self, a, b):
        return a + b

    def dell(self, a, b):
        if b == 0:
            return print("На ноль делить нельзя")
        return a // b

    def razn(self, a, b):
        return a - b

    def umn(self, a, b):
        return a * b

    def voz(self, a, b):
        return a ** b

    def procent(self, a, b):
        return a * b / 100

    def abss(self, a):
        return abs(a)

    def negativ(self, a):
        return -a


#инженерный калькулятор, который наследует атрибуты основного и добавляет свои функции
class EngineeringCalculator(Calculator):
    def __init__(self, name = "Инженерный калькулятор"):
        super().__init__(name)

    def square(self, a):
        return self.voz(a, 2)

    def square_root(self, a):
        if a < 0:
            return print("Нельзя извлечь действительный корень из отрицательного числа")

        return math.sqrt(a)

    def sin(self, angle):
        #градусы необходимо перевести в радианы
        radians = math.radians(angle)
        return math.sin(radians)

    def cos(self, angle):
        radians = math.radians(angle)
        return math.cos(radians)

class UnitCalculator(Calculator):
    def __init__(self, name="Калькулятор единиц"):
        super().__init__(name)

    def cm_to_feet(self, cm):
        # в одном футе 30.48 сантиметра.
        return cm / 30.48

    def feet_to_cm(self, feet):
        return feet * 30.48

    def km_to_miles(self, km):
        # в одной миле 1.609344 километра.
        return km / 1.609344

    def miles_to_km(self, miles):
        return miles * 1.609344

    def kg_to_pounds(self, kg):
        # в одном фунте 0.45359237 килограмма.
        return kg / 0.45359237

    def pounds_to_kg(self, pounds):
        return pounds * 0.45359237


while True:
    print("\nВыберите режим:")
    print("1 — Обычный калькулятор")
    print("2 — Инженерный калькулятор")
    print("3 — Перевод единиц")
    print("0 — Выход")

    mode = input("Ваш выбор: ")

    if mode == "0":
        print("Программа завершена")
        break
    elif mode == "1":
        calc = Calculator()
    elif mode == "2":
        calc = EngineeringCalculator()
    elif mode == "3":
        calc = UnitCalculator()
    else:
        print("Такого режима нет")
        continue

    while True:
        print(f"\n{calc.name}")

        # обычные операции доступны и инженерному калькулятору.
        if mode == "1" or mode == "2":
            print("1 — Сложение")
            print("2 — Вычитание")
            print("3 — Умножение")
            print("4 — Деление с округлением вниз")
            print("5 — Возведение в степень")
            print("6 — Процент от числа")
            print("7 — Модуль числа")
            print("8 — Смена знака")

            if mode == "2":
                print("9 — Квадрат числа")
                print("10 — Квадратный корень")
                print("11 — Синус угла в градусах")
                print("12 — Косинус угла в градусах")

        elif mode == "3":
            print("1 — Сантиметры в футы")
            print("2 — Футы в сантиметры")
            print("3 — Километры в мили")
            print("4 — Мили в километры")
            print("5 — Килограммы в фунты")
            print("6 — Фунты в килограммы")

        print("0 — Вернуться к выбору режима")
        action = input("Выберите действие: ")

        if action == "0":
            break

        # проверяем выбор до ввода чисел.
        if mode == "1":
            allowed = ["1", "2", "3", "4", "5", "6", "7", "8"]
        elif mode == "2":
            allowed = [
                "1", "2", "3", "4", "5", "6",
                "7", "8", "9", "10", "11", "12"
            ]
        else:
            allowed = ["1", "2", "3", "4", "5", "6"]

        if action not in allowed:
            print("Такого действия нет")
            continue

        try:
            if mode == "1" or mode == "2":
                a = float(input("Введите число: "))

                # Для этих операций нужно второе число.
                if action in ["1", "2", "3", "4", "5", "6"]:
                    if action == "6":
                        b = float(input("Введите процент: "))
                    else:
                        b = float(input("Введите второе число: "))

                if action == "1":
                    result = calc.add(a, b)
                elif action == "2":
                    result = calc.razn(a, b)
                elif action == "3":
                    result = calc.umn(a, b)
                elif action == "4":
                    result = calc.dell(a, b)
                elif action == "5":
                    result = calc.voz(a, b)
                elif action == "6":
                    result = calc.procent(a, b)
                elif action == "7":
                    result = calc.abss(a)
                elif action == "8":
                    result = calc.negativ(a)
                elif action == "9":
                    result = calc.square(a)
                elif action == "10":
                    result = calc.square_root(a)
                elif action == "11":
                    result = calc.sin(a)
                elif action == "12":
                    result = calc.cos(a)

            elif mode == "3":
                a = float(input("Введите значение для перевода: "))

                if action == "1":
                    result = calc.cm_to_feet(a)
                elif action == "2":
                    result = calc.feet_to_cm(a)
                elif action == "3":
                    result = calc.km_to_miles(a)
                elif action == "4":
                    result = calc.miles_to_km(a)
                elif action == "5":
                    result = calc.kg_to_pounds(a)
                elif action == "6":
                    result = calc.pounds_to_kg(a)

            print("Результат:", result)

        except ValueError as error:
            print("Ошибка ввода или вычисления:", error)
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        except OverflowError:
            print("Результат слишком большой")