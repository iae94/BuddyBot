from Intents.Abstract.Intent import Intent
from Actions.ActionInfoCollector import ActionInfoCollector, ActionClarifyIntent

class IntentCreateRequest(Intent):
    '''
    1. Извлекаем entity из введенного текста
    2. Если чего то не хватает дозапрашиваем
    3. Показываем меню (создать/добавить вложение/отменить) заявки
    4. Создание заявки
    5. Отправка номера река

    Stages:
    1. Уточнить интент - [ActionClarifyIntent]
    2. Сбор данных - [ActionInfoCollector]
    3. Показываем меню - [actionShow]
    4. Создаем заявку - [ActionCreateRequest]

    '''



    def __init__(self, state, message):
        super().__init__(state, message)

        # self.intent_info = {
        #     'first_reaction'
        # }


    def flow(self, stage):




        ActionClarifyIntent().do()

        ActionInfoCollector(message=self.message, methods=['name', 'phone'])





