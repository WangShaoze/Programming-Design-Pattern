
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Numer(Singleton):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)


class Connection:
    pass

class DatabasePool(Singleton):
    connections = []
    user_li = []
    def __init__(self, name:str, pwd:str):
        self.name = name
        self.pwd = pwd
        self.user_li.append({"name":name, "pwd":pwd})

    def create_connection(self):
        self.connections.append(Connection())
        print("user {}:{} connection db.".format(self.name, self.pwd))


class Logger(Singleton):
    pass

if __name__ == "__main__":
    a = Numer(10)
    print(a)
    b = Numer(23)
    print(b)

    print("a 地址:{}".format(id(a)))
    print("b 地址:{}".format(id(b)))

    u1 = DatabasePool("u1", "olo")
    u1.create_connection()

    u2 = DatabasePool("u2", "ol")
    u2.create_connection()

    print(u1 is u2)
    print("u1 connections len:{}".format(len(u1.connections)))
    print("u2 connections len:{}".format(len(u2.connections)))

    print("u1 user_name:{}".format(u1.name))
    print("u2 user_name:{}".format(u2.name))


    print("u1 user_li:{}".format(u1.user_li))
    print("u2 user_li:{}".format(u2.user_li))
