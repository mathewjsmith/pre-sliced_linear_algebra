from pre_sliced.apply import apply
from pre_sliced.operands.vectors import TBVector
from pre_sliced.operands.matrices import TBMatrix, LRMatrix
from pre_sliced.operands.scalar import Scalar
from pre_sliced.generator import generate_tb_vector, generate_list
from pre_sliced.operations.vector import dot_product, axpy
from pre_sliced.operands.vectors.fixed_vector import FixedVector


def linear_transformation_1(A: TBMatrix, x: TBVector):

    y = generate_tb_vector(0, 0, len(x.value))

    def kernel(a: TBVector, psi: Scalar):
        return dot_product(a, x) + psi

    return apply(kernel, A, y)


def linear_transformation_2(A: LRMatrix, x: TBVector):

    y = FixedVector(generate_list(0, 0, len(x.value), False))

    def kernel(chi: Scalar, a: TBVector, y: FixedVector):
        return axpy(Scalar(chi), a, TBVector(y.value))

    return apply(kernel, x, A, y)
