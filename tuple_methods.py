n = int(input("Enter the size: "))
l = []  # Create an empty list to store elements

for i in range(n):
    num = int(input("Enter the element at %d position: " % (i)))
    l.append(num)

# Convert the list 'l' to a tuple
t1 = tuple(l)

print("The elements in tuple are: ", t1)

# The sorted() function is used to sort the elements of the tuple.
print("The elements after sorting in the tuple are: ", sorted(t1))

# The max() function is used to find the maximum element in the tuple.
print("The maximum element present in the tuple is: ", max(t1))

# The min() function is used to find the minimum element in the tuple.
print("The minimum element present in the tuple is: ", min(t1))

# Use the == operator to compare the elements of two or more tuples.
if t1 == tuple(l):
    print("The elements are equal")
else:
    print("The elements are not equal")
