from Utils import Utils
import os


class remoteIO:

    def __init__(self, id, name, location, ipAdress):
        self.id = id
        self.name = name
        self.location = location
        self.ipAdress = ipAdress

    def __str__(self):
        return self.name + '@' + self.location

    def connect(self):
        try:
            return True
        except Exception:
            Utils.errorHandler()
            return False

    def connected(self):
        try:
            return True
        except Exception:
            Utils.errorHandler()
            return False

    def testConnection(self):
        hostname = self.ipAdress
        response = os.system("ping -c 1 " + hostname)

        # and then check the response...
        if response == 0:
            return True
        else:
            return False
