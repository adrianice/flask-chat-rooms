from werkzeug.security import check_password_hash, generate_password_hash
from models.entities.User import User

class ModelUser():

    @classmethod
    def login(self, mysql, user):
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT id, username, password FROM users WHERE username=%s', (user.username,))
            row = cur.fetchone()
            if row != None:
                user = User(row[0], row[1], check_password_hash(row[2], user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, mysql, id):
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT id, username FROM users WHERE id=%s', (id,))
            row = cur.fetchone()
            if row != None:
                logged_user = User(row[0], row[1], None)
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def insertUser(self, mysql, user):
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT id, username, password FROM users WHERE username=%s', (user.username,))
            row = cur.fetchone()
            if row == None:
                cur.execute('INSERT INTO users(username, password) VALUES(%s, %s)', (user.username, generate_password_hash(user.password)))
                mysql.connection.commit()
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)