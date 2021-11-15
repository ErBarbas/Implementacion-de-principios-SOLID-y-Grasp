from Interface.ConnectionAPP import ConnectionAPP


class DataAccessAPI(ConnectionAPP):

    def get_data(self):
        print('Trayendo datos de un servicio en el API...')
