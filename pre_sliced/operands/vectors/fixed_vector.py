from pre_sliced.operands import Operand, PartitionedOperand, ExposedOperand
from typing import List


class FixedVector(Operand, PartitionedOperand, ExposedOperand):
    def __init__(self, value: List[float]):
        self.value = value

    def partition(self):
        return self

    def get_value(self):
        return self.value

    def expose(self):
        return self

    def is_complete(self):
        return True

    def combine(self):
        return self

    def repartition(self):
        return self

    def exposed_value(self):
        return self

    def update(self, value: List[float]):
        return FixedVector(value)
