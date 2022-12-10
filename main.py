from tkinter import *

window = Tk()
window.title("Welcome to Mile to Kilometer Converter")
window.minsize(200, 100)
window.config(padx=20 , pady=20)

def mile_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_results.config(text=f"{km}")



miles_input = Entry(width=6)
miles_input.grid(column=1 , row=0 )

miles_label = Label(text= "enter miles")
miles_label.grid(column=2 , row=0 )

is_equal = Label(text= "is equal to:")
is_equal.grid(column=0 , row=1 )

km_results = Label(text="0")
km_results.grid(column=1 , row=1 )

km_label = Label(text="km")
km_label.grid(column=2, row=1 )

button = Button(text="Calculate", command=mile_to_km)
button.grid(column=2 , row= 1)




window.mainloop()
