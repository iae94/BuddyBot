from Auth import Auth
from ML.ML import ML
from APIs.PSQL import PSQL
from State import State

import CrossComponents

class CoreStarter:
    def __init__(self):

        self.a = CrossComponents.components
        self.auth = Auth()
        self.ml = ML()
        self.PSQL = PSQL()

        pass


    def run(self, msg):

        chat_id = msg['user']['chat_id']

        user_info = self.PSQL.get_user_info(chat_id)
        user_state = State(components={'psql': self.PSQL}, chat_id=chat_id)   # History state and fresh state


        if (user_info['auth']):

            intent_name = user_state.get_intent() or self.ml.predict(msg['text'])


            intent_class = getattr(globals()[intent_name], intent_name)
            intent = intent_class(message=msg)






        else:
            self.auth.do_auth(chat_id)



if __name__ == '__main__':
    CoreStarter()