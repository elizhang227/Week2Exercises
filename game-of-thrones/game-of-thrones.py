from characters import characters
from houses import houses
# print(len(characters))
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # print out the key names individually
# # for k in jon_snow:
# #     print(k)

# # print out just the values
# # for k in jon_snow:
# #     print(jon_snow[k])

# print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))

# Characters names start with A

# count = 0
# list_of_characters = []

# for characters in characters:
#     if characters['name'][0] == 'A':
#         list_of_characters.append(characters['name'])
#         count += 1

# print(count) # OR
# print(len(list_of_characters))
# print(list_of_characters) # prints all names with A

# Characters names start with Z

# count = 0

# for characters in characters:
#     if characters['name'][0] == 'Z':
#         count += 1

# print(count)

# How many character are dead?

# count = 0

# for characters in characters:
#     if characters['died'] != "":
#         count += 1

# print(count)

##### Who has the most titles?

# for characters in characters:
#     print(len(characters['titles']))

# How many are Valyrian?

# count = 0

# for characters in characters:
#     if characters['culture'] == 'Valyrian':
#         count += 1
# print(count)

# What actors plays "Hot Pie" (and don't use IMDB)?

# for characters in characters:
#     if characters['name'] == "Hot Pie":
#         print(characters['playedBy'])


###### How many characters are *not* in the tv show?

# count = 0

# for characters in characters:
#     if characters['playedBy'] == "":
#         count += 1
# print(count)


# List of characters with last name Targaryen

# list = []

# for characters in characters:
#     if "Targaryen" in characters['name']:
#         list.append(characters['name'])

# length = len(list)
# print(list)
# print('There are %s people with the last name Targaryen' % length)

# Histogram of the houses

# def letter_counter(str):
#     dict = {}
#     for i in str:
#         if i in dict.keys():
#             dict[i] += 1
#         elif i not in dict.keys():
#             dict[i] = 1
#     return dict

dict = {}
for char in characters:
    if characters["allegiances"] in dict.keys():
        dict[char] += 1
    elif characters['allegiances'] not in dict.keys():
        dict[characters] = 1

print(dict)
