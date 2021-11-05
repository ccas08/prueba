# Lists
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]  # creating a list

len(list)  # returns the number of elements in the list

list1[0]  # returns "Cisco" which is the first element in the list (index 0)

list1[0] = "HP"  # replacing the first element in the list with another value

# Lists - methods
list2 = [-11, 2, 12]

min(list2)  # returns the smallest element (value) in the list

max(list2)  # returns the largest element (value) in the list

list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

list1.append(100)  # appending a new element to the list

del list1[4]  # removing an element from the list by index

list1.pop(0)  # removing an element from the list by index

list1.remove("HP")  # removing an element from the list by value

list1.insert(2, "Nortel")  # inserting an element at a particular index

list1.extend(list2)  # appending a list to another list

list1.index(-11)  # returns the index of element -11

list1.count(10)  # returns the number of times element 10 is in the list

list2 = [9, 99, 999, 1, 25, 500]

list2.sort()  # sorts the list elements in ascending order; modifies the list in place

list2.reverse()  # reverses the elements of the list

sorted(
    list2
)  # sorts the elements of a list in ascending order and creates a new list at the same time

sorted(
    list2, reverse=True
)  # sorts the elements of a list in descending order and creates a new list at the same time

list1 + list2  # concatenating two lists

list1 * 3  # repetition of a list
