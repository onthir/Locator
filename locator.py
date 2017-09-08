from tkinter import *
import requests
import urllib.parse

root = Tk()
root.title("Complete Address Finder")
root.geometry('1920x1080')
root.configure(background="orange")
heading = Label(root, text="Address Locator", font=('arial 50 bold'), fg="steelblue", bg="orange").pack()

lab = Label(root, text="Enter Location, Schools, Restaurants....etc.", font=('arial 25 bold'), bg="orange").place(x=400, y=200)


text = StringVar()
ent = Entry(root, width=50, textvariable=text).place(x=400, y=250)

def  main_function():
     
     address = text.get()
     main_api =  'http://maps.googleapis.com/maps/api/geocode/json?'
     url = main_api + urllib.parse.urlencode({'address' : address})

     json_data = requests.get(url).json()

     #data of status
     json_status = json_data['status']

     if json_status == 'OK':
          
          formatted_address = json_data['results'][0]['formatted_address']
          label2 = Label(root, text=formatted_address, font=('arial 15 bold'), fg="green", bg="lightblue", width=80).place(x=400, y=400)
     else:
          labell = Label(root, text="Invalid Request", font=('arial 15 bold'), fg="red", bg="lightblue").place(x = 400, y= 450)

btn = Button(root, text="Find", width=30, height=3, fg="white", bg="black", command=main_function).place(x=400, y=300)

root.mainloop()
