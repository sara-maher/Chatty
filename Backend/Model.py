import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


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
        #for r in cursor.stored_results():
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
