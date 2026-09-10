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
    pass

connection_instance = DbConnect()
connection_instance.get_connection()
