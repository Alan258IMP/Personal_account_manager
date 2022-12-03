# Alan (Wentao Li), Imperial College London 2022
# All rights reserved

from tkinter import *
from tkinter import ttk
import os
import datetime
import pandas as pd

'''
TODO: Develop a user interface, allow users to log amounts
TODO: Store each set of entries as a dictionary, convert to pd dataframe (or use csvwriter?), then store in csv format
df.to_csv('existing.csv', mode='a', index=False, header=False) seems to do the job
TODO: Allow users to view stats (average expenditure per day/week, total expenditure)
'''

### Functions ###

### Main body ###

### User interface ###

window = Tk()
window.title('Personal Account Manager')
#window.geometry()
frm = ttk.Frame(window, padding=10)
frm.grid()
#ttk.Label(frm, text = f"")
ttk.Label(frm, text="Personal Account Manager", font=12).grid(column=0, row=0, columnspan=1)
ttk.Label(frm, text="Amount").grid(column=0, row=1) # foreground is text color. Can use shorthand fg and bg
ttk.Entry(frm, width=16).grid(column=1, row=1)
ttk.Label(frm, text="... of which food").grid(column=0, row=2)
ttk.Entry(frm, width=16).grid(column=1, row=2)
ttk.Label(frm, text="Note").grid(column=0, row=3)
ttk.Entry(frm, width=16).grid(column=1, row=3)
ttk.Button(frm, text="Quit", command=window.destroy).grid(column=2, row=4)
window.mainloop()


