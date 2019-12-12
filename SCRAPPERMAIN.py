import csv
import collections
import requests
import tkinter as tk
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox


# Main scrapper frame class initialization
class Scrapper(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# Main Initialization
myapp = tk.Tk()
myapp.title("Scrapper")

# Field for text input
e = Entry(myapp)
e.pack()
e.focus_set()

# Scrollbar widget
scrollbar = Scrollbar(myapp)
scrollbar.pack(side=RIGHT, fill=Y)


# Text scrap definition
def urlscrap():
 v = e.get()

 if v == "":
    tk.messagebox.showinfo("ERROR", "URL BOX EMPTY")
 else:
     response = requests.get(v)
     soup2 = BeautifulSoup(response.text, "html.parser")
     print(soup2)

     T = tk.Text(myapp, wrap=NONE, yscrollcommand = scrollbar.set)
     T.pack()
     T.insert(tk.END, soup2.find_all(text=True))
     scrollbar.config(command = T.yview)
     f.config(state=DISABLED)


# Function for scraping href links
def opening():
 v = e.get()

 if v == "":
   tk.messagebox.showinfo("ERROR", "URL BOX EMPTY")
 else :
      links = requests.get(v)
      soup2 = BeautifulSoup(links.content, "html.parser")
      ff = soup2.findAll(href=True)
      soup_string = str(ff)

      with open('links.txt', 'w', encoding='utf-8') as y_out:
        y_out.write(soup_string)


      tk.messagebox.showinfo("Succes", "Scrapped all lInks from the site")



def opening2():
 v = e.get()

 if v == "":
   tk.messagebox.showinfo("ERROR", "URL BOX EMPTY")
 else :
      text = requests.get(v)
      soup2 = BeautifulSoup(text.content, "html.parser")
      ff = soup2.findAll(text=True)
      soup_string = str(ff)

      with open('text.txt', 'w', encoding='utf-8') as y_out:
        y_out.write(soup_string)


      tk.messagebox.showinfo("Succes", "Scrapped whole text from  the site")

def graphdraw():
 letters = set("AEIOUaeioubcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
 vowels = set("AEIOUaeiou")
 cons = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
 fileName = 'text.txt'
 fileNameStrip = fileName.strip()
 infile = open(fileNameStrip, encoding="utf8")
 c = collections.Counter(infile.read())

 countL = sum(c[k] for k in c if k in letters)
 countV = sum(c[k] for k in c if k in vowels)
 countC = sum(c[k] for k in c if k in cons)

 with open('numbers.txt', 'w', encoding='utf-8') as y_out:
     y_out.write("LETTERS:"+str(countL)+'\n'+"Vowels"+str(countV)+'\n'+"Cons"+str(countC))

 with open('numbers.txt', 'r') as in_file:
     stripped = (line.strip() for line in in_file)
     lines = (line.split(",") for line in stripped if line)
     with open('log.csv', 'w') as out_file:
         writer = csv.writer(out_file)
         writer.writerow(('WYNIKI'))
         writer.writerows(lines)

 tk.messagebox.showinfo("SUCCES")


#Scrapper button 0.9
f = Button(myapp, text="Scrap and show text from site", command=urlscrap)
f.pack()

#Scrapper button 1
b = Button(myapp, text="Scrap Href Links from site an save as TXT", command=opening)
b.pack()


#BUTTON:Scrap text and save as TXT
c = Button(myapp, text="Scrap text from site an save as TXT", command=opening2)
c.pack()

#BUTTON:Count Vovels and Cons
h = Button(myapp, text="Count Vovels and Cons from TXT and save as CSV", command=graphdraw)
h.pack()


#start the program
myapp.mainloop()







