# num =int(input("enter your number:"))
# if num %2 == 0:
#     print("even numbert")
# else:
#     print("odd number")

# print("Abhishek want pussy but he has only use dogpussy")

# num = int(input("Enter your choice:"))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# while True:
#     name = input("Enter student name (or'exit' to quit):")
#     if name.lower()==():
#         print("Exiting program so keep smile")
#         break
#         print("Exiting program so keep smile ")
#         break
#     num  = int(input(f"Enter marks  for marks {name}:"))
#     if  num <30:
#         print("fail")
#     elif num <60:
#         print("grade D")
#     elif num <75:
#         print("grade C")
#     elif num <85:
#         print("grade B")
#     elif num <100:
#         print("grade A")
#         break
#     else:
#         grade = "invalid marls! please enter between 0 to 100."
#         print(f" {name} got:{grade}  ")

# while True:
#     num = int(input("Enter your choise:"))
#     if num ==1:
#         print("dog")
#     elif num ==2:
#         print("cat")
#     else:
#         print("no more animals")
#         print("exiting the program..... so try again")
#         break


import random

options =[
    "aalu mater ",
    "gobhi ka bhujiya",
    "soyabin ka sabji",
    "panir mashala ",
    "kuchh bhi bna lo yarr",
    "aalu ka partha",
    "kuchh naya try kro"
]
while True:
    day =input("\nEnter a day name(or type 'exit' to quit):").strip().lower()
    
    if day == "exit":
        print("Exeting program .... so keep chill")
        break
    if day in["sunday",
              "monday",
              "tuesday",
              "wednesday",
              "thuresday",
              "friday",
              "saturday"
            ]:
        suggestion = random.choice(options)
    print(f"today is {day.capitalize()} suggestion dish:{suggestion}")
else:
    print("invali number! ..... place Enter the day name lke sunday, monday")