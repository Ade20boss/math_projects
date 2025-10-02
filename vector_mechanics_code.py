from math import sqrt, sin, cos, asin, degrees, acos
def magnitude():
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
    print(round(new_magnitude, 2))


def magnitude_for_cross_products(x, y, z):
    square = ((int(x))**2) + ((int(y))**2) + ((int(z))**2)
    return sqrt(square)


def add_vector():
    while 1 == 1:
        try:
            num_of_vectors = int(input("Enter number of vectors: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
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

    for _ in range(largest):
        vector = []
        index_of_vectors2.append(vector)

    for vec in index_of_vectors:
        for i in range(largest):
            index_of_vectors2[i].append(vec[i])
    for vec in index_of_vectors2:
        total = 0
        for i in vec:
            i = int(i)
            total += i
        sums.append(total)
    print(sums)

def subtract_vector():
    while True:
        try:
            num_of_vectors1 = int(input("Enter number of vectors: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
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

    for _ in range(largest):
        vector = []
        index_of_vectors2.append(vector)

    for vec in index_of_vectors:
        for i in range(largest):
            index_of_vectors2[i].append(vec[i])

    for vec in index_of_vectors2:
        total = int(vec[0])
        vec.remove(vec[0])
        for i in vec:
            total -= int(i)
        sums.append(total)
    print(sums)

def dot_product():
    choice = input('Geometric calculation or component calculation(press 1 for geometric, 2 for component): ')
    if choice == '2':
        vector1 = input("Enter vector components separated by space: ").split()
        vector2 = input("Enter vector components separated by space: ").split()
        largest = max(len(vector1), len(vector2))
        dotproduct = 0
        if len(vector1) < len(vector2):
            for i in range(largest - len(vector1)):
                vector1.append(0)
                vector1[-1] = int(vector1[-1])
        else:
            for i in range(largest - len(vector2)):
                vector2.append(0)
                vector2[-1] = int(vector2[-1])
        for x in range(largest):
            multiplied_num = int(vector1[x]) * int(vector2[x])
            dotproduct += multiplied_num
        print(dotproduct)
        choice2 = input("Do you want to calculate the angle between the two vectors? (press y for yes, n for no):")
        if choice2 == 'y':
            angle_radians = (dotproduct/(magnitude_for_cross_products(vector1[0], vector1[1], vector1[2]) * magnitude_for_cross_products(vector2[0], vector2[1], vector2[2])))
            angle_degrees = round(degrees(acos(angle_radians)), 2)
            print(f"The angle between the two vectors is {angle_degrees} degrees")
        else:
            exit()
    else:
        magnitude_of_first_vector = float(input("Enter magnitude of first vector: "))
        magnitude_of_second_vector = float(input("Enter magnitude of second vector: "))
        dotproduct1 = int(input("Enter dot product: "))
        angle_process = dotproduct1 / (magnitude_of_first_vector * magnitude_of_second_vector)
        angle = round(degrees(acos(angle_process)), 2)
        dotproduct_geometric = magnitude_of_second_vector * magnitude_of_first_vector * cos(angle)
        print(dotproduct_geometric)

def cross_product():
    choice = input('Geometric calculation or component calculation(press 1 for geometric, 2 for component): ')
    if choice == '2':
        vector1 = input("Enter vector components separated by space: ").split()
        vector2 = input("Enter vector components separated by space: ").split()
        largest = max(len(vector1), len(vector2))
        if len(vector1) < len(vector2):
            for i in range(largest - len(vector1)):
                vector1.append(0)
        elif len(vector2) < len(vector1):
            for i in range(largest - len(vector2)):
                vector2.append(0)
        x1 = int(vector1[0])
        x2 = int(vector1[1])
        x3 = int(vector1[2])
        y1 = int(vector2[0])
        y2 = int(vector2[1])
        y3 = int(vector2[2])

        crosproduct_list = []
        cross_product1 = int(vector1[1]) * int(vector2[2]) - int(vector1[2]) * int(vector2[1])
        crosproduct_list.append(cross_product1)
        cross_product2 = int(vector1[2]) * int(vector2[0]) - int(vector1[0]) * int(vector2[2])
        crosproduct_list.append(cross_product2)
        cross_product3 = int(vector1[0]) * int(vector2[1]) - int(vector1[1]) * int(vector2[0])
        crosproduct_list.append(cross_product3)
        print(crosproduct_list)
        choice2 = input("Do you want to calculate the angle between the two vectors? (press y for yes, n for no):")
        if choice2 == 'y':
            angle_radians = (magnitude_for_cross_products(cross_product1, cross_product2, cross_product3)) / (magnitude_for_cross_products(x1, x2, x3) * magnitude_for_cross_products(y1, y2, y3))
            angle_degrees = round(degrees(asin(angle_radians)), 2)
            print(f"The angle between the two vectors is {angle_degrees} degrees")
        else:
            exit()
    else:
        magnitude_of_first_vector = float(input("Enter magnitude of first vector: "))
        magnitude_of_second_vector = float(input("Enter magnitude of second vector: "))
        cross_product_ = int(input("Enter magnitude of cross product: "))
        angle_process = cross_product_ / (magnitude_of_first_vector * magnitude_of_second_vector)
        angle = round(degrees(acos(angle_process)), 2)
        crossproduct_geometric = magnitude_of_second_vector * magnitude_of_first_vector * sin(angle)
        print(crossproduct_geometric)

print("Welcome to VecPy - A vector mechanics calculator!")
print("1. Add vectors")
print("2. Subtract vectors")
print("3. Dot product")
print("4. Cross product")
print("5. Magnitude")
while True:
    while True:
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
    if choice == "1":
        add_vector()
    elif choice == "2":
        subtract_vector()
    elif choice == "3":
        dot_product()
    elif choice == "4":
        cross_product()
    elif choice == "5":
        magnitude()

    redo = input("Do you want to do another calculation? (press y for yes, n for no): ")
    if redo == "n":
        print("Thank you for using VecPy!")
        break
    else:
        continue























