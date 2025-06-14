def get_connection():
    import mysql.connector
    return mysql.connector.connect(
        host="localhost",  # NOT "3306"
        user="root",
        password="Santhu1@",
        database="signup_db"
    )
