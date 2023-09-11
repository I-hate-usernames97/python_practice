# age = 20
# price = 19.95
# first_name = "chris"
# is_online = False
# print('Hello World', age)
#
# birth_year = input("what is your birth year? ")
#
# age = 2023 - int(birth_year)
#
# print(age)

# first_num = float(input("enter a number: "))
# second_num = float(input("enter a second number: "))
# sum =str(first_num + second_num)
# print("the sum is: " + sum)

# course = "Python for Beginners"
# print("Python" in course)
#  print(course)
#
# x = 10
# x += 3
# x = (10 + 3) * 2
# print(x)

# x = 3 > 2
# print(x)
# x = 3 <= 2
# print(x)

# price = 30
# print(price > 10 or  price < 30)

# temp = int(input("what's it the temp outside? "))
#
# if temp > 86:
#     print("It's a hot day")
#     print("Drink lots of water")
# elif temp > 68:
#     print("It's a nice day")
#     print("But you should still drink water")
# elif temp > 41:
#     print("it's a bit cold")
# else:
#     print("it's cold")
# print("done")

weight = int(input("enter your weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print(" Weight in Lbs:" + str(converted))
else:
    converted = weight * 0.45
    print(" Weight in Lbs:" + str(converted))
