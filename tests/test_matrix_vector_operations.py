from pre_sliced.operations.matrix_vector import linear_transformation_1, linear_transformation_2
from pre_sliced.operands.matrices import TBMatrix, LRMatrix
from pre_sliced.operands.vectors import TBVector, LRVector


def test_linear_transformation_1():
    A = TBMatrix([LRVector([1, 0]), LRVector([1, 1])])
    x = TBVector([2, 2])
    assert linear_transformation_1(A, x) == [4, 2]


def test_linear_transformation_2():
    A = LRMatrix([TBVector([1, 1]), TBVector([0, 1])])
    x = TBVector([2, 2])
    assert linear_transformation_2(A, x) == [4, 2]
