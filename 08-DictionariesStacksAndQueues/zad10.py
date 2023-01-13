countries = [
{
    "name": 'Poland',
    "population": 124412,
},
{
    "name": "Wlochy",
    "population": 32523632, 
}  
]

lenght = len(countries)
while lenght:
    for i,j in countries[lenght-1].items():
        print(i,":",j)
    print()

    lenght=lenght-1     