from Interface.ConnectionAPP import ConnectionAPP


class DataAccess(ConnectionAPP):
    __conn: ConnectionAPP

    def __init__(self, conn):
        self.conn = conn

    @property
    def conn(self):
        return self.__conn

    @conn.setter
    def conn(self, value):
        self.__conn = value

    def get_data(self):
        self.__conn.get_data()
