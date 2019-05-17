import time
from bstree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# Given Code ==> 7.021290302276611 seconds
# Overall Time: O(n^2) / Space: O(n)

# for name_1 in names_1:  # Time: O(n)
#     for name_2 in names_2:  # Time: O(n)
#         if name_1 == name_2:  # Time: O(1)
#             duplicates.append(name_1)  # Time: O(1)


# BinarySearchTree Otion ==> 0.33395981788635254 seconds
# Overall Time: O(nlog(n)) / Space: O(n)

bst = BinarySearchTree()  # Time: O(1) / Space: O(1)
for name_1 in names_1:  # Time: O(n)
    bst.insert(name_1)  # Time: O(h) ==> O(log(n)) / Space: O(n)
for name_2 in names_2:  # Time: O(n)
    if bst.contains(name_2):  # Time: O(h) ==> O(log(n))
        duplicates.append(name_2)  # Time: O(1)/ Space: O(n)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

