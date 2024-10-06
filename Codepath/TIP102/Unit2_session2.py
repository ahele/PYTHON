'''
Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with the 
highest conservation priority based on its population.
The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated 
with a species, including its name, habitat, and wild population. The function should return the name of the species with the 
lowest population.
If there are multiple species with the lowest population, return the species with the lowest index.
'''
# def most_endangered(species_list):
#     min_ = float("inf")
#     check = ""
#     for i in species_list:
#         if i["population"]< min_:
#             min_ = i["population"]
#             check = i["name"]
    
#     return check
            
    
        
# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     }
# ]

# print(most_endangered(species_list)) 

'''
As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. 
Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region,
represented by the string observed_species. Each character in observed_species denotes a species observed in the region.
Your task is to determine how many of the observed species are also considered endangered.
Note: Species are case-sensitive, so "a" is considered a different species from "A".
Write a function to count the number of endangered species observed.
'''

# def count_endangered_species(endangered_species, observed_species):
#     count = 0
#     for i in observed_species:
#         if i in endangered_species:
#             count += 1 
#     return count

# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  

'''
In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. 
Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), 
you start your journey at the first observation point (index 0). To make observations in a specific order represented by a 
string observations, you need to move from one point to another.
The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.
Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.
'''

# def navigate_research_station(station_layout, observations):
#     diction = {j:i for i,j in enumerate(station_layout)}
#     time = 0
#     position = 0

#     for j in observations:
#         next_position = diction[j]
#         time += abs(next_position - position)
#         position = next_position

#     return time
    
# station_layout1 = "pqrstuvwxyzabcdefghijklmno"
# observations1 = "wildlife"

# station_layout2 = "abcdefghijklmnopqrstuvwxyz"
# observations2 = "cba"

# print(navigate_research_station(station_layout1, observations1))  
# print(navigate_research_station(station_layout2, observations2))

'''
In your work with a wildlife conservation database, you have two lists: observed_species 
and priority_species. The elements of priority_species are distinct, and all elements in priority_species are also in observed_species.
Write a function prioritize_observations() that sorts the elements of observed_species such that the relative ordering of items in 
observed_species matches that of priority_species. Species that do not appear in priority_species should be placed at the end of observed_species in ascending order.
'''

# def prioritize_observations(observed_species, priority_species):
#     prioritized = []
#     for species in priority_species:
#         prioritized.extend([s for s in observed_species if s == species])
   
#     remaining_species = sorted([s for s in observed_species if s not in priority_species])
#     prioritized.extend(remaining_species)

#     return prioritized

# observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
# priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

# observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
# priority_species2 = ["cardinal", "sparrow", "bluejay"]

# print(prioritize_observations(observed_species1, priority_species1))
# print(prioritize_observations(observed_species2, priority_species2)) 

'''
You are given a 0-indexed integer array species_populations of even length, 
where each element represents the population of a particular species in a wildlife reserve.
As long as species_populations is not empty, you must repetitively:
Find the species with the minimum population and remove it.
Find the species with the maximum population and remove it.
Calculate the average population of the two removed species.
The average of two numbers a and b is (a+b)/2.
For example, the average of 200 and 300 is (200+300)/2=250.
Return the number of distinct averages calculated using the above process.
Note that when there is a tie for a minimum or maximum population, any can be removed.
'''
  
# def distinct_averages(species_populations):
#   averages = set()
#   species_populations.sort()
#   while species_populations:
#     min_pop = species_populations.pop(0)
#     max_pop = species_populations.pop(-1)
#     average = (min_pop+max_pop)/2
#     averages.add(average)
#   return len(averages)
  
# species_populations1 = [4,1,4,0,3,5]
# species_populations2 = [1,100]

# print(distinct_averages(species_populations1))
# print(distinct_averages(species_populations2)) 

