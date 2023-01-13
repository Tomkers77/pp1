import random

with open("zad20.txt",'w') as file:
     for i in range(1,51):
          file.write(str(random.randint(100,999))+"\n")

file.close()