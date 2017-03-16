import psycopg2
import psycopg2.extras
import pprint
import logging

class RoseQuartzException(Exception):
    pass

class Data_Ops():

    def __init__(self):
        self.conn = None

        # setup logging
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        fh = logging.FileHandler('logs/sign_up.log')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.setLevel(logging.INFO)

    def connect_db(self):

        conn_string = "host='localhost' dbname='rose_quartz' user='admin' password='Pineapple01'"
        print("Connecting to database {0}".format(conn_string))

    	# get a connection, if a connect cannot be made an exception will be raised here
        try:
            self.conn = psycopg2.connect(conn_string)
        except Exception as e:
            self.logger.error("DB_CONNECT_FAILED")
            raise RoseQuartzException("DB_CONNECT_FAILED")

        return self.conn

    def close_db_connect(self):
        self.conn.close();

    def query(self):

    	# get a connection
        c = self.connect_db()

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        # server-side cursor, which prevents all of the records from being downloaded at once from the server.
        # cursor = c.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
        cursor = c.cursor()

        # execute our Query
        cursor.execute("SELECT * FROM users")

        row_count = 0
        for row in cursor:
        	row_count += 1
        	print("row: {0} {1}".format(row_count, row))

        self.close_db_connect()


    def insert_user(self, user):
        print(user)
        # open a connection
        c = self.connect_db()
        print("MAX USER ID: {0}".format(self.get_max_user_id(c)))
        # get max user id
        user_id = self.get_max_user_id(c) + 1
        email = user['email']
        name = user['name']
        password = user['password']
        level = 0
        insert_statement = 'INSERT INTO USERS (ID, EMAIL, NAME, PASSWORD, LEVEL) ' \
                   'VALUES ({0}, {1}, {2}, {3}, {4})'.format(user_id,
                                                             '\'' + email + '\'',
                                                             '\'' + name + '\'',
                                                             '\'' + password + '\'',
                                                             level)
        print(insert_statement)
        # get a cursor
        cursor = c.cursor()
        try:
            # run the insert statement
            cursor.execute(insert_statement)
        except psycopg2.ProgrammingError as e:
            self.logger.error("INSERT FAILED. STATEMENT: " + insert_statement + '\nError: ' + str(e))
        finally:
            # commit db changes
            c.commit()
            # close cursor
            cursor.close()
            # close the connection
            self.close_db_connect()

    def get_max_user_id(self, connection):
        # cursor = connection.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
        cursor = connection.cursor()

        # execute our Query
        cursor.execute('SELECT MAX(ID) FROM users')

        # returns row count, -1 if empty
        row_count = cursor.rowcount
        max_row = None
        if row_count < 0:
            max_row = 0
        else:
            max_row = row_count

        return max_row

    def does_user_exists(self, connection):
