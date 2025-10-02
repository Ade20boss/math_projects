def sum_square_of_two_largest(x, y, z):
    arr = [x, y, z]
    largest = max(arr)
    arr.remove(arr[arr.index(largest)])
    second_largest = max(arr)
    sum_of_squares = largest**2 + second_largest**2
    return sum_of_squares

print(sum_square_of_two_largest(5, 5, 5))