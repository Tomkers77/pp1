num = int(input("Liczba: "))
array = [15,38,7,23,14]
for i in array:
    if array.count(num) >= 1:
        print(f"Liczba {num} wystepuje w tablicy")
        break
    else:
        print(f"Liczba {num} nie wystepuje w tabicy")
        break