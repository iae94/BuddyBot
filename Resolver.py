
import CrossComponents
class Resolver:
    def __init__(self, function, step1, step2):
        self.components = CrossComponents.components
        self.logger = self.components.get_logger()

        self.function = function
        self.step1 = step1
        self.step2 = step2

        pass

    def resolve(self, action_result):

        return self.step1 if self.function(action_result) else self.step2