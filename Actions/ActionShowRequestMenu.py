from Actions.Abstract.Action import Action


class ActionShowRequestMenu(Action):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)

        self.TREE = {


            #{'id': '1', 'action': EventStart(), 'resolver': lambda res: 'START' if not res['next_state'] else res['next_state']},


            {'id': 'START', 'action': EventSendButtons(text='', buttons='создать, добавить вложение, добавить коммент, отмена'), 'resolver': '2'},
            {'id': '2', 'action': EventWait(), 'resolver': '3'},
            {'id': '3', 'action': EventEntityExtractor('raw'), 'resolver': 'END'},


            #{'id': '4', 'action': EventStop(), 'resolver': 'END'},

        }
