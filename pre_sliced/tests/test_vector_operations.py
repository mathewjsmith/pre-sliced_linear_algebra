from pre_sliced.operations import axpy, scal, dot_product, euclidean_length
from pre_sliced.matrix_entities.scalar import Scalar
from pre_sliced.matrix_entities.vectors import TBVector


def test_axpy():
    alpha = Scalar(2)
    x = TBVector([1, 1, 1])
    y = TBVector([2, 2, 2])
    assert axpy(alpha, x, y) == [4, 4, 4]


def test_scal():
    alpha = Scalar(3)
    x = TBVector([3, 3, 3])
    assert scal(alpha, x) == [9, 9, 9]


def test_dot_product():
    x = TBVector([1, 2])
    y = TBVector([2, 1])
    assert dot_product(x, y) == 4


def test_euclidean_length():
    x = TBVector([3, 4])
    assert euclidean_length(x) == 5
