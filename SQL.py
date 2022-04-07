from psycopg2 import connect
from psycopg2.extras import DictCursor
from nextcord import Member

from config import DATABASE_URL, STANDART_LANGUAGE_USER

class SQL:
    def __init__(self): 
        self.conn = connect(DATABASE_URL, keepalives=1, keepalives_idle=30, keepalives_interval=10, keepalives_count=5) 
        self.conn.autocommit = True

    def create_table(self):  
        cursor=self.conn.cursor()  
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        channel TEXT,
        user_id BIGSERIAL,
        user_tag TEXT PRIMARY KEY,
        user_name TEXT,
        avatar TEXT,
        time TIMESTAMP,
        number BIGSERIAL,
        welcome_message BIGSERIAL,
        language TEXT,
        Author TEXT
        )''')
        cursor.close()

    def insert(self, message_author, user_id, user_tag, user_name, avatar, user_num, datatime, welcome_message): 
        cursor=self.conn.cursor()
        cursor.execute('''INSERT INTO users VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (message_author, user_id, user_tag, user_name, avatar, datatime, user_num, welcome_message, STANDART_LANGUAGE_USER ,'IPOleksenko'))
        cursor.close()

    def Del_user(self, user_id):
        cursor=self.conn.cursor()
        try:
            cursor.execute('''DELETE FROM users WHERE user_id = %s''',(user_id,))
        finally:
            cursor.close()

    def select(self, select, user_id):
        cursor=self.conn.cursor(cursor_factory=DictCursor)
        cursor.execute('''SELECT * FROM users WHERE user_id = %s''', (user_id,))
        result = cursor.fetchone()
        cursor.close()
        return result[select]

    def get_member(self, member):
        cursor=self.conn.cursor() 
        cursor.execute('''SELECT * FROM users WHERE user_id = %s''', (member.id,))
        result = cursor.fetchone()
        return result
        
    def update_lang(self, language, user_id):
        cursor=self.conn.cursor() 
        cursor.execute('''UPDATE users SET language = %s WHERE user_id = %s''', (language, user_id,))
        cursor.close() 

Database_SQL = SQL()
#Author: IPOleksenko