# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:27:21 2023

@author: willi
"""

import math
import tkinter as tk
from tkinter import ttk

cache=[]

def updatetopscreen(cache):
    topscreen.config(text=''.join(map(str,cache)))

def clear(cache):
    cache.clear()
    midscreen.config(text='')
    updatetopscreen(cache)
    botscreen.config(text='')
    
    
# append numbers to the display+cache    
    
    
def app(cache,num):
    cache.append(num)
    topscreen.config(text=''.join(map(str,cache)))
    return

def calc(cache):
    midscreen.config(text='')
    try:
        value=eval(''.join(map(str,cache)))
    except ZeroDivisionError as err:
        midscreen.config(text='Error: '+str(err))
    except SyntaxError as err:
        midscreen.config(text='Error: '+str(err))
    
    botscreen.config(text=str(value))


root = tk.Tk()
root.geometry('400x400')
root.title('Calculator')
notebook = ttk.Notebook(root)
notebook.grid()


frame1 = ttk.Frame(notebook, width=320, height=400)
frame1.grid()
notebook.add(frame1, text='calculator')

style = ttk.Style()
style.layout('TNotebook.Tab', [])
style.configure("BW.TLabel", foreground="black", background="white")


topscreen=ttk.Label(frame1,style='BW.TLabel',text='',anchor='w')
topscreen.grid(row=0,column=1,columnspan=4,padx=2,pady=0,sticky='nsew')
midscreen=ttk.Label(frame1,style='BW.TLabel',text='')
midscreen.grid(row=1,column=1,columnspan=4,padx=2,pady=0,sticky='nsew')
botscreen=ttk.Label(frame1,style='BW.TLabel',text='',anchor='e')
botscreen.grid(row=2,column=1,columnspan=4,padx=2,pady=0,sticky='nsew')



#seperators
screenseptop=ttk.Separator(frame1,orient='horizontal')
screenseptop.grid(column=1,row=0,columnspan=4,sticky='new')
screensepbot=ttk.Separator(frame1,orient='horizontal')
screensepbot.grid(column=1,row=2,columnspan=4,sticky='sew')
sepright=ttk.Separator(frame1,orient='vertical')
sepright.grid(column=5,row=0,rowspan=10,sticky='nse')
sepleft=ttk.Separator(frame1,orient='vertical')
sepleft.grid(column=0,row=0,rowspan=10,sticky='nsw')

sepnum=ttk.Separator(frame1,orient='vertical')
sepnum.grid(column=4,row=3,rowspan=5,sticky='nsw')

sepnumbot=ttk.Separator(frame1,orient='horizontal')
sepnumbot.grid(column=1,row=7,columnspan=4,sticky='sew')



##############buttons############


###numbers
button_num_one=ttk.Button(frame1,text='1',command=lambda: app(cache,1))
button_num_one.grid(row=3,column=1)

button_num_two=ttk.Button(frame1,text='2',command=lambda: app(cache,2))
button_num_two.grid(row=3,column=2)

button_num_three=ttk.Button(frame1,text='3',command=lambda: app(cache,3))
button_num_three.grid(row=3,column=3)

button_num_four=ttk.Button(frame1,text='4',command=lambda: app(cache,4))
button_num_four.grid(row=4,column=1)

button_num_five=ttk.Button(frame1,text='5',command=lambda: app(cache,5))
button_num_five.grid(row=4,column=2)

button_num_six=ttk.Button(frame1,text='6',command=lambda: app(cache,6))
button_num_six.grid(row=4,column=3)

button_num_seven=ttk.Button(frame1,text='7',command=lambda: app(cache,7))
button_num_seven.grid(row=5,column=1)

button_num_eight=ttk.Button(frame1,text='8',command=lambda: app(cache,8))
button_num_eight.grid(row=5,column=2)

button_num_nine=ttk.Button(frame1,text='9',command=lambda: app(cache,9))
button_num_nine.grid(row=5,column=3)

button_num_zero=ttk.Button(frame1,text='0',command=lambda: app(cache,0))
button_num_zero.grid(row=6,column=2)

###basic functions

button_add=ttk.Button(frame1,text='+',command=lambda: app(cache,'+'))
button_add.grid(row=3,column=4,padx=1)

button_minus=ttk.Button(frame1,text='-',command=lambda: app(cache,'-'))
button_minus.grid(row=4,column=4,padx=1)

button_multiply=ttk.Button(frame1,text='*',command=lambda: app(cache,'*'))
button_multiply.grid(row=5,column=4,padx=1)

button_div=ttk.Button(frame1,text='/',command=lambda: app(cache,'/'))
button_div.grid(row=6,column=4,padx=1)

button_calc=ttk.Button(frame1,text='=',command=lambda: calc(cache))
button_calc.grid(row=6,column=3,padx=1)

#useful

button_dot=ttk.Button(frame1,text='.',command=lambda: app(cache,'.'))
button_dot.grid(row=6,column=1)

button_lb=ttk.Button(frame1,text='(',command=lambda: app(cache,'('))
button_lb.grid(row=8,column=1)

button_rb=ttk.Button(frame1,text=')',command=lambda: app(cache,')'))
button_rb.grid(row=8,column=2)

button_mod=ttk.Button(frame1,text='mod(%)',command=lambda: app(cache,'%'))
button_mod.grid(row=8,column=3)

button_clc=ttk.Button(frame1,text='clc',command=lambda: clear(cache))
button_clc.grid(row=8,column=4)

button_del=ttk.Button(frame1,text='del',command=lambda: [cache.pop(),updatetopscreen(cache)])
button_del.grid(row=9,column=4)

button_exp=ttk.Button(frame1,text='**',command=lambda: app(cache,'**'))
button_exp.grid(row=9,column=1)

####constants

constants={
    'pi':3.14159,
    'e':2.71828
    }

button_pi=ttk.Button(frame1,text='π',command=lambda: app(cache,constants['pi']))
button_pi.grid(row=0,column=6)

button_e=ttk.Button(frame1,text='e',command=lambda: app(cache,constants['e']))
button_e.grid(row=1,column=6)

##New Frame
#Graphing Software
frame2 = ttk.Frame(notebook, width=320, height=400)
frame2.grid()
notebook.add(frame2, text='Graphing')


root.mainloop()