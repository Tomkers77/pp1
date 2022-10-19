import random


rzut_1 = random.randint(1,6)
#print(rzut_1)
liczba = input("\nZgadnij ile oczek wypadlo na kostce: ")
print(int(liczba) == rzut_1,"\n")