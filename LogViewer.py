import sqlite3
import json
from tkinter import *
from LogClient import LogClient

class LogViewer:

    def __init__(self):

        self.log_client = LogClient()
        self.window = Tk()
        self.main_frame = Frame(self.window)
        self.view_frame = Frame(self.window)

        self.main_frame.grid(row=0, column=0)
        self.view_frame.grid(row=0, column=0)

        l1=Label(self.main_frame, text="Dziennik zdarzeń")
        l1.grid(row=0, column=0, columnspan=2)
        l1=Label(self.main_frame, text="Host:")
        l1.grid(row=1, column=0)
        l1=Label(self.main_frame, text="Port:")
        l1.grid(row=2, column=0)

        b1=Button(self.main_frame,text="Połącz", command=self.viewLogs())
        b1.grid(row=3,column=0, columnspan=2)

        host=StringVar()
        port=StringVar()
        e1=Entry(self.main_frame ,textvariable=host)
        e2=Entry(self.main_frame ,textvariable=port)
        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)

        self.main_frame.tkraise()
        self.window.mainloop()

    def viewLogs(self):
            self.log_client.connect()
            self.view_frame.tkraise()
            l2 = Label(main_frame, text="Dziennik zdarzeń")
            l2.grid(row=0, column=0, columnspan=2)
            b2 = Button(window, text="Dodaj log", command=self.log_client.sendLog())
            b2.grid(row=1, column=0, columnspan=2)
            content=StringVar()
            e1 = Entry(self.view_frame, textvariable=content)
            e1.grid(row=1, column=1)
            conn = sqlite3.connect("Log.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM log")
            records = cur.fetchall()
            for record in records:
                rec = json.loads(record)
            print(rec["TIME"])

log_viewer = LogViewer()
