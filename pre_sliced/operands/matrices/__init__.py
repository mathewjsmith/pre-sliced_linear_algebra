from pre_sliced.operands.matrices.forward_matrix import ForwardMatrix
from pre_sliced.operands.vectors import LRVector, TBVector
from typing import List


class TBMatrix(ForwardMatrix):
    def __init__(self, rows: List[LRVector]):
        self.value = rows


class LRMatrix(ForwardMatrix):
    def __init(self, columns: List[TBVector]):
        self.value = columns
