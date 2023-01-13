add = input("Podaj nazwe produktu: ")
file = open('shopping.txt','a')
file.write(add+"\n")