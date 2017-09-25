import pymysql
import pymysql.cursors

# connection = pymysql.connect(host='10.13.37.95', user='kyle', password='Password1@', db='PieFace', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = ""

class database_handler:
    def __init__(self):
        # default constructor
        print("New database instance created")

    def connect_to_database(self):
        cursor = connection.cursor()

    def select_all(self):
        sql = "SELECT * FROM PieFace.PieFace;"
        cursor.execute(sql)
        result = cursor.fetchone()
        return result


# Connect to the database


#cursor = connection.cursor()
