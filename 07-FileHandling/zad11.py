film_titles = ["Slaby punkt","Ksiegowy","Sully","Avatar","Zaginiona dziewczyna"]
file = open('zad11.txt','w')
for i in range(5):
    file.write(film_titles[i]+"\n")