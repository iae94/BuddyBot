from Actions.Abstract.Action import Action


class ActionCreateRequest(Action):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)

        self.ABSTRACT_TREE = [

            {'id': '1', 'action': EventSendMessage(text='Подожди создаю заявку'), 'resolver': 'INHERIT_IN'},

            {'id': 'INHERIT_OUT', 'action': EventSendMessage(text='Номер река'), 'resolver': '2'},
            {'id': '2', 'action': EventStop(), 'resolver': 'END'},

            #{'id': '1', 'action': 1, 'resolver': 'INHERIT_IN'},
            #{'id': 'INHERIT_OUT', 'action': 2, 'resolver': '3'},
            #{'id': '3', 'action': 3, 'resolver': 'END'},

        ]



class ActionCreateRequest1(ActionCreateRequest):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)

        #super(ActionCreateRequest, self).__getattribute__('TREE').copy()

        self.TREE = [


            {'id': '1', 'action': 4, 'resolver': '2'},
            {'id': '2', 'action': 5, 'resolver': '3'},
            {'id': '3', 'action': 6, 'resolver': '4'},

        ]

        self.inherit()

A = ActionCreateRequest1('123')
x = 5