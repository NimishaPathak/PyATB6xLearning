# take 2 user inputs from the user
# print thr Quotient and Reminder

# for example: 14/2--Q: 7, R: 0
num1 = int(input("Enter first number: "));
num2 = int(input("Enter second number: "));
Quotient_value = int(num1//num2);
Reminder_value = int(num1%num2);
print(Quotient_value);
print(Reminder_value);

print("---")

q, r = divmod(5, 2); #divmod is a function in python which can return multiple argument

# we can assign multiple values as well
a, b, c = 1, 2, 3

print("---")

x = 10
x += 5
print(x) # result: 15

x *=2
print(x) # result: 30