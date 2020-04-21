from ShapeFunction import ShapeFunction, Quad4, Quad8

shape = ShapeFunction()

# define local coordinate
point = [0.0,0.0]


# Test: Shape Function Quad4
N1 = shape.deltaN(Quad4(), point)
N2 = shape.N(Quad4(), point)

print("N = {}".format(N1))
print("∇N = {}".format(N2))


## Test: Shape Function Quad8
N1 = shape.N(Quad8(), point)
N2 = shape.deltaN(Quad8(), point)

print("N = {}".format(N1))
print("∇N = {}".format(N2))

