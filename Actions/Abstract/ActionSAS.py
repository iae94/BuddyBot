from Actions.Abstract.Action import Action


class ActionSAS(Action):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)

        self.ABSTRACT_TREE = [

            {'id': 'START', 'action': EventStart(), 'resolver': 'INHERIT_IN'},
            {'id': 'INHERIT_OUT', 'action': EventStop(), 'resolver': 'END'},

        ]

