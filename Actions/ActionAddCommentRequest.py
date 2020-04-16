from Actions.Abstract.Action import Action


class ActionAddCommentRequest(Action):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)

        self.TREE = {


            {'id': 'START', 'action': EventSendMessage(text='Введи коментарий'), 'resolver': '2'},
            {'id': '2', 'action': EventWait(), 'resolver': '3'},
            {'id': '3', 'action': EventEntityExtractor('raw'), 'resolver': 'END'},

        }
