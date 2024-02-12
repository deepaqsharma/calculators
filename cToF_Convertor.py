#this is to convert the temperature units; deg C to deg F

import tkinter as tk


root = tk.Tk()
root.geometry("490x290")
root.title("Temp. Convertor")

subLabel = chr(176)+"C" +" to " + chr(176)+"F"

tk.Label(root, text="Temperature Convertor", fg="Black", font="impact 15").place(x=140, y=0)
tk.Label(root, text=subLabel, fg="Black", font="impact 12").place(x=220, y=30)


#function to convert the Degree Celsius value to Fahrenheit
def convert():
    valueF = float(input_C_Var.get())*1.8+32
    input_F_Var.set(valueF)
    print(f"{input_C_Var.get()} C = {input_F_Var.get()} F")

input_C_Var = tk.StringVar(root)
input_F_Var = tk.StringVar(root)

celsius = chr(176)+"Celsius"

tk.Label(root, text=celsius, font=30).place(x=110, y=70)
entry_C = tk.Entry(root, textvariable=input_C_Var)
entry_C.place(x=100, y = 100, width=90)


fehrenheit = chr(176)+"Fehrenheit"
tk.Label(root, text=fehrenheit, font=30).place(x=300, y=70)
entry_F = tk.Entry(root, textvariable=input_F_Var)
entry_F.place(x=300, y = 100, width=90)

button = tk.Button(root, text="Convert", command=convert, font=20)
button.place(x=200, y = 200)




root.mainloop()

#code ended.