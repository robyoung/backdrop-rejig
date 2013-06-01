import pymongo

class Database(object):
    @classmethod
    def from_config(cls, config):
        return cls(
            config['MONGO_HOST'],
            config['MONGO_PORT'],
            config['DATABASE_NAME'],
        )

    def __init__(self, host, port, name):
        self._mongo = pymongo.Connection(host, port)
        self.name = name