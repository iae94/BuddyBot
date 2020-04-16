import logging, sys
from EntityExtractor import EntityExtractor
from State import State

class CrossComponents:
    def __init__(self):

        logger = logging.getLogger('some Parser')
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '[%(asctime)s] - %(name)-20s - %(module)-20s - %(threadName)-20s - [%(levelname)-8s] - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        self.logger = logger
        self.entity_extractor = EntityExtractor()
        self.verbosity = 1

    def set(self, v):
        self.x = v

    def get_logger(self):
        return self.logger
    def get_entity_extractor(self):
        return self.entity_extractor
    def get_verbosity(self):
        return self.verbosity
    def get_state(self, chat_id, intent_name):
        return State(chat_id, intent_name)



components = CrossComponents()