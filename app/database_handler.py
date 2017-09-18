import pymysql
import pymysql.cursors






# Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Password1',
                                 db='PieFace',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    sql = "SELECT * FROM PieFace.new_table;"
    cursor.execute(sql)

    result = cursor.fetchone()

    selectedSet = result["test"]