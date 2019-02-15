import pre_sliced.operations
from pre_sliced.matrix_entities.scalar import Scalar
from pre_sliced.matrix_entities.vectors import TBVector


def test_axpy():
    alpha = Scalar(2)
    x = TBVector([1, 1, 1])
    y = TBVector([2, 2, 2])
    assert operations.axpy(alpha, x, y) == [4, 4, 4]
