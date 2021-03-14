import numpy as np

def TestMatrix():
    # initialization
    matrix3x3 = np.array([[1,2,3],[4,5,6],[7,9,8]])
    print(matrix3x3)
    print(type(matrix3x3))

    # transpose
    transposedMatrix3x3 = matrix3x3.T
    print(transposedMatrix3x3)

    # adder / substractor, scaling (linear combination)
    indentityMatrix3x3 = np.array([[1,0,0],[0,1,0],[0,0,1]])
    zeroMatix3x3 = np.array([[0,0,0],[0,0,0],[0,0,0]])
    print(zeroMatix3x3 - indentityMatrix3x3)
    print(3 * indentityMatrix3x3)

    # vector production
    unitVectorX = np.array([1,0,0])
    unitVectorY = np.array([0,1,0])
    unitVectorZ = np.array([0,0,1])

    print(indentityMatrix3x3 @ unitVectorX)
    print(indentityMatrix3x3 @ unitVectorY)
    print(indentityMatrix3x3 @ unitVectorZ)

    print(matrix3x3 @ unitVectorX)
    print(matrix3x3 @ unitVectorY)
    print(matrix3x3 @ unitVectorZ)
    # or
    print(np.matmul(matrix3x3, unitVectorX))
    print(np.matmul(matrix3x3, unitVectorY))
    print(np.matmul(matrix3x3, unitVectorZ))
    # or
    print(np.dot(matrix3x3, unitVectorX))
    print(np.dot(matrix3x3, unitVectorY))
    print(np.dot(matrix3x3, unitVectorZ))

    # inner production
    print(np.inner(unitVectorX, unitVectorY))

    # invert matrix, matrix production
    invertMarix3x3 = np.linalg.inv(matrix3x3)
    print(invertMarix3x3)
    print(np.matmul(invertMarix3x3, matrix3x3))

    # eigenvalue vector
    eigenvalueMatrix3x3, eignevalueVectorMatrix3x3 = np.linalg.eig(matrix3x3)
    print(eigenvalueMatrix3x3)
    print(eignevalueVectorMatrix3x3)
def main():
    TestMatrix()

if __name__ == "__main__":
    main()
