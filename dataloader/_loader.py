from abc import ABCMeta, abstractmethod
from typing import Protocol, runtime_checkable

from pandas import DataFrame


@runtime_checkable
class LoaderProtocol(Protocol):
    """
    This Protocol is used to store class variables that can be checked with a
    linter.
    """

    name: str

    df: DataFrame
    trainingDF: DataFrame
    validationDF: DataFrame
    testingDF: DataFrame


class LoaderABC(LoaderProtocol, metaclass=ABCMeta):
    """
    This abstract base class is used to store class methods that are to be
    implemented.
    """

    @abstractmethod
    def loadData(self) -> None:
        ...

    @abstractmethod
    def validateDF(self) -> bool:
        ...

    @abstractmethod
    def trainValidateTestSplit(
        self,
        validationSplit: float,
        testingSplit: float,
    ) -> None:
        ...
