import time
from bstree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# Given Code ==> 7.021290302276611 seconds
# Overall Time: O(n^2) / Space: O(n)

# duplicates = []
# for name_1 in names_1:  # Time: O(n)
#     for name_2 in names_2:  # Time: O(n)
#         if name_1 == name_2:  # Time: O(1)
#             duplicates.append(name_1)  # Time: O(1)


# BinarySearchTree Option ==> 0.33395981788635254 seconds
# Overall Time: Average - O(nlog(n)) ; Worst O(n^2) / Space: O(n)

# duplicates = []
# bst = BinarySearchTree()  # Time: O(1) / Space: O(1)
# for name_1 in names_1:  # Time: O(n)
#     bst.insert(name_1)  # Time: O(h) ==> O(log(n)) / Space: O(n)
# for name_2 in names_2:  # Time: O(n)
#     if bst.contains(name_2):  # Time: O(h) ==> O(log(n))
#         duplicates.append(name_2)  # Time: O(1)/ Space: O(n)


# Set Intersections ==> 0.006030082702636719 seconds
# Overall Time: Average - O(n) ; Worst - O(n^2) / Space: O(n)

# duplicates = set(names_1) & set(names_2)

# Sets are a collection of items that are unordered and unindexed but only contain unique items.
# In Python sets are written with curly brackets {"item1", "item2", "item3"}
# Set intersections are useful here because it creates a new set with elements common to set1 and set2
# Intersections have an average case of O(min(len(set1), len(set2)) 
# So here O(n) -> n being the number of names in minimal list
# However, intersecting sets does have a worst case of O(len(set1) * len(set2))
# Which would bring big O back to O(n^2) presuming both files have near the same amount of names
# Either way 0.006 seconds much faster


# Set Add and Check ==> 0.007300853729248047 seconds
# Overall Time: O(2n) -> O(n) / Space: O(n)

duplicates = []
names = set()		# O(1)
for name in names_1:	# O(n)
    names.add(name)	# O(1)
for name in names_2:	# O(n)
    if name in names:	# O(1)
        duplicates.append(name)	# O(1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

