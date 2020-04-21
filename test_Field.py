from Field import Field
from Field import FieldSet


def test_Field():
    fld = Field(7)
    print("Original fld: ", fld)

    fld.push(5)
    print("fld after push: ", fld)

    fld.push(3)
    print("fld after push: ", fld)

    fld.push(1)
    print("fld after push: ", fld)

    fld.push(7)
    print("fld after push: ", fld)

    fld.push(4, 10.0)
    print("fld after push: ", fld)

    fld.push(6)
    print("fld after push: ", fld)

    print("fld[4] = ", fld[4])
    print("fld[10.0] = ", fld[10.0])
    print("fld[1.5] = ", fld[1.5])#

    print("fld = ", fld[1.4])#

    fld.delete(1)
    print("fld after delete: ", fld)

    fld.pop(1)
    print("fld after pop: ", fld)

    f = Field([1, 2, 3])
    print("Original f: ", f)

    f.push([2,3,5])
    print("f after push: ", f)

    f.push([2, 4, 1])
    print("f after push: ", f)
    print(f.get_data()[1])


def test_FieldSet():
    x = FieldSet()
    x["stress"] = Field([1.0, 1.0, 1.0])
    x["strain"] = Field([0.0, 0.0, 0.0])
    x["stiffness"] = Field(10)
    print(x)
    print()
    print()

    x["stress"].push([1.0, 2.0, 1.0])
    print(x["stress"])
    print(x["stress"].data)
    print(x["stress"][-1])

    print("loop")
    print(x)
    for i in x["stress"]:
        print(i)

test_Field()
test_FieldSet()





