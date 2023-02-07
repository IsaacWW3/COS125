
# Task 1
int(5.999)  # this is 5
float(1//2)  # 0.0
int(1.2) - int(True)  # 0
float(str(1.5))  # 1.5
float(7+bool(7.2))  # 8.0

# Task 2
x = 0
if x > 1:
    x = 1
elif 1 > x > -1:
    x = 0
else:
    x = -1

y = 10
if 20 > y > 10:
    print("yes")
else:
    print("no")

a = 10
b = 11
c = 12

if a == b or a == c:
    print("Correct")
else:
    print("Incorrect")

t = float(5.001)
if t - int(t) == 0:
    print("int")
else:
    print("float")



i = 0
j = 0
k = 1
if i == 0 and j == 0 and k == 1:
    print('True')
elif i == 0 and j == 1 and k == 0:
    print('True')
elif i == 1 and j == 0 and k == 0:
    print('True')
else:
    print("False")

# Task 3
x = 0
while x != 10:
    x += 1
    print(x)

y = 10
while y != 0:
    y -= 1
    print(y)

user_input = 'm'
while user_input != 'q' or user_input != 'Q':
    user_input = input("Please enter a letter: ")
    if user_input == 'n' or user_input == 'N':
        print('Starting new game')
    elif user_input == 'l' or user_input == 'L':
        print("Loading save game")
    elif user_input == 'q' or user_input == 'Q':
        print("Thanks for playing!")
        break

b = 0

nbm = 0
while b != 1000:
    b += 1
    nb = b % 2
    if nb == 1:
        nbm = nbm + b
print(nbm)

# Task 4
cash = 1.5
if int(cash)*2.0 != int(cash *2.0):
    print("The devil is in the details") # it will print this because int cash @ 2.0 is a float where as in the paraenthesis is int

    temp = 40
    if temp < 40:
        print(" It is cold . ")
    elif temp < 70:
        print(" It is mild . ")  # It will print this because it comes first
    elif temp < 90:
        print(" It is hot . ")
    else:
        print(" It is unbearable . ")


#  the issue with this code is that val is never declared
if val < 0:
    print(" Negative ")
elif val > 0:
    print(" Positive ")
