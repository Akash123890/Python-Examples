# 1 -> initialization
# 2 -> condition
# 3 -> increment or decrement

# x = 1
# while x <= 10:
#     print(x, "-> Manoj")
#     x += 1  # x = x + 1

# print(x)

# x = 10
# while x >= 1:
#     print(x)
#     x -= 1

# counter = 0
# pass1 = input("Enter you password : ")

# while True:
#     if pass1 == "Password":
#         print("You are successfully Login...")
#         break
#     elif counter == 4:
#         print("You try max attempt ")
#         break
#     else:
#         counter += 1
#         pass1 = input("Enter you password : ")


# using while loop print 2 to 20 table

# nested while loop

x = 2
while x <= 20:
    y = 1
    while y <= 10:
        print("{:3}".format(x * y), end="   ")
        y += 1
    print()
    x += 1
