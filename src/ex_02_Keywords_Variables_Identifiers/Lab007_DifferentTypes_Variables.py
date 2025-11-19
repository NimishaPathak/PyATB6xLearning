#123abc = 90 --> not a valid variable name
#_abc = "aaa" --> valid variable name
_dc = 23
pi = 3.14
name = "advef"
isFemale = True

#Type function = gives you details about the data type of the variable --> type()
print(type(_dc)) #output --> <class 'int'>
print(type(pi)) # output --> <class 'float'>
print(type(name)) # output --> <class 'str'>
print(type(isFemale)) # output --><class 'bool'>

# for complex numbers in python, "j" is used.
complex_number = 2+3j
print(complex_number)
print(complex_number.real)
print(complex_number.imag)
print(type(complex_number))
