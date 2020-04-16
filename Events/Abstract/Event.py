import CrossComponents
from abc import abstractmethod, ABC
import sys
import types

class Event(ABC):

    def __init__(self, message):

        self.components = CrossComponents.components
        self.logger = self.components.get_logger()
        self.verbosity = self.components.get_verbosity()
        self.state = self.components.get_state()
        self.message = message


    @abstractmethod
    def do(self):
        pass

    def exception_with_traceback(self, message):
        tb = None
        depth = 0
        while True:
            try:
                frame = sys._getframe(depth)
                depth += 1
            except ValueError as exc:
                break

            tb = types.TracebackType(tb, frame, frame.f_lasti, frame.f_lineno)

        return Exception(message).with_traceback(tb)


    def make_response(self, status, error=None, data=None, **kwargs):


        error = None if not error else self.exception_with_traceback(error) if not isinstance(error, Exception) else error


        if self.verbosity > 1:
            if kwargs:
                self.logger.info("Args:")
                for k, v in kwargs:
                    self.logger.info(f"{k}: {v}")

        if error:
            self.logger.exception(f"{self.__class__.__name__} | Error: {error}")


        return {
            'status': status,
            'error': error,
            'data': data
        }
