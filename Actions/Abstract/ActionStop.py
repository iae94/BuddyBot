from Actions.Abstract.Action import Action


class ActionStop(Action):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)

        self.TREE = {

            {'id': 'START', 'action': EventSendMessage('спасибо за обращение, и все'), 'resolver': 'END'},

        }

