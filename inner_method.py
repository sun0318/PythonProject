class RangeIterator(object):
    def __init__(self, maxnum):
        self.maxnum = maxnum
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == self.maxnum:
            raise StopIteration

        return self.count


class Xrange():
    def __init__(self, maxnum):
        self.maxnum = maxnum

    def __iter__(self):
        return RangeIterator(self.maxnum)

test = Xrange(4)