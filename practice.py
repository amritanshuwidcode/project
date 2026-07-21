# #Write a program to print the first 10 natural numbers using a while loop. Each number should be printed on a new line.

# i = 1
# while(i<=12):
#     #i+=1
#     print(i)
#     i+=2

# # #Display numbers from -10 to -1 using for loop

# # for i in range (-10,2):
# #     print(i)

# #Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4.
# for i in range(5):
#     #if i ==3:
#         print(i)
    
# else: 
#     print('done')

# # Calculate the sum of all numbers from 1 to N
# n = int(input("Enter number: "))

# s =0
# for i in range(0 , n+1):
#      s += i
# print(s)

# n=2
# for i in range (1,11):
#     product= n*i
#     print(product)    

# n = int(input("Enter number: "))
# for i in range (1,n+1):
#     cube = i ** 3
#     print(cube , end = '')

# n  = int(input('enter number of rows: '))
# flag = input('enter True or False: ')

# if flag.lower() == 'true':
#     for i in range (1, n + 1):
#         print('x ' * i)

# elif flag.lower() == 'false':
#     for i in range (n, 0, -1):
#         print('x ' * i) 

# else:
#     print('invalid input')
     
#Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.

# list = (1,2,3,4,4,333,1)
# # target = 4
# r = int(input())
# count = 0

# for num in list:
#     if num == r:
#         count+=1
# print(count)

#Given a Python list
#use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).

# list = [1,2,3,4,56,7,8]

# for i in range (len(list)):
#     if i%2!=0:


# #for i in range (1,len(list),2):
#      print(list[i])

#alternate solution

# r= int(input('enter the number of elements: '))
# list=[]

# for i in range(r):
#    value= int(input(f'enter element {i+1}: '))
#    list.append(value)
# print('original list' , list)

# print('element at odd position: ')
# for i in range (len(list)):
#     if i%2!=0:
#      print(list[i]) 
   
#Given a list, iterate it in reverse order and print each element.

# list = [1,2,4,5,7,8]

# # size = len(list) -1

# # for i in range (size , -1 ,-1):
# list.reverse()
# print(list)

#Reverse a string using a for loop (no slicing)

# str = 'amit'
# reversed_str = ''
# for char in str:
#     reversed_str = char + reversed_str
# print(reversed_str)

#Count vowels and consonants in a sentence

# str = ('amrit anshu')
# vowel = 'aeiou'
# v_vowel = 0
# v_consonants = 0

# for char in str:
#     if char.lower() in vowel:
#        v_vowel += 1
#     else:
#         if char != ' ':
#          v_consonants += 1
# print(v_vowel)
# print(v_consonants)        

#Count total number of digits in a number

# number = 7896
# count = 0

# while number != 0:
#     number = number // 10 
#     count += 1
# print(count)

#Write a program to reverse a given integer number (e.g., 76542 should become 24567).

# number = 76542
# reversed = 24

# while number != 0:
#     digit = number % 10
#     reversed = (reversed * 10) + digit
#     number = number // 10
# print(reversed)

#Write a program to find the largest and smallest digit within a given integer 
# (e.g., in 75869, the largest is 9 and the smallest is 5).

# number = 75869
# smallest = 9
# largest = 0

# while number != 0:
#     digit = number % 10

#     if digit > largest:
#         largest = digit
#     if digit < smallest:
#         smallest = digit
#     number = number // 10
# print(smallest)
# print(largest)

# r = 121
# original=r
# reverse = 0

# while r > 0:
#      digit = r % 10
#      reverse = (reverse * 10) + digit
#      r = r // 10
# if original ==reverse:
#     print('its a palindrone number')
# else:
#     print('not a palindrone')

# Write a program to use a loop to find the factorial of a given number (e.g., 5!).
#  The factorial of N is the product of all integers from 1 to N.

# r = int(input('enter a number'))

# for i in range (1,11):
#     product = r  * i
#     print(product)


n= 5

# for i in range (1, n+1):
#      #for j in range (1, i+1):
#       print('x'*i) 


#         print('x',end=' ') 
#     print() 

# for i in range (1,6):
#     for j in range(1,6):
#         print('*', end = '')
#     print()

# for i in range (n , 0 , -1):
#     for j in range (i):
#         print('x',end='')
#     print()   

# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(j,end='')
#     print()

for i in range (n , 0 ,-1):
    for j in range(i ,0, -1):
         print(j,end='')
    print()