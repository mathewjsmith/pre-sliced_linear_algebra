from pre_sliced.apply import apply
from pre_sliced.operands.vectors import TBVector, LRVector
from pre_sliced.operands.scalar import Scalar
from math import sqrt


def axpy(alpha: Scalar, x: TBVector, y: TBVector):

    def kernel(alpha: float, chi: float, psi: float):
        return alpha * chi + psi

    return apply(kernel, alpha, x, y)


def scal(alpha: Scalar, x: TBVector):

    return apply(lambda alpha, x: alpha * x, alpha, x)


def dot_product(x: LRVector, y: TBVector):

    alpha = Scalar(0)

    def kernel(chi: float, psi: float, alpha: float):
        return chi * psi + alpha

    return apply(kernel, x, y, alpha)


def euclidean_length(x: TBVector):

    sum_of_squares = dot_product(x, x)

    return sqrt(sum_of_squares)


def add(x: TBVector, y: TBVector):

    return apply(lambda chi, psi: chi + psi, x, y)
