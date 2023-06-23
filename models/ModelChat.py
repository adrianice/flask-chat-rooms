class ModelChat():
    
    @classmethod
    def insertChat(self, mysql, chat):
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO chats(host_id, password, name, description) VALUES(%s, %s, %s, %s)', (chat.host_id, chat.password.strip(), chat.name.strip(), chat.description.strip()))
        mysql.connection.commit()

    @classmethod
    def getAllChats(self, mysql):
        cur = mysql.connection.cursor()
        cur.execute('SELECT c.id, u.username, c.password, c.name, c.description FROM chats as c LEFT JOIN users as u ON c.host_id = u.id ORDER BY c.name ASC')
        return cur.fetchall()
    
    @classmethod
    def getMyChats(self, mysql, host_id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM chats WHERE host_id = %s ORDER BY name ASC', (host_id,))
        return cur.fetchall()
    
    @classmethod
    def getMyChatsId(self, mysql, host_id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT id FROM chats WHERE host_id = %s', (host_id,))
        return cur.fetchall()
    
    @classmethod
    def getChat(self, mysql, id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM chats WHERE id = %s', (id,))
        return cur.fetchone()
    
    @classmethod
    def updateChat(self, mysql, id, name, description):
        cur = mysql.connection.cursor()
        cur.execute('UPDATE chats SET name=%s, description=%s WHERE id = %s', (name, description, id))
        mysql.connection.commit()
        
    @classmethod
    def updateChatPassword(self, mysql, id, password):
        cur = mysql.connection.cursor()
        cur.execute('UPDATE chats SET password=%s WHERE id = %s', (password.strip(), id))
        mysql.connection.commit()

    @classmethod
    def deleteChat(self, mysql, id):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM chats WHERE id = %s', (id,))
        mysql.connection.commit()
        