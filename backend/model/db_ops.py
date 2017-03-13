import psycopg2
import psycopg2.extras
import pprint

class RoseQuartzException(Exception):
    pass

class Data_Ops():

    def __init__(self):
        self.conn = None

    def connect_db(self):

        conn_string = "host='localhost' dbname='rose_quartz' user='admin' password='Pineapple01'"
        print("Connecting to database {0}".format(conn_string))

    	# get a connection, if a connect cannot be made an exception will be raised here
        try:
            self.conn = psycopg2.connect(conn_string)
        except Exception as e:
            raise RoseQuartzException("DB_CONNECT_FAILED")

        return self.conn

    def close_db_connect(self):
        self.conn.close();

    def query(self):

    	# get a connection
        c = self.connect_db()

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        # server-side cursor, which prevents all of the records from being downloaded at once from the server.
        cursor = c.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)

        # execute our Query
        cursor.execute("SELECT * FROM users")

        row_count = 0
        for row in cursor:
        	row_count += 1
        	print("row: {0} {1}".format(row_count, row))

        self.close_db_connect()


    def insert_user(self, user):
        print(user)
