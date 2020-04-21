"""
    Resources for field class
    Create by Nguyen_Pham_Quang_Vu on 2020/04/21
"""


class Field(object):

    def __init__(self, data: float, time=0.0):
        """Initialize data"""
        self.data = []
        self.data.append(data)

        self.time = []
        self.time.append(time)

        """This is for iteration"""
        self._start = 0
        self._next = self._start

    def __repr__(self):
        """Print to the screen"""
        return "Field({}, {})".format(self.time, self.data)

    def get_data(self):
        """Get data"""
        return self.data

    def set_data(self, new_data):
        """Set data"""
        self.data = new_data

    def push(self, new_data, *args):
        """Push in new data"""

        # push new_data to self.data
        self.data.append(new_data)

        # if there is no time specified
        if len(args) == 0:
            self.time.append(self.time[-1]+1)

        # if there is time specified (in args)
        else:
            self.time.append(*args)

    def delete(self, index):
        """delete data at the specific index"""
        del self.data[index]
        del self.time[index]

    def pop(self, index):
        """pop data at the specific index"""
        self.data.pop(index)
        self.time.pop(index)

    def shift(self, new_data):
        pass

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        """This is for iteration"""
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self

    def __next__(self):
        """This is for iteration"""
        if self._next > len(self.data)-1:
            raise StopIteration()
        else:
            _r = self.data[self._next]
            self._next += 1
            return _r

    def __getitem__(self, x):
        """To access the index ith of the object"""

        # in case x is index, (integer type)
        if type(x) == int:
            return self.data[x]

        # in case x is time, (float type)
        else:

            # search the index of time that have that index
            if x in self.time:
                i = self.time.index(x)
                return self.data[i]

            # need to do interpolation
            else:

                # check if the given time is larger than time in the object.time
                if x > self.time[-1]:
                    # return the first data
                    return self.data[-1]

                # check if the given time is less than the beginning time in the object.time
                elif x < self.time[0]:
                    # return the first data
                    return self.data[0]
                else:
                    for i in self.time:
                        if i > x:
                            i_index_big = self.time.index(i)
                            i_index_small = self.time.index(i-1)

                            t0 = self.time[i_index_small]
                            t1 = self.time[i_index_big]
                            dt = t1 - t0

                            data0 = self.data[i_index_small]
                            data1 = self.data[i_index_big]

                            data = data0*(1-(x-t0)/dt) + data1*(1-(t1-x)/dt)
                            break
                    return data


class FieldSet(dict):
    """Create FieldSet class similar to dictionary class"""
    pass

