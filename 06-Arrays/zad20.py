def star(n):
    print(n,": ",end="")
    for i in range(n):
        print("*",end="")
    print()

array = [12,6,4,9,10]
for j in array:
    star(j)
