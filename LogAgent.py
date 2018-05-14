import socket
import sqlite3
import json
import datetime
"""
class LogRecord:
    def __init__(self, id):
        self.id = id

    def getTime(self):
        return json.dumps(self.time['time'])

    def getContent(self):
        return json.dumps(self.content['text'])
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 9898))
sock.listen(1)
c, addr = sock.accept()
data = c.recv(1024) # max size of data: 1024 bytes
if data:
        conn = sqlite3.connect("Log.db")
        cur = conn.cursor()
        data_json = json.dumps({"TIME":str(datetime.datetime.now()),"IP":addr, "CONTENT":data})
        cur.execute("CREATE TABLE IF NOT EXISTS log (log_record VARCHAR)")
        cur.execute("INSERT INTO log VALUES(?)", (data_json,))
        conn.commit()
        conn.close()



