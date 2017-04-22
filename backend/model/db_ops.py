import psycopg2
import psycopg2.extras
import pprint
import logging
import time

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
        insert_user_status = False
        print(user)
        # open a connection
        c = self.connect_db()

        # Check if the user exists
        self.does_user_exists(c, user['email'])

        # get max user id
        user_id = self.get_max_user_id(c) + 1
        email = user['email']
        name = user['name']
        password = user['password']
        # TAMBY: YOU ARE HERE. need to refactor this insert
        date_user_created = time.strftime("%Y-%m-%d") # yyyy-mm-dd
        date_user_updated = date_user_created
        date_last_login = date_user_created
        insert_statement = 'INSERT INTO USERS (USER_ID, EMAIL, NAME, PASSWORD, DATE_CREATED, DATE_UPDATED, LAST_LOGIN) ' \
                   'VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(user_id,
                                                             '\'' + email + '\'',
                                                             '\'' + name + '\'',
                                                             '\'' + password + '\'',
                                                             '\'' + date_user_created + '\'',
                                                             '\'' + date_user_updated + '\'',
                                                             '\'' + date_last_login + '\'')
        print(insert_statement)
        # get a cursor
        cursor = c.cursor()
        try:
            # rcreate user record
            cursor.execute(insert_statement)
            insert_user_status = True
        except psycopg2.ProgrammingError as e:
            insert_user_status = False
            self.logger.error("INSERT FAILED. STATEMENT: " + insert_statement + '\nError: ' + str(e))
        finally:
            # commit db changes
            c.commit()
            # close cursor
            cursor.close()
            # close the connection
            self.close_db_connect()

        return insert_user_status

    def get_max_user_id(self, connection):

        max_row = None
        try:
            # cursor = connection.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
            cursor = connection.cursor()

            # execute our Query
            cursor.execute('SELECT MAX(USER_ID) FROM USERS')
            for record in cursor:
                max_row = record[0]

            if max_row == None:
                max_row = 0


        except psycopg2.ProgrammingError as e:
            self.logger.error(str(e))
        finally:
            cursor.close()

        return max_row

    def does_user_exists(self, connection, email):
        exists = False
        try:
            # cursor = connection.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
            cursor = connection.cursor()
            # execute our Query
            cursor.execute('SELECT COUNT(*) FROM USERS WHERE EMAIL = {0}'.format('\'' + email + '\''))
            user_count = 0
            for record in cursor:
                user_count += 1
            if user_count != 0:
                exists = True
        except psycopg2.ProgrammingError as e:
            self.logger.error(str(e))
        finally:
            cursor.close()

        return exists

    def get_languages(self):
        try:
            connection = self.connect_db()
            cursor = connection.cursor()
            # get the event id of last event for this user
            cursor.execute('SELECT language from language order by 1')

            language_list = []
            for record in cursor:
                language_list.append(record[0])

        except psycopg2.ProgrammingError as e:
            self.logger.error(str(e))
        finally:
            cursor.close()

        return language_list

    def user_last_event(self, connection, user_email):
        # return none if no records. else return event id
        last_event_obj = None
        try:
            cursor = connection.cursor()
            # get the event id of last event for this user
            cursor.execute('SELECT EVENT_ID, MAX(EVENT_TIMESTAMP) '
                   'FROM EVENTS '
                   'JOIN USERS ON EVENTS.USER_ID = USERS.USER_ID '
                   'AND USERS.EMAIL = {0}  GROUP BY 1'.format('\'' + user_email + '\''))

            count = 0
            for record in cursor:
                last_event_obj = record[0]
                count += 1

        except psycopg2.ProgrammingError as e:
            self.logger.error(str(e))
        finally:
            cursor.close()

        return last_event_obj

    def login_user(self, user):
        login_status = None
        next_screen = None
        print('Email: ', user['email'])
        print('Pasword: ', user['password'])

        c = self.connect_db()
        user_exists = self.does_user_exists(c, user['password'])
        if user_exists:
            # last_event is a dict with last event in the events table.
            # if no events then rediect to the 'select language screen'
            last_event = self.user_last_event(c, user['email'])
            if last_event == None:
                # go to language_selection()
                print("NO LAST EVENT. GO TO language_selection")
                login_status = True
                next_screen = 'GO_TO_LANGUAGE_SELECTION'
            else:
                # go to next question
                print("FOUND LAST EVENT. GOING TO NEXT QUESTIONs")
                login_status = True
                next_screen = 'GO_TO_NEXT_QUESTION'
        else:
            login_status = False

        return login_status, next_screen
