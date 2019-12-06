#from flask_mysqldb import MySQL
import MySQLdb as mariadb
from .db_credentials import host, user, password, db


def connect_to_database(host = host, user = user, password = password, db = db):
    print("In connect to database")
    db_connection = mariadb.connect(host, user, password, db)
    print("Connected to database")
    return db_connection

def execute_query(db_connection = None, query = None, query_params = ()):
    if db_connection is None:
        print("No database connection")
        return None

    if query is None or len(query.strip()) == 0:
        print("Query is empty")
        return None
        
    print("Executing %s with %s" % (query, query_params))

    cursor = db_connection.cursor()

    cursor.execute(query, query_params)

    db_connection.commit()
    return cursor

# class Database():
#     def __init__(self, app):
#         self.db = MySQL(app)

#     # run a single query with optional parameters
#     def runQuery(self, query, params=None):
#         cursor = self.db.connection.cursor()
#         cursor.execute(query, params)
#         result = cursor.fetchall()
#         cursor.close()
#         self.db.connection.commit()
#         return result

#     # run multiple insert operations; takes list of queries (no parameters)
#     def runMultipleQueries(self, queries):
#         cursor = self.db.connection.cursor()

#         for q in queries:
#             print(q)
#             cursor.execute(q)
#             result = cursor.fetchall()

#         cursor.close()
#         self.db.connection.commit()
#         return result