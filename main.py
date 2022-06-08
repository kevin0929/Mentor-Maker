# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 13:40:26 2022

@author: tn781
"""

import csv
import tkfile
import tkinter as tk
from tkinter import *


class Teacher:
    def __init__(self, name, year, will):
        self.name = name
        self.year = year
        self.will = will
    
    def __lt__(self, other):
        return self.year < other.year
        
class ToPickTeacher:
    def calYearBetterList(self, TeacherList):
        for i in TeacherList:
            tmplist = i.year.split(',') #分割字串(因為year不是一個list)
            tmplist = sorted(tmplist)   #sorted不是inplace的，所以要存起來
            if i.year != '已當過導師年度' and i.year != '':
                i.year = 111 - int(tmplist[len(tmplist) - 1])
        TeacherList.sort(reverse = True)
    
    def calWillBetterList(self, TeacherList):
        for i in range(len(TeacherList)):
            if TeacherList[i].will == 'T':
                continue
            else:
                for j in range(i+1, len(TeacherList)):
                    if TeacherList[j].will == 'T':
                        TeacherList[i],TeacherList[j] = TeacherList[j],TeacherList[i]
                        break
    
    def calBestTeacherListDependOnWill(self, TeacherList, peopleNumber):
        BestTeacherList = []
        Allflag = 0
      
        while peopleNumber > 0:
            if Allflag == 1:
                break
            for i in range(len(TeacherList)):
                if peopleNumber <= 0:
                    break
                
                if TeacherList[i].will == 'T':
                    BestTeacherList.append(TeacherList[i].name)
                    peopleNumber = peopleNumber - 1
                
                else:
                    Min = '999'
                    flag = -1
                    for j in range(i+1, len(TeacherList)):
                        if (TeacherList[j].year < Min) and (TeacherList[j].name not in BestTeacherList):
                            Min = TeacherList[j].year
                            flag = j
                    if flag != -1:
                        BestTeacherList.append(TeacherList[flag].name)
                        peopleNumber = peopleNumber - 1
                    else:
                        Allflag = 1 
                        break
        return BestTeacherList 
                        
    def calBestTeacherListDependOnYear(self, TeacherList, peopleNumber):    
        BestTeacherList = []
        Allflag = 0
        i = 0
        while i < len(TeacherList) - 1:
            if Allflag == 1:
                break
            
            tmplist = []
            tmplist.append(TeacherList[i])
            for j in range(i+1, len(TeacherList)):
                if TeacherList[j].year == TeacherList[i].year:
                    if TeacherList[j].will == 'T':
                        if peopleNumber <= 0:
                            Allflag = 1
                            break
                        BestTeacherList.append(TeacherList[j].name)
                        peopleNumber = peopleNumber - 1
                    else:
                        tmplist.append(TeacherList[j])
                else:
                    for k in range(len(tmplist)):
                        if peopleNumber <= 0:
                            Allflag = 1
                            break
                        BestTeacherList.append(tmplist[k].name)
                        peopleNumber = peopleNumber - 1
                    flag = j
                    break
            i = flag
                        
        return BestTeacherList
                   
        
class TeacherGroup:
    def __init__(self, ToPickTeacher):
        self.TeacherList = []
        self.YearBetter = []
        self.WillBetter = []
        self.BestTeacherList = []
        self.PeopleNUm = 0
    
    def addTeacherToList(self, teacher):
        self.TeacherList.append(teacher)
    
    def getYearBetterList(self):
        self.YearBetter = ToPickTeacher.calYearBetterList(self, self.TeacherList)
        
    def getWillBetterList(self):
        self.WillBetter = ToPickTeacher.calWillBetterList(self, self.TeacherList)
    
    def addPeopleNum(self, peopleNumber):
        self.PeopleNum = peopleNumber
    
    def getBestTeacherListDependOnWill(self):
        self.BestTeacherList = ToPickTeacher.calBestTeacherListDependOnWill(self,  self.TeacherList, self.PeopleNum)
        return self.BestTeacherList
    
    def getBestTeacherListDependOnYear(self):
        self.BestTeacherList = ToPickTeacher.calBestTeacherListDependOnYear(self,  self.TeacherList, self.PeopleNum)
        return self.BestTeacherList
        
        

def main():
    
    tkGUI = tkfile.Application()
    filepath = tkGUI.getFilePath()
    peopleNumber = int(tkGUI.getPeopleValue())
    first, second = tkGUI.getPriorityCondition()
      
    with open(filepath, newline='', encoding="utf-8") as csvfile:
        rows = csv.reader(csvfile)
        teacher = TeacherGroup(ToPickTeacher)
        for data in rows:
            name = data[0]
            year = data[1]
            will = data[2]
            teacher.addTeacherToList(Teacher(name, year, will))
    
    #print(peopleNumber)
    teacher.addPeopleNum(peopleNumber)
    
    if first == '有沒有意願':
        teacher.getWillBetterList()
        BestTeacherList = teacher.getBestTeacherListDependOnWill()
    
    else:
        teacher.getYearBetterList()
        BestTeacherList = teacher.getBestTeacherListDependOnYear()
    
    #tkGUI.getBestTeacherList(BestTeacherList)
    
    window1 = tk.Tk()
    window1.geometry("500x500")
    window1.title('導師挑選結果')
    lb = tk.Listbox(window1)
    lb.pack(pady=20)
    for item in BestTeacherList:
        lb.insert(tk.END, item)
    window1.mainloop()
        
            
        
if __name__ == '__main__':
    main()