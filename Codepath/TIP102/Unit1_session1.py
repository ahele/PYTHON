'''
Write a function welcome() that prints the string "Welcome to The Hundred Acre Wood!".
'''
# def welcome():
# 	print("Welcome to The Hundred Acre Wood!")

# welcome()

'''
Write a function greeting() that accepts a single parameter, a string name, and prints the string
"Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."
'''

# def greeting(name):
# 	print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")
	
# greeting("Michael")
# greeting("Winnie the Pooh")

'''
Write a function print_catchphrase() that accepts a string character as a parameter and prints the catchphrase of the given 
character as outlined in the table below.If the given character does not match one of the characters included above,
print "Sorry! I don't know <character>'s catchphrase!"
'''

# def print_catchphrase(character):
#     if character == "Pooh":
# 	    print("Oh bother!")
#     elif character == "Tigger":
#         print("TTFN: Ta-ta for now!")
#     elif character == "Eeyore":
#         print("Thanks for noticing me.")
#     elif character == "Christopher Robin":
#         print("Silly old bear.")
#     else:
#         print(f"Sorry! I don't know {character}'s catchprase!")

# character = "Pooh"
# character1= "Piglet"
# print_catchphrase(character)
# print_catchphrase(character1)

'''
Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at 
index x in items. If x is not a valid index of items, return None.
'''

# def get_item(items, x):
# 	if x < len(items):
# 		return items[x]
# 	else:
# 		return None
# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# x1 = 5
# print(get_item(items, x))
# print(get_item(items, x1))

'''
Winnie the Pooh wants to know how much honey he has. Write a function sum_honey() that accepts a list of integers hunny_jars and 
returns the sum of all elements in the list. Do not use the built-in function sum().
'''

# def sum_honey(hunny_jars):
# 	sum = 0
# 	for i in hunny_jars:
# 		sum += i
# 	return sum

# hunny_jars = [2, 3, 4, 5]
# hunny_jars1 = []
# print(sum_honey(hunny_jars))
# print(sum_honey(hunny_jars1))

'''
Winnie the Pooh and his friends are playing a game called Poohsticks where they drop sticks in a stream and race them.
They time how long it takes each player's stick to float under Poohsticks Bridge to score each round.

Write a function count_less_than() to help Pooh and his friends determine how many players should move on to the next round of Poohsticks. 
count_less_than() should accept a list of integers race_times and an integer threshold and return the number of race times less than threshold
'''

# def count_less_than(race_times, threshold):
# 	count = 0
# 	for i in race_times:
# 		if i < threshold:
# 			count += 1
# 	return count

# race_times = [1, 2, 3, 4, 5, 6]
# race_times1 = []
# threshold = 4
# print(count_less_than(race_times, threshold))
# print(count_less_than(race_times1, threshold))

'''
Write a function print_todo_list() that accepts a list of strings named tasks. 
The function should then number and print each task on a new line using the format:
'''

# def print_todo_list(task):
# 	print("Pooh's To Dos:")
# 	for i, j in enumerate(task):
# 		print(f"{i+1}.", j)
	
# task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)
# task1 = []
# print_todo_list(task1)


'''
Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. 
Write a function can_pair() that accepts a list of integers item_quantities.
Return True if each number in item_quantities is even. Return False otherwise.
'''
# def can_pair(item_quantities):
#     for i  in item_quantities:
#         if i % 2 != 0:
#             return False
#     return True

# item_quantities = [2, 4, 6, 8]
# item_quantities1 = [1, 2, 3, 4]
# item_quantities2 = []
# print(can_pair(item_quantities))
# print(can_pair(item_quantities1))
# print(can_pair(item_quantities))

'''
Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. 
Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. 
split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.
'''

# def split_haycorns(quantity):
# 	divisors = [i for i in range(1,quantity+1) if quantity % i == 0]
# 	return divisors

# quantity = 6
# quantity1 = 1
# print(split_haycorns(quantity))
# print(split_haycorns(quantity1))

'''
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. 
Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.
'''

# def tiggerfy(s):
# 	check = "tiger"
# 	new_s = []
# 	for i in s.lower():
# 		if i not in check: 
# 			new_s.append(i)
# 	return "".join(new_s)

# s = "suspicerous"
# s1 = "Trigger"
# s2 = "Hunny"
# print(tiggerfy(s))
# print(tiggerfy(s1))
# print(tiggerfy(s2))

'''
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function locate_thistles() that takes in a list of strings items 
and returns a list of the indices of any elements with value "thistle". The indices in the resulting list should be ordered from least to greatest.
'''

# def locate_thistles(items):
# 	thistle_list = []
# 	for i in range(len(items)):
# 		if items[i] == "thistle":
# 			thistle_list.append(i)
# 	return thistle_list

# items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
# items1 = ["book", "bouncy ball", "leaf", "red balloon"]
# print(locate_thistles(items))
# print(locate_thistles(items1))

	

		


        
	

