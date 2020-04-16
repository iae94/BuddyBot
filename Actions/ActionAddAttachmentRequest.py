from Actions.Abstract.Action import Action


class ActionAddAttachmentRequest(Action):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)

        self.TREE = {

            {'id': 'START', 'action': EventSendButtons(text='Добавь вложение', buttons=('назад')), 'resolver': '2'},
            {'id': '2', 'action': EventWait(), 'resolver': '3'},
            {'id': '3', 'action': EventEntityExtractor('raw'), 'resolver': lambda res: '3.1' if res['text'] is None else 'END'},
            {'id': '3.1', 'action': EventAttachmentExtractor(), 'resolver': 'START'},
        }
