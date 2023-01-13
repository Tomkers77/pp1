person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
}
print(person)

print(person["name"])

print(person['hobby'])

print(person['surname'])
person['surname'] = "Nowak"
print(person["surname"])

person['married'] = False

person['gender'] = 'male'
print(person)

print(person['hobby'])
person["hobby"].append("Basketball")
print(person['hobby'])

person['phone']["work"] = "313131444"

print(person)