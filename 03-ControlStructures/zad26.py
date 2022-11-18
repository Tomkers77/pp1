#pin = int(input("Enter the PIN code: "))
for i in range(3):
    pin = input("Enter the PIN code: ")
    if pin == "0805":
        print("Correct")
        break
    else:
        print("Incorrect...")
        if i ==2:
            print("Sorry, your payment card has been blocked")