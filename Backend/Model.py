import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


# add user
def DB_add(name, password):
    try:
        mySQL_conn = mysql.connector.connect(host='localhost',
                                             database='chatroom',
                                             user='root',
                                             password='')
        cursor = mySQL_conn.cursor()
        cursor.callproc('AddUser', [name, password])
        # print out User details
        mySQL_conn.commit()
        # for r in cursor.stored_results():
        #    print(r.fetchall())
        #    result.append(r.fetchall())
        result = True
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
        result = False
    finally:
        # closing database connection.
        if (mySQL_conn.is_connected()):
            cursor.close()
            mySQL_conn.close()
            print("connection is closed")
    return result


# login
def DB_check(name, password):
    result = []
    try:
        mySQL_conn = mysql.connector.connect(host='localhost',
                                             database='chatroom',
                                             user='root',
                                             password='')
        cursor = mySQL_conn.cursor()
        result = cursor.callproc('SelectUser', [name, password])
        res = True
        # print(result)
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
        res = False
    finally:
        # closing database connection.
        if (mySQL_conn.is_connected()):
            cursor.close()
            mySQL_conn.close()
            print("connection is closed")
    return res, result[0]


# add chatroom
def DB_add_chatroom(chatname):
    try:
        mySQL_conn = mysql.connector.connect(host='localhost',
                                             database='chatroom',
                                             user='root',
                                             password='')
        cursor = mySQL_conn.cursor()
        cursor.callproc('CreateChatRoom', [chatname])
        # print out User details
        mySQL_conn.commit()
        # for r in cursor.stored_results():
        #    print(r.fetchall())
        #    result.append(r.fetchall())
        result = True
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
        result = False
    finally:
        # closing database connection.
        if (mySQL_conn.is_connected()):
            cursor.close()
            mySQL_conn.close()
            print("connection is closed")
    return result


#add admin to chatroom
def DB_AddAdmin(userName, chat):
    res, roomID = DB_choose_chatroom(chat)
    try:
        mySQL_conn = mysql.connector.connect(host='localhost',
                                             database='chatroom',
                                             user='root',
                                             password='')
        cursor = mySQL_conn.cursor()
        cursor.callproc('AddMember', [userName, roomID])
        # print out User details
        mySQL_conn.commit()
        # for r in cursor.stored_results():
        #    print(r.fetchall())
        #    result.append(r.fetchall())
        result = True
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
        result = False
    finally:
        # closing database connection.
        if (mySQL_conn.is_connected()):
            cursor.close()
            mySQL_conn.close()
            print("connection is closed")
    return result


# view all chatrooms
def DB_view_chatrooms():
    result = []
    try:
        mySQL_conn = mysql.connector.connect(host='localhost',
                                             database='chatroom',
                                             user='root',
                                             password='')
        cursor = mySQL_conn.cursor()
        """
        result = cursor.callproc('ViewChatRooms')
        print("HERE")
        print(result)
        """
        sql = "SELECT name FROM chatroom"
        cursor.execute(sql)
        result = cursor.fetchall()
        res = True
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
        res = False
    finally:
        # closing database connection.
        if (mySQL_conn.is_connected()):
            cursor.close()
            mySQL_conn.close()
            print("connection is closed")
    return res, result


# choose chatroom
def DB_choose_chatroom(name):
    result = []
    try:
        mySQL_conn = mysql.connector.connect(host='localhost',
                                             database='chatroom',
                                             user='root',
                                             password='')
        cursor = mySQL_conn.cursor()
        # result = cursor.callproc('GetChatRoomPort', [name])
        sql = "SELECT Port FROM chatroom WHERE Name = %s"
        data = (name,)
        cursor.execute(sql, data)
        result = cursor.fetchone()
        res = True
        #print(result)
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
        res = False
    finally:
        # closing database connection.
        if (mySQL_conn.is_connected()):
            cursor.close()
            mySQL_conn.close()
            print("connection is closed")
    #print(result)
    return res, result[0]


#only the admin of chatroom can delete it
def DB_delete_chatroom(name, username):
    res, roomID = DB_choose_chatroom(name)
    res, admin = DB_view_admin(roomID)
    if(admin == username):
        result = []
        print("HERE!")
        try:
            mySQL_conn = mysql.connector.connect(host='localhost',
                                                database='chatroom',
                                                user='root',
                                                password='')
            cursor = mySQL_conn.cursor()
            # result = cursor.callproc('GetChatRoomPort', [name])
            sql = "DELETE FROM userchatroom WHERE RoomID = %s"
            data = (roomID,)
            cursor.execute(sql, data)
            mySQL_conn.commit()
            sql = "DELETE FROM chatroom WHERE Port = %s"
            data = (roomID,)
            cursor.execute(sql, data)
            mySQL_conn.commit()
            # result = cursor.fetchone()
            res = True
            # print(result)
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
            res = False
        finally:
            # closing database connection.
            if (mySQL_conn.is_connected()):
                cursor.close()
                mySQL_conn.close()
                print("connection is closed")
        # print(result)
        return res
    return False


def DB_view_admin(_id):
    result = []
    try:
        mySQL_conn = mysql.connector.connect(host='localhost',
                                             database='chatroom',
                                             user='root',
                                             password='')
        cursor = mySQL_conn.cursor()
        # result = cursor.callproc('GetChatRoomPort', [name])
        sql = "SELECT * FROM userchatroom WHERE RoomID = %s"
        data = (_id,)
        cursor.execute(sql, data)
        result = cursor.fetchone()
        res = True
        #print(result)
    except mysql.connector.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
        res = False
    finally:
        # closing database connection.
        if (mySQL_conn.is_connected()):
            cursor.close()
            mySQL_conn.close()
            print("connection is closed")
    #print(result)
    return res, result[0]
