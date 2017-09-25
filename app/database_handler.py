import pymysql
import pymysql.cursors

connection = pymysql.connect(host='10.13.37.103',
                             user='sqlusr',
                             password='Raspberry',
                             db='PieFace',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



class database_handler:
    def __init__(self):
        # default constructor
        print("New database instance created")



    def select_all(self):

        result = ""
        try:
            cursor = connection.cursor()
            sql = "SELECT * FROM PieFace.PieFace;"
            cursor.execute(sql)
            result = cursor.fetchall()


        finally:
            connection.close()

        return result[0]


# Connect to the database


# cursor = connection.cursor()
