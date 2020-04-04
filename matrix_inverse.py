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
        self.size = self.np_matrix.size
        self.n = self.np_matrix[0].size
        #print(self.n, "\n")

    # returns the minor of the current matrix given a row and column
    def minor(self, r, c, curr_matrix):
        return self.determinate(InverseCalculator.delete(curr_matrix, r, c))

    def cofactor(self, r, c, curr_matrix):
        return (-1)**(r+1+c) * self.minor(r, c, curr_matrix)

    #def minor_helper(self, r, c, siz):

    def determinate(self, curr_matrix = np.matrix("")):
        if (curr_matrix.size == 0):
            curr_matrix = self.np_matrix
        if (curr_matrix.size == 4):
            # ad - bc
            return (curr_matrix.item((0,0)) * curr_matrix.item((1,1)) -
                   curr_matrix.item((0,1)) * curr_matrix.item((1,0)))
        det = 0
        # sumation formula
        for i in range(0, curr_matrix[0].size):
            det = det + (curr_matrix.item(i, 0)) * self.cofactor(i, 0, curr_matrix)
        return det

    # def determinate_helper(self, curr_matrix):


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
