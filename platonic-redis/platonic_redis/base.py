from redis import Redis


class RedisMixin:
    url = 'localhost'

    _connection: Redis = None

    def create_connection(self):
        return Redis(self.url)

    @property
    def redis(self):
        if self._connection is None:
            self._connection = self.create_connection()

        return self._connection
