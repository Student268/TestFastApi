import mysql.connector


class Database:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="test_360db"
        )

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    # def select_query(self, query):
    #     cursor = self.conn.cursor()
    #     cursor.execute(query)
    #     return cursor.fetchall()

    def select_query(self, query: str) -> list:
        cursor = self.conn.cursor()
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        results = []
        for row in cursor.fetchall():
            result = {}
            for item in range(len(columns)):
                result[columns[item]] = row[item]
            results.append(result)
        return results
