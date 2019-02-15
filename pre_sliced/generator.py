import random
from pre_sliced.matrix_entities.scalar import Scalar
from pre_sliced.matrix_entities.vectors import TBVector, LRVector


def generate_scalar(minimum=0, maximum=10, integers_only=False):
    if integers_only:
        return Scalar(random.randint(minimum, maximum))
    else:
        return Scalar(random.random(minimum, maximum))


def generate_tb_vector(minimum=0, maximum=10, length=3, integers_only=False):
    return TBVector(generate_list(minimum, maximum, length, integers_only))


def generate_lr_vector(minimum=0, maximum=10, length=3, integers_only=False):
    return LRVector(generate_list(minimum, maximum, length, integers_only))


def generate_list(minimum, maximum, length, integers_only):
    if integers_only:
        return [random.randint(minimum, maximum) for _ in range(length)]
    else:
        return [random.randrange(minimum, maximum) for _ in range(length)]

