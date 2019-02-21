import random
from pre_sliced.operands.scalar import Scalar
from pre_sliced.operands.vectors import TBVector, LRVector


def generate_scalar(minimum=0, maximum=10, allow_decimals=False):
    if allow_decimals:
        return Scalar(random.uniform(minimum, maximum))
    else:
        return Scalar(random.randint(minimum, maximum))


def generate_tb_vector(minimum=0, maximum=10, length=3, allow_decimals=False):
    return TBVector(generate_list(minimum, maximum, length, allow_decimals))


def generate_lr_vector(minimum=0, maximum=10, length=3, allow_decimals=False):
    return LRVector(generate_list(minimum, maximum, length, allow_decimals))


def generate_list(minimum, maximum, length, allow_decimals):
    assert length < 993, "A list of length " + str(length) + " will exceed python's recursion limit."
    if allow_decimals:
        return [random.uniform(minimum, maximum) for _ in range(length)]
    else:
        return [random.randint(minimum, maximum) for _ in range(length)]
