from Actions.Abstract.Action import Action


class ActionStart(Action):

    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)

        self.TREE = {

            {'id': 'START', 'action': EventStart(), 'resolver': lambda res: 'START' if not res['next_state'] else res['next_state']},
        }

