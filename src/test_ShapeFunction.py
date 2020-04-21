from ShapeFunction import ShapeFunctionQuad4, ShapeFunctionQuad8

# Test: Shape Function Quad4
s = ShapeFunctionQuad4()

# define local coordinate
ξ = [0.0,0.0]

print("N = {}".format(s.N(ξ)))

print("∇N = {}".format(s.deltaN(ξ)))

## Test: Shape Function Quad8
s = ShapeFunctionQuad8()

# define local coordinate
ξ = [0.0, 0.0]

print("N = {}".format(s.N(ξ)))

print("∇N = {}".format(s.deltaN(ξ)))
