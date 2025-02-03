#prompting the user to input marks between 1-100
marks=int(input("Enter the marks you obtained in your examination:"))

#informing the user that their grade is A
if marks<=100 and marks>=90:
    print("A")
#informing the user that their grade is B
elif marks<=89 and marks>=80:
    print("B")
#informing the user that their grade is C
elif marks<=79 and marks>=70:
    print("C")
#informing the user that their grade is D
elif marks<=69 and marks>=60:
    print("D")
#informing the user that their grade is F
elif marks<60 and marks>=0:
    print("F")
#informing the user that the given input is incorrect
else:
    print("Wrong input")