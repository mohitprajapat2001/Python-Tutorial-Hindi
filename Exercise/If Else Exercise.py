#Difference Between OR and And

# if False and True:
#     print("Correct")

#Exercise 1 : Create a Program to Find Greater Number Takes Two Number From User
# num1 = int(input("Enter Your First Number :"))
# num2 = int(input("Enter Your Second Number :"))
# if num1 > num2:
#     print(f"{num1} is Bigger Than {num2}")
# elif num2 > num1:
#     print(f"{num2} is Bigger Than {num1}")
# else:
#     print("Enter Valid Input")

#Exercise 2 : Find Vowel And Consonents
# test = input("Enter Your Word :")[0]
# if test == 'a' or test == 'A' \
#         or test == 'e' or test == 'E'\
#         or test == 'i' or test == 'I'\
#         or test == 'o' or test == 'O'\
#         or test == 'u00' or test == 'U':
#     print("Word is Vowel")
# else:
#     print("Word is Consonent")

# Exercise 3 : GRade System User Input Assign Student Grade
#Student 91-100 A, 81-90 B, 71-80 C, 61-70 D, F
grade = int(input("Enter Student Marks :"))
if grade < 0 or 100 < grade:
    print("Enter Valid Number Between 0 to 100")
else:
    if 100 >= grade and 90 < grade:
        print("User Grade is A")
    elif 90 >= grade and 80 < grade:
        print("User Grade is B")
    elif 80 >= grade and 70 < grade:
        print("User Grade is C")
    elif 70 >= grade and 60 < grade:
        print("User Grade is D")
    else:
        print("User Grade is F")
