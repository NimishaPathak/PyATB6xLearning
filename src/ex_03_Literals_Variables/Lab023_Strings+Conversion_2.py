name = "This is a big line"
print(type(name))

# name = name + 1 # will give error as string concatenation of string & int is not allowed
# print(type(name)) # will give error as string concatenation of string & int is not allowed

name = name + str(1)
print(type(name))

first_name = "test"
last_name = "abc"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))