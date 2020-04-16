from Intents.Abstract.Intent import Intent
from Actions.ActionInfoCollector import ActionInfoCollector
from Actions.ActionClarifyIntent import ActionClarifyIntent


class IntentCreateRequestUFO(Intent):
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
            'flow': {

            }
        }




    def flow(self, stage):
        ActionClarifyIntent().do()

        ActionInfoCollector(message=self.message, methods=['name', 'phone'])
