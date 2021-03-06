class InListPredicate(object):

    def __init__(self, ls, true_if_in=True):

        self.ls = ls
        self.true_if_in = true_if_in

    def is_true(self, x):

        if self.true_if_in:
            for i in self.ls:
                if x == i: # __eq__ method
                    # if np.array_equal(x.data, i.data):
                    return True
            return False
        else:
            for i in self.ls:
                if x == i:
                    return False
            return True
        # return x in self.ls
