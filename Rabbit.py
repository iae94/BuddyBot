from threading import Thread
class Rabbit:
    def __init__(self):
        pass
    def receive(self):

        basic_consumer = channel.basic_consume(Thread(target=CoreStarter.run, args=(json.loads(channel.body),)))
        basic_consumer.start()





