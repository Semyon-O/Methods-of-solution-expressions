# method of Touchment
import math


def F(x: float):
    return math.tan(0.55 * x + 0.1) - (x * x)


def Fd(x: float):
    return (0.55 / math.pow(math.cos(0.55 * x + 0.1), 2)) - 2 * x


if __name__ == '__main__':
    a: float
    b: float
    e: float
    x: float = 0
    a = float(input("Enter A:"))
    b = float(input("Enter B:"))
    e = float(input("Enter E:"))
    next_x = b
    while abs(next_x - x) >= e:
        x = next_x
        next_x = x - (F(x) / Fd(x))
    print(f"Результат: {round(next_x, 3)} +- {e}")



