from Actions.Abstract.Action import Action


class ActionClarifyIntent(Action):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)

        self.TREE = {


            {'id': '1', 'action': EventSendButtons(text='', buttons='да или нет'), 'resolver': '2'},
            {'id': '2', 'action': EventWait(), 'resolver': '3'},
            {'id': '3', 'action': EventEntityExtractor('raw'), 'resolver': '4'},
            {'id': '4', 'action': EventStop(), 'resolver': 'END'},
        }
