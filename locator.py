from tkinter import *
import requests
import urllib.parse

root = Tk()
root.title("Complete Address Finder")
root.geometry('1920x1080+50+50')
heading = Label(root, text="Complete Address Finder", font=('arial 20 bold'), fg="steelblue").pack()

lab = Label(root, text="Enter Location, Schools, Restaurants....etc.", font=('arial 13 bold')).pack()


text = StringVar()
ent = Entry(root, width=50, textvariable=text).pack()

def  main_function():
     
     address = text.get()
     main_api =  'http://maps.googleapis.com/maps/api/geocode/json?'
     url = main_api + urllib.parse.urlencode({'address' : address})

     json_data = requests.get(url).json()

     #data of status
     json_status = json_data['status']

     if json_status == 'OK':
          
          formatted_address = json_data['results'][0]['formatted_address']
          label2 = Label(root, text=formatted_address, font=('arial 15 bold'), fg="green", bg="lightgrey", width=80).place(x=100, y=160)
     else:
          labell = Label(root, text="Invalid Request", font=('arial 13 bold'), fg="red").pack()

btn = Button(root, text="Find", width=30, height=3, bg="lightgreen", command=main_function).pack()

root.mainloop()














