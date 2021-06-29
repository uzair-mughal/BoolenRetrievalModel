from PreProcessing import filereader
import InvertedIndex
import PositionalIndex
from BooleanQuery import B_Query
from ProximityQuery import P_Query
import tkinter
import json
import os.path
from os import path

def main_window():

    def Qurey_Input():
        query = entry.get()
        if '/' in query:
            ProximityQuery(query)    
        else:
            BooleanQuery(query)

    def ProximityQuery(query):
        res = P_Query(query,PositionalIndex)
        textbar.delete("1.0",tkinter.END)
        if type(res)==list:
            res.sort()
        textbar.insert(tkinter.INSERT, str(res))

    def BooleanQuery(query):
        res = B_Query(query,InvertedIndex)
        textbar.delete("1.0",tkinter.END)
        if type(res)==list:
            res.sort()
        textbar.insert(tkinter.INSERT, str(res))

    window = tkinter.Tk()
    window.title('Information Retrieval (CS317) Assignment-1 18K-0179')
    window.config(bg='black')
    width = 920
    height = 340
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cod = (screen_width / 2) - (width / 2)
    y_cod = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x_cod, y_cod))

    label = tkinter.Label(window, text='Boolean Query Format:\t ||  X AND Y  ||  X OR Y  ||  NOT X  ||  (Upto 3 Terms)', bg='black', fg='white')
    label.place(x=75, y=50)

    label = tkinter.Label(window, text='Proximity Query Format:\t ||  X AND Y /K  || X Y /K  ||  (K defines max distance between X and Y, K must be positive)', bg='black', fg='white')
    label.place(x=75, y=80)

    label = tkinter.Label(window, text='Query:', bg='black', fg='white')
    label.place(x=75, y=140)

    label = tkinter.Label(window, text='Result-Set:', bg='black', fg='white')
    label.place(x=75, y=190)

    entry = tkinter.Entry(window)
    entry.pack()
    entry.place(x=160, y=140,height=25 , width=550)

    textbar = tkinter.Text(window)
    textbar.pack()
    textbar.place(x=160, y=190,height=70 , width=660)


    button1 = tkinter.Button(window, text="Search", command=Qurey_Input)
    button1.place(x=732, y=139, height=27, width= 88)

    window.mainloop()

if __name__ == "__main__":

    if not path.exists('PreProcessedDocs.json'):
        docs = filereader()
        InvertedIndex = InvertedIndex.Make_InvertedIndex(docs)
        PositionalIndex = PositionalIndex.Make_PositionalIndex(docs)
    else:
        docs = json.load(open('PreProcessedDocs.json'))
        InvertedIndex = InvertedIndex.Read_InvertedIndex()
        PositionalIndex = PositionalIndex.Read_PositionalIndex()
    
    main_window()

    if not path.exists('PreProcessedDocs.json'):
        j = json.dumps(docs)
        f = open('PreProcessedDocs.json','w')
        f.write(j)
        f.close()

    if not path.exists('InvertedIndex.json'):
        j = json.dumps(InvertedIndex, indent=2)
        f = open('InvertedIndex.json','w')
        f.write(j)
        f.close()

    if not path.exists('PositionalIndex.json'):
        j = json.dumps(PositionalIndex, indent=2)
        f = open('PositionalIndex.json','w')
        f.write(j)
        f.close()