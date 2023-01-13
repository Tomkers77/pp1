with open("sample3.txt",'r') as file:
    with open("copylines.txt",'w') as plik:
        for line in file:
            plik.write(line)
file.close()
plik.close()