import json

class ModelMessage():
    
    @classmethod
    def insertMessage(self, mysql, message):
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO messages(chat_id, user_id, message) VALUES (%s, %s, %s)', (message.chat_id, message.user_id, message.message))
        mysql.connection.commit()

    @classmethod
    def getAllMessages(self, mysql, chat_id):
        cur = mysql.connection.cursor()
        cur.execute("CALL `getallmessages`(%s)", (chat_id,))
        return json.dumps(cur.fetchall(), ensure_ascii=False)