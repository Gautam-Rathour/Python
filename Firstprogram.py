





# print(average)

# a = int(input("Enter a Number :- "))
# b = int(input("Enter another Number :- "))

# print(a >= b)
# if(a >= b) {
#     print("True")
# } else {
#     print("False")
# }

# str1 = "This is a boy"
# str2 = 'This is good boy'
# str3 = """This is a very good boy . \nBut he is not a Honest boy"""

# print(str3)
# final_str = str1 + " " + str2
# print(len(final_str))
# print(final_str)
# print(str1[:4])
# print(str1[5:])

# print(len(str1))
# print(str1[-13:-1])












###===================================================================================================
###===================================================================================================


# str = "i am gautam rathour , from Bihar"

# # endswith :-
# print(str)
# print(str.endswith("Bihar"))

# # capitalize :- 
# str = str.capitalize()
# print(str)
# print(str)

# # replace :-
# str = "i am from gautam from rathour , from Bihar"
# print(str.replace("gautam", "Saurabh"))

# # find :-
# str = "i am gautam rathour , from Bihar"
# print(str.find("rathour"))

# # count :- 
# str = "i am from gautam from rathour , from Bihar"
# print(str.count("from"))

## ======= Question :- ===========================
# name = input("Enter first name :- ")

# length = len(name)
# print(length)

# str = input("enter a string :- ")
# str = str.count("$")
# print(str)

###===================================================================================================
###===================================================================================================

## Conditional Statements :- 

# age = 19
# if(age >= 18):
#     print("Yes you can vote")
# else:
#     print("No you can not cast vote")


# light = "green"
# if(light == "green"):
#     print("You can go")
# elif(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("You have to wate")

# marks = 85
# if(marks >= 90):
#     print("Grade - A")
# elif(marks >= 80):
#     print("Grade - B")
# elif(marks >= 70):
#     print("Grade - C")
# else:
#     print("Grade - D")


# # Nasting :- 

# age = 13

# if(age >= 18):
#     if(age >= 80):
#         print("Cant drinve")
#     else:
#         print("Can drive")
# else:
#     print("Cant drive")

###===================================================================================================
###===================================================================================================

# # Question :-
# num = 66
# if(num % 2 == 0):
#     print(num , " This number is Even")
# else:
#     print(num , " This number is Odd")

# # Question :-
# num1 = input("Enter the num1 :- ")
# num2 = input("Enter the num2 :- ")
# num3 = input("Enter the num3 :- ")
# num4 = input("Enter the num4 :- ")


# if(num1 > num2 and num1 > num3 and num1 > num4):
#     print("num1 is greater" , num1)
# elif(num2 > num1 and num2 > num3 and num2 > num4):
#     print("num2 is greater :- " , num2)
# elif(num3 > num1 and num3 > num2 and num3 > num4):
#     print("num3 is greater :- " , num3)
# else:
#     print("num4 is greater :- " , num4)

# # Question :-
# num = int(input("Enter a number :- "))

# if(num % 7 == 0):
#     print("yes it is multiple of 7 " , num)
# else:
#     print("No, it is not multiple of 7 " , num)

###===================================================================================================
###===================================================================================================
###===================================================================================================
###===================================================================================================

##  List & Tuple :-

# marks = [34.3, 37.5, 56.2, 63.3, 93.2, 25.9]
# print(marks)
# print(type(marks))
# print(marks[1])
# print(marks[3])
# print(len(marks))


# # Lists are mutable :-
# student = ["Saurabh", 34 , "Bihar"]
# print(student)
# print(type(student))

# student[0] = "Raju"
# print(student)
# print(len(student))

# student1 = [34.3, 37.5, 56.2, 63.3, 93.2, 25.9]
# print(len(student1))
# print(student1[-3:])

###===================================================================================================
###===================================================================================================



### List Methodes :-
# list = ["a","f","c","g","b"]
# list.append(h)
# print(list)

## Sort in ascending order :-
# print(list.sort())
# print(list)

## Sort in descending order :-
# print(list.sort(reverse=True))
# print(list)

## reverse :-
# list.reverse()
# print(list)

## insert :-
# list1 = [1,3,4,6,]
# list1.insert(1,2)
# list1.insert(4,5)
# print(list1)
# print(len(list1))

## removes first occurrence of element :-
# list = [2,1,2,3,1]
# list.remove(2)
# print(list)

# # delete element at idx :-
# list = [2,1,2,3,1]
# list.pop(4)
# print(list)

### tupls :- 
# tup = (2,1,3,1)
# print(type(tup))
# # print(tup[0])
# print(tup[0:3])

# tup = (1,)
# print(tup)
# print(type(tup))

# tup = (1,2,3,4,9,7,1)
# print(tup.index(7))

# print(tup.count(1))

###===================================================================================================
###===================================================================================================

# # Question :-

# list = [] 
# mov1 = str(input("Enter Your fevorite movies name1 :- "))
# mov2 = str(input("Enter Your fevorite movies name2 :- "))
# mov3 = str(input("Enter Your fevorite movies name3 :- "))

# list.append(mov1)
# list.append(mov2)
# list.append(mov3)

# print(list)
# print(type(list))


# # Question :-

# list1 = ["r", "a", "a", "r", "t" ]

# list1_copy = list1.copy()
# list1_copy.reverse()

# if(list1_copy == list1):
#     print("palindrome")
# else:
#     print("Not Palindrome")

# # # Question :-
# grade = ("C", "D", "A", "A", "B", "B", "A")
# print(grade.count("B"))

# # # Question :-
# list = ["C", "D", "A", "A", "B", "B", "A"]
# print(list)

# list.sort()
# print("This is the sorted list :- " , list)

###===================================================================================================
###===================================================================================================

# length = len("Saurabh Singhtania")

# print("your name has " + str(length) +  " charactors")
# newlenght = str(length)
# print(type(newlenght))
# print(type(length))

# print(10 + 10)
# print(10 + float("10"))

# name = "123"
# print(10 + int (name))

## Question :-
# num1 = input("Enter the first number :- ")
# num2 = input("Enter the second number :-")

# print(int(num1) + int(num2))

###===================================================================================================
###===================================================================================================

# number = input("Enter a two digite number :- ")

# a = number[0] 
# b = number[1]
# print(int(a) + int(b))

###===================================================================================================

# print(5+2*3-1+10//5)

# a = 5
# b = 2
# print(a/b)


# a,b,c= 5,6,7
# print(b)

# a = 5
# a *= 4
# print(a)

# a, b = 4, 3
# c = a + b # 7
# a += 2 #6
# c //= a # 7 + 6
# print(c) ## 13


# a = 5

# print(a==5)
# print(a<=5)
# print(a<5)
# print(a != 6)
# print((a+1) != 6)



###===================================================================================================

# Oprater In Python :- 

# a,b = 3,7
# c = True
# print(a<5 and c )

# a,b = 5,4
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)
# print(a << 2)
# print(a >> 2)


# print(26 & 23)
# print(17 | 24)
# print(17 ^ 24)
# print(~45)
# print(68 << 2)
# print(56 >> 3)



###===================================================================================================
## Identity Operators :-

# a = 7
# b = 7

# print(a is b)
# # print(a is not  b)
# # print(a == b)

# print(id(a))
# print(id(b))

###==========================
## Membership Operators :-

# name = "saurabh kumar"
# print("ku" in name)

# print("T" in name)
# print("T" not in name)
# print("a" not in name)

# l1 = [4,65,34,9,-2,0,23]
# print(-7 not in l1)

# weight = int(input('Enter weight in kg:'))
# height = float(input('Enter height in meter:'))

# bmi = weight / height ** 2

# print(int(bmi))


###=============================
## Round Function :-


# print(round(11.5))
# print(round(12.5))


# print(round(674,2))
# print(round(674,0))
# print(round(674,-2))

# print(round(665,-1))
# print(round(675,-1))

# print(round(-8/3))
# print(round(-1.5))
# print(round(-8/3,2))

# print(round(6.75,1)) # 6.8
# print(round(6.85,1)) # 6.8
# print(round(674.1012,-1)) # 670
# print(round(1212,-2)) # 1200

# print(round(774,-2))
# print(type(round(769,-2)))

# print(round(-8/3))
# print(round(-1.5))
###===================================================================================================

# print("hello raju")

name = "Gaurav"
age = 30
height = 1.6

print("my name is: "+name, "I am "+ str(age), "years old")

print("My name is: " , name , "I am " , age , "years old" )

###===================================================================================================
###===================================================================================================






















































