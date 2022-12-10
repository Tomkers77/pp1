num = [2,3,7,5,4]
print("a",num)
print("b",len(num))
print("c",num[0])
print("d",num[1])
print("e",num[len(num)-1])
print("f",num[-2])
print("g",num[0]+num[-1])
print("h",num[len(num)//2])

print("i",end=" ")
for i in num:
    print(i,end=" ")

print()

print("j",end=" ")
for j in range(len(num)//2+1):
    print(num[j],end=" ")
