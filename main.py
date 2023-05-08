# Alan (Wentao Li), Imperial College London 2022
# All rights reserved

from tkinter import *
from tkinter import ttk
import os
from datetime import date
import pandas as pd
import csv

'''
TODO: Develop a user interface, allow users to log amounts
TODO: Store each set of entries as a dictionary, convert to pd dataframe (or use csvwriter?), then store in csv format
df.to_csv('existing.csv', mode='a', index=False, header=False) seems to do the job
TODO: Allow users to view stats (average expenditure per day/week, total expenditure)
'''

### Functions ###

### Main body ###

def main_logger():
    amount = amount_entry.get()
    food = food_entry.get()
    note = note_entry.get()
    today = date.today().strftime('%Y-%m-%d')
    headers = {'Date': [today], 'Amount': [amount], 'Food': [food], 'Note': [note]}
    df = pd.DataFrame(headers)

    try:
        # Append to existing CSV file
        df.to_csv('daily_expenses.csv', mode='a', header=False, index=False)
    except FileNotFoundError:
        # Create new CSV file with headers
        df.to_csv('daily_expenses.csv', mode='w', header=True, index=False)
    amount_entry.delete(0, END)
    food_entry.delete(0, END)
    note_entry.delete(0, END)

### Interface ###

window = Tk()
window.title('Personal Account Manager')
window.geometry("300x250")
frm = ttk.Frame(window, padding=10)
frm.grid()

ttk.Label(frm, text="Personal Account Manager", font=("", 16)).grid(column=0, row=0, columnspan=2, pady=10)

ttk.Label(frm, text="Amount:").grid(column=0, row=1, padx=10, pady=10)
amount_entry = ttk.Entry(frm, width=16, font=("", 12))
amount_entry.grid(column=1, row=1)

ttk.Label(frm, text="... of which food:").grid(column=0, row=2, padx=10, pady=10)
food_entry = ttk.Entry(frm, width=16, font=("", 12))
food_entry.grid(column=1, row=2)

ttk.Label(frm, text="Note:").grid(column=0, row=3, padx=10, pady=10)
note_entry = ttk.Entry(frm, width=16, font=("", 12))
note_entry.grid(column=1, row=3)

# Set up buttons
confirm_button = ttk.Button(frm, text="Confirm", command=main_logger)
confirm_button.grid(column=0, row=4, pady=20)

quit_button = ttk.Button(frm, text="Quit", command=window.destroy)
quit_button.grid(column=1, row=4, pady=20)

# Set button colors and font
confirm_button.configure(style='Accent.TButton')
quit_button.configure(style='Accent.TButton')
ttk.Style().configure('Accent.TButton', foreground='white', font=("", 12), background='#0080ff')

# Set background color for the frame
frm.configure(style='MainFrame.TFrame')
ttk.Style().configure('MainFrame.TFrame', background='#e6e6e6')

window.mainloop()