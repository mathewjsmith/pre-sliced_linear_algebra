from pre_sliced.apply import apply
from pre_sliced.operands.vectors import TBVector, LRVector
from pre_sliced.operands.scalar import Scalar
from math import sqrt


def axpy(alpha: Scalar, x: TBVector, y: TBVector):
    return apply(axpy_kernel, alpha, x, y)


def axpy_kernel(alpha: float, chi: float, psi: float):
    return alpha * chi + psi


def scal(alpha: Scalar, x: TBVector):
    return apply(lambda alpha, x: alpha * x, alpha, x)


def dot_product(x: LRVector, y: TBVector):
    alpha = Scalar(0)
    return apply(lambda chi, psi, alpha: chi * psi + alpha, x, y, alpha)


def euclidean_length(x: TBVector):
    sum_of_squares = dot_product(x, x)
    return sqrt(sum_of_squares)
