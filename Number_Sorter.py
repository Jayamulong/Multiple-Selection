#Create a program that ask 4 numbers
#Print the 4 numbers from highest to lowest using only if-else statement

# Ask 4 number from users
First = float(input("Insert First Number: "))
Second = float(input("Insert Second Number: "))
Third = float(input("Insert Third Number: "))
Fourth = float(input("Insert Fourth Number: "))

#Display the given numbers
Numbers = [First, Second, Third, Fourth]
print(F"The numbers are: {Numbers}")

#Sort the numbers using the python built-in function sort()
#Use reverse=True to reverse the order from low -> high to high -> low
Numbers.sort(reverse=True)

#Display the outcome
print(Numbers)