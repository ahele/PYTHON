name = input("what is your name? ")
color = input("what is your favourite color? ")
age = int(input("How old are you? "))

# print(name, end=" ")
# print("is " + str(age) + " years old ", end=" ")
# print("and loves " + "color " + color + ".", end="")

print(name, 'is', age, 'years old and loves the color', color, '.', sep=" ")