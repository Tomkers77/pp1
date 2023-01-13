def f(player1,player2):
    wynik1 = 0
    wynik2 = 0
    
    for i in player1:
        if i =="A" or i=="K" or i=="Q" or i =="J" or i == "T":
            wynik1 +=10
        else:
            wynik1 += int(i)
    
    for i in player2:
        if i =='A' or i=='K' or i=='Q' or i =='J' or i == 'T':
            wynik2 +=10
        else:
            wynik2 += int(i)
    
    if wynik1 > wynik2:
        return True
    else:
        return False

#print(f("AJ972","AQT72"))
#print(f("9532","K8"))
#print(f("987","AT4")) 
