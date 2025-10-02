from math import sqrt, sin, cos, asin, degrees, acos
def magnitude(vector):
    vector = list(input("Enter vector components separated by space: ").split())
    squares = []
    magnitude = 0
    for i in vector:
        i = int(i)
        square = (i**2)
        squares.append(square)
    for j in squares:
        magnitude += j
    new_magnitude = sqrt(magnitude)
    return new_magnitude
def magnitude_for_cross_products(x, y, z):
    square = (x**2) + (y**2) + (z**2)
    return sqrt(square)
def add_vector():
    num_of_vectors = int(input("Enter number of vectors: "))
    index_of_vectors = []
    list_lengths = []
    index_of_vectors2 = []
    sums = []

    for i in range(num_of_vectors):
        i = list(input("Enter vector components separated by space: ").split())
        for stuff in i:
            stuff = int(stuff)
        index_of_vectors.append(i)

    for j in index_of_vectors:
        list_lengths.append(len(j))
    largest = max(list_lengths)

    for l in index_of_vectors:
        if len(l) < largest:
            for k in range(largest - len(l)):
                l.append(0)
    print(index_of_vectors)

    for _ in range(largest):
        vector = []
        index_of_vectors2.append(vector)

    for vec in index_of_vectors:
        for i in range(largest):
            index_of_vectors2[i].append(vec[i])
    print(index_of_vectors2)

    for vec in index_of_vectors2:
        total = 0
        for i in vec:
            i = int(i)
            total += i
        sums.append(total)
    print(sums)

def subtract_vector():
    num_of_vectors1 = int(input("Enter number of vectors: "))
    index_of_vectors = []
    list_lengths = []
    index_of_vectors2 = []
    sums = []

    for i in range(num_of_vectors1):
        i = list(input("Enter vector components separated by space: ").split())
        for stuff in i:
            stuff = int(stuff)
        index_of_vectors.append(i)

    for j in index_of_vectors:
        list_lengths.append(len(j))
    largest = max(list_lengths)

    for l in index_of_vectors:
        if len(l) < largest:
            for k in range(largest - len(l)):
                l.append(0)
    print(index_of_vectors)

    for _ in range(largest):
        vector = []
        index_of_vectors2.append(vector)

    for vec in index_of_vectors:
        for i in range(largest):
            index_of_vectors2[i].append(vec[i])
    print(index_of_vectors2)

    for vec in index_of_vectors2:
        total = int(vec[0])
        vec.remove(vec[0])
        for i in vec:
            total -= int(i)
        sums.append(total)
    print(sums)

def dot_product():
    vector1 = list(input("Enter vector components separated by space: ").split())
    vector2 = list(input("Enter vector components separated by space: ").split())
    largest = max(len(vector1), len(vector2))
    choice = input('Geometric calculation or component calculation(press 1 for geometric, 2 for component): ')
    dotproduct = 0
    if choice == '2':
        if len(vector1) < len(vector2):
            for i in range(largest - len(vector1)):
                vector1.append(0)
        else:
            for i in range(largest - len(vector2)):
                vector2.append(0)
        for x in range(largest):
            multiplied_num = int(vector1[x]) * int(vector2[x])
            dotproduct += multiplied_num
        print(dotproduct)
        choice2 = input("Do you want to calculate the angle between the two vectors? (press y for yes, n for no):")
        if choice2 == 'y':
            angle_radians = acos((dotproduct)/(magnitude(vector1) * magnitude(vector2)))
            angle_degrees = degrees(angle_radians)
            print(f"The angle between the two vectors is {angle_degrees} degrees")
        else:
            exit()
    else:
        magnitude_of_first_vector = int(input("Enter magnitude of first vector: "))
        magnitude_of_second_vector = int(input("Enter magnitude of second vector: "))
        angle = int(input("Enter angle between the two vectors: "))
        dotproduct_geometric = magnitude_of_second_vector * magnitude_of_first_vector * sin(angle)
        print(dotproduct_geometric)

def cross_product():
    vector1 = list(input("Enter vector components separated by space: ").split())
    vector2 = list(input("Enter vector components separated by space: ").split())
    if len(vector1) != 3 or len(vector2) != 3:
        print("Invalid vector")
        exit()
    x1 = int(vector1[0])
    x2 = int(vector1[1])
    x3 = int(vector1[2])
    y1 = int(vector2[0])
    y2 = int(vector2[1])
    y3 = int(vector2[2])
    largest = max(len(vector1), len(vector2))
    crosproduct_list = []
    choice = input('Geometric calculation or component calculation(press 1 for geometric, 2 for component): ')
    if choice == '2':
        if len(vector1) < len(vector2):
            for i in range(largest - len(vector1)):
                vector1.append(0)
        else:
            for i in range(largest - len(vector2)):
                vector2.append(0)
        cross_product1 = int(vector1[1]) * int(vector2[2]) - int(vector1[2]) * int(vector2[1])
        crosproduct_list.append(cross_product1)
        cross_product2 = int(vector1[2]) * int(vector2[0]) - int(vector1[0]) * int(vector2[2])
        crosproduct_list.append(cross_product2)
        cross_product3 = int(vector1[0]) * int(vector2[1]) - int(vector1[1]) * int(vector2[0])
        crosproduct_list.append(cross_product3)
        print(crosproduct_list)
        choice2 = input("Do you want to calculate the angle between the two vectors? (press y for yes, n for no):")
        if choice2 == 'y':
            angle_radians = asin((magnitude_for_cross_products(cross_product1, cross_product2, cross_product3)) / (magnitude_for_cross_products(x1, x2, x3) * magnitude_for_cross_products(y1, y2, y3)))
            angle_degrees = round(degrees(angle_radians), 2)
            print(f"The angle between the two vectors is {angle_degrees} degrees")
        else:
            exit()

























