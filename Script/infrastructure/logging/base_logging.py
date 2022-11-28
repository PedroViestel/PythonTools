
from abc import ABC, abstractmethod

class BaseLogging(ABC):
    @abstractmethod
    def log(self, message):
        pass