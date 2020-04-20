import CrossComponents
from datetime import datetime
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
        self.intent_name = intent_name

        self.state = self.PSQL.get_state(chat_id)

        self.state_example = {
            'Homer': {
                'steps': [
                    {'date': 1, 'step': '1', 'status': 'success', 'name': 'Action1', 'state': [
                        {'date': 1, 'step': '1', 'status': 'success', 'name': 'Event1'},
                        {'date': 2, 'step': '2', 'status': 'success', 'name': 'Event2'},
                        {'date': 3, 'step': '3', 'status': 'success', 'name': 'Event3'},
                    ]},
                    {'date': 2, 'step': '2', 'status': 'success', 'name': 'Action2', 'state': [
                        {'date': 1, 'step': '1', 'status': 'success', 'name': 'Event1'},
                        {'date': 2, 'step': '2', 'status': 'success', 'name': 'Event2'},
                        {'date': 3, 'step': '3', 'status': 'success', 'name': 'Event3'},
                    ]},
                ],

                'next': {
                    'action': {'id': '4', 'name': 'Action1'},
                    'event': {'id': '5', 'name': 'Event1'},
                },

                'data': {
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

                },

                'last_response': {
                    'status': "status",
                    'error': "error",
                    'data': "данные"
                }
            }
        }

    def get_data(self, key=None):
        """
        Обычное поведение:
        Возвращает словарь с данными, которые были извлечены на этапе EntityExtractor.

        Поведении при отсутствии ключа - key:
        Если по каким то причинам данных нет, то возвращается пустой список.
        :param key: Ключ из словаря с данными (например phone).
        :return:
        """
        return self.state[self.intent_name]['data'].get(key, {}).get("value", [])

    def get_next(self):
        """

        Обычное поведение:
        Возвращает словарь со следующими шагами:
        :return:
        {
            'action': {'id': '4', 'name': 'ActionName4'},
            'event': {'id': '5', 'name': 'EventName5'},
        }

        Поведение при всех видах ошибок:
        Отсутствует, т.к. если объекта State нет, то должно было выйти из обработки еще на этапе входа в Intent.
        """
        if self.intent_name not in self.state:
            self.state[self.intent_name] = {
                'steps': [],
                'next': {},
                'data': {},
                'last_response': {}
            }
        return self.state[self.intent_name]['next']


    def set_data(self, key, value):
        """
        Записывает в State данные из Value по переданному ключу Key.

        :param key: Ключ для записи данных в объекте State
        :param value: Данные, которые необходимо внести в объект State.
        :return: Ничего не возвращяет.
        """

        self.state[self.intent_name]['data'][key] = {
            'action': self.state[self.intent_name]['next']['action']['id'],
            'event': self.state[self.intent_name]['next']['event']['id'],
            'value': value
        }


    def set_next(self, action, event):
        """
        Функция обновления состояний бота, вызывается после кажедого завершения Event и Action.

        :param action: {"id": "1", "name": "Action1", "status": "Success"}
        :param event: {"id": "1", "name": "Event1", "status": "Bad"}
        :return: Ничего не возвращяет.
        """
        #todo  возможно имеет смысл сделать через датафрейм
        try:

        for step in reversed(self.state[self.intent_name]['steps']):
            if step['id'] == self.state[self.intent_name]['next']['action']['id']:

                if self.state[self.intent_name]['next']['action']['id'] != action['id']:

                    # добавляем новую запись о начале экшена
                    self.state[self.intent_name]['steps'].append({
                        'date_start': str(datetime.now()),
                        'date_end': str(datetime.now()),
                        'step': action['id'],
                        'status': 'in_progress',
                        'name': action['name'],
                        'state': []
                    })
                    step['status'] = self.state[self.intent_name]['last_response']['status']
                    step['date_end'] = str(datetime.now())

                for evnt in step['state']:
                    if event['id'] == self.state[self.intent_name]['next']['event']['id']:
                        if self.state[self.intent_name]['next']['event']['id'] != event['id']:
                            step['state'].append({
                                'date_start': str(datetime.now()),
                                'date_end': str(datetime.now()),
                                'step': event['id'],
                                'status': 'in_progress',
                                'name': event['name']
                            })
                            evnt['status'] = self.state[self.intent_name]['last_response']['status']
                            evnt['date_end'] = str(datetime.now())


                        break
                break
        # записываем
        self.state[self.intent_name]['next']['action'] = action
        self.state[self.intent_name]['next']['event'] = event

def update(func):
    def update_inner(*args, **kwargs):
        # Before
        func(*args, **kwargs)
        # After



        return func(*args, **kwargs)
    return update_inner