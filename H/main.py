from math import atan
from random import random
from time import time


def arctg(x: float, a: int):
  result = 0
  for n in range(1, a+1):
    result += ((-1)*(n-1))*(x*(2*n-1))/(2*n-1)
  return result

def print_16(x: float, strstart: str):
  print(f"{strstart} {x:.16f}")
  return

if __name__ == "__main__":
  num = random()
  print("Случайное число: ", num)
  print("="*30)
  for i in range(5, 100, 5):
    start = time()
    atan_result = atan(num)
    print(f"Время для math.atan: {time()-start}")
    print_16(atan_result, "Результат для math.atan:")
    start = time()
    taylor_result = arctg(num, i)
    print(f"Время по Ряду Тейлора: {time()-start}")
    print_16(taylor_result, " Результат по Ряду Тейлора:")
    print("Итерации: ", i)
    print("="*30)

