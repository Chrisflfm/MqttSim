class dm_Channel:

    def getAllChannels():
        from dm_Connection import dm_Connection
        from channel import channel
        connection = dm_Connection.getConnection()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_select_Query = ("SELECT * FROM Munerica.tblChannel "
                                "INNER JOIN Munerica.tblRemoteIo "
                                "ON tblChannel.remoteId"
                                " = tblRemoteIo.id;")
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            result1 = list()
            result = dict()
            for row in records:
                itm = channel(row[0], row[1], row[2], row[3], row[4], row[5],
                              row[6], row[7], row[8], row[9], row[10],
                              row[12], row[13], row[14])
                result1.append(itm)

            for itm in result1:
                result[itm.id] = itm
            return result

    def getChannelonId(id):
        from dm_Connection import dm_Connection
        from channel import channel
        connection = dm_Connection.getConnection()
        if connection.is_connected():
            cursor = connection.cursor()
            sql_select_Query = ("SELECT * FROM Munerica.tblChannel "
                                "INNER JOIN Munerica.tblRemoteIo "
                                "ON tblChannel.remoteId"
                                " = tblRemoteIo.id "
                                "WHERE tblChannel.id = " + str(id))
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            row = records[0]
            itm = channel(row[0], row[1], row[2], row[3], row[4], row[5],
                          row[6], row[7], row[8], row[9], row[10],
                          row[11], row[12], row[13])
            return itm

    def UpdateChannel(channel):
        from dm_Connection import dm_Connection
        # from Objects.channel import channel
        try:
            return True
        except Exception:
            from Utils import Utils
            Utils.errorHandler()