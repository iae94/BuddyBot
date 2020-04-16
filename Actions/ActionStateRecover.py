from Actions.Abstract.Action import Action


class ActionStateRecover(Action):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)

        self.TREE = {

            {'id': '1', 'action': EventStateExtractor(), 'resolver': '2'},
            {'id': '2', 'action': EventStop(), 'resolver': 'END'},

        }

