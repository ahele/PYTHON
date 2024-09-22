# def count_mississippi(limit):
#   for num in range(1, limit +1):
#     print( f"{num} mississippi")

# count_mississippi(5)

'''
Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.
'''

# def swap_ends(my_str):
#     new_str=""

#     if len(my_str) < 2:
#         new_str = my_str

#     if len(my_str) == 2:
#         for i in range(len(my_str)):
#             new_str += my_str[-(i+1)]

#     if len(my_str) > 2:
#         end = my_str[0]
#         start = my_str[-1]
#         mid = my_str[1:(len(my_str)-1)]
#         new_str = start + mid + end
#     return new_str 

# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)

'''
Write a function is_pangram() that takes in a string my_str as a parameter and returns True if the string is a pangram and False if not. A pangram is a sentence containing every letter in the English alphabet.
'''

# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)

# def is_pangram(my_str):
#     alphabet = "qwertyuiopasdfghjklzxcvbnm"
#     for i in alphabet:
#         return i in my_str.lower()

# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))

'''
Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.
'''

# def reverse_string(my_str):
#     new_str = ""
#     for i in range(len(my_str)):
#         new_str += my_str[-(i+1)]
#     return new_str

# my_str = "live"
# print(reverse_string(my_str))

'''
Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.
'''
# def first_unique_char(my_str):
#   id_count = {}
#   for i in my_str:
#       if i in id_count:
#           id_count[i] += 1
#       else:
#           id_count[i] = 1
#   print(id_count)
#   for i in my_str:
#       if id_count[i] == 1:
#         ind = my_str.index(i)
#         return ind
#   return -1

# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))

# def min_distance(words, word1, word2):
#     index_collection1 = [i for i, j in enumerate(words) if j == word1]
#     index_collection2 = [k for k, l in enumerate(words) if l == word2 ]
#     dist = [ ]
#     for x in index_collection1:
#         for y in index_collection2:
#             dist.append(abs(x-y))
#     return sorted(dist)[0]
 

# words = ["the", "quick", "brown", "fox", "jumped", "the"]
# dist1 = min_distance(words, "quick", "jumped")
# dist2 = min_distance(words, "the", "jumped")
# print(dist1)
# print(dist2)

# words2 = ["code", "path", "code", "contribute",  "practice"]
# dist3 = min_distance(words2, "code", "practice")
# print(dist3)


# def sum_of_number_strings(nums):
#     sum = 0
#     for i in nums:
#         sum += int(i)
#     return sum

# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)

# def remove_duplicates(nums):
#     no_dups = {}
#     for i in nums:
#         if i in no_dups:
#             no_dups[i] += 1
#         else:
#             no_dups[i] = 1
#     return list(no_dups.keys())

# nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_duplicates(nums))

# def reverse_only_letters(s):
#     rev = ""
#     for i in range(len(s)):
#         rev += s[-(i+1)]
#     return rev

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)

# def longest_uniform_substring(s):
#     longest={}
#     for i in s:
#         if i in longest:
#             longest[i] += 1
#         else:
#             longest[i] = 1
    
#     largest = None
#     for j in longest.values():
#         if largest == None:
#             largest = j
#         elif largest < j:
#             largest = j
#     print(longest.values())
#     return largest

# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)

# s = "Hello Word"    
# new_s =sorted(s)
# print(new_s)

# nums1 = [1,4,5]
# nums2 = [2,3,6]

# nums1_pointer = 0
# nums2_pointer = 0

# combined = []
# while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
#     if nums1[nums1_pointer] < nums2[nums2_pointer]:
#         combined.append(nums1[nums1_pointer])
#         nums1_pointer += 1
#     else:
#         combined.append(nums2[nums2_pointer])
#         nums2_pointer += 1
# combined.append(nums2[nums2_pointer])
# print(combined)

# nums = [3,1,4,8,1,6]
# for i in range(len(nums) - 2):
#     window = nums[i:i+3]
#     totals = sum(window)
#     print(totals)


# def mergeAlternately(word1, word2):
#     output=[]

#     for i,j in zip(word1,word2):
#         output.append(i)
#         output.append(j)

#     if len(word2) > len(word1):
#         output.append(word2[len(word1):])
#     elif len(word2) < len(word1):
#         output.append(word1[len(word2):])

#     return "".join(output)



# word1="abcd"
# word2 = "pq"
# print(mergeAlternately(word1, word2))


# def is_long_pressed(name, typed):
#   i, j = 0, 0  # Initialize two pointers for name and typed strings

#   while i < len(name) and j < len(typed):
#       if name[i] == typed[j]:
#           i += 1
#           j += 1
#       elif j > 0 and typed[j] == typed[j-1]:
#           j += 1
#       else:
#           return False

#   # If there are still characters left in name, it means not all characters were matched
#   if i < len(name):
#       return False

#   # Check remaining characters in typed to ensure they are all the same as the last character in name
#   while j < len(typed):
#       if typed[j] != name[-1]:
#           return False
#       j += 1

#   return True

# def moves_zeros(nums):
#     left = 0
#     for right in range(len(nums)):
#         if nums[right] != 0:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#     return nums
# nums = [0,1,0,3,12]
# print(moves_zeros(nums))

# l = [ 5, -1]
# y = sum(l)
# print(y)

# Example 1:
# Input: nums = [5, -1, 3, 2, -4], k = 2
# Output:  -3
# Explanation: Explanation: The sublist of length 2 are [5, -1], [-1, 3], [3, 2], and [2, -4]. 
# Their sums are 4, 2, 5, and -2 respectively. The smallest sum among these is -2, which comes from 
# the sublist [2, -4].

# Example 2: 
# Input: nums[4,2,-5,1,3], k =1
# Output: -5
# Explanation: Here the sublist is just one element, smallest element is -5.

# # Complete the 'find_min_sublist_sum' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY nums
# #  2. INTEGER k
# #

# def find_min_sublist_sum(nums, k):


# def create_list(nums, k):
#     n_list=[]
#     for i in range(k):
#         n_list.append(nums[i])
#     return n_list

# nums=[5,-1,3,2,-4]
# print(create_list(nums, 2))

# x=[1,2,3,4]
# y=[4,3,2,1]
# print(x==y)


# def is_subsequence(lst, sequence):
#   for i in lst:
#     if i not in sequence:
#       lst.remove(i)
#   print(lst)
#   return lst == sequence

# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))

# x = [5, 6, 8, 2, 4, 6, 9]
# for i in range(len(x)-1,-1, -1):
#     print(x[i])


# tru = ""
# print(not tru)

# class Node:
#    def __init__(self, value, next_node = None):
#        self.value = value
#        self.next = next_node

# def shuffle(head):
#     lst = []
#     current = head
#     while current:
#         lst.append(current.value)
#         current = current.next
        
    
#     i = len(lst)-1
#     j = len(lst) -2
#     new_head = None
#     while i >= 0 and j >= 0:
#         if i % 2 != 0:
#             new_head=Node(lst[j], new_head)
#             new_head = Node(lst[i], new_head)
#             i -= 2
#             j -= 2
#         else:
#             new_head=Node(lst[j], new_head)
#             new_head = Node(lst[i], new_head)
#             i -= 2
#             j -= 2

# head = Node("a", Node("b"), Node)




# def is_power_of_two(n):
#     if n == 1:
#         return True

#     if n % 2 != 0:
#         return False
#     return is_power_of_two(n // 2)

  
# print(is_power_of_two(12))

# def count_ones(lst):
#   #happy case = [0,1] result = 1
#   #case 2 = [0,0,0,1,1,1,1] result = [4]

#   left_arrow = 0
#   right_arrow = len(lst) - 1
#   count = 0
#   while left_arrow <= right_arrow:
#     middle = (left_arrow + right_arrow)//2
#     if lst[middle] == 1:
#       if lst[middle -1] == 0 or middle == 0:
#         count += len(lst) - middle
#       right_arrow = middle -1
#     else:
#       left_arrow = middle +1 
#   return count    
      
# lst = [0,0,0,0,0,0,1,1,1]
# print(count_ones(lst))

# x = [2]
# print([x[0], x[-1]])

# class TreeNode:
#   def __init__(self, value):
#     self.value = value
#     self.left = None
#     self.right = None

# def add_node(root, value):
#   new_node = TreeNode(value)

#   current = root
#   previous = None

#   while current is not None:
#     previous = current
#     # Increment current pointer

#     if value > current.value:
#       current = current.right
#     else:
#       current = current.left

#   # After the loop is done,
#   # the previous pointer is guaranteed to be pointing at a Node
#   if value > previous.value:
#     previous.right = new_node
#   else:
#     previous.left = new_node

# x = TreeNode(8)
# add_node(x, 10)
# add_node(x, 9)
# add_node(x, 4)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared=[nums**2 for nums in numbers if nums < 5]
# dict_sq = {num : num**2 if num < 5 else num*2 if num > 8 else num//2 for num in numbers }
# print(dict_sq)

# sum_set=set(numbers)
# print(sum_set)



# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union=set1|set2 #{1,2,3,4,5}
# inter= set1 & set2 #{3}
# diff = set1 - set2 #{1,2}
# symm = set1 ^ set2 #{1,2,4,5}
# print(union)
# print(inter)
# print(diff)
# print(symm)

#case1: [1,2,3,5] val = 5 output = [1,2,3]
#case2: [1,2,3] val = 4 output = [1,2,3]
#case3: [2,2,2] val = output = []

# def addfun(n):
#     if n <= 0:
#         return 0
#     if n ==1:
#         return 2
#     return addfun(n-1) + addfun(n-2)

# print(addfun(6))


s = [1,2,3,4,5]
t = [6,7,8,9,10]

dict = {x:y for x,y in zip(s,t)}
print(dict.get(3))






