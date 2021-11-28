#Create a program that ask 4 numbers
#Print the 4 numbers from highest to lowest using only if-else statement

# Ask 4 number from users
First = int(input("Insert First Number: "))
Second = int(input("Insert Second Number: "))
Third = int(input("Insert Third Number: "))
Fourth = int(input("Insert Fourth Number: "))

#Initials for the Descending Order
Start = 0  
Next = 0
Then = 0
Last = 0

#Sort for Descending Order
if First > Second and First > Third and First > Fourth:
    Start = First
    if Second > Third and Second > Fourth:
        Next = Second
    elif Third > Second and Third > Fourth:
        Next = Third
    elif Fourth > Second and Fourth > Third:
        Next = Fourth
        if Second < Third and Second > Fourth:
            Then = Second
        elif Second > Third and Second < Fourth:
            Then = Second
        elif Third < Second and Third > Fourth:
            Then = Third
        elif Third > Second and Third < Fourth:
            Then = Third
        elif Fourth < Second and Fourth > Third:
            Then = Fourth
        elif Fourth > Second and Fourth < Third:
            Then = Fourth
            if Second < Third and Second < Fourth:
                Last = Second
            elif Third < Second and Third < Fourth:
                Last = Third
            elif Fourth < Second and Fourth < Third:
                Last = Fourth

if Second > First and Second > Third and Second > Fourth:
    Start = Second
    if First > Third and First > Fourth:
        Next = First
    elif Third > First and Third > Fourth:
        Next = Third
    elif Fourth > First and Fourth > Third:
        Next = Fourth
        if First < Third and First > Fourth:
            Then = First
        elif First > Third and First < Fourth:
            Then = First
        elif Third < First and Third > Fourth:
            Then = Third
        elif Third > First and Third < Fourth:
            Then = Third
        elif Fourth < First and Fourth > Third:
            Then = Fourth
        elif Fourth > First and Fourth < Third:
            Then = Fourth
            if First < Third and First < Fourth:
                Last = First
            elif Third < First and Third < Fourth:
                Last = Third
            elif Fourth < First and Fourth < Third:
                Last = Fourth

if Third > First and Third > Second and Third > Fourth:
    Start = Third
    if First > Second and First > Fourth:
        Next = First
    elif Second > First and Second > Fourth:
        Next = Second
    elif Fourth > First and Fourth > Second:
        Next = Fourth
        if First < Second and First > Fourth:
            Then = First
        elif First > Second and First < Fourth:
            Then = First
        elif Second < First and Second > Fourth:
            Then = Second
        elif Second > First and Second < Fourth:
            Then = Second
        elif Fourth < First and Fourth > Second:
            Then = Fourth
        elif Fourth > First and Fourth < Second:
            Then = Fourth
            if First < Second and First < Fourth:
                Last = First
            elif Second < First and Second < Fourth:
                Last = Second
            elif Fourth < First and Fourth < Second:
                Last = Fourth

if Fourth > First and Fourth > Second and Fourth > Third:
    Start = Fourth
    if First > Second and First > Third:
        Next = First
    elif Second > First and Second > Third:
        Next = Second
    elif Third > First and Third > Second:
        Next = Third
        if First < Second and First > Third:
            Then = First
        elif First > Second and First < Third:
            Then = First
        elif Second < First and Second > Third:
            Then = Second
        elif Second > First and Second < Third:
            Then = Second
        elif Third < First and Third > Second:
            Then = Third
        elif Third > First and Third < Second:
            Then = Third
            if First < Second and First < Third:
                Last = First
            elif Second < First and Second < Third:
                Last = Second
            elif Third < First and Third < Second:
                Last = Third

print(Start, Next, Then, Last)