"""
list = ["Deva","lekka",1,1.2]
print(list)

#access by index
print(list[0]) 

#add element to list
list.append("AI")
print(list)

#insert element at specific index
list.insert(2, "saha")
print(list)

#remove element from list
list.remove("lekka")
print(list)

# removes last item
list.pop()  
print(list)    

for item in list:
    print(item)






"""

"""my_tuple = ("Deva", "lekka", 1, 1.2)
print("Original tuple:", my_tuple)

print(my_tuple[0]) 


for item in my_tuple:
    print(item)
"""






my_dict = {
    "name": "Deva",
    "lastname": "lekka",
    "age": 21,
    "cgpa": 8.5
}

print(my_dict)

# to access value by key
print(my_dict["name"])


#Adding new value to dictionary
my_dict["course"] = "AI & DS"
print(my_dict)


#update value in dictionary
my_dict["age"] = 22
print(my_dict)

#remove key-value pair from dictionary
my_dict.pop("cgpa")
print(my_dict)



#set
my_set = {1, 2, 3, 4, 5}
print(my_set)

#add element to set
my_set = {1, 2, 3}
my_set.add(4)

print(my_set)


#remove element from set
my_set = {1, 2, 3, 4}

my_set.remove(2)
print(my_set)



#union,intersection,difference
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference:", a.difference(b))