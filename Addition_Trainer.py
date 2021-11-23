#Create a program that automatically genererate 2 random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct number 
#The program will ask the user 10 additional operation
#Display the result summary of the 10 operations (ex 9/10)

#Import random from module
import random

#Generate two random numbers and ask the user to answer the mathematical question
First_Random = random.randint(0,99)
Second_Random = random.randint(0,99)
Sum_1 = First_Random + Second_Random
print(f"{First_Random} + {Second_Random} = ")
First_Sum = int(input("Input Answer: "))
if First_Sum == Sum_1:
    print("Correct")
else:
    print("Wrong")

#Repeat the codeblock nine times to form a ten operations
Third_Random = random.randint(0,99)
Fourth_Random = random.randint(0,99)
Sum_2 = Third_Random + Fourth_Random
print(f"{Third_Random} + {Fourth_Random} = ")
Second_Sum = int(input("Input Answer: "))
if Second_Sum == Sum_2:
    print("Correct")
else:
    print("Wrong")

Fifth_Random = random.randint(0,99)
Sixth_Random = random.randint(0,99)
Sum_3 = Fifth_Random + Sixth_Random
print(f"{Fifth_Random} + {Sixth_Random} = ")
Third_Sum = int(input("Input Answer: "))
if Third_Sum == Sum_3:
    print("Correct")
else:
    print("Wrong")

Seventh_Random = random.randint(0,99)
Eight_Random = random.randint(0,99)
Sum_4 = Seventh_Random + Eight_Random
print(f"{Seventh_Random} + {Eight_Random} = ")
Fourth_Sum = int(input("Input Answer: "))
if Fourth_Sum == Sum_4:
    print("Correct")
else:
    print("Wrong")

Nineth_Random = random.randint(0,99)
Tenth_Random = random.randint(0,99)
Sum_5 = Nineth_Random + Tenth_Random
print(f"{Nineth_Random} + {Tenth_Random} = ")
Fifth_Sum = int(input("Input Answer: "))
if Fifth_Sum == Sum_5:
    print("Correct")
else:
    print("Wrong")

Eleventh_Random = random.randint(0,99)
Twelve_Random = random.randint(0,99)
Sum_6 = Eleventh_Random + Twelve_Random
print(f"{Eleventh_Random} + {Twelve_Random} = ")
Sixth_Sum = int(input("Input Answer: "))
if Sixth_Sum == Sum_6:
    print("Correct")
else:
    print("Wrong")

Thirteen_Random = random.randint(0,99)
Fourtheen_Random = random.randint(0,99)
Sum_7 = Thirteen_Random + Fourtheen_Random
print(f"{Thirteen_Random} + {Fourtheen_Random} = ")
Seventh_Sum = int(input("Input Answer: "))
if Seventh_Sum == Sum_7:
    print("Correct")
else:
    print("Wrong")

Fifteen_Random = random.randint(0,99)
Sixteen_Random = random.randint(0,99)
Sum_8 = Fifteen_Random + Sixteen_Random
print(f"{Fifteen_Random} + {Sixteen_Random} = ")
Eight_Sum = int(input("Input Answer: "))
if Eight_Sum == Sum_8:
    print("Correct")
else:
    print("Wrong")

Seventeen_Random = random.randint(0,99)
Eighteen_Random = random.randint(0,99)
Sum_9 = Seventeen_Random + Eighteen_Random
print(f"{Seventeen_Random} + {Eighteen_Random} = ")
Nineth_Sum = int(input("Input Answer: "))
if Nineth_Sum == Sum_9:
    print("Correct")
else:
    print("Wrong")

Nineteen_Random = random.randint(0,99)
Twenty_Random = random.randint(0,99)
Sum_10 = Nineteen_Random + Twenty_Random
print(f"{Nineteen_Random} + {Twenty_Random} = ")
Tenth_Sum = int(input("Input Answer: "))
if Tenth_Sum == Sum_10:
    print("Correct")
else:
    print("Wrong")

#Count the correct answers from the user and display, showing the overall score over ten
Correct = [First_Sum == Sum_1, Second_Sum == Sum_2, Third_Sum == Sum_3, Fourth_Sum == Sum_4, Fifth_Sum == Sum_5, Sixth_Sum == Sum_6, Seventh_Sum == Sum_7, Eight_Sum == Sum_8, Nineth_Sum == Sum_9, Tenth_Sum == Sum_10]
Right_Answer = sum(Correct)
print(f"Your overall score is: {Right_Answer}/10")