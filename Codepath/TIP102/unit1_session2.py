'''
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed.
The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, 
the function should return the original string.
'''

# def reverse_sentence(sentence):
#     sentence_list = sentence.split(" ")
#     return " ".join(sentence_list[::-1])

# sentence = "tubby little cubby all stuffed with fluff"
# sentence1 = "Pooh"
# print(reverse_sentence(sentence))
# print(reverse_sentence(sentence1))
    
'''
In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. 
She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. 
Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number 
from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.
Return the selected integer.
'''
# def goldilocks_approved(nums):
#     if len(nums) < 2:
#         return -1
    
#     min_num = min(nums)
#     max_num = max(nums) 

#     for i in nums:
#         if i != min_num and i != max_num:
#             return i
#         else:
#             return -1
    
# nums = [3, 2, 1, 4]
# nums1 = [1, 2]
# nums2 = [2, 1, 3]
# print(goldilocks_approved(nums))
# print(goldilocks_approved(nums1))
# print(goldilocks_approved(nums2))


'''
Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers hunny_jar_sizes, 
write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty. 
Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.
'''

# def delete_minimum_elements(hunny_jar_sizes):
#     return sorted(hunny_jar_sizes)

# hunny_jar_sizes = [5, 3, 2, 4, 1]
# hunny_jar_sizes1 = [5, 2, 1, 8, 2]
# print(delete_minimum_elements(hunny_jar_sizes))
# print(delete_minimum_elements(hunny_jar_sizes1))	
	

'''
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.
bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! 
Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.
'''

# def final_value_after_operations(operations):
#     count = 1
#     for i in operations:
#         if i == "bouncy":
#             count += 1
#         elif i == "flouncy":
#             count += 1
#         else:
#             count -= 1
#     return count
      

# operations = ["trouncy", "flouncy", "flouncy"]
# operations1 = ["bouncy", "bouncy", "flouncy"]
# print(final_value_after_operations(operations))
# print(final_value_after_operations(operations1))

'''
Given an array of strings words and a string s, implement a function is_acronym() that returns True 
if s is an acronym of words and returns False otherwise.
The string s is considered an acronym of words if it can be formed by concatenating the first character 
of each string in words in order. For example, "pb" can be formed from ["pooh"", "bear"], but it can't be formed from ["bear", "pooh"].
'''
		
# def is_acronym(words, s):
#     acr = []
#     for i in range(len(words)):
#         str = words.pop(0)
#         acr.append(str[0])
#     acr = "".join(acr)
#     print(acr)
#     return acr == s

# words = ["christopher", "robin", "milne"]
# s = "crm"
# print(is_acronym(words, s))

'''
Write a function make_divisible_by_3() that accepts an integer array nums. In one operation, you can add or 
subtract 1 from any element of nums. Return the minimum number of operations to make all elements of nums divisible by 3.
'''

# def make_divisible_by_3(nums):
#     count = 0
#     for i in nums:
#         if (i + 1) % 3 == 0 or (i -1 ) % 3 == 0:
#             count += 1
#     return count

# nums = [1, 2, 3, 4]
# nums1 = [3, 6, 9]
# print(make_divisible_by_3(nums))
# print(make_divisible_by_3(nums1))

'''
Given two lists lst1 and lst2, write a function exclusive_elemts() that returns a new list that 
contains the elements which are in lst1 but not in lst2 and the elements that are in lst2 but not in lst1.
'''
        
# def exclusive_elemts(lst1, lst2):
# 	combined = []
# 	for i in lst1:
# 		if i not in lst2:
# 			combined.append(i)
# 	for i in lst2:
# 		if i not in lst1:
# 			combined.append(i)
# 	return combined

# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["piglet", "eeyore", "owl"]
# lst1a = ["pooh", "roo"]
# lst2a = ["piglet", "eeyore", "owl", "kanga"]
# lst1b = ["pooh", "roo", "piglet"]
# lst2b = ["pooh", "roo", "piglet"]
# print(exclusive_elemts(lst1, lst2))
# print(exclusive_elemts(lst1a, lst2a))  
# print(exclusive_elemts(lst1b, lst2b))  

'''
Write a function merge_alternately() that accepts two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
'''

# def merge_alternately(word1, word2):
#     merge = []
#     i, j = 0, 0
#     while i < len(word1) and j < len(word2):
#         if i <= j:
#             merge.append(word1[i])
#             i += 1
#         else:
#             merge.append(word2[j])
#             j += 1
#     merge.append(word1[i:])
#     merge.append(word2[j:])

#     return "".join(merge)

# word1 = "wol"
# word2 = "oze"
# word1a = "hfa"
# word2a = "eflump"
# word1b = "eyre"
# word2b = "eo"
# print(merge_alternately(word1, word2))
# print(merge_alternately(word1a, word2a))
# print(merge_alternately(word1b, word2b))

'''
Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the 
right proportion. Write a function good_pairs() that accepts two integer arrays pile1 and pile2 where each integer represents the length 
of a stick. The function also accepts a positive integer k. The function should return the number of good pairs.
A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1
'''

# def good_pairs(pile1, pile2, k):
# 	count = 0
# 	for i in pile1:
# 		for j in pile2:
# 			if i % (j*k) == 0:
# 				count += 1
# 	return count

# pile1 = [1, 3, 4]
# pile2 = [1, 3, 4]
# k = 1
# pile1a = [1, 2, 4, 12]
# pile2a = [2, 4]
# ka = 3
# print(good_pairs(pile1, pile2, k))
# print(good_pairs(pile1a, pile2a, ka))

