
# # age= int(input())
# # if age<18:
# #     print('you are ready')
# # else:
# #     print('still updedraction required')

# # car=int(input())
# # if car>100:
# #     print('rash driving')
# # elif car<60:
# #     print('well speed')
# # else:
# #     print('slow down')


# # n1=input('enter the first number')
# # n2=input('enter the second number')
# # op=input('enter operator')

# # if op =='+':
# #     if n1 == 56 and n2 == 9:
# #      print(77)
# #     else: 
# #        print(n1+n2)
# #     if op == '*':
# #        if n1 == 45 and n2 ==3:
# #           print(555)
# #        else:
# #           print(n1*n2)
          
          

# n1 = int(input("Enter 1st number: "))
# n2 = int(input("Enter 2nd number: "))
# op = input("Enter the operation you want to perform: ")
# if op == '+':
#     if n1 == 56 and n2 == 9:
#         print('77')
#     else:
#         print(n1 + n2)
# elif op == '-':
#     print(n1 - n2)
# elif op == '*':
#     if n1 == 45 and n2 == 3:
#         print('555')
#     else:
#         print(n1 * n2)
# elif op == '/':
# #     if n1 == 56 and n2 == 6:
# #         print('4')
# #     else:
# #         print(n1 / n2)


# a=(9,7.7,"ture")
# a.append()
# print(a)

# nl = []

# # Iterate through numbers from 1500 to 2700 (inclusive)
# for x in range(1500, 2701):
#     # Check if the number is divisible by 7 and 5 without any remainder
#     if (x % 7 == 0) and (x % 5 == 0):
#         # If the conditions are met, convert the number to a string and append it to the list
#         nl.append(str(x))

# # Join the numbers in the list with a comma and print the result
# print(" , ".join(nl))

#Write a program that takes a traffic light color ("Red", "Yellow", "Green") 
# as input and prints the action required: "Stop", "Slow Down", or "Go". For any other input, print "Invalid Color"

# traffic=input(str())
# if traffic=="stop":
#     print("stop")

# color = input("Enter traffic light color: ").strip().capitalize()  
# #strip input ka starting or last wala space hata deta hai 
# # string ka pehla letter capital bake small

# if color == "Red":
#     print("Stop")
# elif color == "Yellow":
#     print("Slow Down")
# elif color == "Green":
#     print("Go")
# else:
#     print("Invalid Color")

#Write a program that checks whether an input integer is Positive, Negative, or Zero

# number=int(input())

# if number>0:
#     print('positive')
# elif number<0:
#  print('negative')
# else:
#     print('zero')

# Write a program to determine if a given year is a leap year.
# Rule: A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.
    
#Ek number input lo aur batao Even hai ya Odd.

# n = int(input())
# if n % 2== 0:
#     print('even')
# else: 
#     print('odd')



#Do numbers input lo aur bada number print karo.

# n1 = input('enter first number')
# n2 = input("enter second number")

# if n1>n2:
#     print('larger number')
# else: n1<n2
# print('smaller number')

#Marks input lo.

# 33 ya usse zyada → Pass
# Warna → Fail

# marks = int(input())

# if marks >= 33:
#     print('pss')
# else: 
#  print('fail')

#Ek character input lo aur batao vowel hai ya consonant.

# ch = input()

# if ch in ('a,e,i,o,u'):
#     print('vowel')
# else:
#     print('consonant')

#Teen numbers me se sabse bada number print karo.

# a = int(input()) #1
# b = int(input()) #2
# c = int(input()) #3

# if a>=b and a>=c:
#     print(a)   
# elif  b<=a and b<=c:
#  print(b)
# else: 
#  print(c)

# Marks ke according grade print karo.

# 90–100 → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → Fail

# marks =int(input())

# if  marks >=90:
#     print('grade A')
# elif marks >= 80:
#     print('grade B')
# elif marks >= 70:
#     print('grade C')
# elif marks >=60:
#     print('grade D')
# else:
#     print('fail')

# Year input lo aur check karo leap year hai ya nahi.

# year = int(input())

# if year%400 == 0 or (year%4 == 0 and 100 !=0):
#     print(' leap ')
# else:
#     print('not leap')

# Number 3-digit hai ya nahi.

#n = int(input())
# for i in range(n): 
#     for j in range(n): 
#         print(i, j)

# for i in range(n):
#     for j in range(i, n):
#         print(i, j)

# for i in range(1,n):
#     # for j in range(1,i*i):
#         print(i,j)

# guesses number = 5
# input= int(input(' enter the guesses number' ))
# while (True):

# n=18
# number_of_guesses=1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses<=9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses,"no.of guesses he took to finish.")
#         break
#     print(9-number_of_guesses,"no. of guesses left")
#     number_of_guesses = number_of_guesses + 1

# if(number_of_guesses>9):
#     print("Game Over")


# pc = 100
# print("please guess a number")
# k = int(input())
# while(True):
#     if k>pc:
#         print("\n",k,"is too much please reduce a bit\n")
#         k= int(input())
#         continue
#     elif k<pc:
#         print("\n",k,"is very low. please raise a little\n")
#         k =  int(input())
#         continue
#     if k==pc:
#         print("\n",k,"congrats you entered correct answer\n")
#         print("Game over !")
#         break

n=19
number_of_guess = 1
print('number of guesses is limited to 9 times\n')
while(True):
    number_of_guess<=6
    guess_number= int(input('guess the number'))
    if guess_number<n:
        print('guess number is low\n')
    elif guess_number>n:
        print('guess number is larger')
    else:
        print('you won')
        print(number_of_guess,'no of guesses he took to finish')
        break
    print(6-number_of_guess, 'number of guess is left')
    number_of_guess = number_of_guess + 1

    if(number_of_guess>9):
        print('game over')



