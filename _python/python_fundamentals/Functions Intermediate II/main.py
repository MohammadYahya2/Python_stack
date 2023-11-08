# # first q1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x=[1][0]=15

students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z=[0]['y']=30
print(x)
print(students)
print(sports_directory)

# q2

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for dictionary in some_list:
        output = ""
        for key, value in dictionary.items():
            output += f"{key} - {value}, "
        print(output[:-2])  # To remove the trailing comma and space
iterateDictionary(students) 


# q3
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])
print(students)

# q4.



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key.upper())
        for item in value:
            print(item)



printInfo(dojo)














