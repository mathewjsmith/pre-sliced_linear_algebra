from pre_sliced.matrix_entities import MatrixEntity, PartitionedMatrixEntity, ExposedMatrixEntity
from typing import List


class ForwardVector(MatrixEntity):
    def __init__(self, value: List[float]):
        self.value = value

    def partition(self):
        return PartitionedForwardVector([], self.value)


class PartitionedForwardVector(PartitionedMatrixEntity):
    def __init__(self, top: List[float], bottom: List[float]):
        self.top = top
        self.bottom = bottom

    def expose(self):
        chi, *xs = self.bottom
        return ExposedForwardVector(self.top, chi, xs)

    def is_complete(self):
        return len(self.bottom) == 0

    def combine(self):
        return ForwardVector(self.top + self.bottom)

    def as_tuple(self):
        return self.top, self.bottom


class ExposedForwardVector(ExposedMatrixEntity):
    def __init__(self, x: List[float], chi: float, xs: List[float]):
        self.x = x
        self.chi = chi
        self.xs = xs

    def repartition(self):
        self.x.append(self.chi)
        return PartitionedForwardVector(self.x, self.xs)

    def exposed_value(self):
        return self.chi

    def update(self, chi):
        return ExposedForwardVector(self.x, chi, self.xs)

    def as_tuple(self):
        return self.x, self.chi, self.xs
