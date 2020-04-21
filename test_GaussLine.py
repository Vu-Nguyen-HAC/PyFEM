from GaussLine import GaussLine, GaussPoint
from Field import Field, FieldSet
# ---------------------------------------------------------------------------------------------------------------------
# Test
A = GaussLine(2, 2)

print("A =", A)

print("Gauss points of A: ")
print(A.get_points())

print("Gauss weights of A: ")
print(A.get_weights())

print("Length of A: ")
print(len(A))

# Iteration of A
print()
print("Iteration of A:")
for i in GaussLine(2, 2):#A:
    print("i = ", i)

# Access index ith of the object (by using def __getitem__)
print()
print("Access the element of i-th index of the object")
print("A[1]=", A[1])
print("A[2]=", A[2])
print("A[3]=", A[3])
print("A[4]=", A[4])

# ---------------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------")
gl = GaussLine(2, 2)
a = [GaussPoint(i[0], i[1]) for i in gl]
print("gauss points: ", a)
print("The first Gauss Point: ", a[1])
print("Gauss Line (2, 2):", GaussLine(2,2))


# ---------------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------")
gp = GaussPoint(2, 2)
print(gp)

gp.field["stress"] = Field([1, 1, 1])
gp.field["stress"].push([1, 2, 1])
print(gp)

gp.field["strain"] = Field([1, 1, 1])
print(gp)
gp.field["strain"].push([1, 2, 1])
print(gp)
gp.field["strain"].push([1, 2, 1])
print(gp)
