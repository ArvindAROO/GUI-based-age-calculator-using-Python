# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:01:25 2019

@author: ARVIND KRISHNA
"""

"""A small project by ArvindKrishna. Find your age here"""
from datetime import date


def calculate_age(born):
    today = date.today()
    if (today.month, today.day) == (born.month, born.day):
        AgeYr=today.year - born.year
        AgeMo=0
        AgeDay=0
        print("Wow! It seems today is your birthday\nHappy Birthday")
    else:
        AgeYr=today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        if today.month<=born.month:
            AgeMo=12+today.month-born.month
        else:
            AgeMo=today.month-born.month
        if today.day<born.day:
            if born.month in [1,3,5,7,8,10,12]:
                AgeDay=31+today.day-born.day
            elif born.month==2:
                AgeDay=28+today.day-born.day
            else:
                AgeDay=30+today.day-born.day
        elif today.day==born.day:
            AgeDay=0
        else:
            AgeDay=today.day-born.day
    return Ageyr,AgeMo,AgeDay

import datetime
import tkinter as tk
from PIL import Image,ImageTk

window=tk.Tk()
window.geometry("600x600")
window.title("Age Calculator App \nBy ArvindKrishna\n Find your age here")
	
name = tk.Label(text = "Name")
name.grid(column=0,row=1)
year = tk.Label(text = "Year")
year.grid(column=0,row=2)
month = tk.Label(text = "Month")
month.grid(column=0,row=3)
date1 = tk.Label(text = "Day")
date1.grid(column=0,row=4)
	
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)
	
def getInput():
    name=nameEntry.get()
    givenyr,givenmo,givenday=yearEntry.get(),monthEntry.get(),dateEntry.get()
    B=(datetime.date(int(givenyr),int(givenmo),int(givenday)))
    textArea = tk.Text(master=window,height=10,width=25,wrap='word')
    textArea.grid(column=1,row=6)
    Ageyear,AgeMonth,AgeDay=calculate_age(B)
    print('hey',name,'you are',AgeYear,'years',AgeMonth,'months',AgeDay,'days old')
    textArea.insert(tk.END," Heyy "+str(name)+" !!! You are "+str(AgeYear)+" years "+str(AgeMonth)+" months "+str(AgeDay)+" days old!!! ")
    
button=tk.Button(window,text="Calculate Age",command=getInput,bg="cyan")
button.grid(column=1,row=5)


#image=Image.open('AkCalc.jpg')
#image.thumbnail((300,300),Image.ANTIALIAS)
#photo=ImageTk.PhotoImage(image)
#label_image=tk.Label(image=photo)
#label_image.grid(column=1,row=0)

window.mainloop()
