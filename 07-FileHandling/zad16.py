import shutil

with open("sample3.txt",'r') as file:
    with open("copy.txt",'w') as plik:
        shutil.copyfileobj(file,plik)
file.close()
plik.close()