from tkinter import *;
import pyspeedtest

def speedc():
    sp = pyspeedtest.SpeedTest("www.google.com");
    down = str(round(sp.download()/(10**3),3))+" kbps";
    
    labd.config(text=down);

sp=Tk();
sp.title("Internet Speed test");
sp.geometry("500x700");
sp.config(bg="purple")

lab=Label(sp,text="Internet Speed Test",font=("Time new Roman",30,"bold"),fg="black",bg="purple");
lab.place(x=60,y=40,height=50,width=380);

lab=Label(sp,text=" Speed ",font=("Time new Roman",20,"bold"));
lab.place(x=50,y=130,height=50,width=380);

labd=Label(sp,text="00",font=("Time new Roman",20,"bold"));
labd.place(x=50,y=200,height=50,width=380);

#lab=Label(sp,text="Upload Speed ",font=("Time new Roman",20,"bold"));
#lab.place(x=50,y=290,height=50,width=380);

#labu=Label(sp,text="00",font=("Time new Roman",20,"bold"));
#labu.place(x=50,y=360,height=50,width=380);

b=Button(sp,text="CHECK SPEED",font=("Time new Roman",20,"bold"),relief=RAISED,bg="Red",command=speedc);
b.place(x=60,y=500,height=50,width=380);

sp.mainloop();