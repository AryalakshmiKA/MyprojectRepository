import mysql.connector

class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Arya@181094",
                database="companydb"
            )
            return self.connection
        except Exception as e:
            return None
class GymManagement(DbConnect):
    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from member where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()
            return records
        except Exception as e:
            return None

connection_instance = DbConnect()
connection_instance.get_connection()
