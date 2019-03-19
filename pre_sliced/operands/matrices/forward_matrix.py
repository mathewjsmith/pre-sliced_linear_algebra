from pre_sliced.operands import Operand, PartitionedOperand, ExposedOperand
from pre_sliced.operands.vectors.forward_vector import ForwardVector, PartitionedForwardVector, ExposedForwardVector
from typing import List


class ForwardMatrix(Operand):
    def __init__(self, values: List[ForwardVector]):
        self.value = values

    def partition(self):
        return PartitionedForwardMatrix([v.partition() for v in self.value])

    def get_value(self):
        return self.value


class PartitionedForwardMatrix(PartitionedOperand):
    def __init__(self, values: List[PartitionedForwardVector]):
        self.value = values

    def expose(self):
        return ExposedForwardMatrix([v.expose() for v in self.value])

    def is_complete(self):
        return all(v.is_complete for v in self.value)

    def combine(self):
        return ForwardMatrix([v.combine() for v in self.value])


class ExposedForwardMatrix(ExposedOperand):
    def __init__(self, values: List[ExposedForwardVector]):
        self.value = values

    def repartition(self):
        return PartitionedForwardMatrix([v.repartition() for v in self.value])

    def exposed_value(self):
        return ForwardVector([v.exposed_value() for v in self.value])

    def update(self, x):
        updates = [v.update(chi) for chi, v in (x, self.value)]
        return ExposedForwardMatrix(updates)
