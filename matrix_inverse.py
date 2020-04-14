import numpy as np

class InverseCalculator:
    """
    Matrix class for computing the determinate of a maxtrix. Uses numpy's matrix
    for basic operations.
    """

    # Takes a matrix as a string, or as a 2D array and stores it into the underlying
    # numpy matrix
    def __init__(self, imatrix):
        self.np_matrix = np.matrix(imatrix)
        self.n = self.np_matrix[0].size
        self.size = self.np_matrix.size
        self.upper_m = self.np_matrix.astype(float) # keep track of the original matrix
        self.upper_ops = []
        self.lower_mi = np.identity(self.n)
        self.det = 1
        self.upper()
        self.upper_mi = np.identity(self.n)


    # returns the upper triangular matrix
    def upper(self):
        for j in range(0, self.n - 1):
            for i in range(j + 1, self.n):
                # if the current item in the diagonal is zero, need to find the
                # first non-zero item in the col below it, and add the row it's
                # in to this row
                if (self.upper_m[j, j] == 0):
                    complete = False
                    for k in range(j+1, self.n):
                        if (self.upper_m[k, j] != 0):
                            self.upper_m[j] = self.upper_m[j] + self.upper_m[k]
                            self.lower_mi[j] = self.lower_mi[j] + self.lower_mi[k]
                            break
                        complete = True
                    if (complete):
                        print("no inverse")
                        break
                # find what needs to be subtracted to get zero in row,col below
                m = self.upper_m[i, j] / self.upper_m[j, j]

                # do the operation
                self.upper_m[i] = self.upper_m[i] - m * self.upper_m[j]
                self.lower_mi[i] = self.lower_mi[i] - m * self.lower_mi[j]

    # multiple diagonal of upper matrix
    def determinate(self):
        for j in range(self.n):
            self.det = self.det * self.upper_m[j, j]
        return self.det

    def upper_inverse(self):
        for j in range(self.n - 1, 0, -1):
            for i in range(j - 1, -1, -1):
                m = self.upper_m[i, j] / self.upper_m[j, j]
                self.upper_m[i] = self.upper_m[i]  - m * self.upper_m[j]
                self.upper_mi[i] = self.upper_mi[i] - m * self.upper_mi[j]

        for j in range(self.n):
            c = self.upper_m[j, j]
            self.upper_m[j, j] = 1
            self.upper_mi[j] = self.upper_mi[j] / c


    def inverse(self):
        if (self.determinate() == 0):
            print("Matrix not invertable, determinate = 0")
            return -1
        self.upper_inverse()
        return np.dot(self.upper_mi, self.lower_mi)


    # delete row r and col c using numpy.delete, indexing starting at 0 i.e.
    # row 1 gives an r value of 0
    def delete(matrix, r, c):
        ret_matrix = np.delete(matrix, r, 0)
        ret_matrix = np.delete(ret_matrix, c, 1)
        return ret_matrix

    def item(self, r, c = None):
        return self.np_matrix((r,c))

    # string version of the matrix
    def __str__(self):
        return str(self.np_matrix)
