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
        self._db = self._mongo[name]
        self.name = name

    def _collection(self, bucket_name):
        return self._db[bucket_name]

    def store(self, bucket_name, records):
        for record in records:
            self._collection(bucket_name).save(record.to_dict())
