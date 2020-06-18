from abc import ABC, abstractmethod

class Sentimenter(ABC):
    @abstractmethod
    def analyze_text(self, text):
        pass

