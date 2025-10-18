class_held = int(input("Enter the number of classes held:"))
class_attended = int(input("Enter the number of class attended by student:"))

#Calculate attendence

attendence = class_held / class_attended * 100
print("Attendence in percentage is:", attendence)

#Updated program to check eligibility

if attendence >= 75:
    print("Student is eligible for exams"):
else:
    print("You are not eligible for exams")
