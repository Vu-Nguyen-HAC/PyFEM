"""
    Resource to get shape function for Gauss Integration
    Create by Nguyen Pham Quang Vu on 2020/04/21
"""
import numpy as np

class Bar2(object):
    """Bar element with 2 nodes"""
    pass


class Bar3(object):
    """Bar element with 3 nodes"""
    pass


class Quad4(object):
    """Quad 4 element type"""
    pass


class Quad8(object):
    """Quad 8 element type"""
    pass


class ShapeFunction(object):
    """
     Shape function of Quad 4 element
    """

    @staticmethod
    def N(self, point):
        """Calculate the value of shape functions at  a specific point"""

        ##################
        # Quad 4 element:
        ##################
        if isinstance(self, Quad4):
            N = np.zeros(shape=4)  # Declare empty array by numpy
            ξ, η = point
            N[0] = 0.25 * (1-ξ) * (1-η)
            N[1] = 0.25 * (1+ξ) * (1-η)
            N[2] = 0.25 * (1+ξ) * (1+η)
            N[3] = 0.25 * (1-ξ) * (1+η)
            return N

        ##################
        # Quad 8 element:
        ##################
        elif isinstance(self, Quad8):
            N = np.zeros(shape=8)
            ξ, η = point
            N[0] = 0.25 * (1 - ξ) * (1 - η) * (-1 - ξ - η)
            N[1] = 0.25 * (1 + ξ) * (1 - η) * (-1 + ξ - η)
            N[2] = 0.25 * (1 + ξ) * (1 + η) * (-1 + ξ + η)
            N[3] = 0.25 * (1 - ξ) * (1 + η) * (-1 - ξ + η)
            N[4] = 0.5 * (1 - ξ ** 2) * (1 - η)
            N[5] = 0.5 * (1 + ξ) * (1 - η ** 2)
            N[6] = 0.5 * (1 - ξ ** 2) * (1 + η)
            N[7] = 0.5 * (1 - ξ) * (1 - η ** 2)
            return N

        # TODO: Bar2, Bar3 element

    @staticmethod
    def deltaN(self, point):
        """Calculate the value of the derivative of shape functions at  a specific point"""

        ##################
        # Quad 4 element:
        ##################
        if isinstance(self, Quad4):
            A = np.zeros(shape=(2, 4))
            ξ, η = point
            A[0, 0] = 0.25 * (-1+η)
            A[0, 1] = 0.25 * (-1+ξ)
            A[0, 2] = 0.25 * ( 1-η)
            A[0, 3] = 0.25 * (-1-ξ)
            A[1, 0] = 0.25 * ( 1+η)
            A[1, 1] = 0.25 * ( 1+ξ)
            A[1, 2] = 0.25 * (-1-η)
            A[1, 3] = 0.25 * ( 1-ξ)
            return A

        ##################
        # Quad 8 element:
        ##################
        elif isinstance(self, Quad8):
            A = np.zeros(shape=(2, 8))
            ξ, η = point
            A[0, 0] = 0.25 * (1 - η) * (2 * ξ + η)
            A[0, 1] = 0.25 * (1 - ξ) * (2 * η + ξ)
            A[0, 2] = 0.25 * (1 - η) * (2 * ξ - η)
            A[0, 3] = 0.25 * (1 + ξ) * (2 * η - ξ)
            A[0, 4] = 0.25 * (1 + η) * (2 * ξ + η)
            A[0, 5] = 0.25 * (1 + ξ) * (2 * η + ξ)
            A[0, 6] = 0.25 * (1 + η) * (2 * ξ - η)
            A[0, 7] = 0.25 * (1 - ξ) * (2 * η - ξ)
            A[1, 0] = -ξ * (1 - η)
            A[1, 1] = -0.5 * (1 - ξ ** 2)
            A[1, 2] = 0.5 * (1 - η ** 2)
            A[1, 3] = -η * (1 + ξ)
            A[1, 4] = -ξ * (1 + η)
            A[1, 5] = 0.5 * (1 - ξ ** 2)
            A[1, 6] = -0.5 * (1 - η ** 2)
            A[1, 7] = -η * (1 - ξ)
            return A

        # TODO: Bar2, Bar3 element
