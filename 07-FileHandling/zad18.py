import shutil

with open("MeatAndFish.txt",'r') as file1:
    with open("GrainsAndBread.txt",'r') as file2:

        with open("shoppinglist1.txt",'w') as plik:
            shutil.copyfileobj(file1,plik)
            shutil.copyfileobj(file2,plik)

file1.close()
file2.close()
plik.close()