def bubble_sort(a):
    a.sort()
    return(a)

a = []
number = int(input("Please enter the total number of elements: "))
for i in range(number):
    value = int(input("Please enter the %d element: " %i))
    a.append(value)
print("The sorted list in ascending order: ", bubble_sort(a))