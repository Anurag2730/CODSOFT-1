from tkinter import *
import requests

root=Tk()
root.title('Weather Forecast')
root.geometry('480x150')

l=Label(root, text = "Enter City Name: ", font=("Ariel", 15))
l.place(x=5,y=10)

w_entry = Entry(root, width=32, font=("Ariel", 17))
w_entry.place(x=170, y=10, height=27)

def Gen_report():
    C=w_entry.get()
    url = 'https://wttr.in/{}?format=4'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    z=Label(root, text=f"The weather in {T}", font=("Ariel", 15))
    z.place(x=0, y=80)


get_button = Button(root, text="Get Weather", width = 10, font=("Ariel", 12), command=Gen_report)
get_button.place(x=200, y=40)

root.mainloop()