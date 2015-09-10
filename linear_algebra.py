class ShapeException(Exception):
    pass

def shape(vector):
    if type(vector[0]) != list:
        return (len(vector),)
    return (len(vector),len(vector[0]))



def add_vector(vector1,vector2):
    raise_exception(vector1, vector2)
    addition = [x + y for x, y in zip(vector1, vector2)]
    return addition


def vector_sum():
    raise_exception(vector1, vector2)
    subtraction = [x - y for x, y in zip(vector1, vector2)]
    return subtraction



def dot(vector1,vector2)



def vector_multiply(vector, scalar)



def vector_mean():



def magnitude(vector):
