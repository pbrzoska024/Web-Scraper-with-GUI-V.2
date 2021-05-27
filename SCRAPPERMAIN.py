import pandas as pd
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
from matplotlib.pyplot import pie, axis, show




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


# Main scrap function and putting it all togheter in widnows
def urlscraptowindow():
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


# Main function for scraping links from sites
def scraplinksandsave():
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


#Scrap text and save
def scraptextandsave():
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

def splitandcount():
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

#Analyze
def analyze():
     df = pd.read_csv ('log.csv')

     vowels_data = df["Vowels"]
     cons_data = df["Cons"]
     colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
     explode = (0.1, 0, 0, 0, 0)
     plt.pie(Vowels_data, Cons_data, explode=explode, colors=colors,
     autopct='%1.1f%%', shadow=True, startangle=140)
     plt.title("Vowels and cons pie chart")
     plt.show()



#Scrapper button 0.9
f = Button(myapp, text="Scrap and show text from site", command=urlscraptowindow)
f.pack()

#Scrapper button 1
b = Button(myapp, text="Scrap Href Links from site an save as TXT", command=scraplinksandsave)
b.pack()


#BUTTON:Scrap text and save as TXT
c = Button(myapp, text="Scrap text from site an save as TXT", command=scraptextandsave)
c.pack()

#BUTTON:Count Vovels and Cons
h = Button(myapp, text="Count Vovels and Cons from TXT and save as CSV", command=splitandcount)
h.pack()

#BUTTON:Analyze vovels and visualize
j = Button(myapp, text="Analyze Vovels and Cons", command=analyze)
j.pack()

#start the program
myapp.mainloop()
