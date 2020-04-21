"""
    Resources for GaussLine class
    Created by Nguyen Pham Quang Vu on 2020-04-17
"""

from math import sqrt
import numpy as np
from Field import FieldSet, Field

###################
# GaussLine
###################
class GaussLine(object):
    """Create GaussPoint class to calculate Gauss Integration"""

    def __init__(self, npoint, dim):
        """Initialize GaussPoint object with number of points and dimension data input"""

        """Calculate line_points"""
        if npoint == 1:
            line_points = np.array([0.0])
        elif npoint == 2:
            line_points = np.array([-1, 1]) / sqrt(3.0)
        elif npoint == 3:
            line_points = np.array([-1, 0, 1]) / sqrt(3/5)

        """Calculate line_weights"""
        if npoint == 1:
            line_weights = 2.0
        elif npoint == 2:
            line_weights = np.array([1.0, 1.0])
        elif npoint == 3:
            line_weights = np.array([5/9, 8/9, 5/9])

        """Calculate points"""
        if dim == 1:
            points = np.array([i for i in line_points])
        elif dim == 2:
            points = np.array([np.array([i, j]) for i in line_points for j in line_points])
        elif dim == 3:
            points = np.array([np.array([i, j, k]) for i in line_points for j in line_points for k in line_points])

        """Calculate weights"""
        if dim == 1:
            weights = np.array([i for i in line_weights])
        elif dim == 2:
            weights = np.array([i*j for i in line_weights for j in line_weights])
        elif dim == 3:
            weights = np.array([i*j*k for i in line_weights for j in line_weights for k in line_weights])

        """Return points and weight"""
        self.points = points
        self.weights = weights

        """This is for iteration"""
        self._start = 0
        self._step = 1
        self._next = self._start
        self._stop = len(self.points)

    def get_points(self):
        """Return points vector of the object"""
        return self.points

    def get_weights(self):
        """Return weights vector of the object"""
        return self.weights

    def __len__(self):
        """Return length of the object"""
        return len(self.points)

    def __iter__(self):
        """This is for iteration"""
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def __next__(self):
        """This is for iteration"""
        if self._next > self._stop:
            raise StopIteration()
        else:
            _r = (self.points[self._next - 1], self.weights[self._next - 1])
            self._next += 1
            return _r

    def __getitem__(self, index):
        """To access the index ith of the object"""
        return self.points[index-1], self.weights[index-1]

    def __str__(self):
        """Format to display to the screen"""
        return "GaussLine" + str([i for i in list(self)])

    def __repr__(self):
        """Format to display on the screen"""
        return str(self)

##############
# GaussPoint
##############

class GaussPoint(object):

    def __init__(self, point, weight):
        self.point = point
        self.weight = weight
        self.field = FieldSet()

    def __str__(self):
        """Format to display to the screen"""
        return "GaussPoint(Point: {}; " \
               " Weight: {};" \
               " Field: {})".format(self.point, self.weight, self.field)

    def __repr__(self):
        """Format to display on the screen"""
        return str(self)

#############
# Create Gauss Point Function
#############


def create_gauss_point_quad4():
    gauss_line = GaussLine(2, 2)
    gauss_point = [GaussPoint(i[0], i[1]) for i in gauss_line]
    return gauss_point
