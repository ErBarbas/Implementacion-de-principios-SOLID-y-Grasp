from Interface.ConnectionAPP import ConnectionAPP


class DataAccessDB(ConnectionAPP):

    def get_data(self):
        print('Trayendo datos de la base de datos...')
