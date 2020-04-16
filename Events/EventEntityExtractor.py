from Events.Abstract.Event import Event
from State import State
class EventEntityExtractor(Event):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.EE = self.components.get_entity_extractor()
        self.text = kwargs['text']
        self.methods = kwargs['methods']

    @State.update
    def do(self):
        try:
            result = self.EE.extract(text=self.text, methods=self.methods)
            #result = '123123'



            return self.make_response(status=True, error='231123', data=result)

        except Exception as e:
            x = 5
            #return self.make_response(status=True, error=e)
        x = 6
        return