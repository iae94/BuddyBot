from APIs.Abstract.API import API
import psycopg2

class PSQL(API):
    def __init__(self):
        super().__init__()
        self.conn = self.connect()

    def connect(self):
        try:
            self.conn = psycopg2.connect(f"dbname='{self.config['dbname']}' user='{self.config['dbuser']}' host='{self.config['dbhost']}' password='{self.config['dbpassword']}'")
            self.conn.autocommit = True
        except Exception as e:
            self.logger.exception(e)
            raise e

    def close(self):
        try:
            self.conn.close()
            self.conn = None
        except Exception as e:
            self.logger.exception(e)
            self.conn = None

    def get_state(self, chat_id):
        try:

        except Exception as e:
            self.logger.exception(e)

    def get_user_info(self, chat_id):
        return True