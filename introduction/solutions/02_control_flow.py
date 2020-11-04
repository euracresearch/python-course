#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# -----------------------------------------------------------------

# 0) define a list
elements = ["a", "b", "c", "d", "e"]
# 1) define a variable with the element in the list that we want to find
lookingfor = "c"
# 2) initialize a position variable
position = None
# 3) initialize a counter
counter = 0
# 4) cycle over the elements in the list
for element in elements:
    # 5) check if the element in the list is equal to the element that you are looking for
    if element == lookingfor:
        # 6) if is equal save the position
        position = counter
    # 7) increase the counter
    counter += 1
# 8) print the element and the position
print(f"Element {lookingfor!r} is in position: {position}")


# -----------------------------------------------------------------

elements = ["a", "b", "c", "d", "e"]

lookingfor = "c"
position = None
counter = 0
while counter < len(elements):
    element = elements[counter]
    if element == lookingfor:
        position = counter
    counter += 1
print(f"Element {lookingfor!r} is in position: {position}")

# -----------------------------------------------------------------

elements = ["a", "b", "c", "d", "e"]

lookingfor = "c"
position = None
counter = 0
while counter < len(elements):
    element = elements[counter]
    if element == lookingfor:
        position = counter
        break
    counter += 1
print(f"Element {lookingfor!r} is in position: {position}")

# -----------------------------------------------------------------

elements = ["a", "b", "c", "d", "e"]

lookingfor = "c"

position = None
counter = 0
for element in elements:
    if element == lookingfor:
        position = counter
        break
    counter += 1

print(f"Element {lookingfor!r} is in position: {position}")


# -----------------------------------------------------------------

elements = ["a", "b", "c", "d", "e"]

lookingfor = "c"

position = None
for counter, element in enumerate(elements):
    if element == lookingfor:
        position = counter
        break

print(f"Element {lookingfor!r} is in position: {position}")

# -----------------------------------------------------------------

lst = [3, 5, 2, 1]

sortedlst = [lst[0], ]
for element in lst[1:]:
    added = False
    for i, el in enumerate(sortedlst):
        if element < el:
            sortedlst.insert(i, element)
            added = True
            break
    if added == False:
        sortedlst.append(element)
print(f"From: {lst}   to: {sortedlst}")

# -----------------------------------------------------------------


