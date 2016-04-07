class ShapeError(Exception):
    pass


def shape(list_or_maxtrix):
    return (len(list_or_maxtrix),)

def vector_add(vec_one, vec_two):
    if len(vec_one) !=  len(vec_two):
        raise ShapeError
    return [(a + b) for a, b in zip(vec_one, vec_two)]


def vector_sub(vec_one, vec_two):
    if len(vec_one) !=  len(vec_two):
        raise ShapeError
    return [(a - b) for a, b in zip(vec_one, vec_two)]

def vector_sum(*args):
    lengths = [len(i) for i in args]
    if max(lengths) != min(lengths):
        raise ShapeError
    return [sum(a) for a in zip(*args)]

def dot(vec_one, vec_two):
    if len(vec_one) !=  len(vec_two):
        raise ShapeError
    return sum([(a * b) for a, b in zip(vec_one, vec_two)])

def vector_multiply(vec_one, scalar):
    return [(i*scalar) for i in vec_one]

def vector_mean(*args):
    return [(sum(a)/len(a)) for a in zip(*args)]


def magnitude(vec_one):
    return sum(a**2 for a in vec_one)**.5


m = [3, 4]
n = [5, 0]

v = [1, 3, 0]
w = [0, 2, 4]
u = [1, 1, 1]
y = [10, 20, 30]
z = [0, 0, 0]
