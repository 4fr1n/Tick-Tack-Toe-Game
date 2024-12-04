from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Tick Tack Toe")
frame1= Frame(root)
frame1.pack()
titleLabel=Label(frame1,text="Tick Tack Toe",font=("Arial",20),fg="white",bg="black")
titleLabel.pack()

frame2=Frame(root)
frame2.pack()

turn="x"

def play(event):
    global turn
    button=event.widget
    if turn=="x":
        button["text"]="X"
        turn="o"
    else:
        button["text"]="O"
        turn="x"

button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30))
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)
button2=Button(frame2,text=" ",width=4,height=2,font=("Arial",30))
button2.grid(row=0,column=1)
button2.bind("<Button-1>",play)
button3=Button(frame2,text=" ",width=4,height=2,font=("Arial",30))
button3.grid(row=0,column=2)
button3.bind("<Button-1>",play)

button4=Button(frame2,text=" ",width=4,height=2,font=("Arial",30))
button4.grid(row=1,column=0)
button4.bind("<Button-1>",play)
button5=Button(frame2,text=" ",width=4,height=2,font=("Arial",30))
button5.grid(row=1,column=1)
button5.bind("<Button-1>",play)
button6=Button(frame2,text=" ",width=4,height=2,font=("Arial",30))
button6.grid(row=1,column=2)
button6.bind("<Button-1>",play)

button7=Button(frame2,text=" ",width=4,height=2,font=("Arial",30))
button7.grid(row=2,column=0)
button7.bind("<Button-1>",play)
button8=Button(frame2,text=" ",width=4,height=2,font=("Arial",30))
button8.grid(row=2,column=1)
button8.bind("<Button-1>",play)
button9=Button(frame2,text=" ",width=4,height=2,font=("Arial",30))
button9.grid(row=2,column=2)
button9.bind("<Button-1>",play)


root.mainloop()


