import pymysql
import pymysql.cursors

connection = pymysql.connect(host='LARRY',
                             user='sqlusr',
                             password='Raspberry',
                             db='PieFace',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



class database_handler:

        
    def __init__(self):
        # default constructor
        print("New database instance created")



    def get_all_media_sets(self):

        result = ""
        try:
            cursor = connection.cursor()
            cursor.callproc("get_all_media_sets")
            result = cursor.fetchall()


        finally:
            connection.close()
            

        return result

    def get_active_media_sets(self):
        
        result = ""
        try:
            cursor = connection.cursor()
            cursor.callproc("get_active_media_sets")
            result = cursor.fetchall()

        finally:
            connection.close()

        return result
        


# Connect to the database


# cursor = connection.cursor()
