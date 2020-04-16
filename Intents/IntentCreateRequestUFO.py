from Intents.Abstract.Intent import Intent
from Actions.ActionInfoCollector import ActionInfoCollector
from Actions.ActionClarifyIntent import ActionClarifyIntent
from Actions.ActionStateRecover import ActionStateRecover


class IntentCreateRequestUFO(IntentCreateRequest):
    '''
    1. Извлекаем entity из введенного текста
    2. Если чего то не хватает дозапрашиваем
    3. Показываем меню (создать/добавить вложение/отменить) заявки
    4. Создание заявки
    5. Отправка номера река
    '''

    def __init__(self, state, message):
        super().__init__(state, message)

        self.intent_info = {
            'intent_name': 'Ошибка UFO',
            'text': {
                'greetings': [
                    'Привет',
                    'Доров',
                ],
                'state': ['Хочешь продолжить заполнять заявку UFO?'],
                'clarify': ['Хочешь создать заявку по шаблону 0.1 0.1 0.1 UFO?']
            }
        }



        self.TREE = {

            #{'id': '1', 'action': ActionStateRecover(''), 'resolver': lambda res: '2' if not res['next_state'] else res['next_state']},

            {'id': 'START', 'action': ActionClarifyIntent(''), 'resolver': lambda res: '3' if res['Да'] else 'END'},
            {'id': '2.1', 'action': ActionInfoCollector('some'), 'resolver': '3'},


            {'id': '3', 'action': ActionShowRequestMenu(), 'resolver': lambda res: '3' if res['Да'] else '5'},
            {'id': '3.1', 'action': ActionCreateRequestUFO(), 'resolver': 'END'},
            {'id': '3.2', 'action': ActionAddAttachmentRequest(), 'resolver': '3'},
            {'id': '3.3', 'action': ActionAddCommentRequest(), 'resolver': '3'},


            #{'id': '5', 'action': ActionStop(), 'resolver': 'END'},

        }

