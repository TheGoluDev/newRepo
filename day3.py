students = [
    {"name": "Golu", "roll": 22, "marks": 90000000000020},
    {"name": "ABhishek", "roll": 23, "marks": 60000000000},
    {"name": "Piyush", "roll": 30, "marks":309000000000},
    {"name": "chhote", "roll": 445, "marks":323}
]

name_input = input("Enter student name to search:\n").strip().lower()
roll_input = input("\nEnter student roll to search:     ehdvehwefv\n")

result = ""
isPass = False


for one_student in students:

    if(one_student['name'].strip().lower() == name_input and one_student['roll'] == int(roll_input)):
        
        result = f"{one_student['name']} got {one_student['marks']} Marks!!!"

        if(one_student["marks"] > 30):
            isPass = True

        break

if(result):
    print(result)
    if(isPass):
        print("\nCongrats!! You have passed the exam!")
    else:
        print("\nSorry to say, You have failed!!!")

else:
    print("\nMarks not found. Please Check 'Roll' or 'Name' again.")