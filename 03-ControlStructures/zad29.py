i = 1
quan = 0
sum = 0
mean = 0
while i>0:
    num = int(input("Enter number: "))
    quan += 1
    sum += num 
    if num ==0:
        quan -=1
        break
mean = sum/quan
print(f"RESULT: Quantity={quan}, Sum={sum}, Mean={mean}")