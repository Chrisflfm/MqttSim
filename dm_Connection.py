import mysql
import mysql.connector
from mysql.connector import Error
from Utils import Utils


class dm_Connection:

    def getConnection():
        try:
            connection = mysql.connector.connect(host='UbuntuPrime',
                                                 database='Munerica',
                                                 user='mqtt',
                                                 password='')

            if connection.is_connected():
                return connection
            else:
                print("No connection!")
                Utils.errorHandler()

        except Error as e:
            print("Error while connecting to MySQL", e)

    def closeConnection(self, connection):
        try:
            if (connection.is_connected()):
                cursor = connection.cursor()
                cursor.close()
                connection.close()
                # print("MySQL connection is closed")
        except Exception as e:
            Utils.errorHandler(e)