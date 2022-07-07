marks = int(input("Enter the students score"))
if marks >= 70 and marks <=100:
    print("Congrats!! you scored grade A")
elif marks > 60 and marks <= 69:
    print("you scored grade B")
elif marks > 50 and marks <= 59:
    print("you scored grade C")
elif marks > 40 and marks <= 49:
    print("you scored grade D")
elif marks > 0 and marks <= 39:
    print("you scored grade D")
else:
    print("This is an invalid score!!")