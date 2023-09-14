def sum_arr(arr, n):
    if n == 0:
        return 0
    else:
        return arr[n - 1] + sum_arr(arr, n - 1)

n = int(input("Enter the number of elements: "))
l = []
for i in range(0, n):
    ele = int(input("Enter element: "))
    l.append(ele)
print("Elements in the array are:")
print(l)
print("The sum of the elements in the array is:")
m = sum_arr(l, n)
print(m)
