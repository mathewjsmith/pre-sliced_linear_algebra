from abc import ABC, abstractmethod


class MatrixEntity(ABC):

    @abstractmethod
    def partition(self):
        pass


class PartitionedMatrixEntity(ABC):

    @abstractmethod
    def expose(self):
        pass

    @abstractmethod
    def is_complete(self):
        pass

    @abstractmethod
    def combine(self):
        pass


class ExposedMatrixEntity(ABC):

    @abstractmethod
    def repartition(self):
        pass

    @abstractmethod
    def exposed_value(self):
        pass

    @abstractmethod
    def update(self, alpha: float):
        pass