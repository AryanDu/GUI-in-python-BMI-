from tkinter import *
from tkinter import font
from tkinter.font import Font
from typing import Sized
from PIL import ImageTk, Image
from tkinter import messagebox

# Making window 
root = Tk()
root.title("BODY MASS INDEX CALCULATOR ")
root.geometry('700x400')

# to mix th minimum size of window 
root.minsize(700, 400)

# to mix th maximum size of window 
root.maxsize(700, 400)

#use PIcture as Bacgroung image!!
'''img = ImageTk.PhotoImage(Image.open("normal.png"))
canvas1 = Canvas( root, width = 400, height = 400)

canvas1.pack(fill = "both", expand = True)    

canvas1.create_image( 0, 0, image = img,  achor = "nw")'''

#second method osf using image as background...........                                         
img = ImageTk.PhotoImage(Image.open("normal.png"))  
l=Label(image=img)
l.place(relx = 0.0, rely = 1.0,   anchor ='sw')



#making label = titile {Body mass Index}
name = Label(root,
                  text = "BODY MASS INDEX" ,    # name  
                                            fg = "black" ,  #color 
                                            bg="pink",       
                                           font = "Times 36 bold ") # font size and bold
name.pack()

#Giving extra Space Between two Label
Label(root, text="").pack()

# declaring string variable
# for storing Mass and Height 

mass_var= StringVar()
height_var= StringVar()

# making label and entry for mass
mass = Label(root,
                   text="Enter Your Mass " 
                   ,bg="pink"
                  ,font = "Times 24 bold ").pack()
mass_entery  = Entry(root,
                         textvariable=mass_var) # making location to store string      

#making size of mass entry                                   
mass_entery.pack(ipadx= 35, ipady=4)

#making space between Mass and Height
Label(root, text="").pack()                          

# making label and entry for Height
height = Label(root, 
                     text="Enter Your Height", bg="pink", 
                      font = "Times 24 bold ").pack()

height_entery  = Entry(root,
                             textvariable = height_var )

#making size of  height entry                              
height_entery.pack(ipadx= 35, ipady=4)                             

#making space after height entry
Label(root, text="").pack()    

# function for buttton
try:
    def calculate():
        mass = mass_var.get()           #To collect data from entry which is store in string variable
        mass = float(mass)              #Converting str into float to perform calculation 
        height = height_var.get()
        height = float(height)
        b_m_i =  mass/(height*height)                # the main formula for Body mass index calculation 
        if( b_m_i<18.5):
            print(f"Your Body Mass Index Is {b_m_i}, You Are Under Weight!!")
            messagebox.showinfo("Body Mass Index",
                                            f"Your Body Mass Index Is {b_m_i}, You Are Under Weight!!")


        elif(b_m_i<=24.9 and b_m_i>=18.5 ):
            print(f"Your Body Mass Index Is {b_m_i}, You Are Normal Weight!!")
            messagebox.showinfo("Body Mass Index",
                                          f"Your Body Mass Index Is {b_m_i},You Are Normal Weight!! !!")


        elif(b_m_i<=30 and b_m_i>24.9 ):
            print(f"Your Body Mass Index Is {b_m_i}, You Are over  Weight!!")
            messagebox.showinfo("Body Mass Index", 
                                           f"Your Body Mass Index Is {b_m_i},You Are over  Weight!!")    

        elif(b_m_i>30):
            print(f"Your Body Mass Index Is {b_m_i}, You Are a Patient Of Obesity!!") 
            messagebox.showinfo("Body Mass Index",
                                         f"Your Body Mass Index Is {b_m_i},You Are a Patient Of Obesity!!") 

except ValueError as a:
    print(a)
    messagebox.showerror("showerror", "Error")

# functioning submit buttton 
Button_font = font.Font(size=16, weight='bold')  #font etc for button 

sub_btn= Button(root,
                text = 'CALCULATE'  ,
                 bg="deep sky blue" , 
                 fg="gray4",      
                 font = Button_font,        
                 activebackground="cyan",       # color after click 
                width=15,height=1,         # size
                 command = calculate) # GIVING FUNCTION to button
sub_btn.pack()   # packing font 







































root.mainloop()

