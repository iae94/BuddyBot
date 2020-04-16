from Actions.Abstract.Action import Action
from Actions.Abstract.ActionCreateRequest import ActionCreateRequest


class ActionCreateRequestUFO(ActionCreateRequest):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


        self.TREE = {


            #{'id': '1', 'action': EventSendMessage(text='Подожди создаю заявку'), 'resolver': '2'},

            {'id': 'START', 'action': EventRequestPrepareUFO(), 'resolver': '2'},
            {'id': '2', 'action': EventRemedyAPI('post'), 'resolver': '3'},
            {'id': '3', 'action': EventRemedyAPI('put'), 'resolver': 'END'},



            #{'id': '4', 'action': EventSendMessage(text='Подожди создаю заявку'), 'resolver': '5'},
            #{'id': '5', 'action': EventStop(), 'resolver': 'END'},

        }

        self.inherit()
