from os import name
from tkinter import *
from subprocess import call
import tkinter as tk
import csv


root = Tk() #instantiate an instance of a window
root.geometry("960x560")
root.title("Artemis Hotel Management System")
Hotel_Details = []
Customer_Payment_Details = []

def check_out_customer(Name):
        lines = list()
        with open('Hotel_Details.csv', 'r') as readFile:
                reader = csv.reader(readFile)
                lines = []
                for row in reader:
                        lines.append(row)
                        if row[0] != name:
                                lines.append(row)
        

def destroy_window(top):
        top.destroy()
        

def send(): 
        with open('Hotel_Details.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(Hotel_Details)
                f.close()
                
def read():
        with open('Hotel_Details.csv', 'r') as file:
                lines = []
                for line in file:
                        lines.append(line.rstrip())
                return lines
        

def check_in_customer(name, number, address, days, room, top):
        headerList = ["NAME", "PHONE NUMBER", "EMAIL ADDRESS", "DAYS BOOKED", "TYPE OF ROOM"]
        with open("Hotel_Details.csv", "w") as file:
                dw = csv.DictWriter(file, delimiter=',', fieldnames=headerList)
                dw.writeheader()
                                    
        for item in [name, number, address, days, room]:
                Hotel_Details.append(item.get())
        send()
        top.destroy()
        

global single_room_label
single_room_label = None

global double_room_label
double_room_label = None

global deluxe_room_label
deluxe_room_lable = None

global suite_room_label
suite_room_label = None


def single_room(top):
        global single_room_label
        text = "•Single bed\n•Air Conditioning\n•Cable/Satellite TV\n•Laundry Facilities\n•Heating\n•Roomservice\n•Wireless Internet\n•Showever over bath\n•Bathroom facilities & products\n•Direct dial telephone\n•Fridge/freezer & Microwave"
        
        if Check1.get() == 1:
                single_room_label = Label(top, text=text,anchor = "w",height=12,width=25, borderwidth=2, relief="raised")
                single_room_label2 =Label
                single_room_label.place(x=380, y=210)
        if Check1.get() == 0:
                single_room_label.place_forget()

def double_room(top):
        global double_room_label
        text = "•2 Single beds\n•Air Conditioning\n•Cable/Satellite TV\n•Laundry Facilities\n•Heating\n•Roomservice\n•Wireless Internet\n•Showever over bath\n•Bathroom facilities & products\n•Mini Fridge\n•Room safe\n•Lift Access"
        
        if Check2.get() == 1:
                double_room_label = Label(top, text=text,anchor = "w",height=12,width=25, borderwidth=2, relief="raised")
                double_room_label2 =Label
                double_room_label.place(x=380, y=210)
        if Check2.get() == 0:
                double_room_label.place_forget()

def deluxe_room(top):
        global deluxe_room_label
        text = "        •Can accomodate up to 2 people\n•Air Conditioning\n•Laundry Facilities\n•Heating\n•Roomservice\n•Wireless Internet\n•Showever over bath\n•Bathroom facilities & products\n•Smart TV\n•Gym dumbbells\n•Soundproof walls\n•Coffee/Tea maker\n•Daily maid services"
        
        if Check3.get() == 1:
                deluxe_room_label = Label(top, text=text,anchor = "w",height=13,width=30, borderwidth=2, relief="raised")
                deluxe_room_label2 =Label
                deluxe_room_label.place(x=350, y=210)
        if Check3.get() == 0:
                deluxe_room_label.place_forget()

def suite_room(top):
        global suite_room_label
        text = "•King size bed\n      •Luxurious white marble bathroom with separate shower & bathtub\n•Soap and bath amentities\n•Coffew & tea making facilities\n•32 Inch flat screen tv\n•Mini bar\n•Private terrace with pagoda view\n•24 hour room service\n•Complimentary WIFI\n•In-room safe"
        
        if Check4.get() == 1:
                suite_room_label = Label(top, text=text,anchor = "w",height=20,width=55, borderwidth=2, relief="raised")
                suite_room_label2 =Label
                suite_room_label.place(x=290, y=140,)
        if Check4.get() == 0:
                suite_room_label.place_forget()

def presidential_room(top):
        global presidential_room_label
        text ="•King bed\n•3 49-55 inch Smart TVs\n•Separate lounge area\n•Private dining room\n•Walk in wardrobe\n•Separate walk-in shower\n•Access to spa\n•Complimentary WIFI\n•24 hour room service\n•24 hour laundry service"

        if Check5.get() == 1:
                presidential_room_label = Label(top, text=text,anchor = "w",height=10,width=20, borderwidth=2, relief="raised")
                presidential_room_label2 =Label
                presidential_room_label.place(x=410, y=210,)
        if Check5.get() == 0:
                presidential_room_label.place_forget()


def payment(Name, PhoneNumber, EmailAddress, TotalPrice, CardNumber, CardHolderName, ExpirationDate, TownOrCity, PostalCode, Country,top):
        headerList = ["Name", "Phone Number", "Email Address", "Total Price", "Card Number", "Card Holder Name", "Expiration Date", "Town/City", "Postal Code", "Country"]
        with open("Customer_Payment_Details.csv", "w") as file:
                dw = csv.DictWriter(file, delimiter=',', fieldnames=headerList)
                dw.writeheader()
                                    
        for item in [Name, PhoneNumber, EmailAddress, TotalPrice, CardNumber, CardHolderName, ExpirationDate, TownOrCity, PostalCode, Country]:
                Customer_Payment_Details.append(item.get())
        send()
        top.destroy()



        

text = StringVar()
text2 = StringVar()
text3 = StringVar()
text4 = StringVar()
text5 = StringVar()
text6 = StringVar()
text7 = StringVar()
text8 = StringVar()
text9 = StringVar()
text10 = StringVar()


Check1 = IntVar()
Check2 = IntVar()
Check3 = IntVar()
Check4 = IntVar()
Check5 = IntVar()


def newWindow():
    top = Toplevel()
    top.title("Artemis Hotel Management System")
    top.geometry("960x560")
    
    button = Button(top,text = "CHECK IN",background = "gray",height = 5,width = 60,command=newWindow2).place(x=100, y=30)
    button2 = Button(top,text = "CHECK OUT",background = "gray",height = 5,width = 60,command=newWindow3).place(x=100, y=130)
    button3 = Button(top,text = "HOTEL ROOM DETAILS",background = "gray",height = 5,width = 60,command=newWindow4).place(x=100, y=230)
    button4 = Button(top,text = "BILLING & PAYMENT",background = "gray",height = 5,width = 60, command=newWindow5).place(x=100, y=330)
    button5 = Button(top,text = "EXIT",background = "gray",height = 5,width = 60,command = quit,).place(x=100, y=430)


def newWindow2():
    top = Toplevel()
    top.title("Check In")
    top.geometry("960x560")

    label =Label(top, text = "NAME", borderwidth=2, relief="raised", height=3, width=60).place(x=100, y=50)
    label2 =Label(top, text = "PHONE NUMBER", borderwidth=2, relief="raised", height=3, width=60).place(x=100, y=150)
    label3 =Label(top, text = "EMAIL ADDRESS", borderwidth=2, relief="raised", height=3, width=60).place(x=100, y=250)
    label4 =Label(top, text= "DAYS BOOKED", borderwidth=2, relief="raised", height=3, width=60).place(x=100, y=350)
    label5 =Label(top, text = "TYPES OF ROOMS", borderwidth=2, relief ="raised", height=3, width=30).place(x=100, y=420)
    
    label6 =Label(top, text = "Single Room").place(x=350, y=420)
    label7 =Label(top, text = "Double Room").place(x=430, y=420)
    label8 =Label(top, text = "Deluxe Room").place(x=350, y=450)
    label9 =Label(top, text = "Suite").place(x=450, y=450)
    label_10 =Label(top, text = "Presidential Suite").place(x=370, y=480)

    Button(top, text = "OK", borderwidth=2, relief="raised", height=3, width=30, command=lambda: check_in_customer(entry, entry2, entry3, entry4, entry5, top)).place(x=670, y=480)
    Button(top, text = "BACK", borderwidth=2, relief="raised", height=3, width=30, command=lambda: destroy_window(top)).place(x=670, y=410)
    
    entry =Entry(top,textvariable=text,)
    entry.place(x=550, y=65,width=400, height=20)

    entry2 =Entry(top,textvariable=text2)
    entry2.place(x=550, y=165, width=400, height=20)

    entry3 =Entry(top,textvariable=text3)
    entry3.place(x=550, y=265, width=400, height=20)

    entry4 =Entry(top,textvariable=text4)
    entry4.place(x=550, y=365, width=400, height=20)

    entry5 =Entry(top,textvariable=text5)
    entry5.place(x=100, y=490, width=215, height=25)

    



def newWindow3():
        top = Toplevel()
        top.title("Check Out")
        top.geometry("960x560")

        label =Label(top, text = "CHECK OUT", borderwidth=2, relief="raised", width=60, height=4, background="gray").place(x=270, y=40)
        label2 =Label(top, text = "PLEASE ENTER YOUR NAME", borderwidth=2, relief="raised", width=80, height=4, background="gray").place(x=200, y=120)
        
        entry =Entry(top,textvariable=text)
        entry.place(width=500, height=35, x=230, y=200)

        Button(top,text = "BACK", borderwidth=2, relief="raised", height=3, width=30,background="gray",command=lambda: destroy_window(top)).place(x=140, y=460)
        Button(top,text = "OK", borderwidth=2, relief="raised", height=3, width=30, background="gray",command=lambda: check_out_customer(entry)).place(x=540, y=460)


def newWindow4():
        top = Toplevel()
        top.title("Hotel Room Details")
        top.geometry("960x560")

        label =Label(top, text = "PLEASE CHOOSE ONE OF THE ROOMS FOR THE DETAILS", borderwidth=2, relief="raised", height=3, width=100, background="gray").place(x=150, y=20)

        check1 = Checkbutton(top,text = "Single Room",state =ACTIVE, onvalue=1, offvalue=0,variable =Check1, command=lambda: single_room(top)).place(x=190, y=110)
        check2 = Checkbutton(top,text = "Double Room", state =ACTIVE,onvalue=1, offvalue=0, variable =Check2, command=lambda: double_room(top)).place(x=310, y=110)
        check3 = Checkbutton(top,text = "Deluxe Room", state =ACTIVE,onvalue=1, offvalue=0, variable =Check3, command=lambda: deluxe_room(top)).place(x=436, y=110)
        check4 = Checkbutton(top,text = "Suite", state =ACTIVE,onvalue=1, offvalue=0, variable =Check4, command=lambda: suite_room(top)).place(x=560, y=110)
        check5 = Checkbutton(top,text = "Presidential Suite", state =ACTIVE,onvalue=1, offvalue=0, variable =Check5, command=lambda: presidential_room(top)).place(x=670, y=110)

        Button(top,text = "BACK", borderwidth=2, relief="raised", height=3, width=90,background="gray",command=lambda: destroy_window(top)).place(x=160, y=460)

def newWindow5():
        top = Toplevel()
        top.title("Billing & Payments")
        top.geometry("960x560")

        label =Label(top, text = "PLEASE ENTER YOUR PAYMENT DETAILS", borderwidth=3, relief="raised", height=3, width=120, background="gray").place(x=65, y=20)
        label2 =Label(top, text = "NAME", borderwidth=3, relief="raised", height=3, width=30).place(x=80, y=110)
        label3 =Label(top, text ="PHONE NUMBER", borderwidth=3, relief="raised", height=3, width=30).place(x=380, y=110)
        label4 =Label(top, text = "EMAIL ADDRESS", borderwidth=3, relief="raised", height=3, width=30).place(x=680, y=110)
        label5 =Label(top, text = "PLEASE ENTER THE PRICE OF YOUR ROOM", borderwidth=3, relief="raised", height=3, width=40).place(x=80, y=310)
        label6 =Label(top, text = "◾Single room - £60\n\n ◾Double room - £102\n\n ◾Deluxe room - £187\n\n ◾Suite room - £267\n\n ◾Presidential room - £504",width =25, height=10).place(x=90, y=400)

        label7 =Label(top,borderwidth=3, relief="raised", height=17, width=70).place(x=455, y=285)
        label8 =Label(top,text = "PAYMENT DETAILS", relief="raised", height=2, width=20).place(x=630, y=300)
        label9 =Label(top,text = "Card Number").place(x=500, y=370)
        label0 =Label(top,text = "Card Holder Name").place(x=750, y=370)
        label_11 =Label(top,text = "Expiration Date").place(x=500, y=435)
        label_12 =Label(top,text = "Town/City").place(x=740, y=430)
        label_13 =Label(top,text = "Postal Code").place(x=740, y=470)
        label_14 =Label(top,text = "Country").place(x=740, y=510)

        Button(top,text = "BACK", borderwidth=2, relief="raised", height=1, width=10,background="gray",command=lambda: destroy_window(top)).place(x=500, y=515)
        Button(top,text = "CONFIRM", borderwidth=2, relief="raised", height=1, width=10,background="gray",command=lambda: payment(entry, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10,top)).place(x=500, y=485)
        

        entry =Entry(top,textvariable=text)
        entry.place(width=190, height=20, x=95, y=170)

        entry2 =Entry(top,textvariable=text2)
        entry2.place(width=190, height=20, x=395, y=170)

        entry3 =Entry(top,textvariable=text3)
        entry3.place(width=190, height=20, x=695, y=170)

        entry4 =Entry(top,textvariable=text4)
        entry4.place(width=230, height=25, x=110, y=380)

        entry5 =Entry(top,textvariable=text5)
        entry5.place(width=130, height=15, x=490, y=400)

        entry6 =Entry(top,textvariable=text6)
        entry6.place(width=190, height=15, x=740, y=400)

        entry7 =Entry(top,textvariable=text7)
        entry7.place(width=90, height=15, x=500, y=460)

        entry8 =Entry(top,textvariable=text8)
        entry8.place(width=90, height=15, x=830, y=433)

        entry9 =Entry(top,textvariable=text9)
        entry9.place(width=90, height=15, x=830, y=473)

        entry10 =Entry(top,textvariable=text10)
        entry10.place(width=110, height=15, x=830, y=513)

    
def Staff():
    mLabel =Label(root,text = "Please enter your username").pack()
    mEntry = Entry(root,textvariable=ment).pack()



mLabel = Label(text = "Hello! Please click on the Customer button to access the main hotel menu").pack()
m2Button = Button(text = "CUSTOMER",command=newWindow,width = 25,height = 5,).place(x = 380, y = 125)
m3Button = Button(text = "EXIT",width = 25, height =5,command=quit).place(x=380, y=350)



root.mainloop()

        
        
    
