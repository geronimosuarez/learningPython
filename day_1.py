import platform
import math

# 1st exercise
 
print(platform.python_version())

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Gero'))
print(type('Suarez'))
print(type('Arg'))

# 2nd exercise (did it)

# 3rd exercise


print('this is a tuple', ('Earth', 'Jupiter'))
print('this is a dictionary', {
    'language': 'Python',
    'version': platform.python_version(),
    'knownLanguages': {'Javascript', 'Typescript', 'Golang'}
})

print('Euclidean distance between (2, 3) and (10, 8) is ', math.sqrt((10 - 2)**2 + (8 - 3)**2))