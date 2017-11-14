#TODO separate subs and save boxes into different tabs
#TODO add labels, descriptions, how to use
#TODO add clear save box button
#TODO better the layout
#TODO add small box telling you number of saved sentences
#TODO make listboxes stretch vertically
#TODO add delete, delete all buttons
#TODO Wrap text
#TODO Add 3 modes:
#       One mode for combining and directly editing saved entries
#       one mode for adding entries to save list

import codecs
import pyperclip
from appJar import gui

def move(btn):
    for line in app.getListBox("subs"):
        if(line != ""):
            app.setListItem("save", "", line, first = True)
            app.addListItem("save", "", select = False) 
            

def copy(btn):
    for line in app.getListBox("save"):
        if(line != ""):
            pyperclip.copy(line)
            app.removeListItem("save", line)

def open_file(btn):
    file_name = app.openBox("Open .srt", dirName=None, fileTypes=[("subtitle files", '*.srt')],
                asFile=False, parent=None)
    with codecs.open(file_name, encoding = "utf-8") as f:
        sub_text = f.read()
        #start = sub_raw.index('0')
        #f.seek(0)
        #sub_raw = f.read()
        #TODO Ensure proper formatting by getting rid of possible excess space on top

    sub_list = []
    sub_raw_list = sub_text.splitlines()
    #splitlines() does not add last line break
    sub_raw_list.append("")
    #list of ending indexes of each sub section
    sub_sec = []                            
    #get ending indexes of each sub section
    for i in range(len(sub_raw_list)):      
        if(sub_raw_list[i] == ""):
            sub_sec.append(i)
    #start at 2 because of .srt format
    start = 2
    
    for i in range(len(sub_sec)):
        end = sub_sec[i]
        #temp string for concatenation
        conc = ""                           
        for j in range(start, end):
            conc = conc + sub_raw_list[j]
            
        sub_list.append(conc)
        sub_list.append("")
        start = end + 3

    app.updateListBox("subs", sub_list, select=False)
    

with gui("SRT Reader") as app:
    #holds loaded subs
    sub_list = []
    #holds all sentences user wants to save
    save = []
    app.addListBox("subs", sub_list)
    app.setListBoxChangeFunction("subs", move)
    app.addListBox("save", save)
    app.setListBoxChangeFunction("save", copy)
    app.addListItem("save","",select=False)
    app.setGeometry(300, 500)
    app.setLocation(0, 0)
    app.setFont(12, font = "Consolas")
    app.addButton("Open", open_file)
    app.setResizable(canResize=True)
    

    

                                   



    
    

