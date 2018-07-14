from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def is_valid_day(x):
    try:
        x = int(x)

        if(x >= 0 and x <= 365):
            return True

        return False
    except:
        return False

def clicked():
    #check for invalid inputs
    if(not is_valid_day(daySelector.get())):
        messagebox.showerror('Error', 'Please input valid day.')
        return
    
    #run code
    print(daySelector.get())

def outputResult(result):
    messagebox("Result", result)

window = Tk()
window.title("Weather Forcastatron 9000")
#window.geometry('500x350')

yearLabel = Label(window, text="Forecast Year:", width=20, font=18)
yearLabel.grid(column=0, row=0)

yearSelector = Combobox(window, width=15, font=18)
yearSelector['values']=(2016, 2017, 2018, 2019, 2020)
yearSelector.current(0)
yearSelector.grid(column=1, row=0)

dayLabel = Label(window, text="Forecast Day:", width=20, font=18)
dayLabel.grid(column=0, row=1)

daySelector = Spinbox(window, from_=0, to=365, width=15, font=18)
daySelector.grid(column=1, row=1)

btn = Button(window, text="Forecast!", command=clicked)
btn.grid(column=0, row=2)

window.mainloop()

