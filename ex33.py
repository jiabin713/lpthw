#ex33: While Loops

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

# def while_func(max_num):
#     i = 0
#     numbers = []

#     while i < max_num:
#         print(f"At the top i is {i}")
#         numbers.append(i)

#         i = i + 1
#         print("Numbers now: ", numbers)
#         print(f"At the bottom i is {i}")

#     print("The numbers: ")

#     for num in numbers:
#         print(num)


# print(while_func(6))