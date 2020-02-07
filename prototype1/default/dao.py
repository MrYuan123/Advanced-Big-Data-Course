import redis


class dao(object):
    host = '127.0.0.1'
    port = '6379'
    connection = None

    def __init__(self):
        self.connection = self.connectfunc()

    def connectfunc(self):
        return redis.Redis(host=self.host, port=self.port)

    def getfunc(self, name):
        result = self.connection.hgetall(name)
        return {k.decode('utf8'): v.decode('utf8') for k, v in result.items()}

    def setfunc(self, name,  mapping):
        self.connection.hmset(name, mapping=mapping)

    def delfun(self, name):
        self.connection.delete(name)

    def setETagfun(self, etag_value):
        self.connection.sadd('ETag', etag_value)

    def getETagfun(self, hash_value):
        return self.connection.sismember('ETag', hash_value)

    def clearETagfun(self):
        self.connection.delete('ETag')


if __name__ == "__main__":
    r = dao()
    r.setfunc('Leo', 12, 'Jingchuan', 'email@123.com', 123456)
    # print(r.getfunc('Leo'))
    # r.delfun('Leo')
    # print(r.getfunc('Leo'))
