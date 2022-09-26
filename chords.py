# method chords
import math


def F(x: float):
    return (x ** 3) - 0.2 * (x ** 2) + 0.5 * x + 1.5


if __name__ == '__main__':
    a: float
    b: float
    e: float
    x: float = 0
    a = float(input("Enter A:"))
    b = float(input("Enter B:"))
    e = float(input("Enter E:"))
    next_x = b
    while True:
        x = next_x
        next_x = x + F(x) * ((x - a) / (F(a) - F(x)))
        if not abs(next_x - x) >= e:
            break
    print(f"Результат: {round(next_x, 4)} +- {e}")
