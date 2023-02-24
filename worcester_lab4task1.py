
# Task 1
# The following program will print the sum of all odd and even numbers
# between 1 and 100 (inclusive).

vals = [0,0]
i = 1
j = 2

while i < 100:
    i+=2
    j+=2

    vals[0] += i
    vals[1] += j


print(f"The sum of all even numbers from 1 to 100: {vals[1]}")
print(f"The sum of all odd numbers from 1 to 100: {vals[0]}")

# i flipped the values in the two prints because it was flipped

