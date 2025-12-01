user_age = int(input("Enter your age: \n"))
if user_age >= 18:
    print("Yes, you can go to GOA and vote")
else:
    print("Not you can't go and can't vote")

print("Yes you can go to GOA and vote" if user_age>=18 else "No you can't go to GOA and vote")

# -----------------------------------
# logic building formula
# step 1 ---> Figure out the inputs and outputs
# input r ---> data type Float
# pi = 3.14
# power ---> pow or ** ---> both are same used to calculate power of the number
# o/p ---> String ---> float - area, print area

# step 2 ---> rough logic = area = 3.14 * pow(r,2)
r_input = float(input("Enter value r: \n"))
area = 3.14*(r_input**2)

# string data formatting, also called python f-strings, formatted string literals
print(f"Area of circle is -> {area:.2f}")