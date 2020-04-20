import CrossComponents
from abc import abstractmethod, ABC

class API(ABC):
    def __init__(self, *args, **kwargs):
        self.components = CrossComponents.components
        self.config = self.components['config']
        self.logger = self.components['logger']

