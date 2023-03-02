import mathlib
import random as r

"""
@file profiling.py
@brief functions for profiling includes writing to file and calculation of deviation

"""

def writeToFile(count):
  """
  @brief opening file "data.txt" and writing random number into it
  @param count number of random numbers (in range 0-1000) to write to file

  """
  file = open("data.txt", "w")
  for i in range(count):
    x = r.randint(0, 1000)
    string = str(x) + " "
    file.write(string)
  file.close()


def deviation():
  """
  @brief calculating standard deviation from input

  """
  x2 = 0
  sampleList = []
  count = 0
  while(count <= 1000):
    try:
      i = input()
    except EOFError:
      break
    for x in i.split():
      x = float(x)
      sampleList.append(x)
      x2 = mathlib.add(x2, x) #x2 + x
      count += 1

  #N = len(sampleList)
  x = mathlib.div(x2, len(sampleList)) #x2/N

  s = 0
  sumx = 0
  for xi in sampleList:
    power = mathlib.power(xi, 2) #xi**2
    sumx = mathlib.add(power, sumx) #sumx + xi**2

  power = mathlib.power(x, 2) #x**2
  mul = mathlib.mul(power, len(sampleList)) #x**2 * N
  sub = mathlib.sub(sumx, mul) #sumx - N*x**2

  subN = mathlib.sub(len(sampleList), 1) #N-1
  div = mathlib.div(1, subN) #1/(N-1)
  mul2 = mathlib.mul(div, sub) #(1/(N-1)) * sumx

  s = mathlib.sqrt(mul2) #sqrt((1/(N-1)) * sumx)
  return s

#writeToFile(1000)
x = deviation()
print(x)
