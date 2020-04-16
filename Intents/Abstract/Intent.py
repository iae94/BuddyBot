from abc import abstractmethod, ABC, abstractproperty
import CrossComponents

class Intent(ABC):

    def __init__(self, message):

        self.components = CrossComponents.components
        self.logger = self.components.get_logger()
        self.verbosity = self.components.get_verbosity()
        self.state = self.components.get_state()
        self.message = message


        #self.intent_info
        #self.TREE

    @abstractmethod
    def flow(self, stage):


        pass
