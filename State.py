import CrossComponents

class State:
    '''
    Таблица с завершенными интентами
    Один интент - один state
    History:
        date: дата завершения
        chat_id:
        intent_name:
        state:
    Таблица с еще незавершенными интентами
    Fresh:
        chat_id:
        state:





    '''

    def __init__(self, chat_id, intent_name):

        self.components = CrossComponents.components
        self.logger = self.components.get_logger()
        self.verbosity = self.components.get_verbosity()
        self.state = self.components.get_state()
        self.PSQL = self.components.get_psql()


        self.chat_id = chat_id

        self.state = self.PSQL.get_state(chat_id)

        self.state = {
            'Homer': {
                'steps': [
                    {'date': 1, 'step': '1', 'status': 'success', 'name': 'Action1', 'state': {
                        {'date': 1, 'step': '1', 'status': 'success', 'name': 'Event1'},
                        {'date': 2, 'step': '2', 'status': 'success', 'name': 'Event2'},
                        {'date': 3, 'step': '3', 'status': 'success', 'name': 'Event3'},
                    }},
                    {'date': 2, 'step': '2', 'status': 'success', 'name': 'Action2', 'state': {
                        {'date': 1, 'step': '1', 'status': 'success', 'name': 'Event1'},
                        {'date': 2, 'step': '2', 'status': 'success', 'name': 'Event2'},
                        {'date': 3, 'step': '3', 'status': 'success', 'name': 'Event3'},
                    }},
                ],

                'next': {
                    'action': {'id': '4', 'name': 'Action1'},
                    'event': {'id': '5', 'name': 'Event1'},
                },


                'data': {
                    #'phone': 90890384902348
                    'my_phone': {
                        'action': '2',
                        'event': '3',
                        'value': ['90890384902348', '90890384902348']
                    },
                    'friend_phone': {
                        'action': '2',
                        'event': '3',
                        'value': ['90890384902348', '90890384902348']
                    },
                    'my_age': {
                        'action': '2',
                        'event': '3',
                        'value': ['13', '80']
                    }

                }
            }
        }

    def get_data(self, key=None):
        pass
    def get_next(self):
        pass

    def set_data(self, key, value):
        pass
    def set_next(self, action, event):
        pass


    def update(self, func):



        def update_inner(**kwargs):

            # Before

            func()

            # After

        return update_inner