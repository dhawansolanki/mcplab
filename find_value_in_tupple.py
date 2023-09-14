example_tuple = ("p", "r", "o", "g", "r", "a", "m")
x = "a"
y = "z"

if x in example_tuple:
    print("The element", x, "is present in the tuple")

if y in example_tuple:
    print("The element", y, "is present in the tuple")

# Check if both elements are not present in the tuple before printing "The tuple is deleted"
if x not in example_tuple and y not in example_tuple:
    print("The tuple is deleted")
else:
    print("The element", y, "is not present in the tuple")

# Delete the tuple if needed
if "z" in example_tuple:
    del example_tuple
