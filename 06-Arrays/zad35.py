def rand_elem(array):
    import random
    return array[random.randint(0,len(array)-1)]

for i in range (3):
    print(rand_elem([234,5,67,7,532,5,23,54,5256,7,7,3,3,12]))
    print(rand_elem([523,6,6,7,87,34,3,5,6,7,77,4,3,2,2]))