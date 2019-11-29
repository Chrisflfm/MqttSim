from remoteIO import remoteIO
from datetime import datetime
from Utils import Utils
import dm_Channel


class channel(remoteIO):
    def __init__(self, id, channelName, Description, IoType, ioLengte, target,
                 actual, targetTime, actualTime, remoteId, adress, remoteName,
                 location, ipAdress):
        super().__init__(remoteId, remoteName, location, ipAdress)
        self.id = id
        self.channelName = channelName
        self.Description = Description
        self.IoType = IoType
        self.ioLengte = ioLengte
        self.target = target
        self.actual = actual
        self.targetTime = targetTime
        self.actualTime = actualTime
        self.remoteId = remoteId
        self.adress = adress

    def __str__(self):
        return self.channelName

    def Id(self):
        return "Hello my name is " + self.name

    def WriteReg(self):
        try:
            return True
        except Exception:
            Utils.errorHandler()
            return False

    def WriteBit(self):
        try:
            return True
        except Exception:
            Utils.errorHandler()
            return False

    def ReadReg(self):
        return self.actual

    def ReadBit(self):
        return self.actual
