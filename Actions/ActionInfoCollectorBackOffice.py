from Actions.Abstract.Action import Action
from Events.EventEntityExtractor import EventEntityExtractor

class ActionInfoCollectorBackOffice(Action):
    '''
    1. Отправляем тематики пользователю кнопками
    2. В зависимости от нажатой кнопки отправляем подтематики кнопками
    3. Уточняем город
    4. В зависимости от нажатой подтематики отправляем текст с запросом кучи данных за один присест
    5. Сохраняем полученные данные

    '''
    def __init__(self, message, **kwargs):
        super().__init__(message)


        self.methods = kwargs['methods']



        self.TREE = [

            {'id': 'START', 'action': EventStart(), 'resolver': '1'},

            {'id': '1', 'action': EventSendButtons('тематики'), 'resolver': '2'},
            {'id': '2', 'action': EventWait(), 'resolver': '3'},

            {'id': '3', 'action': EventEntityExtractor('извлекаем первую цифру'), 'resolver': lambda res: '3.1' if res else '3.2', 'childrens': [

                {'id': '3.1', 'action': EventSendButtons("Регистрация документов"), 'resolver': '4'},
                {'id': '3.2', 'action': EventSendButtons("Запросы от СЗБ"), 'resolver': '4'},

            ]},

            {'id': '4', 'action': EventWait(), 'resolver': '5'},
            {'id': '5', 'action': EventEntityExtractor('извлекаем вторую цифру'), 'resolver': '6'},
            {'id': '6', 'action': EventSendButtons('уточняем город'), 'resolver': '7'},
            {'id': '7', 'action': EventWait(), 'resolver': '8'},


            {'id': '8', 'action': EventEntityExtractor('извлекаем город'), 'resolver': lambda res: '3.1' if res else '3.2', 'childrens': [
                {'id': '8.1', 'action': EventSendMessage('запрос кучи данных'), 'resolver': '10'},
                {'id': '8.2', 'action': EventSendMessage('запрос кучи данных'), 'resolver': '10'},
                {'id': '8.3', 'action': EventSendMessage('запрос кучи данных'), 'resolver': '10'},
                {'id': '8.4', 'action': EventSendMessage('запрос кучи данных'), 'resolver': '10'},
            ]},

            {'id': '10', 'action': EventWait(), 'resolver': '11'},

            {'id': '11', 'action': EventEntityExtractor('извлекаем кучу данных'), 'resolver': '12'},
            {'id': '12', 'action': EventRemedyAPI('извлекаем авто комплит данные'), 'resolver': 'END'},

            {'id': 'END', 'action': EventStop(), 'resolver': 'END'}



                # {'id': '3.1.1', 'action': EventEntityExtractor('извлекаем вторую цифру'), 'resolver': '?',
                #  'childrens': [
                #
                #      {'id': '3.1.1.1', 'action': EventEntityExtractor('извлекаем город'), 'resolver': '3'},
                #      {'id': '2', 'action': EventSendMessage('запрос кучи данных'), 'resolver': '3'},
                #      {'id': '2', 'action': EventEntityExtractor('извлекаем кучу данных'), 'resolver': '3'},
                #
                #  ]},
                #
                #
                #
                # {'id': '3.1.1', 'action': EventEntityExtractor('извлекаем вторую цифру'), 'resolver': '?',
                #  'childrens': [
                #
                #      {'id': '3.1.1.1', 'action': EventEntityExtractor('извлекаем город'), 'resolver': '3'},
                #      {'id': '2', 'action': EventSendMessage('запрос кучи данных'), 'resolver': '3'},
                #      {'id': '2', 'action': EventEntityExtractor('извлекаем кучу данных'), 'resolver': '3'},
                #
                #  ]},

        ]


        self.state = {
            'Homer': {
                'пройденные шаги': [
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
                'next_action': '4',
                'next_event': '5',

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



        self.MAP = {
            "Регистрация документов": {
                "counter": 3,
                "subjects": {
                    "Договор": {
                        "counter": 1,
                        'SLM': 56,
                        "auto_complete": {
                            "Дирекция": self.remedy.get_direction,
                            "Региональный центр": self.remedy.get_regional_centre
                        },
                        "need_data": [
                            "Код партнера",
                            "Комментарий"
                        ]
                    },
                    "ДС на МА": {
                        "counter": 2,
                        'SLM': 56,
                        "auto_complete": {
                            "Дирекция": self.remedy.get_direction,
                            "Региональный центр": self.remedy.get_regional_centre
                        },
                        "need_data": [
                            "Код партнера",
                            "Комментарий"
                        ]
                    },
                    "ДС на ТТ": {
                        "counter": 3,
                        'SLM': 56,
                        "auto_complete": {
                            "Дирекция": self.remedy.get_direction,
                            "Региональный центр": self.remedy.get_regional_centre
                        },
                        "need_data": [
                            "Код партнера",
                            "Комментарий"
                        ]
                    },
                    "Уведомление на ТТ": {
                        "counter": 4,
                        'SLM': 56,
                        "auto_complete": {
                            "Дирекция": self.remedy.get_direction,
                            "Региональный центр": self.remedy.get_regional_centre
                        },
                        "need_data": [
                            "Код партнера",
                            "Комментарий"
                        ]
                    },
                    "Соглашение об ЭДО": {
                        "counter": 5,
                        'SLM': 56,
                        "auto_complete": {
                            "Дирекция": self.remedy.get_direction,
                            "Региональный центр": self.remedy.get_regional_centre
                        },
                        "need_data": [
                            "Код партнера",
                            "Комментарий"
                        ]
                    }
                }
            },  # Ready
            "Запросы от СЗБ": {
                "counter": 4,
                "subjects": {
                    "Предоставление РК / Реестра": {
                        "counter": 1,
                        'SLM': 56,
                        "auto_complete": {
                            "Дирекция": self.remedy.get_direction,
                            "Региональный центр": self.remedy.get_regional_centre
                        },
                        "need_data": [
                            "Комментарий",
                        ]
                    },
                    "Принятие полномочий на сотрудников ТО": {
                        "counter": 2,
                        'SLM': 56,
                        "auto_complete": {
                            "Дирекция": self.remedy.get_direction,
                            "Региональный центр": self.remedy.get_regional_centre
                        },
                        "need_data": [
                            "Комментарий",
                        ]
                    }
                }
            },  # Ready
        }



    def do(self):

        EventSendButtons('тематики')
        EventWait()
        EventEntityExtractor('извлекаем первую цифру')
        EventSendButtons('подтематики')
        EventWait()
        EventEntityExtractor('извлекаем вторую цифру')
        EventSendButtons('уточняем город')
        EventWait()
        EventEntityExtractor('извлекаем город')
        EventSendMessage('запрос кучи данных')
        EventWait()
        EventEntityExtractor('извлекаем кучу данных')
        EventRemedyAPI('извлекаем авто комплит данные')




        event_entity_extractor = EventEntityExtractor(text=self.message['text'], methods=self.methods)
        event_entity_extractor_result = event_entity_extractor.do()

        # Дозапрашиваем недостающие данные





"""
{
"user": {
    "chat_id": "",
    "fio": "",
    "language": "ru"
},
"message": {
    "date": "",
    "message_id": ""
},
"text": "",

"video": {
    "original": {
        "link": "",
        "name": "",
        "duration": 72,
        "size": 7845662
    }
    "thumb": {
        "link": "",
        "name": "",
        "duration": 72,
        "size": 7845662
    }
},
"photo": {
    "original": {
        "link": "",
        "name": "",
        "size": 7845662
    }
    "thumb": {
        "link": "",
        "name": "",
        "size": 7845662
    }
},
"file": {
    "link": "",
    "name": "",
    "size": 7845662
},
"contact": {
    "phone": "79611505050",
    "fio": "",
    "chat_id": ""
},
}
"""

