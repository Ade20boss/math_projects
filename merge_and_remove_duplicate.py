def merge_arrays(array1, array2):
    new_array = []
    new_array1 = []
    k = 0
    for i in array1:
        new_array.append(i)
    for j in array2:
        if j not in new_array:
            new_array.append(j)
    print(new_array)

    while new_array:
        smallest = min(new_array)
        new_array1.append(smallest)
        new_array.remove(smallest)
        
    print(new_array1)


a = [4, 6, 3, 1, 5, 2]
b = [4, 4, 5, 6, 7, 8, 9]
merge_arrays(a, b)



