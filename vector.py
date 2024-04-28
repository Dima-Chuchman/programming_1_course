import math

class Vector:

    def __init__(self, components):
        self.components = list(components)
        
    def __str__(self):
        return f"Vector({self.components})"
    
    def dimension(self):
        return len(self.components)
    
    def magnitude(self):
        return math.sqrt(sum([x**2 for x in self.components]))
    
    def mean(self):
        return sum(self.components) / len(self.components)
    
    def max_component(self):
        if not self.components:
            return None
        return max(self.components)
    
    def min_component(self):
        if not self.components:
            return None
        return min(self.components)
    
    
def read_vector_file(filename):
    vectors = []
    with open(filename, 'r') as file:
        for line in file:
            components = [float(x) for x in line.strip().split()]
            vectors.append(Vector(components))
    return vectors

def biggest_dimension(vectors):
    max_dimension_vector = max(vectors, key=lambda x: (x.dimension()))
    return max_dimension_vector

def biggest_magnitude(vectors):
    max_magnitude_vector = max(vectors, key=lambda x: (x.magnitude()))
    return max_magnitude_vector

def find_average_magnitude(vectors):
    average_length = sum([vector.magnitude() for vector in vectors])
    return average_length / len(vectors)

def above_average_magnitude(vectors):
    average_magnitude = find_average_magnitude(vectors)
    above_average_count = len([vector for vector in vectors if vector.magnitude() > average_magnitude])
    return above_average_count

#def find_max_component(vectors):
    #max_component_vector = min(vectors, key=lambda x: (x.max_component(), -x.min_component()))
    #return max_component_vector
    
def find_max_component(vectors):
    max_component_vector = None
    max_component = float('-inf')
    for vector in vectors:
        component = vector.max_component()
        if component is not None and component > max_component:
            max_component = component
            max_component_vector = vector
        elif component is not None and component == max_component and vector.min_component() < max_component_vector.min_component():
            max_component_vector = vector
    return max_component_vector


#def find_min_component(vectors):
    #min_component_vector = min(vectors, key=lambda x: (-x.min_component(), x.max_component()))
    #return min_component_vector
    
def find_min_component(vectors):
    min_component_vector = None
    min_component = float('inf')
    for vector in vectors:
        component = vector.min_component()
        if component is not None and -component < min_component:
            min_component = -component
            min_component_vector = vector
        elif component is not None and -component == min_component and vector.max_component() > min_component_vector.max_component():
            min_component_vector = vector
    return min_component_vector


def main(filename):
    vectors = read_vector_file(filename)
    
    max_dimension_least_magnitude = biggest_dimension(vectors)
    print("Той з них, що має найбільшу розмірність. Якщо таких векторів кілька, виведіть той з них, що має найменшу довжину: ", max_dimension_least_magnitude)
    
    max_magnitude_least_dimension = biggest_magnitude(vectors)
    print("Вектор, що має найбільшу довжину. Якщо серед набору міститься кілька таких векторів, покажіть той з них, що має найменшу розмірність: ", max_magnitude_least_dimension)
    
    average_magnitude = find_average_magnitude(vectors)
    print("Середню довжину вектора серед заданого набору: ", average_magnitude)
    
    above_average_least = above_average_magnitude(vectors)
    print("Кількість векторів, що мають довжину більшу за середню довжину заданого набору: ", above_average_least)
    
    max_component_vector = find_max_component(vectors)
    print("Вектор з максимальною найбільшою компонентою. Якщо таких векторів у наборі міститься кілька, вкажіть той з них, що має меншу найменшу компоненту: ", max_component_vector)
    
    min_component_vector = find_min_component(vectors)
    print("Вектор з мінімальною найменшою компонентою. Якщо таких векторів у наборі міститься кілька, вкажіть той з них, що має більшу найбільшу компоненту: ", min_component_vector)

filename = ["input01.txt", "input02.txt", "input03.txt","input04.txt"]
for file_name in filename:
    print("\n" + "="*20 + " " + file_name + " " + "="*20)
    main(file_name)
    