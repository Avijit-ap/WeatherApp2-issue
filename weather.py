from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    try:
        city=textfield.get()

        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj= TimezonFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        print(result)


        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api="https://https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=71dc9ae85ee5f828c02ebd57d2a6fdf5"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data["main"]['humidity']
        wind = json_data['wind']['speed ']
    

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=presssure)



    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry !!")
    
#searchbox
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="Centre",width=17,font=("poppins",25,"bold"),bg="404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage-icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100) 

#bottom Box
Frame_image=PhotoImage(file=box.png)
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Labe1(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Labe1(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=225,y=400)

label3=Labe1(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Labe1(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="1ab5ef")
p.place(x=670,y=430)