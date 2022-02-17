import threading
# from multiprocessing import Pool
# from multiprocessing import Process, 
from multiprocessing import Manager
import numpy as np

def check_factor(buffer, num, factor):
  if num % factor == 0:
    buffer.append(factor)
    if factor == 1 or factor == (num//factor):
      pass
    else:
      buffer.append(num//factor)
      #print(num//factor)
    #print(factor)
    

if __name__ == "__main__":
  N = int(input("Number: "))
  P = int(input("Number of threads: "))

  if int(N**0.5) >= P:
    t = [[] for _ in range(P)]
  else: t = [[] for _ in range(int(N**0.5))]

  shared_arr = Manager().list()

  i = 1
  while(i <= int(N**0.5)):
    for j in range(len(t)):
      t[j] = threading.Thread(target= check_factor, args= (shared_arr, N, i, ))
      t[j].start()
      i += 1

    for j in range(len(t)):
      t[j].join()

  shared_arr = np.unique(shared_arr)  # Double check so that only unique value appears
  #print(shared_arr)

  if N == sum(shared_arr):
    print(bool(True))
  else: print(bool(False))