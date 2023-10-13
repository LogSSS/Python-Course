class Iterator:
    end: float

    def __init__(self, start: float, end: float, step: float):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.step == 0:
                raise ValueError('Step cannot be zero')
            if ((self.step > 0 and self.start > self.end)
                    or (self.step < 0 and self.start < self.end)):
                raise StopIteration
            else:
                res = self.start
                self.start += self.step
                return res
        except ValueError as e:
            print(e)
            raise StopIteration
