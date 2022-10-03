# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 20:38:23 2022

@author: tn781
"""


import tkinter as tk
from tkinter import filedialog
from tkinter import ttk 

class Application():
    def __init__(self):
        self.filepath = None
        self.PeopleNumber = None
        self.first = None
        self.second = None
        self.Anslist = []
        self.createWidgets()
        
    def createWidgets(self):
        window = tk.Tk()
        window.geometry("500x500")
        window.title('導師挑選器')
        self.button_import = tk.Button(window, text="匯入檔案", command = self.openfile).pack()
        self.entry_filename = tk.Entry(window, width=30, font=("宋體", 10, 'bold'))
        self.entry_filename.pack(pady=10)
        self.People = ttk.Combobox(window,
                             values=["1","2","3","4","5","6","7","8","9","10"])
        self.First = ttk.Combobox(window,
                             values=[
                                    "當過的年份", 
                                    "有沒有意願",])
        self.Second = ttk.Combobox(window,
                              values=[
                                    "當過的年份", 
                                    "有沒有意願",])                    
        self.People.pack(pady=10)
        self.People.insert(0, '要挑選幾位導師')
        self.First.pack(pady=10)
        self.First.insert(0,'第一順位')
        self.Second.pack(pady=10)
        self.Second.insert(0,'第二順位')
        tk.Button(window, text="匯入資訊", command=self.getValue).pack(pady=20)
        tk.Button(window, text="確認", command=window.destroy).pack() 
        window.mainloop()
    
    def openfile(self):
        filename = filedialog.askopenfilename(title='開啟csv檔案', filetypes=[('csv', '*.csv')])
        self.filepath = filename
        self.entry_filename.insert('insert', filename)  
    
    def getFilePath(self):
        return self.filepath
    
    def getPeopleValue(self):
        return self.PeopleNumber
    
    def getPriorityCondition(self):
        return self.first, self.second    
    
    def getValue(self):
        self.first = self.First.get()
        self.second = self.Second.get()
        self.PeopleNumber = self.People.get()
        
