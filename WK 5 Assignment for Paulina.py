print('Assignment number 1')
print('...........\
.............')
cities = ('Lagos', 'Kano', 'Abuja', 'Warri')
empty_list = []
for city in cities:
    empty_list.append(city)
print(empty_list)
    
print('Assignment number 2 and 3')
print('............\
............')
States = {'Lagos' : 'Ikeja', 'Imo' : 'Owerri', 'Delta' : 'Asaba'}

for State in States:
    print((States[State], 'Is the capital of', State))

    
print('Assignment number 4')
print('..............\
..............')
names = {'Pauline' : 25, 'Esther' : 26, 'John' : 30, 'Peace' : 15, 'Joy' : 18}
list1 = []
for name in names:
    list1.append(names[name])
    p = names[name]
    q = len(name)
    meanAges = p/q
print(list1)
print('The mean age is', meanAges)


print('Assignmnet number 5')
print('..............\
...............')

dictionary = {'Sarah' : 20,
              'Praise': 12,
              'Joy' : 25,
              'Sam' : 5,
              'Isaac' : 19,
              'Peter' : 6,
              'Paul' : 8,
              'Dave' : 22,
              'Felix' : 28,
              'Ruth' : 9
              }

adults = []
children = []
adultDic = {}
childrenDic = {}
print(dictionary)
for key, value in dictionary.items():
    if value >= 18:
        adultDic[key] = value
print('adultDic', adultDic)
for key, value in dictionary.items():
    if value < 18:
        childrenDic[key] = value
print('childrenDic', childrenDic)
for key in dictionary:
    if dictionary[key] >= 18:
        adults.append(dictionary[key])
        x = dictionary[key]
        y = len(key)
        meanAdult = x/y
    if dictionary[key] < 18:
        children.append(dictionary[key])
        a = dictionary[key]
        b = len(key)
        meanChildren = a/b
print('adults ages are', adults)
print( 'children ages are', children)
print('The mean of adults is', meanAdult)
print('The mean of children is', meanChildren)
    
    
    




